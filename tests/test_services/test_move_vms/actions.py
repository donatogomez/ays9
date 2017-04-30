# issue: https://github.com/0-complexity/openvcloud/issues/768
def init_actions_(service, args):
    """
    this needs to returns an array of actions representing the depencies between actions.
    Looks at ACTION_DEPS in this module for an example of what is expected
    """
    return {
        'test': ['install']
    }


def input(job):
    service = job.service
    repo = service.aysrepo
    g8clients = repo.servicesFind(actor='g8client')

    action = job.model.args.get('action')
    if action == 'live_migration' or action == 'node_maintenance':
        pass
    else:
        raise j.exceptions.Input("action should be only live_migration or node_maintenance")

    if g8clients:
        g8client = g8clients[0]
        client = j.clients.openvcloud.getFromService(g8client)
    else:
        raise j.exceptions.Input("can not get stacks ids as there is no g8client")
    cpunodes = client.api.cloudbroker.computenode.list()
    cpunodes_ids = [cpunodes[i]['id'] for i in range(len(cpunodes)) if cpunodes[i]['status'] == 'ENABLED']
    args = job.model.args
    args['cpunodes'] = cpunodes_ids
    return args


def init(job):
    service = job.service
    cpunodes_ids = service.model.data.cpunodes
    repo = service.aysrepo
    # ovc node.
    vm = {
        'os.image': service.model.data.image,
        'vdc': service.parent.name,
        'sizeID': 1,
        'stackID': -1
    }

    vm['stackID'] = cpunodes_ids[0]
    service_name = 'stack_%s' % cpunodes_ids[0]
    nodevm = repo.actorGet('node.ovc').serviceCreate(service_name, vm)
    os = repo.actorGet('os.ssh.ubuntu').serviceCreate(service_name, {'node': nodevm.name})
    service.consume(os)


