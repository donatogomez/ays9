# template : node.kvm

## Description:

The actor template represents a virtual machine. Executing the install action will create the node.
uninstall action will delete the virtual machine.
The virtual machine is started using the start action and stopped using the stop action.


## Schema:
 - os: parent os service. *Required*
 - image: image used to run.
 - disks: list of required data disks.
 - nics: name of networks to be used by the machine.
 - memory: specify memory size.
 - cpu: number of cores.
 - ipPublic: automatically set public ip.
 - ipPrivate: automatically set private ip.
 - sshLogin: user to log in.
 - sshPassword: password to login with.

## Example:
```yaml
sshkey__ovh_install:

node.physical__ovh4:
  ipPublic: '172.17.0.2'
  sshLogin: 'root'
  sshPassword: '<root password>'
  sshAddr: 'localhost'
  sshPort: 22
  ports:
      - '112:22'


os.ssh.ubuntu__ovh4:
  sshAddr: 'localhost'
  sshPort: 22
  sshkey: 'ovh_install'
  node: 'ovh4'

openvswitch__kvm_switch:
  os: 'ovh4'

storagepool.kvm__main:
    os: 'ovh4'
    name: 'vms'

image_os__osimg:
  os: 'ovh4'
  url: '<img url>'

network.kvm__net_kvm:
  os: 'ovh4'
  openvswitch: 'kvm_switch'
  name: 'net_kvm'


node.kvm__ubuntutest:
  image: 'osimg'
  os: 'ovh4'
  disks:
      - 10
  memory: 256
  cpu: 1
  nics:
      - 'net_kvm'

os.ssh.ubuntu__kvm_ovh4:
  sshkey: 'ovh_install'
  node: 'ubuntutest'

actions:
    - action: 'install'
```
