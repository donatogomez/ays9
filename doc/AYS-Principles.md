# principles

## actor

- delivers a service to other actors
- defined by

  - core properties (actor.hrd or actor.yaml)

    - if has parent and which type
    - which dependencies required (types) = actors required
    - recurring events (period)
    - code recipe (which code required when building)
    - expiration date (optional), after this any self respecting ays robot will discard this actor

  - model (only 1)

    - defines which info is relevant for a service (instance)
    - hrd or capnp schema

  - actions file

    - is the actions which can be executed by the actor
    - is a python file with X methods
    - arguments for each method = ...

  - this info is stored in aysdb as a json object

- methods to start an actor

  - j.atyourservice.actor

    - get()

## service

- is 1 specific service delivered by the actor

  - e.g. I manage a github account
  - e.g. I am a ssh ubuntu OS, I allow apps to run on me

- each service instance has following info

  - ays robot GUID
  - ays logger GUID
  - 1 model object

    - follows the schema
    - format is hrd or capnp object

  - 1 optional expiration date

  - 1 or more optional recurring events: an event launches an action

## ays robot

- executes (recurring) actions for a service contract
- the robot will log the info to specified ays logger
- robot has following methods

  - get(instance_guid,format=json)

    - returns serialized full object for the service instance e.g. in json

  - list(actor_role="",actor_full_id="",instance_id="",dataparts={})

    - uses embedded index to find the relevant instances

  - new(oauth2key,actor_full_id,instance_id,data,format=json)

    - return unique guid for the instance & state

  - do(instance_guid,actionname,data={},format=json)

    - returns

  - wait

## ays logger

- gets logging info from a contract
- the logging info will be stored in ays db

## ays stor

- a global distributed storage db, split in zones
- each entry in the storage db is normally encrypted
- there is no search or list function
- only methods are

  - get
  - set
  - delete (only for the owner)

- each object is owned by only 1 person (is the one who pays & decides to remove)

- each object has a unique key
- each object is uniquely encrypted with the hash of the content
- to be able to read an object there are 3 parts of a key required

  - part 1 = domain key
  - part 2 = location key (position/size/crc)
  - part 3 = encryption key

- to retrieve & store there are only 2 parts required (domain/location key)

- implemented rest methods

  - get(oauth2key,domainkey,lockey)

    - crc will be used to verify data is indeed the data asked for
    - there is protection that for 1 person a certain location can only be asked for X times (this to disalow guessing)

  - delete(oauth2key,domainkey,lockey)

  - set(oauth2key,domainkey,storkey,data)

    - max size = 1 MB

  - mset(oauth2key,domainkey,storkey,data,partnr,size,...) #TBD

    - max size = 1 MB

  - mdelete(...) #TBD

## ays directory service

- -

```
!!!
title = "AYS Principles"
date = "2017-04-08"
tags = []
```
