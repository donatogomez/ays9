# Telegram Bot for AYS

## Description

This bot let you manage and run some `ays` projects (repositories) via Telegram.

## Basic demo

This is a basic way to see how the bot works:
```
/start
/project hello
[upload some blueprints]
/ays init
/ays install
```

## Complete usage

The first step to make this bot working for you is to talk with the bot and send `/start` command. Internally this create an environment for you.

Now you are able to create/delete some projects (repositories) via `/project` command:
 * `/project`: without argument will list your projects and tell you which is your running project
 * `/project [name]`: will create or checkout (change current) project called `[name]`
 * `/project delete [name]`: will delete the `[name]` project

A project is a ays repository, to customize it, you'll need to upload some blueprints. Simply upload files to add them to blueprints directory.

You can manage blueprints like projects:
 * `/blueprint`: without argument will list your project's blueprints
 * `/blueprint delete [name]`: will delete `[name]` blueprint
 * `/blueprint [name]`: will show you the blueprint `[name]` contents

To add blueprint, you only can upload files.

When you have a project with blueprints, you can apply some `ays` stuff on it:
 * `/ays init`
 * `/ays do install`
 * ...


## Installation
Generate a token via @botfather on Telegram, then use it to launch this bot:

With a python script:
```python
from js9 import j
bot = j.core.atyourservice.telegramBot('1857YYYY:XXXXXXXXXXXX')
bot.run()
```
Using ays CLI:
`ays bot -token 1857YYYY:XXXXXXXXXXXX`
```shell
ays bot --help
Usage: ays bot [OPTIONS]

Options:
  -t, --token TEXT  Telegram bot token. talk to @BotFather to get one.
  -r, --repo TEXT   Directory where to store the projects
  --help            Show this message and exit.
```
