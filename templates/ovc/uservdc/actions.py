
def install(job):
    service = job.service

    # create user if it doesn't exists
    username = service.model.dbobj.name
    password = service.model.data.password
    email = service.model.data.email

    provider = service.model.data.provider
    username = "%s@%s" % (username, provider) if provider else username
    password = password if not provider else "fakeeeee"

    g8client = service.producers["g8client"][0]
    client = j.clients.openvcloud.getFromService(g8client)
    if not client.api.system.usermanager.userexists(name=username):
        groups = service.model.data.groups
        client.api.system.usermanager.create(username=username, password=password, groups=groups, emails=[email], domain='', provider=provider)


def uninstall(job):
    service = job.service

    # unauthorize user to all consumed vdc
    username = service.model.dbobj.name
    g8client = service.producers["g8client"][0]
    client = j.clients.openvcloud.getFromService(g8client)
    provider = service.model.data.provider
    username = "%s@%s" % (username, provider) if provider else username
    if client.api.system.usermanager.userexists(name=username):
        client.api.system.usermanager.delete(username=username)
