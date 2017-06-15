# Start AYS

With the below command we make AYS listen on port 5000 on all interface:
```shell
ays start -b 0.0.0.0 -p 5000
```

As a result a new TMUX session will start, attach to it:
```shell
tmux at
```

Next you will probably want to join you container into your ZeroTier network, as documented in [Join Your ZeroTier Network](zt.md).
