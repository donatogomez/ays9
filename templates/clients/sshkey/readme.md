# Template: sshkey
Used to manage your remote ays services through  by `consuming existing ones` or `generating new ones.`

## Schema
```
key.path = type:str
key.name = type:str
key.passphrase= type:str default:'' descr:'Specify passphrase (default is empty)'
key.priv = type:str
key.pub = type:str
```
where:
- `key.path`: is the path of an existing key to be used.
- `key.name`: sshkey name (can be used to get the path of the sshkey by its name).
- `key.passphrase`: sshkey passphrase.
- `key.priv`: private sshkey.
- `key.pub`: public sshkey.


## preferred method specify name of loaded ssh key

```yaml
sshkey__main:
    key.name: ovh_install
```

## Example (using `key.path`)

```
root@myjs8xenial:/opt/repos/testssh# ls /root/.ssh/
dns_rsa  dns_rsa.pub  known_hosts
root@myjs8xenial:/opt/repos/testssh# cat blueprints/1_test.yaml

```

```yaml
sshkey__main:
    key.path: /root/.ssh/dns_rsa
```

### usage through jumpscale script

Here we make sure to use the `dns_rsa` key by setting its path.

```python3
In [1]: repo = j.atyourservice.server.repoGet("/opt/repos/testssh")

In [2]: repo.services
Out[2]: [service:sshkey!main]

In [3]: ss=repo.services[0]

In [4]: ss
Out[4]: service:sshkey!main

In [5]: ss.model.data
Out[5]: <schema_87832e6cdcb81edf_capnp:Schema builder (keyPath = "/opt/repos/testssh/services/sshkey!main/id_rsa", keyName = "", keyPassphrase = "", keyPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAzw9d+SNDrte75YkYIeQRGzDpRn7Dgppo/Go8NvAECZIp4Hfn\ntB8aab/y0FIJcE/DHGhg/GzDTkJQC1PtvM5EiM20XaAuKOcdssLV56psPJ4GdRC2\nhhgepGW7REqBO6M1ooSFPA+JKXOhsX8yh+4l93wTmI7CrQ2nki0A+onUzh8I8yUN\nU1sHe5hlkf3RwXQM/VC43FzXAPOXkkxO0QTph94ACKVAmdPzrASMpttwh81qNFX3\nsfL57doGywye5h/b+KulDDfeiVrdL9ifrz9t7qfqamGyLPBz2kegLxIu5OJLCJ6t\nk34F69SBeSXtLyraxQyj+t84H8Jhjw9kk1/UpQIDAQABAoIBACk/F2osoyvuH6je\nwWbm5p1zBdUcJVgb6DP3+Zy7/SHm8t6bJBXWaE2OhhEHdoff6675/+/ovpMVVJqd\nEmuc7zwNNhO8d9WADINymme2pC8DD6g8Nw/JODlpZn95E/tMTL/eBChts9YFCb2w\n5+D6CKgfGEw4jAErCiltO5es4y5X1ktzpMeztAcK1Ts1+mND//kLmLbMwVMCvVIp\nPUQ/jK+7I5xIo7cuDiLLJxV/I6DWo7xKoQeGxL50263mB5zY0cPDtA79e4LkAJh6\nckeLSwGgest7/OQzyxOoLkNXXlFWiw9G1Ocvdw2VOVJKKm+ZRyLIC6Xb8GMCdoMW\nIWMoj5UCgYEA+YhTykE6V8VkXCANckFVNYPSMzcWQ3ehiOaG6/dg60Xpm2LEHA2F\nV1vrnSdzBJVLUjY8h86pOQYQcpfWCpRvg5a6sIESmQe1M0p8yRk1TgdaJ+9lBUyy\n/99DkP3AQ9v6HcwqZ0sGOuDxDLsmzhlvt2TXWyF7jbmdEgf7qohcQQMCgYEA1G07\nB77qbsA++Tove9nOVzV/WbF7rQ2BgWM5nze/2/6enXy27IITU0pnsGbVQEcY/vjv\nWV+OdZnjJZaoa9QGELf1T97J18jqwehvxB1BHjf8lp1x5IEA7uIRViEIJ4kOhlg0\nG/c9IwxflcYa89TPYVcWE+LeZUvzWv0DwWQPnzcCgYBWEJs1y0GgPEjdLYD1w2rs\nRkcduwZGxuBEI56tjGk1PKvSGEKjmlY/R0kArzaQgh20gVhnTvQ24syReaUtiPzd\nWgOSFTKg7XOl+S8I/VTRUN/bnkothcLHVe4r+Bl0Tk76MA0AC3Reom8BgRtlQoix\nrGpK2EWRIE/4hCBdNSL8mQKBgQDKkQrsfPsS95JVmU20feONN/+j6WJ1iF6JorRN\nBx2WzLw2k7nf2L5S+63bAoSykdndMkcT49J2hHOd4Yfjo0DRaoqsSlgRxI9Qr7T8\nv6TcCyl7+tGjw/y+z6cWidM72C+Ynr26OU78gA0aRtpmz/Wd7iyoc/v9fqqmhoWx\nQhi/iwKBgQCtNZIhHXtrFkAUMp40DBDY7zhD67Lm9M8Djham7/VaBwlZX72nZ0Hp\nGTLf5rzJ7DMXFmMfnsIerK1RpJ2RPpK3TOSqKP2DYlbmaVxsokE7j79OLNPr3KtI\ncB8XTMASFU5Zq5wMBNc8VcCjO+DwZnHP3SZBenlYfBFablnyqt0wVA==\n-----END RSA PRIVATE KEY-----", keyPub = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDPD135I0Ou17vliRgh5BEbMOlGfsOCmmj8ajw28AQJkingd+e0Hxppv/LQUglwT8McaGD8bMNOQlALU+28zkSIzbRdoC4o5x2ywtXnqmw8ngZ1ELaGGB6kZbtESoE7ozWihIU8D4kpc6GxfzKH7iX3fBOYjsKtDaeSLQD6idTOHwjzJQ1TWwd7mGWR/dHBdAz9ULjcXNcA85eSTE7RBOmH3gAIpUCZ0/OsBIym23CHzWo0Vfex8vnt2gbLDJ7mH9v4q6UMN96JWt0v2J+vP23up+pqYbIs8HPaR6AvEi7k4ksInq2TfgXr1IF5Je0vKtrFDKP63zgfwmGPD2STX9Sl\n")>

```

