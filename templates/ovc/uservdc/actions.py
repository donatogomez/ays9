
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


def processChange(job):
    service = job.service
    g8client = service.producers["g8client"][0]
    client = j.clients.openvcloud.getFromService(g8client)
    old_args = service.model.data
    new_args = job.model.args
    # Process Changing Groups
    old_groups = set(old_args.groups)
    new_groups = set(new_args.get('groups', []))
    if old_groups != new_groups:
        username = service.model.dbobj.name
        provider = old_args.provider
        username = "%s@%s" % (username, provider) if provider else username
        # Editing user api requires to send a list contains user's mail
        emails = [old_args.email]
        new_groups = list(new_groups)
        client.api.system.usermanager.editUser(username=username, groups=new_groups, provider=provider, emails=emails)
        service.model.data.groups = new_groups
        service.save()


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
