# G8OS FileSystem (G8OS FS)

G8OS FS is a virtual file system that simplifies the distribution of files over the grids.

It is written in Go which makes it really simple to deploy on bare metal machines in order to bootstrap an environment, install JumpsScale and the AYS services.

## How it works

### Metadata and binary files

The G8OS FS uses two kinds of files to recreate a file system:

- Metadata files
- Binary files

There is one metadata file for each AYS actor template or AYS service instance.

The following is an excerpt of the metadata files of the `jumpscale__base` services:

```
/opt/jumpscale8/bin/jsnet|8a3e5e03a10ecc3601a1f14fbc371019|4857
/opt/jumpscale8/bin/jsnode|793384b5bde2901461606146adbed382|5088
/opt/jumpscale8/bin/jsportalclient|76f87551c60336da45c379f38625144b|1553
/opt/jumpscale8/bin/jsprocess_monitor|127546640e1f98c3d35bbd03153a1e17|248
/opt/jumpscale8/bin/jsprocess_startAllReset|e839ddaa3d391c9d099cb513d538c62b|184
/opt/jumpscale8/bin/jsprocess|397f026a662f1316421b78e8c6c5b5f7|4506
```

The format is `/$path/$name|$hash|$size`.

The hash is an MD5 hash of the content of the file. It is used to link the metadata with its binary content. It also allows us to create a namespace where the binary content is never duplicated.

The binary content is stored in a directory structure with 3 levels:

- The first two levels are respectivelly the first and second character of the hash of the file
- Tast level contains the actual binary file named with the full MD5 hash

```
a
├── 0
│   ├── a001d62d00fbeb0f1ef4e77e5d8c5e3d
│   ├── a0237c980711ed468f39b5c178ccf875
│   ├── a03e021c3623542e16c47df9799ff8a5
│   ├── a043b3974df8701a8d3cf686690795f8
├── 1
│   ├── a12abc97671995529a05ae1fa73120c9
│   ├── a134ce45aa49528684f9bbc6c2e8042c
│   ├── a139377c7036f280449d8a6746501c18
│   ├── a13bc16af414cc4bdfb9d554c50842d9
...
```

## G8OS FS workflow

When starting, the AYS file system

- Looks in its configuration files which stores can be used
- Looks for the AYS services that need to be exposed in the FUSE and download the corresponding metadata files from a store
- Then as the user opens files, the AYS file system will download the binary files and cache them locally

In a typical environment, multiple layers of caching are available.

To speed up the downloading of the files, some 'grid caches' can exists. These are used the same way as the stores, but they are populated by the G8OS FS as it downloads files and located in the local network of the OpenvCloud nodes.

The G8OS FS will always first look into its local cache for the binary files. If can't find them, it will look into the 'grid caches', and if not found there it will download them from a store.

```
!!!
title = "G8OS FS"
date = "2017-04-08"
tags = []
```
