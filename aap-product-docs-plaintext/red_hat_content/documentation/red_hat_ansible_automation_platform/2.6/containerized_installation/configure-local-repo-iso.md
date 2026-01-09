# 10. Disconnected installation
## 10.1. Obtaining and configuring RPM source dependencies
### 10.1.2. Configuring a local repository from a mounted ISO




You can use a Red Hat Enterprise Linux Binary DVD image to access the necessary RPM source dependencies in a disconnected environment.

**Prerequisites**

- You have downloaded the Red Hat Enterprise Linux Binary DVD image from the [Red Hat Enterprise Linux downloads page](https://access.redhat.com/downloads/content/rhel) and moved it to your disconnected environment.


**Procedure**

1. In your disconnected environment, create a mount point directory to serve as the location for the ISO file:


```
$ sudo mkdir /media/rhel
```


1. Mount the ISO image to the mount point. Replace `    &lt;version_number&gt;` and `    &lt;arch_name&gt;` with suitable values:


```
$ sudo mount -o loop rhel-&lt;version_number&gt;-&lt;arch_name&gt;-dvd.iso /media/rhel
```


- Note: The ISO is mounted in a read-only state.

1. Create a Yum repository file at `    /etc/yum.repos.d/rhel.repo` with the following content:


```
[RHEL-BaseOS]    name=Red Hat Enterprise Linux BaseOS    baseurl=file:///media/rhel/BaseOS    enabled=1    gpgcheck=1    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release        [RHEL-AppStream]    name=Red Hat Enterprise Linux AppStream    baseurl=file:///media/rhel/AppStream    enabled=1    gpgcheck=1    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
```


1. Import the gpg key to allow the system to verify the packages:


```
$ sudo rpm --import /media/rhel/RPM-GPG-KEY-redhat-release
```


1. Verify the repository configuration:


```
$ sudo yum repolist
```




