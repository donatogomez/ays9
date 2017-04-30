def install(job):
    service = job.service
    if 'dnsclient' not in service.producers:
        return

    # dict of node producers consumed
    # key name, value service object
    consumed_nodes = {i.name: i for i in service.producers['node']}

    for dns_client in service.producers['dnsclient']:
        dnscl = j.clients.dns.getFromService(dns_client)

        domain = dnscl.ensure_domain(service.model.data.domain, ttl=service.model.data.ttl)

        for record in service.model.data.aRecords:
            sub_domain, ip = record.split(':')

            if ip in consumed_nodes.keys():
                # mean ip is the name of a comsumed node, we need to get the public ip of that node
                ip = consumed_nodes[ip].model.data.ipPublic

            domain.add_a_record(ip=ip, subdomain=sub_domain)

        for record in service.model.data.cnameRecords:
            sub_domain, ip = record.split(':')

            if ip in consumed_nodes.keys():
                # mean ip is the name of a comsumed node, we need to get the public ip of that node
                ip = consumed_nodes[ip].model.data.ipPublic

            domain.add_cname_record(ip=ip, subdomain=sub_domain)

        domain.save()


def uninstall(job):
    service = job.service
    if 'dnsclient' not in service.producers:
        return

    for dns_client in service.producers['dnsclient']:
        dnscl = j.clients.dns.getFromService(dns_client)
        domain = dnscl.get_domain(service.model.data.domain)

        for record in service.model.data.aRecords:
            sub_domain, ip = record.split(':')
            try:
                domain.del_a_record(ip=ip, subdomain=sub_domain)
            except KeyError:
                pass
        for record in service.model.data.cnameRecords:
            sub_domain, ip = record.split(':')
            try:
                domain.del_cname_record(subdomain=sub_domain)
            except KeyError:
                pass

        domain.save()
