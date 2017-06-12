# Join Your ZeroTier Network

First check status of the ZeroTier daemon:
```shell
zerotier-cli info
```

In case the ZeroTier daemon is not yet running, launch it:
```shell
zerotier-one -d
```

Check if your container already joined a ZeroTier network:
```shell
zerotier-cli listnetworks
```

If no ZeroTier network was yet joined, join your ZeroTier network:
```shell
export ZEROTIER_NETWORK_ID="..."
zerotier-cli join $ZEROTIER_NETWORK_ID
```

You will now need to go to `https://my.zerotier.com/network/$ZEROTIER_NETWORK_ID` in order to authorize the join request.
