# template: disk.ovc

## Description:

This actor template represents a disk in ovc to be used later on by other services.

## Schema:
 - size: disk size in GB.
 - type: type of disk boot or normal.
 - description: description of disk. 
 - maxIOPS: max inputs outputs per second.
 - devicename: device name.
 - ssdSize: ssd size always available , will default to 10

## Example:
Replace \<with actual value \>

```yaml
sshkey__demo:

g8client__env1:
    # url: 'du-conv-3.demo.greenitglobe.com'
    url: '<env url>'
    login: '<login>'
    password: '<password>'
    account: 'Acoount'

vdcfarm__vdcfarm1:

vdc__scality:
    vdcfarm: 'vdcfarm1'
    g8client: 'env1'
    location: '<location>'

disk.ovc__disk1:
  size: 1000

s3__demo:
    vdc: 'scality'
    disk:
      - 'disk1'
    domain: 'mystorage.com'
```