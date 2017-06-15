# AYS Commands

Since the number of command available in the AYS CLI is quite important, we organized them into groups.  
 - actor
 - blueprint
 - repo
 - run
 - service
 - template
 - generatetoken

Each groups has sub-commands. To inspect the available sub-commands of a groups do `ays group --help`.
E.g:
```shell
ays service --help
Usage: ays service [OPTIONS] COMMAND [ARGS]...

 Group of commands about services

Options:
 --help  Show this message and exit.

Commands:
 delete  Delete a service and all its children Be...
 list    The list command lists all service instances...
 show    show information about a service
 state   Print the state of the selected services.
```

## Basic commands

the following commands show you the typical order in which you need to execute at your service
- [repo create](repo/create.md) creates a new AYS repository
- [blueprint](blueprint/blueprint.md) executes one or more blueprints, converting them into service instances
- [service show](service/show.md) inspect the service that you created during the excuting of the blueprint.
- [run create](run/create.md) creates jobs (runs) for the scheduled actions, and proposes to start the jobs, which then executes the actions
- [generate token](generatetoken.md) Generate an Itsyou.online JWT token based on client_id and client_secret

## Extensive list of all commands
- [actor](actor)  : Grouf of command about to actors.
    - [list](actor/list.md) : list all actor that exist in the current AYS repository.
    - [update](actor/update.md) : Update an actor to a new version.
- [blueprint](blueprint/blueprint.md) : executes one or more blueprints, converting them into service instances.
- [repo](repo) : Group of commands about AYS repositories.
    - [create](repo/create.md) : create a new AYS repository.
    - [destroy](repo/destroy.md) : reset all services & recipe's in current repo (DANGEROUS) all instances will be lost !!!
    - [list](repo/list.md) :  List all known repositories.
    - [delete](repo/delete.md) : delete repo.
- [run](run) : Group of commands about runs.
    - [create](run/create.md) : creates jobs (runs) for the scheduled actions, and proposes to start the jobs, which then executes the actions.
    - [list](run/list.md) : List all the keys and creation date of the previous runs.
    - [show](run/show.md) : Print the detail of a run.
- [service](service) : Group of commands aobut services.
    - [delete](service/delete.md) : Delete a service and all its children.
    - [list](service/list.md) : List services.
    - [show](service/show.md) : Show information about a service.
    - [state](service/state.md) : Show actions state of a service.
- [start](start/start.md) : start AYS server.
- [template](template) : Groupf of commands about actor templates
    - [list](template/list): List available template to be used in a blueprint.

```toml
!!!
title = "AYS Commands Intro"
tags= ["ays"]
date = "2017-03-02"
categories= ["ays_cmd"]
```
