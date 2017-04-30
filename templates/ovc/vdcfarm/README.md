# template: vdcfarm

## Description

Used for logical grouping of cloudspaces. For example: having a farm for cloudpsaces used as databases.

## Schema

- description: Description of the farm.

## Example

```yaml
vdcfarm__vdcfarm1:


  vdc__cs2:
      description: '<description>'
      vdcfarm: 'vdcfarm1'
      g8client: 'example'
      account: '<account name>'
      location: '<name of the environment>'
      uservdc:
          - '<username to give access to>'
```
