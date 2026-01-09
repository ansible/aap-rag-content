# 5. Disconnected installation
## 5.4. Accessing RPM repositories from a locally mounted DVD




In disconnected or air-gapped environments, you can install Ansible Automation Platform by using packages from a locally mounted RHEL DVD or ISO image. Learn how to mount the media and configure yum repositories to access BaseOS and AppStream packages for offline installation.

If you plan to access the repositories from the RHEL binary DVD, you must first set up a local repository.

**Procedure**

1. Mount DVD or ISO:


1. DVD


```
# mkdir /media/rheldvd &amp;&amp; mount /dev/sr0 /media/rheldvd
```


1. ISO


```
# mkdir /media/rheldvd &amp;&amp; mount -o loop rhrhel-8.6-x86_64-dvd.iso /media/rheldvd
```



1. Create yum repo file at `    /etc/yum.repos.d/dvd.repo`


```
[dvd-BaseOS]    name=DVD for RHEL - BaseOS    baseurl=file:///media/rheldvd/BaseOS    enabled=1    gpgcheck=1    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release        [dvd-AppStream]    name=DVD for RHEL - AppStream    baseurl=file:///media/rheldvd/AppStream    enabled=1    gpgcheck=1    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
```


1. Import the gpg key:


```
# rpm --import /media/rheldvd/RPM-GPG-KEY-redhat-release
```

Note
If the key is not imported you will see an error similar to


```
# Curl error (6): Couldn't resolve host name for    https://www.redhat.com/security/data/fd431d51.txt [Could not resolve host:    www.redhat.com]
```






**Additional resources**

-  [Need to set up yum repository for locally-mounted DVD on Red Hat Enterprise Linux 9](https://access.redhat.com/solutions/6913101)


