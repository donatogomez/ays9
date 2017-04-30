# template: vdc

## Description

This actor template creates a cloudspace (Virtual Data Center) on the specified environment. If required cloudspace already exists it will be used.

## Schema

- description: Description of the cloudspace.
- vdcfarm: Specify vdc group.
- g8client: User login.
- account: Account used for this space(if doesn't exist will be created), if empty will use existing account that belongs to the specified user.
- location: Environment to deploy this cloudspace.
- uservdc: Users to have access to this cloudpsace, if a user doesn't exist it will be created.
- allowedVMSizes: Specify the allowed size ids for virtual machines on this cloudspace.
- cloudspaceID: id of the cloudspace (leave empty).
- maxMemoryCapacity: Cloudspace limits, maximum memory.
- maxCPUCapacity: Cloudspace limits, maximum CPU capacity.
- maxDiskCapacity: Cloudspace limits, maximum disk capacity.
- maxNumPublicIP: Cloudspace limits, maximum allowed number of public IPs.
- externalNetworkID: External network to be attached to this cloudspace.

## Example

```yaml
g8client__example:
    url: '<url of the environment>'
    login: '<username>'
    password: '<password>'
    account: '<account name>'

vdcfarm__vdcfarm1:


vdc__cs2:
    description: '<description>'
    vdcfarm: 'vdcfarm1'
    g8client: 'example'
    account: '<account name>'
    location: '<name of the environment>'
    uservdc:
        - '<username to give access to>'
    allowedVMSizes:
        - 1
        - 2
```
