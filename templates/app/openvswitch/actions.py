def install(job):
    cuisine = job.service.executor.cuisine
    # install openvswitch, used for kvm networking
    cuisine.systemservices.openvswitch.install()
    # start openvswitch switch
    job.service.executeActionJob('start')

    job.service.model.actions['uninstall'].state = 'new'
    job.service.saveAll()

def start(job):
    cuisine = job.service.executor.cuisine
    if not cuisine.processmanager.exists('openvswitch-switch'):
        raise j.exceptions.RuntimeError("openvswitch-switch service doesn't exists. \
                                         it should have been created during installation of this service")

    cuisine.processmanager.start('openvswitch-switch')

    job.service.model.actions['stop'].state = 'new'
    job.service.saveAll()

def stop(job):
    cuisine = job.service.executor.cuisine
    if not cuisine.processmanager.exists('openvswitch-switch'):
        raise j.exceptions.RuntimeError("openvswitch-switch service doesn't exists. \
                                         it should have been created during installation of this service")

    cuisine.processmanager.stop('openvswitch-switch')

    job.service.model.actions['start'].state = 'new'
    job.service.saveAll()

def uninstall(job):
    cuisine = job.service.executor.cuisine
    cuisine.systemservices.openvswitch.uninstall()

    job.service.model.actions['install'].state = 'new'
    job.service.saveAll()
