# ays repo create

```shell
ays repo create [OPTIONS]

  create a new AYS repository

Options:
  -n, --name TEXT  name of the new AYS repo you want to create
  -g, --git TEXT   URL of the git repository to attach to this AYS repository
  --help           Show this message and exit.
```

Example usage :

```shell
$ ays repo create -n test -g http://github.com/user/ays_repo
AYS repository created at /optvar/cockpit_repos/test
```

```toml
!!!
title = "AYS Repo Create"
tags= ["ays"]
date = "2017-03-02"
categories= ["ays_cmd"]
```
