FROM registry.fedoraproject.org/fedora:26

# Very Safe FTP Daemon
#
# Volumes:
#  * /home/vsftpd/vsftpd.conf - Home directory with shared files
#  * /var/log/vsftpd - Log file


ENV SUMMARY="Very Secure Ftp Daemon" \
    DESCRIPTION="vsftpd is a Very Secure FTP daemon. It was written completely from scratch." \
    NAME=vsftpd \
    VERSION=0 \
    RELEASE=1 \
    ARCH=x86_64 \
    APP_DATA=/opt/app-root

LABEL maintainer="Dominika Hodovska <dhodovsk@redhat.com>" \
      summary="$SUMMARY" \
      description="$DESCRIPTION" \
      io.k8s.description="$SUMMARY" \
      io.k8s.display-name="Very Safe FTP Daemon" \
      io.openshift.expose-services="fds" \
      io.openshift.tags="vsftpd,ftp" \
      com.redhat.component="$NAME" \
      name="$FGC/$NAME" \
      version="$VERSION" \
      release="$RELEASE.$DISTTAG" \
      architecture="$ARCH" \
      usage="docker run -p 20:20 -p 21:21 -p 21100-21110:21100-21110 --rm -v /etc/vsftpd/:/etc/vsftpd/ -v /var/ftp/pub/:/var/ftp/pub --name vsftpd vsftpd" \
      help="help.1" \
      io.openshift.s2i.scripts-url="image:///usr/local/s2i"

RUN dnf install -y vsftpd && dnf clean all && mkdir /home/vsftpd

VOLUME /var/log/vsftpd

EXPOSE 20 21

RUN mkdir -p ${APP_DATA}/src
WORKDIR ${APP_DATA}/src
COPY ./s2i/bin/ /usr/local/s2i
COPY default-conf/vsftpd.conf /etc/vsftpd/vsftpd.conf

CMD ["/usr/local/s2i/run"]
