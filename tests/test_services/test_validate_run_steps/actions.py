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
    Tests parsing of a bp with/without default values
    """
    import sys
    RESULT_OK = 'OK : %s'
    RESULT_FAILED = 'FAILED : %s'
    RESULT_ERROR = 'ERROR : %s %%s' % job.service.name
    model = job.service.model
    model.data.result = RESULT_OK % job.service.name
    failures = []
    repos = []
    repo1_path = j.sal.fs.joinPaths(j.dirs.codeDir, 'github/jumpscale/jumpscale_core8/tests/sample_repo1')
    repo2_path = j.sal.fs.joinPaths(j.dirs.codeDir, 'github/jumpscale/jumpscale_core8/tests/sample_repo3')
    try:
        repo1_expected_steps = [
                                ('datacenter.ovh_germany1.install', 'datacenter.ovh_germany2.install', 
                                'datacenter.ovh_germany3.install', 'sshkey.main.install'),
                                ('cockpit.cockpitv1.install', 'cockpit.cockpitv2.install')
                                ]
        j.atyourservice.server.reposDiscover()
        repo1 = j.atyourservice.server.repoGet(repo1_path)
        repos.append(repo1)
        for bp in repo1.blueprints:
            repo1.blueprintExecute(path=bp.path)
        run = repo1.runCreate(profile=False, debug=False)
        for index, step in enumerate(run.steps):
            expected_step_jobs = repo1_expected_steps[index]
            for job in step.jobs:
                job_name = '%s.%s.%s' % (job.model.dbobj.actorName, job.model.dbobj.serviceName, job.model.dbobj.actionName)
                if job_name not in expected_step_jobs:
                    failures.append('Job [%s] is added to step #%s unexpectedly' % (job_name, index + 1))
        

        expected_job_statuses = {
            'runtime_error_service.instance.install': 'ok',
            'runtime_error_service.instance.test': 'error',
            'runtime_error_service.instance.test2': 'ok',
            'runtime_error_service.instance.test3': 'new'
        }
        expected_step_statuses = ['ok', 'error', 'new']
        expected_run_status = 'error'
        repo2 = j.atyourservice.server.repoGet(repo2_path)
        repos.append(repo2)
        for bp in repo2.blueprints:
            repo2.blueprintExecute(path=bp.path)
        run = repo2.runCreate(profile=False, debug=False)
        try:
            run.execute()
        except:
            for index, step in enumerate(run.steps):
                for job in step.jobs:
                    job_name = '%s.%s.%s' % (job.model.dbobj.actorName, job.model.dbobj.serviceName, job.model.dbobj.actionName)
                    if job_name not in expected_job_statuses:
                        failures.append('Job [%s] is unexpected in step #%s' % (job_name, index + 1))
                    elif expected_job_statuses[job_name] != job.model.dbobj.state:
                        failures.append('Job [%s] has unexpected status [%s] expected [%s]' % (job_name, job.model.dbobj.state, expected_job_statuses[job_name]))
                if step.state != expected_step_statuses[index]:
                    failures.append('Step #%s has unexpected status [%s] expected [%s]' % (index + 1, step.state, expected_step_statuses[index]))
            if str(run.state) != expected_run_status:
                failures.append('Run has unexpected status [%s] expected [%s]' % (str(run.state), expected_run_status))

        else:
            failures.append('Expected runtime error on repo [%s] did not happend' % repo2)
        

        if failures:
            model.data.result = RESULT_FAILED % '\n'.join(failures)
    except:
        model.data.result = RESULT_ERROR % str(sys.exc_info()[:2])
    finally:
        job.service.save()
        for repo in repos:
            repo.destroy()
