# How to Change VDC Resource Limits

Two options:
- [Change an existing blueprint](change-an-existing-blueprint)
- [Create a new blueprint](create-a-new-blueprint)


## Change an existing blueprint

Here's the `vdc.yaml` blueprint that will defines a VDC with unlimited resources:
```yaml
g8client__cl:
  url: '{url}'
  login: '{login}'
  password: '{password}'
  account: '{account}'

vdc__{vdc}:
  g8client: 'cl'
  location: '{location}'

actions:
  - action: install
```

In order to deploy the VDC, execute the blueprint and create a new run:
```bash
ays blueprint
ays run create
```

Once deployed, update `vdc.yaml` by simply adding for following line, which limit the number of available external IP addresses to 1:
```yaml
maxNumPublicIP: 1
```

Then execute the blueprint again:
```bash
ays blueprint
```

As a result of again executing `ays blueprint` AYS will notice that something changed to the `vdc` service and change the state of the its `processChange` action to `ok`, as you verify as follows:
```bash
ays service state -r
```

This which will automatically trigger a run of the `processChange` action. So there is no need to create a new run for this.


## Create a new blueprint

Create a new blueprint with the name `change.yaml`:

```yaml
vdc__{vdc}:
  maxNumPublicIP: 2
```

And now only execute the new blueprint, by explicitly specifying the name of the new blueprint as an option to the `ays blueprint` command:
```bash
ays blueprint change.yaml
```

Alternatively you could first deleted the existing, and `ays blueprint` command with options:
```bash
rm blueprints/vdc.yaml
ays blueprint
```

> Note: In case you don't to specify the new blueprint as an option to the `aus blueprint` command, or did not delete the old one first, AYS would execute both blueprints in alphabetic order, and since the `change.yaml` will be processed first, processing `vdc.yaml` would override the change, resulting in no change at all.
