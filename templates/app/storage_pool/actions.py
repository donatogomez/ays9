def init_actions_(service, args):
    # some default logic for simple actions
    return {
        'snapshot': ['install'],
        'replicate': ['install']
    }

def install(job):
    return

def snapshot(job):
    service = job.service
    if not service.model.data.snapshot:
        return
    from datetime import date
    d = date.today()
    os = service.producers['os'][0]
    path = service.model.data.path
    root_path = service.producers['fs'][0].model.data.mount
    snapshots_path = j.sal.fs.joinPaths(root_path, 'snapshots')
    cuisine = os.executor.cuisine
    cuisine.core.dir_ensure(snapshots_path)
    cuisine.core.sudomode = True
    cuisine.btrfs.snapshotReadOnlyCreate(path, j.sal.fs.joinPaths(snapshots_path, '%s_%d_%d_%d' % (service.name,
                                                                                                   d.year,
                                                                                                   d.month,
                                                                                                   d.day)))

def replicate(job):
    service = job.service
    if not service.model.data.replicate or not service.model.data.pools:
        return
    os_base = service.producers['os'][0]
    cuisine_base = os_base.executor.cuisine
    cuisine_base.tools.rsync.build()

    for pool in service.producers['storage_pool']:
        os_remote = pool.producers['os'][0]
        node_remote = os_remote.producers['node'][0]
        address = node_remote.model.data.ipPrivate
        cuisine_remote = os_remote.executor.cuisine
        content = ''
        if node_remote.producers['sshkey']:
            key = node_remote.producers['sshkey'][0].model.data.keyPub
            content = node_remote.producers['sshkey'][0].model.data.keyPriv
            cuisine_base.core.dir_ensure('$HOMEDIR/.ssh')
            cuisine_base.core.file_write('$HOMEDIR/.ssh/default.rsa', content, mode=700)
        else:
            keypath = cuisine_base.ssh.keygen()
            key = cuisine_base.file_read()
        cuisine_remote.ssh.authorize('root', key)
        path = j.sal.fs.joinPaths(service.producers['fs'][0].model.data.mount, service.model.data.path)
        tmp = '/'.split('/')
        tmp.pop()
        path_remote = "/".join(tmp)
        cuisine_remote.core.dir_ensure(path)
        cmd = """
        eval `ssh-agent -s`
        ssh-add $HOMEDIR/.ssh/default.rsa
        rsync -avzhe ssh %s root@%s:%s""" % (path, address, path_remote)
        cuisine_base.core.execute_bash(cmd)



# def monitor(job):
#     service = job.service
#     os = service.producers['os']
#     node = os.producers['node']
#     address = node.model.data.ipPublic
#     cuisine = os.executor.cuisine
#     root_path = service.producers['fs'].model.data.mount
#     free_space = cuisine.btrfs.getSpaceFree(root_path)



