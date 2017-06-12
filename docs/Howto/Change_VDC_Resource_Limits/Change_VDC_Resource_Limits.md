# How to Change VDC Resource Limits

- [Using the AYS CLI client](#cli)
- [Curl](#curl)

<a id="cli"></a>
## Using the AYS CLI client

Two options:
- [Change existing blueprint]()
- [Create a new blueprint]()


### Change existing blueprint

recommended?


Simply add for instance following line:

```yaml
maxNumPublicIP: 1
```

Then:
```
ays blueprint
```

then:
```
ays run create -f
```

-> doesn't work
-> not supported in `processChange()`

...

### Create a new blueprint

?? do I first need to "archive" the old blueprint?
