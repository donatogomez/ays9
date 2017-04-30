# Producers & Consumers

Each service instance can consume a service delivered by a producer. A producer is another service instance delivering a service.

The consumption of another service is specified in the `config.yaml` file of a actor template, using the `consume` keyword.

As an example of consumption, see the following `config.yaml` specification:

```yaml
doc:
  property:
  - sshkey: ''

links:
  consume:
  - argname: sshkey
    auto: true
    max: 100
    min: '1'
    role: sshkey

```

This describes that the service consumes a minimum of `1` and a maximum of `100` sshkey instances, and that it should auto-create these instances if they don't already exist. Minimum and maximum tags are optional. As well as `auto`.



```toml
!!!
title = "AYS Producer Consumer"
tags= ["ays","def"]
date = "2017-03-02"
categories= ["ays_def"]
```
