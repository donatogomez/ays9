# template: dns_domain

## Description:
This actor template is responsible to manage a domain name on a DNS server.

## Schema:

- dnsclient: list of dns client to consume. All the actions will be executed on all the dns client consumed. Usefull when you have a cluster of DNS where you need to write the same configutration on each node. **requires at least one**
- ttl: Time to leave for this domain in seconde. default to 600. **required**
- domain: root domain name. **reuired**
- a.records: list of a records to create on this domain. See below for the format used. **optional**
- cname.records: list of cname records to create on this domain. See below for the format used. **optional**

- node: in case you want to assign an a record to the IP of a node in the same AYS repository. you need to consume these node in order to make sure the node get installed and get an IP before AYS install this service.

### Format of records.
The format used for the a and cname records is : `sub_domain:IP`
e.g: `wwww:85.34.67.34`

#### Dynamic IP
In the case you want to assign the IP address of a node that is not yet installed to a sub domain. You can instead of the IP give the instance name of the node and consume this node.
The service will test of the IP part of the records definition match one of the node consumed. And if it's the case will use the ipPublic attribute from the node as IP address. This allow you to create dynamic domains
