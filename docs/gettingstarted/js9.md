# Create a JS9 Docker Container

In order to have your own AYS server instance the quickest and easiest way is to create a JumpScale9 Docker container, follow the below steps.

First check, if your private SSH key is loaded:
```shell
ssh-add -l
```

If not loaded:
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

Then:
```shell
export GIGBRANCH="9.0.0"
export GIGSAFE=1
rm -rf $GIGDIR
rm -rf /tmp/jsinit.sh
curl https://raw.githubusercontent.com/Jumpscale/developer/${GIGBRANCH}/jsinit.sh?$RANDOM > /tmp/jsinit.sh
bash /tmp/jsinit.sh
source ~/.jsenv.sh
js9_build -l -p
```

In order to SSH into the container:
```shell
ssh -A root@localhost -p 2222
```

For more details on the JumpScale9 Docker container see https://github.com/Jumpscale/developer#jumpscale-9.

Next you will probably want start the AYS service, as documented in [Start AYS](startays.md).
