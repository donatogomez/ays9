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
    try:
        # Tests that parsing args with values set in the bp will override default values
        if job.service.name == 'without_defaultvalue':
            if model.data.description != 'another description':
                model.data.result = RESULT_FAILED % ('Values in blueprint do not override default values')
        # Tests that parsing args with default values works
        elif job.service.name == 'with_defaultvalue':
            if model.data.description != 'description':
                model.data.result = RESULT_FAILED % ("Parsing blueprint with default values failed")
        # Tests parsing blueprint that has special characters
        elif job.service.name == 'with_special_characters':
            if model.data.description != 'Können Sie mir behilflich sein?':
                model.data.result = RESULT_FAILED % ("Failed to parse blueprint with special characters")
    except:
        model.data.result = RESULT_ERROR % str(sys.exc_info()[:2])
    job.service.save()
