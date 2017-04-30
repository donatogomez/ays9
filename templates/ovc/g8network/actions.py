def install(job):
    service = job.service
    vdc = service.producers["vdc"][0]
    g8client = vdc.producers["g8client"][0]
    cl = j.clients.openvcloud.getFromService(g8client)
    acc = cl.account_get(vdc.model.data.account)
    # if space does not exist, it will create it
    space = acc.space_get(vdc.model.dbobj.name, vdc.model.data.location)

    data = service.model.data
    for location in cl.locations:
        if location['name'] == space.model['location']:
            gid = location['gid']

    space.add_external_network(name=data.name,
                               subnet=data.publicSubnetCIDR,
                               gateway=data.gatewayIPAddress,
                               startip=data.startIPAddress,
                               endip=data.endIPAddress,
                               gid=gid,
                               vlan=data.vLANID)
