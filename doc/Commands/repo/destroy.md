# ays repo destroy

The `destroy` command is quite dangerous since it destroys AYS service instances.

```shell
ays repo destroy [OPTIONS]

  reset all services & recipe's in current repo (DANGEROUS) all instances
  will be lost !!!

  make sure to do a commit before you do a distroy, this will give you a
  chance to roll back.

Options:
  --help  Show this message and exit.
```

```toml
!!!
title = "AYS Repo Destroy"
tags= ["ays"]
date = "2017-03-02"
categories= ["ays_cmd"]
```
