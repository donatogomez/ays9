# Parents & Children

A service can be a parent for other services.

It's just a way of organizing your services and grouping them.

You will typically do it for indicating some kind of child/parent relationship, e.g. an app living inside a node.

The parent/child relationship defines the location in the AYS repo directory structure (so purely visualization).

Child services also inherit their parent's executor defined in `getExecutor` by default.

See the section [Parent/Child](../FileDetails/Parent-Child.md) for more information on this topic.


```toml
!!!
title = "AYS Parent Children"
tags= ["ays","def"]
date = "2017-03-02"
categories= ["ays_def"]
```
