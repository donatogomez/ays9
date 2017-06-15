# template: uservdc

## Description

This template represents an External network

## Schema

- name: Name of the External Network
- subnet: The subnet to add in CIDR notation (x.x.x.x/y)
- gateway: Gateway of the subnet
- startip: First IP Address from the range to add
- endip: Last IP Address from the range to add
- gid: ID of grid
- vlan: VLAN Tag
- accountid: AccountId that has exclusive access to this network Tag
- g8client: User Login
- id: id field to save the externalID in it after creating it
## Example

```yaml
g8client__example:
    url: '<url of the environment>'
    login: '<username>'
    password: '<password>'
    account: '<account name>'

externalnetwork__main:
    name: '<Name>''
    subnet: '<subnet>'  # e.g 10.0.0.0/24"
    gateway: '<gateway>' #e.g "10.0.0.1"
    startip: '<startip>' #e.g "10.0.0.1"
    endip: '<endip>' # e.g "10.0.0.40"
    gid: '<gid>' # e.g 700
    vlan: '<vlan>' # e.g3


actions:
    - action: install
```
to uninstall the externalnetwork use
```
ays action  uninstall -a externalnetwork -s main -f
```
