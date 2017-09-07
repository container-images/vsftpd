# vsftpd
Very Secure File Transfer Protocol

## How to build the container
```
docker build -t vsftpd .
```

## How to use the container

Vsftpd server uses a config file (/etc/vsftpd/vsftpd.conf) on the host, this file needs to be created first.
Default/example config file can be obtained by installing vsftpd on host.
For the container to function correctly, ```background=NO``` has to be specified in the conf file.

Example usage:
```
docker run -p 20:20 -p 21:21 -p 21100-21110:21100-21110 \
--rm -v /etc/vsftpd/:/etc/vsftpd/ \
-v <shared files directory>:/var/ftp/pub \
--name vsftpd vsftpd
```

## Running on OpenShift 

See reference guide: https://blog.openshift.com/getting-any-docker-image-running-in-your-own-openshift-cluster/