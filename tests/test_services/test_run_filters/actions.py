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
    Tests run filters
    """
    import sys
    RESULT_OK = 'OK : %s'
    RESULT_FAILED = 'FAILED : %s'
    RESULT_ERROR = 'ERROR : %s %%s' % job.service.name
    model = job.service.model
    model.data.result = RESULT_OK % job.service.name
    try:
        services_to_check = {
            'test_run_filters': {
                'instance': 'main', 
                'actions': [('install', ['ok']), ('test', ['running'])]
                },
            'test_run_filter1': {
                'instance': 'main', 
                'actions': [('install', ['ok']), ('test', ['running', 'ok', 'scheduled'])]
                },

            'test_run_filter2': {
                'instance': 'main', 
                'actions': [('install', ['ok']), ('test', ['new'])]
                }

        }
        for actor, actor_info in services_to_check.items():
            srv = job.service.aysrepo.servicesFind(actor=actor, name=actor_info['instance'])[0]
            for action_info in actor_info['actions']:
                if str(srv.model.actions[action_info[0]].state) not in action_info[1]:
                    model.data.result = RESULT_FAILED % ('Action [%s] on service [%s] has unexpected state. Expected [%s] found [%s]' % (action_info[0], 
                                                                                                                                        '%s!%s' % (actor, actor_info['instance']),
                                                                                                                                        action_info[1], 
                                                                                                                                        str(srv.model.actions[action_info[0]].state)
                                                                                                                                        ))

    except:
        model.data.result = RESULT_ERROR % str(sys.exc_info()[:2])
    finally:
        job.service.save()