## Example using (key.name)

```yaml
sshkey__main:
    key.name: dns_rsa

```

```
root@myjs8xenial:/opt/repos/testssh# eval `ssh-agent -s`
Agent pid 19399
root@myjs8xenial:/opt/repos/testssh# ssh-add /root/.ssh/dns_rsa
Identity added: /root/.ssh/dns_rsa (/root/.ssh/dns_rsa)
root@myjs8xenial:/opt/repos/testssh# ays destroy
root@myjs8xenial:/opt/repos/testssh# ays blueprint
[Wed14 15:10] - ...le/baselib/atyourservice81/Service.py:45   - INFO     - init service main from sshkey
[Wed14 15:10] - .../atyourservice81/AtYourServiceRepo.py:458  - INFO     - init service: service:sshkey!main
init done
blueprint done
root@myjs8xenial:/opt/repos/testssh# js
Python 3.5.2 (default, Nov 17 2016, 17:05:23)
Type "copyright", "credits" or "license" for more information.

IPython 5.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: repo = j.atyourservice.server.repoGet("/opt/repos/testssh")

In [2]: ss=repo.services[0]

In [3]: ss.model.data
Out[3]: <schema_c29d6191fd30b4b7_capnp:Schema builder (keyPath = "/opt/repos/testssh/services/sshkey!main/dns_rsa", keyName = "dns_rsa", keyPassphrase = "", keyPriv = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAzw9d+SNDrte75YkYIeQRGzDpRn7Dgppo/Go8NvAECZIp4Hfn\ntB8aab/y0FIJcE/DHGhg/GzDTkJQC1PtvM5EiM20XaAuKOcdssLV56psPJ4GdRC2\nhhgepGW7REqBO6M1ooSFPA+JKXOhsX8yh+4l93wTmI7CrQ2nki0A+onUzh8I8yUN\nU1sHe5hlkf3RwXQM/VC43FzXAPOXkkxO0QTph94ACKVAmdPzrASMpttwh81qNFX3\nsfL57doGywye5h/b+KulDDfeiVrdL9ifrz9t7qfqamGyLPBz2kegLxIu5OJLCJ6t\nk34F69SBeSXtLyraxQyj+t84H8Jhjw9kk1/UpQIDAQABAoIBACk/F2osoyvuH6je\nwWbm5p1zBdUcJVgb6DP3+Zy7/SHm8t6bJBXWaE2OhhEHdoff6675/+/ovpMVVJqd\nEmuc7zwNNhO8d9WADINymme2pC8DD6g8Nw/JODlpZn95E/tMTL/eBChts9YFCb2w\n5+D6CKgfGEw4jAErCiltO5es4y5X1ktzpMeztAcK1Ts1+mND//kLmLbMwVMCvVIp\nPUQ/jK+7I5xIo7cuDiLLJxV/I6DWo7xKoQeGxL50263mB5zY0cPDtA79e4LkAJh6\nckeLSwGgest7/OQzyxOoLkNXXlFWiw9G1Ocvdw2VOVJKKm+ZRyLIC6Xb8GMCdoMW\nIWMoj5UCgYEA+YhTykE6V8VkXCANckFVNYPSMzcWQ3ehiOaG6/dg60Xpm2LEHA2F\nV1vrnSdzBJVLUjY8h86pOQYQcpfWCpRvg5a6sIESmQe1M0p8yRk1TgdaJ+9lBUyy\n/99DkP3AQ9v6HcwqZ0sGOuDxDLsmzhlvt2TXWyF7jbmdEgf7qohcQQMCgYEA1G07\nB77qbsA++Tove9nOVzV/WbF7rQ2BgWM5nze/2/6enXy27IITU0pnsGbVQEcY/vjv\nWV+OdZnjJZaoa9QGELf1T97J18jqwehvxB1BHjf8lp1x5IEA7uIRViEIJ4kOhlg0\nG/c9IwxflcYa89TPYVcWE+LeZUvzWv0DwWQPnzcCgYBWEJs1y0GgPEjdLYD1w2rs\nRkcduwZGxuBEI56tjGk1PKvSGEKjmlY/R0kArzaQgh20gVhnTvQ24syReaUtiPzd\nWgOSFTKg7XOl+S8I/VTRUN/bnkothcLHVe4r+Bl0Tk76MA0AC3Reom8BgRtlQoix\nrGpK2EWRIE/4hCBdNSL8mQKBgQDKkQrsfPsS95JVmU20feONN/+j6WJ1iF6JorRN\nBx2WzLw2k7nf2L5S+63bAoSykdndMkcT49J2hHOd4Yfjo0DRaoqsSlgRxI9Qr7T8\nv6TcCyl7+tGjw/y+z6cWidM72C+Ynr26OU78gA0aRtpmz/Wd7iyoc/v9fqqmhoWx\nQhi/iwKBgQCtNZIhHXtrFkAUMp40DBDY7zhD67Lm9M8Djham7/VaBwlZX72nZ0Hp\nGTLf5rzJ7DMXFmMfnsIerK1RpJ2RPpK3TOSqKP2DYlbmaVxsokE7j79OLNPr3KtI\ncB8XTMASFU5Zq5wMBNc8VcCjO+DwZnHP3SZBenlYfBFablnyqt0wVA==\n-----END RSA PRIVATE KEY-----", keyPub = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDPD135I0Ou17vliRgh5BEbMOlGfsOCmmj8ajw28AQJkingd+e0Hxppv/LQUglwT8McaGD8bMNOQlALU+28zkSIzbRdoC4o5x2ywtXnqmw8ngZ1ELaGGB6kZbtESoE7ozWihIU8D4kpc6GxfzKH7iX3fBOYjsKtDaeSLQD6idTOHwjzJQ1TWwd7mGWR/dHBdAz9ULjcXNcA85eSTE7RBOmH3gAIpUCZ0/OsBIym23CHzWo0Vfex8vnt2gbLDJ7mH9v4q6UMN96JWt0v2J+vP23up+pqYbIs8HPaR6AvEi7k4ksInq2TfgXr1IF5Je0vKtrFDKP63zgfwmGPD2STX9Sl\n")>


```

## typical usecase blueprint
```yaml
#shortcut for not having to specify the ssh key
sshkey__demo:


g8client__env1:
    # url: 'du-conv-3.demo.greenitglobe.com'
    url: 'gig.demo.greenitglobe.com'
    login: 'login'
    password: 'password'
    account: 'account'

disk.ovc__disk1:
  size: 1000
  type: 'D'

uservdc__thabeta:
  g8client: env1

vdc__v2:
  uservdc:
    - thabeta
  location: 'be-conv-2'
  g8client: env1

node.ovc__n1:
  os.image: "Ubuntu 16.04 x64"
  disk:
    - disk1
  vdc: v2
  ports:
        - '22'
        - '80:80'
        - '443:443'

```
