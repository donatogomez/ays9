def init_actions_(service, args):
    """
    this needs to returns an array of actions representing the depencies between actions.
    Looks at ACTION_DEPS in this module for an example of what is expected
    """
    return {
        'test': ['install']
    }


def test(job):
    import requests, sys
    service = job.service
    RESULT_OK = 'OK : %s '
    RESULT_FAILED = 'FAILED : %s'
    RESULT_ERROR = 'ERROR : %s'
    try:
        g8client = service.producers['g8client'][0]
        url = 'https://' + g8client.model.data.url
        username = g8client.model.data.login
        password = g8client.model.data.password

        login_url = url + '/restmachine/system/usermanager/authenticate'
        credential = {'name': username,
                      'secret': password}

        session = requests.Session()
        session.post(url=login_url, data=credential)

        vm = service.producers['node'][0]
        vmID = vm.model.data.machineId

        user = service.producers['uservdc'][0]
        user_name = user.model.data.provider

        API_URL = url + '/restmachine/cloudapi/machines/get'
        API_BODY = {'machineId': vmID}

        response = session.post(url=API_URL, data=API_BODY)

        if response.status_code == 200:
            content = response.json()
            for user in content['acl']:
                if user_name in user['userGroupId']:
                    service.model.data.result = RESULT_OK % 'test_add_user_to_cloudspace'
                    break
                else:
                    continue
            else:
                failure = '%s not in %i cloudspace' % (username, vmID)
                service.model.data.result = RESULT_FAILED % failure
        else:
            response_data = {'status_code': response.status_code,
                             'content': response.content}
            service.model.data.result = RESULT_ERROR % str(response_data) + str(vmID)
    except Exception as e:
        service.model.data.result = RESULT_ERROR % (str(sys.exc_info()[:2]) + str(e))
    service.save()
