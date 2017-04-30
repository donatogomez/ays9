# AYS Blueprints

An AYS _blueprint_ is a [YAML](http://yaml.org/) file used as the entry point for interacting with AYS. It describes the deployment of a specific application.

It does so by defining all service instances that make up a specific application and how these AYS services instances interact with each other.

Example:

```yaml
redis_redis1:
  description:
    - "a description"

redis_redis2:
  description:
    - "a description"

myapp_test:
  redis: 'redis1, redis2'
```

The above example is about the `test` application using two instances of the `Redis`.

```toml
!!!
title = "AYS Blueprints"
tags= ["ays","def"]
date = "2017-03-02"
categories= ["ays_def"]
```
