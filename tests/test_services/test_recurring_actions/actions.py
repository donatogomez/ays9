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
    Test recurring actions
    """
    import sys
    import os
    import time
    RESULT_OK = 'OK : %s'
    RESULT_FAILED = 'FAILED : %s'
    RESULT_ERROR = 'ERROR : %s %%s' % job.service.name
    model = job.service.model
    model.data.result = RESULT_OK % job.service.name
    failures = []
    repos = []
    try:
        expected_nr_of_jobs = 1
        curdir = os.getcwd()
        j.atyourservice.reposDiscover()
        repo = j.atyourservice.repoGet(j.sal.fs.joinPaths(j.dirs.codeDir, 'github/jumpscale/jumpscale_core8/tests/sample_repo_recurring'))
        repos.append(repo)
        bp_path = j.sal.fs.joinPaths(repo.path, 'blueprints', 'test_recurring_actions_1.yaml')
        repo.blueprintExecute(path=bp_path)
        start_time = time.time()
        os.chdir(repo.path)
        job.service.executor.execute('ays run --ask')
        end_time = time.time()
        nr_of_jobs = len(j.core.jobcontroller.db.jobs.find(actor='test_recurring_actions_1', service='instance', 
                action='execution_gt_period', fromEpoch=start_time,
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
    
