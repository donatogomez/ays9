# Blueprint

The `blueprint` command will create all AYS service instances required for the application described by the blueprint.

```shell
ays blueprint --help
Usage: ays blueprint [OPTIONS] [NAME]

  will process the blueprint(s) pointed by name if name is empty    then all
  blueprints found in $aysdir/blueprints will be processed

Options:
  --help  Show this message and exit.
```

The process that takes places is:

- Copy the AYS actor template files to appropriate destination in your AYS repository

  - e.g. `/Users/kristofdespiegeleer1/code/jumpscale/ays_core_it/services/sshkey!main`)

- Call the `actions.input`

  - Goal is to manipulate the arguments which are the basis of the `schema.capnp`, this allows the system to avoid questions to be asked during installations
  - In `actions.input` manipulate the `args` argument to the method
  - Return `True` if action was ok


- Call `actions.init`

  - Now that the input arguments are set, this step allows to further manipulate the service data.

    - Example: create an SSH key and store in the schema

  - After this action the AYS directory is up to date with all required configuration information

  - Information outside can be used to get info in service data, e.g. stats info from Reality DB


  ```toml
  !!!
  title = "AYS Command Blueprint"
  tags= ["ays"]
  date = "2017-03-02"
  categories= ["ays_cmd"]
  ```

```
!!!
title = "Blueprint"
date = "2017-04-08"
tags = []
```
