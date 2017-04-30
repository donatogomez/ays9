# template: network.zerotier

## Description:

This actor template is a helper method for the zerotier_daemon service, it allows a 1 to many relation ship.

## Schema:
 - id = type:string, string id of the zerotier network to connect to.

## Example:
```yaml
sshkey__key1:

 node.physical__nodevm1:
   ip.public: 'ip'
   ssh.login: 'login'
   ssh.password: 'password'
   sshkey: 'key1'
   ssh.port: 22

network.zerotier__gigstorage:
    id: '8056c2e21c000001'

zerotier_daemon__ztrvm1:
    os: 'nodevm1'
    networks: ['gigstorage']
```