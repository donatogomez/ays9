def install(job):
    cuisine = job.service.executor.cuisine
    # install kvm
    cuisine.systemservices.kvm.install()
    # start libvirt-bin
    job.service.executeActionJob('start', inprocess=True)

    job.service.model.actions['uninstall'].state = 'new'
    job.service.saveAll()


def start(job):
    cuisine = job.service.executor.cuisine

    services_to_start = ['libvirt-bin', 'virtlogd']
    for service in services_to_start:
        if not cuisine.processmanager.exists(service):
            raise j.exceptions.RuntimeError("{} service doesn't exists. \
                                             it should have been created during installation of this service".format(service))

        cuisine.processmanager.start(service)

    job.service.model.actions['stop'].state = 'new'
    job.service.saveAll()

def stop(job):
    cuisine = job.service.executor.cuisine

    services_to_start = ['libvirt-bin', 'virtlogd']
    for service in services_to_start:
        if not cuisine.processmanager.exists(service):
            raise j.exceptions.RuntimeError("{} service doesn't exists. \
                                             it should have been created during installation of this service".format(service))

        cuisine.processmanager.stop(service)

    job.service.model.actions['start'].state = 'new'
    job.service.saveAll()


def uninstall(job):
    cuisine = job.service.executor.cuisine
    cuisine.systemservices.kvm.uninstall()

    job.service.model.actions['install'].state = 'new'
    job.service.saveAll()
