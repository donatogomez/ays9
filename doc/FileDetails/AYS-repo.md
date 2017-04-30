# AYS Repo

This is the main repository in which services are deployed, executed, ...

Following 4 directories are relevant in an AYS repo:

- **blueprints**

  - Contains blueprints (YAML files) defining what needs to be done

- **actortemplates**

  - Local set of AYS actor templates
  - AYS will always first look here for an AYS actor template, and if not found, will look in the available actor template repos as discussed above to know where to get the AYS actor template

- **actor**

  - Here all the local copies of the AYS actor template are stored
  - From the AYS service recipes one or more service instances are created
  - Has no further meaning than being a local copy, this is done to be able to see changes in the template on local (Git) repo level

- **services**

  - Here the actual expanded services instances live
  - A `service.json` file which has checksums of all actions defined to track updated as well states and results of the executing actions and some metadata.
  - A `data.json` file has all the info as required to make a deployment reality (install)
  - An `schema.capnp` file which contains the service schema to be configured by the data.

```
!!!
title = "AYS Repo"
date = "2017-04-08"
tags = []
```
