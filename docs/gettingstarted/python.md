# Install the Python Client

Install the IPython interactive command shell:
```shell
apt-get update
apt-get install ipython3
```

Install the Python client for AYS:
```shell
pip3 install aysclient
```

Start IPython3:
```shell
ipython3
```

Using the IPython shell:
```python
from aysclient.client import Client
cl = Client("http://<IP address of your AYS server>:5000")
```

And from there you go to `c.ays`, for instance to list all repositories:
```
list=cl.ays.listRepositories()
list.json()
```
