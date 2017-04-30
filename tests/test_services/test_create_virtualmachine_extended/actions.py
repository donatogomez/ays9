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
        ports = vm.model.data.ports
        vdc = service.producers['vdc'][0]
        vdcId = vdc.model.data.cloudspaceID


        API_URL = url + '/restmachine/cloudapi/machines/get'
        API_BODY = {'machineId': vmID}
        response = session.post(url=API_URL, data=API_BODY)

        API_URL = url + '/restmachine/cloudapi/portforwarding/list'
        API_BODY = {'cloudspaceId': vdcId, 'machineId': vmID}
        response_2 = session.post(url=API_URL, data=API_BODY)
        ports_ = [x['publicPort']+':'+x['localPort'] for x in response_2.json()]

        if response.status_code == 200:
            content = response.json()
            if vdcId != content['cloudspaceid']:
                failure = vdcId + '!=' + content['cloudspaceid']
                service.model.data.result = RESULT_FAILED % failure
            elif vm.name != content['name']:
                failure = vm.name + '!=' + content['name']
                service.model.data.result = RESULT_FAILED % failure
            elif vm.model.data.osImage != content['osImage']:
                failure = service.model.data.osImage + '!=' + content['osImage']
                service.model.data.result = RESULT_FAILED % failure
            elif vm.model.data.bootdiskSize != content['disks'][0]['sizeMax']:
                failure = service.model.data.bootdiskSize + '!=' + content['disks'][0]['sizeMax']
                service.model.data.result = RESULT_FAILED % failure
            elif vm.model.data.sizeID != content['sizeid']:
                failure = service.model.data.sizeID + '!=' + content['sizeid']
                service.model.data.result = RESULT_FAILED % failure
            elif set(ports) != set(ports_):
                failure = str(ports) + '!=' + str(ports_)
                service.model.data.result = RESULT_FAILED % failure
            else:
                service.model.data.result = RESULT_OK % 'test_create_virtualmachine_extended'
        else:
            response_data = {'status_code': response.status_code,
                             'content': response.content}
            service.model.data.result = RESULT_ERROR % str(response_data)+str(vmID)

    except Exception as e:
        service.model.data.result = RESULT_ERROR % (str(sys.exc_info()[:2]) + str(e))
    service.save()
