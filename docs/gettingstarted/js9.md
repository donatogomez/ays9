# Create a JS9 Docker Container

In order to have your own AYS server instance the quickest and easiest way is to create a JumpScale9 Docker container:

```shell
export GIGBRANCH="9.0.0"
export GIGSAFE=1
export GIGDIR="/Users/yves/gig9"
rm -rf $GIGDIR
rm -rf /tmp/jsinit.sh
curl https://raw.githubusercontent.com/Jumpscale/developer/${GIGBRANCH}/jsinit.sh?$RANDOM > /tmp/jsinit.sh
bash /tmp/jsinit.sh
source ~/.jsenv.sh
js9_build -l -p
js9_start
```

In order to SSH into the container:
```shell
sudo -s -EH ssh -A root@localhost -p 2222
```

For more details on the JumpScale9 Docker container see https://github.com/Jumpscale/developer#jumpscale-9.
