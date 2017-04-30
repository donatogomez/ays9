# Automate the Creation of 2 Virtual Machines in OpenvCloud

(UNCOMPLETE)

Following blueprint will:

- Create a virtual machine
- Inside the virtual machine: (see the [Docker example](DockerExample.md) for more details)

  - Create a Docker container with AYS called master
  - Create a Docker container with AYS called client
  - Install JumpScale in both Docker containers
  - Install JumpScale AgentController8 in master
  - Install JumpScale Agent8 in client
  - Do a test where a command gets executed on client from master & return works

Remarks:

- All Docker based
- Start from Ubuntu 15.04 or 14.04 64 bit, use jsdocker way of working (see docs)
- Start from env arguments for ms1 passwd, rest in ays instance ovc_client
- If password env arguments not filled in dynamically ask for it

# TODO: complete

```
g8_client__main:
    g8.account: {g8.account}
    g8.url: {g8.url}
    g8.password: {g8.password}

sshkey__main:

vdcfarm__main:

vdc__spacename:
    vdcfarm: main

node.ovc__vm:
    vdc: spacename
    ports: '80:80, 443:443, 18384:18384'
    sshkey: 'main
    os.image: 'Ubuntu 16.04 x64'

os.ssh.ubuntu__os:
    node: vm
```

```toml
!!!
title = "AYS OVC Example"
tags= ["ays"]
date = "2017-03-02"
categories= ["ays_example"]
```
