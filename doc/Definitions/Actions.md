# AYS Actions

- Manages the life cycle of your AYS
- you need to implement one or more function (actions) in the actions.py file of the actor of the service

An action file is a python file that contains multiple function.
Each function name correspond to an action. In the example below the actor implement two action, _install_ and _uninstall_.

The function need to accept a single argument called job.

The job object let you access multiple other usefull object:
- **job.service** : the service object on which the action is execute on.
- **job.model.args** : the arguments passed to this action
- **job.service.model.data** : the schema value of the service

## Example:

**actions.py**:

```python
def install(job):
    service = job.service
    vdc = service.parent

    if 'g8client' not in vdc.producers:
        raise j.exceptions.AYSNotFound("no producer g8client found. cannot continue init of %s" % service)

    g8client = vdc.producers["g8client"][0]
    cl = j.clients.openvcloud.getFromService(g8client)
    acc = cl.account_get(vdc.model.data.account)
    space = acc.space_get(vdc.model.dbobj.name, vdc.model.data.location)

    if service.name in space.machines:
        # machine already exists
        machine = space.machines[service.name]
    else:
        image_names = [i['name'] for i in space.images]
        if service.model.data.osImage not in image_names:
            raise j.exceptions.NotFound('Image %s not available for vdc %s' % (service.model.data.osImage, vdc.name))

        datadisks = list(service.model.data.datadisks)
        machine = space.machine_create(name=service.name,
                                       image=service.model.data.osImage,
                                       memsize=service.model.data.osSize,
                                       disksize=service.model.data.bootdiskSize,
                                       datadisks=datadisks)

    service.model.data.machineId = machine.id
    service.model.data.ipPublic = machine.space.model['publicipaddress']
    ip, vm_info = machine.get_machine_ip()
    service.model.data.ipPrivate = ip
    service.model.data.sshLogin = vm_info['accounts'][0]['login']
    service.model.data.sshPassword = vm_info['accounts'][0]['password']

    for i, port in enumerate(service.model.data.ports):
        ss = port.split(':')
        if len(ss) == 2:
            public_port, local_port = ss
        else:
            local_port = port
            public_port = None

        public, local = machine.create_portforwarding(publicport=public_port, localport=local_port, protocol='tcp')
        service.model.data.ports[i] = "%s:%s" % (public, local)

    service.saveAll()

def uninstall(job):
    service = job.service
    vdc = service.parent

    if 'g8client' not in vdc.producers:
        raise j.exceptions.RuntimeError("no producer g8client found. cannot continue init of %s" % service)

    g8client = vdc.producers["g8client"][0]
    cl = j.clients.openvcloud.getFromService(g8client)
    acc = cl.account_get(vdc.model.data.account)
    space = acc.space_get(vdc.model.dbobj.name, vdc.model.data.location)

    if service.name not in space.machines:
        return
    machine = space.machines[service.name]
    machine.delete()
```

```toml
!!!
title = "AYS Actions"
date = "2017-03-02"
tags= ["ays","def"]
categories= ["ays_def"]
```
