def init_actions_(service, args):

    """

    this needs to returns an array of actions representing the depencies between actions.

    Looks at ACTION_DEPS in this module for an example of what is expected

    """
    # some default logic for simple actions
    return {

        'test': ['install']

    }



def test(job):
    """
    Test recurring actions with hanging jobs
    """
    import sys
    import os
    import time
    import threading
    RESULT_OK = 'OK : %s'
    RESULT_FAILED = 'FAILED : %s'
    RESULT_ERROR = 'ERROR : %s %%s' % job.service.name
    model = job.service.model
    model.data.result = RESULT_OK % job.service.name
    failures = []
    repos = []
    try:
        expected_nr_of_jobs = 0
        curdir = os.getcwd()
        j.core.atyourservice.reposDiscover()
        repo = j.core.atyourservice.repoGet(j.sal.fs.joinPaths(j.dirs.codeDir, 'github/jumpscale/jumpscale_core8/tests/sample_repo_recurring'))
        repos.append(repo)
        bp_path = j.sal.fs.joinPaths(repo.path, 'blueprints', 'test_recurring_actions_hanging_jobs.yaml')
        repo.blueprintExecute(path=bp_path)
        # find the service and retrieve the timeout value
        srv = repo.serviceGet('test_recurring_actions_1', 'hanging')
        timeout = srv.model.data.timeout
        thread = threading.Thread(target=job.service.executor.execute, args=("ays run --ask", ), daemon=True)
        start_time = time.time()
        os.chdir(repo.path)
        thread.start()
        time.sleep((timeout * 60) + 60) # add one minute to the configured timeout
        end_time = time.time()
        nr_of_jobs = len(j.core.jobcontroller.db.jobs.find(actor='test_recurring_actions_1', service='hanging',
                action='execute_hanging_job', fromEpoch=start_time,
                toEpoch=end_time))
        if nr_of_jobs != expected_nr_of_jobs:
            failures.append('Wrong number of jobs found. Expected [%s] found [%s]' % (expected_nr_of_jobs, nr_of_jobs))

        if failures:
            model.data.result = RESULT_FAILED % '\n'.join(failures)

    except:
        model.data.result = RESULT_ERROR % str(sys.exc_info()[:2])
    finally:
        job.service.save()
        if repos:
            for repo in repos:
                repo.destroy()
