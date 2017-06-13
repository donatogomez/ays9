# How to Delete a VDC

Here below we discuss how to delete a VDC using the AYS CLI tool. The same can of course be achieved by directly interacting with the AYS API.

For deleting (uninstalling) a virtual datacenter (VDC) use the **vdc** actor template, available here: https://github.com/Jumpscale/ays_jumpscale8/tree/master/templates/ovc/vdc

In case the AYS service for the VDC you want to delete is already initialized in your AYS repository simply use the following blueprint in order to schedule a run of the `uninstall` action:

```yaml
actions:
  - action: uninstall
    actor: vdc
    service: {vdc-name}
```

Executing this blueprint using `ays blueprint <name-of-blueprint>` will change the state of the `uninstall` action as you can verify by executing the `ays service state -r vdc -n <vdc-name>`:

```bash
State of service : vdc!yvesvdc22
        action_post_              : new
        action_pre_               : new
        check_down                : new
        check_requirements        : new
        check_up                  : new
        cleanup                   : new
        consume                   : new
        data_export               : new
        data_import               : new
        halt                      : new
        init                      : ok
        init_actions_             : new
        input                     : ok
        install                   : ok
        monitor                   : new
        processChange             : new
        removedata                : new
        start                     : new
        stop                      : new
        uninstall                 : scheduled
```

To actually run the scheduled `uninstall` action create a new run:

```bash
ays run create
```

As you'll see this will first run the `stop` action of your VDC:

```bash
Creation of the run...
RUN:5afba073cfae19671b4f7a46144f71d8 (new)
step:1 (new)
- vdc                       vdc1                      | stop            (new)
step:2 (new)
- vdc                       vdc1                      | uninstall       (new)
```

Check the result by again executing the `ays service state -r vdc -n <vdc-name>`:

```bash
State of service : vdc!yvesvdc22
        action_post_              : new
        action_pre_               : new
        check_down                : new
        check_requirements        : new
        check_up                  : new
        cleanup                   : new
        consume                   : new
        data_export               : new
        data_import               : new
        halt                      : new
        init                      : ok
        init_actions_             : new
        input                     : ok
        install                   : new
        monitor                   : new
        processChange             : new
        removedata                : new
        start                     : new
        stop                      : ok
        uninstall                 : running
```

Once completed the state of the `uninstall` action will change from `running` to `ok`:

```bash
State of service : vdc!vdc1
        action_post_              : new
        action_pre_               : new
        check_down                : new
        check_requirements        : new
        check_up                  : new
        cleanup                   : new
        consume                   : new
        data_export               : new
        data_import               : new
        halt                      : new
        init                      : ok
        init_actions_             : new
        input                     : ok
        install                   : ok
        monitor                   : new
        processChange             : new
        removedata                : new
        start                     : new
        stop                      : ok
        uninstall                 : ok
```

The `ok` next to the `Uninstall` indicates uninstallation was successful.

The same can be verified in the `service.json` for the VDC in the `services` directory:

```bash
vi services/vdcfarm\!auto_1/vdc\!vdc1/service.json
```

It also shows the time when the `uninstall` action was executed in the value of `lastRun`:
```json
{
 "actionKey":"c48289ff3c0f835440db344c6f593e4a",
 "errorNr":0,
 "isJob":true,
 "lastRun":1495632505,
 "log":true,
 "name":"uninstall",
 "period":0,
 "state":"ok",
 "timeout":0
}
```

In case the VDC is not yet initialized in your repository, use following blueprint instead:
```yaml
g8client__{environment}:
  url: '{url}'
  login: '{login}'
  password: '{password}'
  account: '{account}'

vdc__{vdc-name}:
  g8client: '{environment}'
  location: '{location}'

actions:
  - action: uninstall
    actor: vdc
    service: {vdc-name}
```

>> Deleting the VDC actor will not automatically call the uninstall() action.
