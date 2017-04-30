from js9 import j


def init(job):
    service = job.service
    if 'g8client' not in service.producers:
        raise j.exceptions.AYSNotFound("no producer g8client found. cannot continue init of %s" % service)

    service.saveAll()


def install(job):
    service = job.service
    if 'g8client' not in service.producers:
        raise j.exceptions.AYSNotFound("no producer g8client found. cannot continue init of %s" % service)
    g8client = service.producers["g8client"][0]
    cl = j.clients.openvcloud.getFromService(g8client)

    # Set limits
    # if account does not exist, it will create it
    account = cl.account_get(name=service.model.dbobj.name,
                             create=True,
                             maxMemoryCapacity=service.model.data.maxMemoryCapacity,
                             maxVDiskCapacity=service.model.data.maxDiskCapacity,
                             maxCPUCapacity=service.model.data.maxCPUCapacity,
                             maxNumPublicIP=service.model.data.maxNumPublicIP,
                             )
    service.model.data.accountID = account.model['id']
    service.model.save()

    authorized_users = account.authorized_users
    users = service.model.data.accountusers

    # Authorize users
    for user in users:
        if user not in authorized_users:
            account.authorize_user(username=user)

    # Unauthorize users not in the schema
    for user in authorized_users:
        if user not in users:
            account.unauthorize_user(username=user)

    # update capacity incase acount already existed update it
    account.model['maxMemoryCapacity'] = service.model.data.maxMemoryCapacity
    account.model['maxVDiskCapacity'] = service.model.data.maxDiskCapacity
    account.model['maxNumPublicIP'] = service.model.data.maxNumPublicIP
    account.model['maxCPUCapacity'] = service.model.data.maxCPUCapacity
    account.save()


def processChange(job):
    service = job.service

    args = job.model.args
    category = args.pop('changeCategory')
    if category == "dataschema" and service.model.actionsState['install'] == 'ok':
        for key, value in args.items():
            if key == 'uservdc':
                # value is a list of (uservdc)
                if not isinstance(value, list):
                    raise j.exceptions.Input(message="Value is not a list.")
                for s in service.producers['uservdc']:
                    if s.name not in value:
                        service.model.producerRemove(s)
                for v in value:
                    userservice = service.aysrepo.serviceGet('uservdc', v)
                    if userservice not in service.producers.get('uservdc', []):
                        service.consume(userservice)
            setattr(service.model.data, key, value)

        if 'g8client' not in service.producers:
            raise j.exceptions.AYSNotFound("no producer g8client found. cannot continue init of %s" % service)

        g8client = service.producers["g8client"][0]
        cl = j.clients.openvcloud.getFromService(g8client)
        # Get given space, raise error if not found
        account = cl.account_get(name=service.model.dbobj.name,
                                 create=False)

        authorized_users = account.authorized_users
        users = service.model.data.accountusers

        # Authorize users
        for user in users:
            if user not in authorized_users:
                account.authorize_user(username=user)

        # Unauthorize users not in the schema
        for user in authorized_users:
            if user not in users:
                account.unauthorize_user(username=user)

        # update capacity
        account.model['maxMemoryCapacity'] = service.model.data.maxMemoryCapacity
        account.model['maxVDiskCapacity'] = service.model.data.maxDiskCapacity
        account.model['maxNumPublicIP'] = service.model.data.maxNumPublicIP
        account.model['maxCPUCapacity'] = service.model.data.maxCPUCapacity
        account.save()

        service.save()


def uninstall(job):
    service = job.service
    if 'g8client' not in service.producers:
        raise j.exceptions.AYSNotFound("no producer g8client found. cannot continue init of %s" % service)

    g8client = service.producers["g8client"][0]
    cl = j.clients.openvcloud.getFromService(g8client)
    acc = cl.account_get(service.model.dbobj.name)
    acc.delete()
