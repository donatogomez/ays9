def install(job):
    data = job.service.model.data
    cuisine = job.service.executor.cuisine

    # create bridge
    if data.name not in cuisine.systemservices.openvswitch.networkList():
        cuisine.systemservices.openvswitch.networkCreate(data.name)
        # configure the network and the natting
        gateway = data.gateway if data.gateway else None
        cuisine.net.netconfig(data.name, data.ipAddr, data.netmask, gateway=gateway, masquerading=data.masquerading)
        cuisine.processmanager.start('systemd-networkd')

    if data.dhcpEnable:
        # add a dhcp server to the bridge
        range_start = data.dhcpRangeStart if data.dhcpRangeStart else ''
        range_stop = data.dhcpRangeStop if data.dhcpRangeStop else ''
        # if rangefrom & rangeto not specified then will serve full local range minus bottomn 10 & top 10 addr
        cuisine.apps.dnsmasq.install()
        cuisine.apps.dnsmasq.config(data.name, rangefrom=range_start, rangeto=range_stop)
        cuisine.processmanager.restart('dnsmasq')

    job.service.model.actions['uninstall'].state = 'new'
    job.service.saveAll()

def start(job):
    cuisine = job.service.executor.cuisine
    if not cuisine.processmanager.exists('systemd-networkd'):
        raise j.exceptions.RuntimeError("systemd-networkd service doesn't exists. \
                                         it should have been created during installation of this service")

    cuisine.processmanager.start('systemd-networkd')

    job.service.model.actions['stop'].state = 'new'
    job.service.saveAll()

def stop(job):
    cuisine = job.service.executor.cuisine
    if not cuisine.processmanager.exists('systemd-networkd'):
        raise j.exceptions.RuntimeError("systemd-networkd service doesn't exists. \
                                         it should have been created during installation of this service")

    cuisine.processmanager.stop('systemd-networkd')

    job.service.model.actions['start'].state = 'new'
    job.service.saveAll()

def uninstall(job):
    data = job.service.model.data
    cuisine = job.service.executor.cuisine
    if data.name in cuisine.systemservices.openvswitch.networkList():
        cuisine.systemservices.openvswitch.networkDelete(data.name)

    job.service.model.actions['install'].state = 'new'
    job.service.saveAll()
