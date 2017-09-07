% VSFTPD(1) Container Image Pages
% Dominika Hodovska
% September 04, 2017

# NAME
vsftpd - Very Secure Ftp Daemon

# DESCRIPTION
vsftpd is a Very Secure FTP daemon. It was written completely from scratch.

The container itself consists of:
    - fedora/26 base image
    - vsftpd RPM package

# USAGE
To get the vsftpd container image on your local system, run the following:

    docker pull hub.docker.io/dhodovsk/vsftpd

# SECURITY IMPLICATIONS
Lists of security-related attributes that are opened to the host.

-p 21
    Opens container port 21 and maps it to the same port on the host.
-p 20
    Opens container port 21 and maps it to the same port on the host.


# SEE ALSO
Vsftpd page
<https://security.appspot.com/vsftpd.html>
