def init_actions_(service, args):
    """
    this needs to returns an array of actions representing the depencies between actions.
    Looks at ACTION_DEPS in this module for an example of what is expected
    """
    return {
        'test': ['install']
    }


def init(job):
    service = job.service
    repo = service.aysrepo
    g8clients = repo.servicesFind(actor='g8client')

    if g8clients:
        g8client = g8clients[0]
        client = j.clients.openvcloud.getFromService(g8client)
        cpunodes = client.api.cloudbroker.computenode.list()
        cpunodes_ids = [cpunodes[i]['id'] for i in range(len(cpunodes))]
    else:
       raise j.exceptions.Input("can not get stacks ids as there is no g8client")

    # ovc node.
    vm = {
        'os.image': service.model.data.image,
        'vdc': service.parent.name,
        'stackID': -1
    }

    for i in range(len(cpunodes_ids)):
        vm['stackID'] = cpunodes_ids[i]
        service_name = 'stack_%s' % cpunodes_ids[i]
        nodevm = repo.actorGet('node.ovc').serviceCreate(service_name, vm)
        os = repo.actorGet('os.ssh.ubuntu').serviceCreate(service_name, {'node': nodevm.name})
        service.consume(os)

def test(job):
    import re
    import sys

    try:
        service = job.service
        log = j.logger.get('test')
        log.addHandler(j.logger._LoggerFactory__fileRotateHandler('tests'))
        log.info('Test started')
        log.info('check if sshpass is installed')
        if 'sshpass\n' != j.do.execute('dpkg -l sshpass | grep -o -F sshpass')[1]:
            service.model.data.result = 'FAILED : {} {}'.format('test_network_configuration', 'sshpass need to be installed')
            service.save()
            return

        vdc = service.parent
        g8client = vdc.producers["g8client"][0]
        client = j.clients.openvcloud.getFromService(g8client)
        acc = client.account_get(vdc.model.data.account)
        space = acc.space_get(vdc.model.dbobj.name, vdc.model.data.location)
        cloudspace_ip = space.get_space_ip()
        vm_publicport = 1000

        log.info('Create portforwads and install sshpass and python on the vms')
        vms = space.machines
        machines = []
        for vm in vms.keys():
            machine = vms[vm]
            machine.create_portforwarding(vm_publicport, 22)
            machine_info = client.api.cloudapi.machines.get(machineId=machine.id)
            account = machine_info['accounts'][0]
            machine_ip = machine_info['interfaces'][0]['ipAddress']
            connection = machine.get_ssh_connection()
            connection.execute('echo {} | sudo -S apt-get install -y  sshpass'.format(account['password']))
            connection.execute('echo {} | sudo -S apt-get install -y  python'.format(account['password']))
            machines.append([machine.id, vm_publicport, connection, account, machine_ip])
            vm_publicport += 1

        script = """
        import hashlib
        import sys
        import os
        file = sys.argv[1]
        rx = hashlib.md5(open(file,'r').read()).hexdigest()
        tx = hashlib.md5('This line is for test\\n').hexdigest()
        if(rx==tx):
            os.system('echo "Verified: No errors during transmission" >> results.txt')
        else:
            os.system('echo "Verification failed" >> results.txt')
        """
        with open('machine_script.py', 'w') as f:
            f.write('{}'.format(script))
        j.do.execute("sed -i 's/        //' machine_script.py")
        j.do.execute('echo \'This line is for test\' >> noerror.txt')

        log.info('Send the script and and txt file to all vms')
        for vm in machines:
            vmid = vm[0]
            vm_publicport = vm[1]
            account = vm[3]
            tmp = 'sshpass -p "{0}" scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -P {1} noerror.txt  {2}@{3}:'
            cmd = tmp.format(account['password'], vm_publicport, account['login'], cloudspace_ip)
            j.do.execute(cmd)
            tmp = 'sshpass -p "{0}" scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -P {1} machine_script.py  {2}@{3}:'
            cmd2 = tmp.format(account['password'], vm_publicport, account['login'], cloudspace_ip)
            j.do.execute(cmd2)
            tmp = 'sshpass -p "{}" ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p {} {}@{} '
            tmp += ' python machine_script.py noerror.txt'
            cmd3 = tmp.format(account['password'], vm_publicport, account['login'], cloudspace_ip)
            j.do.execute(cmd3)

        log.info('Send the other txt files from one vm to all other vms')
        for vm in machines:
            vmid = vm[0]
            vm_publicport = vm[1]
            vm_connection = vm[2]
            vm_connection.execute('echo \'This line is for test\' >> noerror{}.txt'.format(vmid))
            for rx_vm in machines:
                rx_vmid = rx_vm[0]
                if rx_vmid == vmid:
                    continue
                rx_vm_connection = rx_vm[2]
                account = rx_vm[3]
                tmp = 'sshpass -p "{0}" scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null noerror{1}.txt  {2}@{3}:'
                cmd = tmp.format(account['password'], vmid, account['login'], rx_vm[4])
                vm_connection.execute(cmd)
                rx_vm_connection.execute('python machine_script.py noerror{}.txt'.format(vmid))

        log.info('get the verification results from all the vms')
        for vm in machines:
            vmid = vm[0]
            vm_publicport = vm[1]
            account = vm[3]
            tmp = 'sshpass -p "{0}" scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -P {1}  {2}@{3}:results.txt .'
            cmd = tmp.format(account['password'], vm_publicport, account['login'], cloudspace_ip)
            j.do.execute(cmd)
            f = open("final.txt", 'a')
            res = open("results.txt", 'r')
            f.write(res.read())
            f.close()
            j.do.execute('rm results.txt')

        log.info('check the data integrity')
        f = open("final.txt", 'r')
        match = re.search('Verification failed', f.read())
        if not match:
            service.model.data.result = 'OK : {}'.format('test_network_configuration')
            service.save()
        else:
            service.model.data.result = 'FAILED : {} {}'.format('test_network_configuration', str(sys.exc_info()[:2]))
            service.save()
            return

    except:
        service.model.data.result = 'ERROR : {} {}'.format('test_network_configuration', str(sys.exc_info()[:2]))
    finally:
        # removing all files in repo directory if they exist
        j.do.execute('rm -f noerror.txt')
        j.do.execute('rm -f final.txt')
        j.do.execute('rm -f machine_script.py')
        log.info('Test Ended')
        service.save()
