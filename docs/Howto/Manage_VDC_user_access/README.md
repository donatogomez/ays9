# How to Manage User Access of a VDC

For granting a user access rights to a virtual datacenter (VDC) you will use a `vdc` blueprint, actually the same blueprint you use for creating a new VDC, as documented in [How to Create a VDC](../Create_VDC/README.md).

The `vdc` blueprint is defined in the `vdc` AYS template, available here: https://github.com/Jumpscale/ays9/tree/master/templates/ovc/vdc

Below we discuss:

- [Blueprint](#blueprint)
- [Example using the AYS CLI tool](#example)

<a id="blueprint"></a>
## Blueprint

```yaml
vdc__{vdc-name}:
  g8client: '{environment}'
  account: '{account}'

  uservdc:
    - `{username_of_new_user}`
    - `{username_of_other_user}`
```

The second user in this blueprint, `{username_of_other_user}`, represents any other user you want to grant access to the VDC, in particular the users that already have access rights. If you don't include them in the blueprint these users will have their access rights revoked.

This blueprint requires that `{environment}` and both the `{username_of_new_user}` and `{username_of_other_user}` are already initialized in the same AYS repository. If not the case you can add them into the same blueprint, or first execute one or more separate blueprint defining these AYS services:

```yaml
g8client__{environment}:
  url: '{url}'
  login: '{login}'
  password: '{password}'
  account: '{account}'

uservdc__{username_of_new_user}:
  g8client: '{environment}'
  email: '{email1}'
  provider: 'itsyouonline'

uservdc__{username_of_other_user}:
  g8client: '{environment}'
  email: '{email2}'
  provider: 'itsyouonline'
```

After having executed the (first) blueprint AYS will notice that something changed to `vdc` service and change the state of the its `processChange` action to `ok`, which will automatically trigger a run of the `processChange` action. So there is no need to create a new run for this.

<a id="example"></a>
## Example using the AYS CLI tool


Create a new repository:
```bash
cd /optvar/cockpit-repos
ays repo create -n testrepo -g http://somewhere
```

First create a blueprint for a new VDC
```bash
vi blueprints/vdc.yaml
```

Here's the definition in one blueprint, including a `actions` section:
```yaml
g8client__gen:
    url: 'du-conv-2.demo.greenitglobe.com'
    login: '****'
    password: '****'
    account: '****'

vdc__testvdc:
    g8client: 'gen'
    location: 'du-conv-2'

actions:
  - action: install
```

Execute the blueprint:
```bash
ays blueprint vdc.yaml
```

This will create the `testvdc` service with the state of its `install` action set to scheduled.

In order to actually run the `install` action you create a run:
```bash
ays run create
```

Now let's create a blueprint to create service for an existing OpenvCloud user. For a user new user, check first the section [How to Create a New OpenvCloud User](../Add_user/README.md):

```bash
vi blueprints/testuser.yaml
```

Here's the blueprint:

```yaml
uservdc__testuser:
  g8client: gen
  provider: 'itsyouonline'
```

Since this is for an existing user, you don't need to specify any actions.

Execute this blueprint:
```bash
ays blueprint testuser.yaml
```

For granting this testuser access to the VDC you created earlier we create a new blueprint:
```bash
vi blueprints/grantaccess.yaml
```

Here's the blueprint:
```yaml
vdc__testvdc:
  uservdc:
    - testuser
```

Execute this blueprint:
```bash
ays blueprint grantaccess.yaml
```

After having executed the (first) blueprint for granting access, you'll notice that the state of the `processChange` action changed from `new` to `ok`:
```bash
ays blueprint <>
ays service state -r vdc

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
        processChange             : ok
        removedata                : new
        start                     : new
        stop                      : ok
        uninstall                 : ok
```

More details are available in the `service.json` for your VDC in the `services` directory:

```json
{
 "actionKey":"086f01c714c60b4b2d0ffeae5c893b10",
 "errorNr":0,
 "isJob":true,
 "lastRun":1495636000,
 "log":true,
 "name":"processChange",
 "period":0,
 "state":"ok",
 "timeout":0
}
```

The `processChange` action will get executed immediately, and doesn't require to create a new run.
