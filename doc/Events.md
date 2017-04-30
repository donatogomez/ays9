# AYS Events

AYS supports events in your services (managed by the `AYSDaemon`)

> `ays start` will run the ays daemon

## Example
Here we have a simple example around two actors `prod`, `cons`, Where `producer` executes a `longjob` and consumer wants to execute some specific action on that event.

### Actor producer

```yaml
msg = type:str default:'hello prince'
```

`actions.py`
```python
def install(job):
    sv = job.service
    print("Done installing the producer")
    cl = j.clients.atyourservice.get().api
    data = { 'command': 'producer_installed'}
    cl.webhooks.webhooks_events_post(data=data)


def longjob(job):
    from time import sleep
    sleep(5)
    cl = j.clients.atyourservice.get().api
    data = {'command': 'producer_longjob_done'}
    cl.webhooks.webhooks_events_post(data)

```

Please note: to fire a new event you need to push a `payload` on the command queue that consists of `command`=`event`, `event`=event_name, `args` is a list of event arguments.

### Actor Consumer
For the consumer

`actions.py`

```python

def init(job):
    service = job.service
    # SET UP EVENT HANDLERS.
    handlers_map = [('producer_installed', ['on_prod_installed']),
                    ('producer_longjob_done', ['on_prod_longjob']),]

    for (event, callbacks) in handlers_map:
        service.model.eventFilterSet(channel='webservice', command=event, actions=callbacks)
    service.saveAll()


def on_prod_installed(job):
    print("*************Producer done with install.")

def on_prod_longjob(job):
    print("************Producer done with the long job")

```
!!!
title = "Events"
date = "2017-04-08"
tags = []
```
