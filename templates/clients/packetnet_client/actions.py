
def install(job):
    j.do.pip("git+https://github.com/gigforks/packet-python.git --upgrade")

def monitor(job):
    import packet
    manager = packet.Manager(auth_token=job.service.model.data.token)
    res=manager.list_projects()
    if len(res)<1:
        raise RuntimeError("Packet.Net projects need to be more than 1")
