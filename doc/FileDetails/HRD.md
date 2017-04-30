# HRD

HRD is the abbreviation for **Human Readable Data**.

We use it as the file format of all configuration files of JumpScale.

The system wide configuration files are in `/optvar/hrd/`.

## Example of an HRD file

```shell
bootstrap.ip=localhost
bootstrap.login=root
bootstrap.passwd=rooter
bootstrap.type=ssh
```

## HRD schema

An HRD schema defines the structure of an HRD file, based on which an HRD file can be generated.

Example:

```shell
email = descr:'comma separated list of email addresses' type:email alias:'mail,mailaddr' @ask list
mobile = descr:'comma separate list of mobile phone nrs' type:tel alias:'tel,landline' @ask list
expire = descr:'format $day:$month:$year' type:date alias:till @ask
test = type:int default:1
testf = type:float default:1.1
testb = type:bool default:False
```

Properties of an HRD schema:

- **descr** describes the field
- **type** for specifying the type of data for the field

  - Can be any of the following values: str, email, int, float, bool, multiline, tel, ipaddr, date
  - Date = epoch (int)

- **default** specifies the default value for the field

- **regex** for validating the entry against a regex
- **minval/maxval** for specifying minimum and maximum values for a field

  - Only relevant for fields of type int

- **multichoice** for specifying a list of items people can choose from, e.g. `'red,blue,orange'`

- **singlechoice** for specifyng a single selection
- **alias** for setting an alias name or multiple alias names for a field
- **@ask** is a tag for specifying that the value needs to be provided for by the user

  - If this is not mentioned then the default value will be used

- **list** to specify that the field is a list

  - Can be a list of integers, strings, ...

- **id** a tag for specifying that the field is the identifier

  - If not specified name = $(instance) will be autoadded

- **consume** to specify the dependencies to other services

  - Format `$role:$minamount:$maxamount,$role2:$min$max, ...`
  - $minamount-$maxamount is optional
  - $role is role of other AYS service, e.g. node (consume service from a node)
  - Example: `node:1:1,redis:1:3`
  - The min-max is important because they define the dependency requirements, e.g. node:1:1 means I need 1 node to be in good shape and if node is not there I cannot function myself.

- **parent** for specifying the role

  - $role is role of other AYS server, e.g. node (consume service from a node)
  - Acts like consume `$role:1:1` but has special (operational) meaning
  - When parent then the service instance will be subdir of parent in ays repo

- **parentauto**

  - is tag to parent
  - means will automatically create the parent if it does not exist yet

Consume example:

```shell
node = type:str list descr:'node on which we are installed' consume:node:1:1
etcd = type:str list consume:etcd:3:3
mongodb = type:str list consume:mongodb:1:3
nameserver = type:str list consume:ns
```

## Get HRD from HRD schema

```
TODO:
```

## Usage As template engine

**Getting application instance HRD's**

```python
TODO: needs to be reworked
hrd=j.application.getAppInstanceHRD(name, instance, domain='jumpscale')
#then e.g. use
j.application.config.applyOnDir
j.application.config.applyOnFile
```

**Getting system wide HRD's**

they are all mapped under j.application.config you can e.g. use following 2 functions to apply your templates to dirs or files

```shell
TODO: needs to be reworked
j.application.config.applyOnDir
j.application.config.applyOnFile
```

to look at the HRD just go in ipshell & print the config

The templating function will look for template params \$(hrdkey) and replace them

you can replace additional arguments e.g:

```python
j.application.config.applyOnDir(adir,additionalArgs={"whoami","kds"})
```

would replace \$(whoami) with kds additional to what found in hrd's

```
!!!
title = "HRD"
date = "2017-04-08"
tags = []
```
