
def install(job):
    service = job.service

    # create external network
    name = service.model.data.name
    gateway = service.model.data.gateway
    subnet = service.model.data.subnet
    startip = service.model.data.startip
    endip = service.model.data.endip
    gid = service.model.data.gid
    vlan = service.model.data.vlan
    accountid = service.model.data.accountid

    g8client = service.producers["g8client"][0]
    client = j.clients.openvcloud.getFromService(g8client)
    netid = client.api.cloudbroker.iaas.addExternalNetwork(name=name, subnet=subnet, gateway=gateway, startip=startip, endip=endip, vlan=vlan, gid=gid, accountid=accountid)
    service.model.data.id = netid
    service.model.save()

def uninstall(job):
    service = job.service
    # delete externalID
    netid = service.model.data.id
    g8client = service.producers["g8client"][0]
    client = j.clients.openvcloud.getFromService(g8client)
    client.api.cloudbroker.iaas.deleteExternalNetwork(externalnetworkId=netid)
