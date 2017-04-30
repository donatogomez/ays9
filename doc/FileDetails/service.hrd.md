# AYS actor.hrd

This is next to `schema.hrd` and the optional `actions.py` the `actor.hrd` is another optional metadatafile for a service.

It contains information defining:

- Recurring action methods
- Register methods to events.

Below we discuss each of them.

## Recurring section

In the recurring section you define the actions to be executed on an recurring bases.

Example:

The service has 2 recurring actions, monitor and export. Monitor runs every minute and export once a day.

```
recurring.monitor =
    period: 2m,
    log: True,

recurring.export =
    period: 1d,
    log: False,
```

Following conditions apply for values used here:

- Only 3m, 3d and 3h (3 can be any integer value) or just an integer when you mean seconds

## Events subscription

A service can subscribe to 5 types of events:

- email: Execute an action when a mail is received.
- telegram: Execute an action when a message from [Telegram](telegram.org) is received
- alarm: Execute an action when an unexpected event happens
- eco: Execute an action when an error condition happens
- generic: The service receives an generic event object and need to manually decide to react to it or not.

Example of a service that register to two types of event. It will execute the escalate method from the actions.py file when a mail is received and the respond_telegram when a message from [Telegram](telegram.org) is received

```
events.mail.escalate =
    log = True,

events.telegram.respond_telegram =
    log = False,
```

## Build instructions

```
!!!
title = "Service.hrd"
date = "2017-04-08"
tags = []
```
