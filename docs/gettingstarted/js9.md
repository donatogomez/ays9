# Create a JS9 Docker Container

In order to have your own AYS server instance creating a JumpScale9 Docker container is the easiest and quickest way, just follow the below steps.

Optionally first check if there is already JS9 Docker container running:
```shell
docker ps -a
```

If there is one running, stop and remove it:
```shell
docker stop <CONTAINER ID>
docker rm <CONTAINER ID>
```

And also check and remove all images:
```shell
docker images
docker rmi <IMAGE ID>
```

Then check, if your private SSH key is loaded by ssh-agent:
```shell
ssh-add -l
```

If not loaded, execute:
```shell
eval "$(ssh-agent -s)"
ssh-add -K ~/.ssh/id_rsa
```

Then specify a directory on your host for the volumes that will be mounted in your JS9 Docker container.

On Mac:
```shell
export GIGDIR="/Users/$USER/gig9"
```

Or on Linux:
```shell
export GIGDIR="/home/user/$USER/gig9"
```

Then remove the old directory:
```shell
rm -rf $GIGDIR
```

Now prepare your environment for building a new Docker image and container:
```shell
export GIGBRANCH="9.0.0"
export GIGSAFE=1
rm -rf /tmp/jsinit.sh
curl https://raw.githubusercontent.com/Jumpscale/developer/${GIGBRANCH}/jsinit.sh?$RANDOM > /tmp/jsinit.sh
bash /tmp/jsinit.sh
```

And finally, start the actual building of your image with the `js9_build ` script, which will also start your container with the name `js9_base`:
```
source ~/.jsenv.sh
js9_build -l -p
```

In order to SSH into your `js9_base` container:
```shell
ssh -A root@localhost -p 2222
```

For more details on the JumpScale9 Docker container see https://github.com/Jumpscale/developer#jumpscale-9.

Next you will probably want start the AYS service, as documented in [Start AYS](startays.md).
