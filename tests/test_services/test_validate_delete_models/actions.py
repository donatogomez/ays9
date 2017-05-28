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
    test_repo_path = j.sal.fs.joinPaths(j.dirs.varDir, 'tmp', 'test_validate_model')
    sample_bp_path = j.sal.fs.joinPaths(job.service.aysrepo.path, 'blueprints', 'test_validate_delete_model_sample.yaml')
    try:
        if j.sal.fs.exists(test_repo_path):
            j.sal.fs.removeDirTree(test_repo_path)
        test_repo =  j.atyourservice.server.repoCreate(test_repo_path, 'git@github.com:0-complexity/ays_automatic_cockpit_based_testing.git')
        bp_path = j.sal.fs.joinPaths(test_repo.path, 'blueprints', 'test_validate_delete_model_sample.yaml')
        j.sal.fs.copyFile(j.sal.fs.joinPaths(sample_bp_path), j.sal.fs.joinPaths(test_repo.path, 'blueprints'))
        test_repo.blueprintExecute(bp_path)
        action = 'install'
        role = 'sshkey'
        instance = 'main'
        for service in test_repo.servicesFind(actor="%s.*" % role, name=instance):
            service.scheduleAction(action=action, period=None, log=True, force=False)

        run = test_repo.runCreate(profile=False, debug=False)
        run.execute()

        test_repo.destroy()
        if j.sal.fs.exists(j.sal.fs.joinPaths(test_repo.path, "actors")):
            model.data.result = RESULT_FAILED % ('Actors directory is not deleted')
        if j.sal.fs.exists(j.sal.fs.joinPaths(test_repo.path, "services")):
            model.data.result = RESULT_FAILED % ('Services directory is not deleted')
        if j.sal.fs.exists(j.sal.fs.joinPaths(test_repo.path, "recipes")):
            model.data.result = RESULT_FAILED % ('Recipes directory is not deleted')
        if test_repo.actors:
            model.data.result = RESULT_FAILED % ('Actors model is not removed')
        if test_repo.services:
            model.data.result = RESULT_FAILED % ('Services model is not removed')
        if not j.core.jobcontroller.db.runs.find(repo=test_repo.model.key):
            model.data.result = RESULT_FAILED % ('Jobs are deleted after repository destroy')
    except:
        model.data.result = RESULT_ERROR % str(sys.exc_info()[:2])
    finally:
        job.service.save()
