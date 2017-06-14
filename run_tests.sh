#!/bin/bash

# start ays
sudo docker exec js9_base js9 'j.atyourservice.server.start()'

# sleep for 30 seconds
sleep 30

# check if the server started
sudo docker exec js9_base js9 'cli=j.clients.atyourservice.get();cli.api.ays.listRepositories()'
