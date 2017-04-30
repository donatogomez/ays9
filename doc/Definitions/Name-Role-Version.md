# Service Name & Role

Each AYS service has a name and a role.

For example in `node.ovc`:

- The name of the service is `node.ovc`
- The role of the service is `node`. So a role is the first part of the name before the `.` (dot). Multiple actor template can have the same role, but a name needs to be unique.

Roles are used to define categories of actors.

For instance, "node.physical", "node.docker" and "node.kvm" all serve the role "node".


```toml
!!!
title = "AYS Role Version"
tags= ["ays","def"]
date = "2017-03-02"
categories= ["ays_def"]
```