def test(job):
    import re
    import sys
    import time
    import threading

    try:
        check_script = """
        #!/usr/bin/env/python
        import sys
        import hashlib
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        md5 = hashlib.md5()
        md52 = hashlib.md5()
        with open(file1,'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                md5.update(chunk)
        with open(file2,'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                md52.update(chunk)
        f1 = md5.digest()
        f2 = md5.digest()
        if(f1==f2):
            print('Two files are identical')
        else:
            print('Two files are different')
        """

        machine_script = """
        #!/usr/bin/env/python
        import sys
        import os
        testname = sys.argv[1]
        os.close(0)
        os.close(1)
        os.close(2)
        ret = os.fork()
        if ret:
            # parent
            os.wait()
        else:
            # child
            os.system('fio --ioengine=libaio --direct=1 --gtod_reduce=1 --name=%s --size=600M --readwrite=randrw' % testname)
        """

        service = job.service
        log = j.logger.get('test')
        log.addHandler(j.logger._LoggerFactory__fileRotateHandler('tests'))
        log.info('Test started')
        log.info('check if sshpass is installed')
        if 'sshpass\n' != j.do.execute('dpkg -l sshpass | grep -o -F sshpass')[1]:
            service.model.data.result = 'FAILED : {} {}'.format('test_move_vms', 'sshpass need to be installed')
            service.save()
            return

        vdc = service.parent
        g8client = vdc.producers["g8client"][0]
        client = j.clients.openvcloud.getFromService(g8client)
        cpunodes = client.api.cloudbroker.computenode.list()
        cpunodes_ids = [cpunodes[i]['id'] for i in range(len(cpunodes))]
        if len(cpunodes_ids) < 2:
            log.info('Not Enough cpu nodes for that test')
            service.model.data.result = 'FAILED : {} {}'.format('test_move_vms', 'Not Enough cpu nodes for that test')
            service.save()
            return

        action = service.model.data.action
        acc = client.account_get(vdc.model.data.account)
        space = acc.space_get(vdc.model.dbobj.name, vdc.model.data.location)
        cloudspace = client.api.cloudapi.cloudspaces.get(cloudspaceId=space.id)
        gid = cloudspace['gid']
        cloudspace_ip = space.get_space_ip()
        vm_publicport = 2200
        vms = space.machines
        machine = [m for m in vms.values()][0]
        vm_os = machine.get_ssh_connection()
        machine_info = client.api.cloudapi.machines.get(machineId=machine.id)
        account = machine_info['accounts'][0]

        vm_os.execute('echo {} | sudo -S apt-get update'.format(account['password']))
        vm_os.execute('echo {} | sudo -S apt-get install -y  fio'.format(account['password']))
        vm_os.execute('echo {} | sudo -S apt-get install -y  python'.format(account['password']))

        # create and send the scripts to the vm
        with open('machine_script.py', 'w') as f:
            f.write('{}'.format(machine_script))
        with open('check_script.py', 'w') as f:
            f.write('{}'.format(check_script))
        j.do.execute("sed -i 's/        //' check_script.py")
        j.do.execute("sed -i 's/        //' machine_script.py")
        tmp = 'sshpass -p "{0}" scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -P {1} machine_script.py  {2}@{3}:'
        cmd1 = tmp.format(account['password'], vm_publicport, account['login'], cloudspace_ip)
        tmp = 'sshpass -p "{0}" scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -P {1} check_script.py  {2}@{3}:'
        cmd2 = tmp.format(account['password'], vm_publicport, account['login'], cloudspace_ip)
        j.do.execute(cmd1)
        j.do.execute(cmd2)

        threads = []
        # Adding the treads that will be executed
        for i in range(2):
            if i == 0:
                testname = 'test1'
                cmd = "python machine_script.py {}".format(testname)
                t = threading.Thread(target=vm_os.execute, args=(cmd,))
            else:
                if action == 'live_migration':
                    d = dict(machineId=machine.id, reason='Testing', targetStackId=cpunodes_ids[1], force=False)
                    t = threading.Thread(target=client.api.cloudbroker.machine.moveToDifferentComputeNode, kwargs=d)
                else:
                    d = dict(id=cpunodes_ids[0], gid=gid, vmaction='move', message='testing')
                    t = threading.Thread(target=client.api.cloudbroker.computenode.maintenance, kwargs=d)
            threads.append(t)

        for l in range(len(threads)):
            if l == 0:
                log.info('started writing a file on the created virtual machine ...')
                threads[l].start()
                time.sleep(15)
            if l == 1:
                log.info('Machine will be moved to another cpunode')
                threads[l].start()
                time.sleep(10)
                machine_db = client.api.cloudbroker.machine.get(machineId=machine.id)
                curr_stackId = machine_db['stackId']
                if action == 'live_migration':
                    if curr_stackId != cpunodes_ids[1]:
                        log.info('The VM didn\'t move to the other cpunode with stackId:{}'.format(cpunodes[1]))
                        service.model.data.result = 'FAILED : {} {}'.format('test_move_vms', 'VM didn\'t move to the other cpunode')
                        service.save()
                        return
                else:
                    if curr_stackId == cpunodes_ids[0]:
                        log.info('The VM didn\'t move to another cpunode ')
                        service.model.data.result = 'FAILED : {} {}'.format('test_move_vms', 'VM didn\'t move to another cpunode')
                        service.save()
                        return

                if machine_db['status'] == 'RUNNING':
                    log.info('The VM have been successfully installed on another node with approximately no downtime during live migration')
                else:
                    log.info('A high downtime (more than 10 secs) have been noticed')
                    service.model.data.result = 'FAILED : {} {}'.format('test_move_vms', 'A high downtime (more than 8 secs) have been noticed')
                    service.save()
                    return

        for k in range(len(threads)):
            threads[k].join()

        log.info('writing a second file to compare with ...')
        vm_os.execute('python machine_script.py test2')

        log.info('checking if there is no data loss ...')
        test_result = vm_os.execute('python check_script.py test1.0.0 test2.0.0')
        match = re.search(r'Two files are identical', test_result[1])
        if match:
            service.model.data.result = 'OK : {}'.format('test_move_vms')
        else:
            service.model.data.result = 'FAILED : {} {}'.format('test_move_vms', 'files are not identical')

    except:
        service.model.data.result = 'ERROR : {} {}'.format('test_move_vms', str(sys.exc_info()[:2]))
    finally:
        j.do.execute('rm -f check_script.py')
        j.do.execute('rm -f machine_script.py')
        service.save()
        if action == 'node_maintenance':
            cpunodes = client.api.cloudbroker.computenode.list(gid=gid)
            for cn in cpunodes:
                if cn['id'] == cpunodes_ids[0] and cn['status'] != 'ENABLED':
                    client.api.cloudbroker.computenode.enable(id=cpunodes_ids[0], gid=gid, message='enable')
        log.info('Test Ended')
