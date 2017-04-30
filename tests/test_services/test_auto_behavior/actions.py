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
    Tests auto bahavior
    """
    import sys
    RESULT_OK = 'OK : %s'
    RESULT_FAILED = 'FAILED : %s'
    RESULT_ERROR = 'ERROR : %s %%s' % job.service.name
    model = job.service.model
    model.data.result = RESULT_OK % job.service.name
    try:
        if job.service.name == 'auto_parent':
            # make sure that the parent service is auto created
            if not job.service.parent.name.startswith('auto_'):
                model.data.result = RESULT_FAILED % ("Parent service did not automatically created")
        if job.service.name == "0min":
            if 'sshkeys' in job.service.producers:
                model.data.result = RESULT_FAILED % ("Producer created while min value is zero")
        if job.service.name == "2min":
            if 'sshkeys2' not in job.service.producers:
                model.data.result = RESULT_FAILED % ("Producers not created while min value is 2")
            elif len(job.service.producers['sshkeys2']) != 2:
                model.data.result = RESULT_FAILED % ("Wrong number of producers is created")
    except:
        model.data.result = RESULT_ERROR % str(sys.exc_info()[:2])
    job.service.save()

    
