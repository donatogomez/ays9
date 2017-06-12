#!/bin/bash

# start ays
sudo docker exec js9 js9 'j.atyourservice.server.start()'

# check if the server started
sudo docker exec js9 js9 'cli=j.clients.atyourservice.get();cli.api.ays.listRepositories()'
