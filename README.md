# vsftpd
Very Secure File Transfer Protocol

## How to build the container
```
docker build -t vsftpd .
```

## How to use the container

### Configuration
Vsftpd server uses a config file (`/etc/vsftpd/vsftpd.conf`) on the host, this file needs to be created first.

Example config file can be found [here](https://github.com/container-images/vsftpd/blob/master/tests/files/configurations/anonymous_enabled/vsftpd.conf).

For default config file, run this command before running container as advised in example usage:
```
$ id=$(docker create vsftpd)
$ docker cp $id:/etc/vsftpd/vsftpd.conf <path-to-destination>
$ docker rm -v $id
```
For the container to function correctly, ```background=NO``` has to be specified in the conf file.

### Example usage:

```
$ docker run -p 20:20 -p 21:21 -p 21100-21110:21100-21110 \
--rm -v /etc/vsftpd/:/etc/vsftpd/ \
-v <shared files directory>:/var/ftp/pub \
--name vsftpd vsftpd
```

## Running in passive mode

Add following lines to the configuration file:
```
pasv_enable=Yes
pasv_max_port=10100
pasv_min_port=10090
```

Find your zone. In this case, zone is 'public':
```
# firewall-cmd --get-active-zones
public
  interfaces: eth0
```
Open files on firewall:
```
# firewall-cmd --permanent --zone=public --add-port=10090-10100/tcp
# firewall-cmd --reload
```
Run the container:
```
$ docker run -P \
--rm -v /etc/vsftpd/:/etc/vsftpd/ \
--name vsftpd vsftpd
```


## Extending using source-to-image

You are able to extend this container image using [source-to-image](https://github.com/openshift/source-to-image):

* supply a custom script which will be executed before running vsftpd
* supply a configuration file on your own

In order to extend the image using s2i, you need to prepare a directory with following structure:
```
$ tree vsftpd-extension
vsftpd-extension
├── init-hook
└── vsftpd.conf
```

There is a sample extension directory provided in this repo, named `./default-conf`.

Both files are optional. But you should supply at least one, what would be the point of supplying neither, right?

The file init-hook will be sourced using default shell. You can take a look at a sample init hook at
[`default-conf`](https://github.com/container-images/vsftpd/tree/master/default-conf)
directory and use it:

```
$ git clone https://github.com/container-images/vsftpd && cd vsftpd

$ sudo s2i build $PWD/default-conf modularitycontainers/vsftpd new-vsftpd
I0915 14:46:16.578040 02356 install.go:251] Using "assemble" installed from "image:///usr/local/s2i/assemble"
I0915 14:46:16.578125 02356 install.go:251] Using "run" installed from "image:///usr/local/s2i/run"
I0915 14:46:16.578184 02356 install.go:251] Using "save-artifacts" installed from "image:///usr/local/s2i/save-artifacts"
/opt/app-root/src
'/tmp/src/init-hook' -> './init-hook'
'/tmp/src/vsftpd.conf' -> './vsftpd.conf'
```

The files are copied into the new container image named `new-vsftpd`, we can run it now:

```
$ sudo docker run new-vsftpd
This is an example init hook.
You can put your custom logic here.
Configuration file: ./vsftpd.conf
```

And as you can see, our init script was sourced and vsftpd is now running using our config file.


## Running on OpenShift 

See reference guide: https://blog.openshift.com/getting-any-docker-image-running-in-your-own-openshift-cluster/
