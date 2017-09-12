# vsftpd
Very Secure File Transfer Protocol

## How to build the container
```
docker build -t vsftpd .
```

## How to use the container

### Configuration
Vsftpd server uses a config file (/etc/vsftpd/vsftpd.conf) on the host, this file needs to be created first.
Example config file can be found here: https://github.com/container-images/vsftpd/blob/master/tests/files/configurations/anonymous_enabled/vsftpd.conf.

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
## Running on OpenShift 

See reference guide: https://blog.openshift.com/getting-any-docker-image-running-in-your-own-openshift-cluster/
