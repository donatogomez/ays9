# Start

The `start` command will start the API server in a tmux window, allowing the executions of the required AYS actions. The server listening address by default is `127.0.0.1` and listening port is `5000`.

By going to that address it is possible to examine the AYS rest api.

```shell
ays start --help
Usage: ays start [OPTIONS]

  start an ays service in tmux

Options:
  -b, --bind TEXT     listening address
  -p, --port INTEGER  listening port
  --debug             enable debug logging
  --help              Show this message and exit.
```

```toml
!!!
title = "AYS Command Start"
tags= ["ays"]
date = "2017-03-02"
categories= ["ays_cmd"]
```
