# template: autosnapshotting

## Description:
This actor template is responsible to create a periodic snapshots on all machines inside the specified VDC.

## Schema:

- vdc: vdc that the service will work in.
- startDate: Start date at which the autosnapshotting will start.
- endDate: End date at which the autosnapshotting will end taking those periodic snapshots.
- cleanupInterval: The duration interval at which the service periodically scan and remove any snapshots that're expired.


## How to use
example blueprint:
```yaml
autosnapshotting__main:
    vdc: 'autosnapshot'
    retention: '1m'

actions:
    - action: 'install'
    - action: 'snapshot'
      actor: 'autosnapshotting'
      recurring: '1d'
    - action: 'cleanup'
      actor: 'autosnapshotting'
      recurring: '12h'
```
You need to specify the snapshot and cleanup interval in your blueprint, otherwise the recurring action won't happen.
