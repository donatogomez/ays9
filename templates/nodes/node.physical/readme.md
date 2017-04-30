# template: node.physical

## Description

This actor template is responsible for specifying a physical node (machine) and granting ssh access to that node.

## Schema

- description: description of the physical node. **optional**
- ports: List of port forwards.
- ipPublic: Public ip of the physical machine.
- sshLogin: Username used for ssh connections.
- sshPassword: Password used for SSH connections.
- sshkey: Key used to authorize ssh connections on this machine.
- sshAddr: Address of the node to connect to.
- sshPort: Port for ssh connections.

## How to use
```yaml
sshkey__key_physical:

node.physical__ovh4:
  ipPublic: '172.17.0.2'
  sshLogin: 'root'
  sshPassword: '<root password>'
  sshAddr: 'localhost'
  sshPort: 22
  sshkey: key_physical

```
A sshkey service need to be specified since `sshkey` parameter consumes the service which is responsible for generating the key.
