
## start an ays service

 To start the AYS service, use the `ays start` command.

```bash
Usage: ays start [OPTIONS]

start an ays service in tmux

Options:
  -b, --bind TEXT     listening address
  -p, --port INTEGER  listening port
  --debug             enable debug logging
  --help              Show this message and exit.
```

Example:
`ays start --bind 0.0.0.0 --port 8080 --debug`

## go to your ays repository and deploy an example packet.net blueprint

initialize the ays repo

```bash
#create the repo starting from an existing one (is just an existing git repo already created)
ays repo create -n myrepo -g ssh://git@docs.greenitglobe.com:10022/despiegk/cockpit_g8os_testenv.git
# go to the created rep
cd /optvar/cockpit_repos/myrepo
# go into the blueprints directory
cd blueprints
rm -f 1_server.yaml
# get an example blueprint (will launch a g8os on packet.net)
wget https://raw.githubusercontent.com/g8os/ays_template_g8os/master/examples/ays_g8os_packetnet/blueprints/1_server.yaml
cd ..
# init the blueprint in ays
ays blueprint 1_server.yaml
# make the ays reality & follow progress
ays run create --follow

```

## how to see logs

```
ays run show -l
```

## how to see data from ays


```
#shows service info from all services with role node
ays service show --role node
```

## to update your actors in a repo

```bash
cd /optvar/cockpit_repos/myrepo
ays actor update #this will make sure that all templates are used in this repo (so we update the local actors)
```


## remove services from ays

```
ays service delete
```
it will ask which services to remove

##  

```
!!!
title = "AYS Getting Started"
date = "2017-04-08"
tags = []
```
