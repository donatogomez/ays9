def input(job):
    r = job.service.aysrepo

    # think node can never be argument
    # if "node" in job.model.args and job.model.args["os"] == "":
    #     res = job.model.args
    #     res["os"] = res["node"]
    #     res.pop("node")
    #     job.model.args = res

    if not "device.name" in job.model.args or job.model.args["device.name"].strip() == "":
        res = job.model.args
        res["device.name"] = job.service.model.name
        job.model.args = res

    return job.model.args


def init(job):
    service = job.service
    if service.model.data.deviceOs != 'custom_ipxe':
        os_actor = service.aysrepo.actorGet('os.ssh.ubuntu')
        os_actor.serviceCreate(service.model.name, args={'node': service.model.name, 'sshkey': service.model.data.sshkey})


def install(job):
    import time
    import packet

    service = job.service

    # create a new packet
    # make sure our sshkey gets there
    sshkey = service.producers.get('sshkey')[0]
    packetclient = service.producers.get('packetnet_client')[0]
    client = packet.Manager(packetclient.model.data.token)

    if packetclient.model.data.token == "":
        raise j.exceptions.Input(message="token for packet.net cannot be empty", level=1, source="", tags="", msgpub="")

    hostname = service.model.data.deviceName
    # hostname = service.model.name

    project_name = service.model.data.projectName
    project_ids = [project.id for project in client.list_projects() if project.name == project_name]
    if not project_ids:
        raise RuntimeError('No projects found with name %s' % project_name)
    project_id = project_ids[0]

    key_pub = sshkey.model.data.keyPub.strip()
    key_label = sshkey.model.name
    key_labels = [key.label for key in client.list_ssh_keys()]
    key_keys = [key.key for key in client.list_ssh_keys()]
    if key_pub not in key_keys and key_label not in key_labels:
        client.create_ssh_key(key_label, key_pub)

    project_devices = {device.hostname: device for device in client.list_devices(project_id)}
    if hostname not in project_devices:
        plan_type = service.model.data.planType
        plan_ids = [plan.id for plan in client.list_plans() if plan.name == plan_type]
        if not plan_ids:
            raise RuntimeError('No plans found with name %s' % plan_type)
        plan_id = plan_ids[0]

        operating_system_name = service.model.data.deviceOs
        if operating_system_name != 'custom_ipxe':
            operating_systems = [operating_system.slug for operating_system in client.list_operating_systems(
            ) if operating_system.name == operating_system_name]
            if not operating_systems:
                raise RuntimeError('No operating_systems found with name %s' % operating_system_name)
            operating_system = operating_systems[0]
        else:
            operating_system = 'custom_ipxe'

        facility_id = None
        for facility in client.list_facilities():
            if facility.name.lower().find(job.service.model.data.location.lower()) != -1:
                facility_id = facility.id

        if facility_id is None:
            raise j.exceptions.Input(message="Could not find facility in packet.net:%s" %
                                     job.service.model.data.location, level=1, source="", tags="", msgpub="")
        try:
            device = client.create_device(project_id=project_id, hostname=hostname, plan=plan_id,
                                          facility=facility_id, operating_system=operating_system, ipxe_script_url=service.model.data.ipxeScriptUrl)
        except Exception as e:
            if "Service Unavailable" in str(e):
                raise j.exceptions.Input(message="could not create packet.net machine, type of machine not available.%s" %
                                         job.service.model.dataJSON, level=1, source="", tags="", msgpub="")
            raise e
    else:
        device = project_devices[hostname]

    timeout_start = time.time()
    timeout = 900
    while time.time() < timeout_start + timeout and device.state != 'active':
        time.sleep(5)
        device = client.get_device(device.id)

    if device.state != 'active':
        raise RuntimeError('Too long to provision')

    service.model.data.deviceId = device.id
    service.model.data.sshLogin = device.user

    ip = [netinfo['address'] for netinfo in device.ip_addresses if netinfo['public'] and netinfo['address_family'] == 4]
    service.model.data.ipPublic = ip[0]
    service.model.data.ports = ['22:22']

    service.saveAll()


def uninstall(job):
    import packet
    service = job.service
    packetclient = service.producers.get('packetnet_client')[0]
    client = packet.Manager(packetclient.model.data.token)

    device_id = service.model.data.deviceId
    if device_id is None or device_id == '':
        raise j.exceptions.NotFound("device id not know, node probably not installed")
    device = client.get_device(device_id)
    device.delete()


def start(job):
    import packet
    service = job.service
    packetclient = service.producers.get('packetnet_client')[0]
    client = packet.Manager(packetclient.model.data.token)

    device_id = service.model.data.deviceId
    if device_id is None or device_id == '':
        raise j.exceptions.NotFound("device id not know, node probably not installed")
    device = client.get_device(device_id)
    if device.state == 'inactive':
        device.power_on()


def stop(job):
    import packet
    service = job.service
    packetclient = service.producers.get('packetnet_client')[0]
    client = packet.Manager(packetclient.model.data.token)

    device_id = service.model.data.deviceId
    if device_id is None or device_id == '':
        raise j.exceptions.NotFound("device id not know, node probably not installed")
    device = client.get_device(device_id)
    if device.state == 'active':
        device.power_off()


def restart(job):
    import packet
    service = job.service
    packetclient = service.producers.get('packetnet_client')[0]
    client = packet.Manager(packetclient.model.data.token)

    device_id = service.model.data.deviceId
    if device_id is None or device_id == '':
        raise j.exceptions.NotFound("device id not know, node probably not installed")
    device = client.get_device(device_id)
    if device.state == 'active':
        device.reboot()
