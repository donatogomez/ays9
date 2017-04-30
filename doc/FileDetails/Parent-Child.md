# AYS Parent/Child Relationship

A service can be a parent for other services.

It's just a way of organizing your services and grouping them.

Child services are created in a subdirectory of its parent.

## Example

Example of `parent` in `config.yaml`:

```yaml
doc:
  property:
  - node: ''
links:
  parent:
    auto: true
    optional: false
    role: node
    argname: 'node'
```

- This means that the service has a parent of role `node` and that it should auto create its parent if it doesn't already exist.
- The `auto` tag is optional and means that we will look if there is a parent if right type if yes will use that one
- The `optional` tag is optional and means that the parent relationship is not required


## Example deployed:

Considering the following blueprint:

```yaml
datacenter__eu:
    location: 'Europe'
    description: 'Main datacenter in Europe'

datacenter__us:
    location: 'USA'
    description: 'Main datacenter in USA'


rack__storage1:
    datacenter: 'eu'
    location: 'room1'
    description: 'rack for storage node'

rack__storage2:
    datacenter: 'eu'
    location: 'room1'
    description: 'rack for storage node'

rack__cpu1:
    datacenter: 'us'
    location: 'east building'
    description: 'rack for cpu node'

rack__storage4:
    datacenter: 'us'
    location: 'west buuilding'
    description: 'rack for cpu node'
```

In this example the `rack` service use the datacenter service as parent.<br>
After execution of the command `ays repo blueprint`, the service tree will look like that:

```shell
$ tree services/
services/
├── datacenter!eu
│   ├── data.json
│   ├── schema.capnp
│   ├── rack!storage1
│   │   ├── data.json
│   |   ├── schema.capnp
│   │   └── service.json
│   ├── rack!storage2
│   │   ├── data.json
│   |   ├── schema.capnp
│   │   └── service.json
│   └── service.json
└── datacenter!us
    ├── data.json
    ├── schema.capnp
    ├── rack!cpu1
    │   ├── data.json
    |   ├── schema.capnp
    │   └── service.json
    ├── rack!storage4
    │   ├── data.json
    |   ├── schema.capnp
    │   └── service.json
    └── service.json

```

```
!!!
title = "Parent Child"
date = "2017-04-08"
tags = []
```
