
This is an example AYS repo to show how to create a machine on packet.net,  install libvirt kvm/qemu, then create network and stargage pool and a vm.

###### TODO: add portforwarding to vm 

To demo/try out this blueprint, do
```python
# Set this repo to be on "noexec" mode
ays noexec --enable

# Apply these blueprints
ays blueprint

# Run!
ays run
```

If you want to actually create a docker on a vm hosted on openvcloud
 1. create a new ays repo
    ```python
    ays create_repo -g "http://github.com/<account>/<repo>" -p "<path>"
    ```
 2. Copy these blueprints into it
 3. Make it reality!
    ```python
    # Apply these blueprints
    ays blueprint

    # Run!
    ays run
    ```

----------------------------------------
#### Services used:
 - [packetnet_client](../../templates/clients/packetnet_client)
 - [node.packet.net](../../templates/nodes/node.packet.net)
 - [sshkey](../../templates/clients/sshkey)
 - [node.kvm](../../templates/nodes/node.kvm)
 - [openvswitch](../../templates/app/openvswitch)
 - [network.kvm](../../templates/network/network.kvm)
 - [storagepool.kvm](../../templates/disk/storagepool.kvm)
 - [image_os](../../templates/disk/image_os)

#### Useful links:
- More about [AYS noexec](https://github.com/Jumpscale/jumpscale_core8/blob/8.1.0/docs/AYS/Commands/noexe.md)
- More about [AYS](https://gig.gitbooks.io/jumpscale-core8/content/AYS/AYS-Introduction.html)
- More about [AYS repo structure](https://gig.gitbooks.io/jumpscale-core8/content/AYS/FileDetails/FilesDetails.html)
- [packet.net](https://www.packet.net/)
- [kvm](http://www.linux-kvm.org/page/Main_Page)
