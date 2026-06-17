# Install in a disconnected environment

If you are not connected to the internet or do not have access to online repositories, you can install Red Hat Ansible Automation Platform without an active internet connection.

## Ansible Automation Platform installation on disconnected RHEL

For a disconnected installation, use the setup bundle with the automation controller's installer-managed database. This bundle simplifies the process by including all necessary Red Hat package managers (RPMs) and default execution environment (EE) images within the package.

### System requirements for disconnected installation

Ensure that your system has all the hardware requirements before performing a disconnected installation of Ansible Automation Platform. You can find these in **System requirements**.

Before installing Ansible Automation Platform on a disconnected network, you must meet the following prerequisites:

- A subscription manifest that you can upload to the platform.


For more information, see **Manage Ansible Automation Platform subscriptions, updates, and support**.

- The Ansible Automation Platform setup bundle at the**Customer Portal** is downloaded.
- The DNS records for the automation controller and private automation hub servers are created.

### Obtain and configure RPM source dependencies

RPM dependencies for Ansible Automation Platform that come from the BaseOS and AppStream repositories are not included in the setup bundle. To add these dependencies, you must first obtain access to BaseOS and AppStream repositories. Use Satellite to sync repositories and add dependencies. If you prefer an alternative tool, you can choose between the following options:

- Reposync
- The RHEL Binary DVD


Note:

The RHEL Binary DVD method requires the DVD for supported versions of RHEL. See **Red Hat Enterprise Linux Life Cycle** for information on which versions of RHEL are currently supported.

### Synchronize the RPM repositories by using reposync

To perform a reposync you need a Red Hat Enterprise Linux host that has access to the internet. After the repositories are synced, you can move the repositories to the disconnected network hosted from a web server.

#### About this task

When downloading RPM, ensure you use the applicable distro.

#### Procedure

1.  Attach the BaseOS and AppStream required repositories:


```
# subscription-manager repos \
--enable rhel-9-for-x86_64-baseos-rpms \
--enable rhel-9-for-x86_64-appstream-rpms
```

2.  Perform the reposync:


```
# dnf install yum-utils
# reposync -m --download-metadata --gpgcheck \
-p /path/to/download
```
1.  Use reposync with `--download-metadata` and without `--newest-only`. See [RHEL 8](https://access.redhat.com/solutions/5186621) Reposync.     - If you are not using `--newest-only,` the repos downloaded may take an extended amount of time to sync due to the large number of GB.
- If you are using `--newest-only,` the repos downloaded may take an extended amount of time to sync due to the large number of GB.

After the reposync is completed, your repositories are ready to use with a web server.

3.  Move the repositories to your disconnected network.

### Create a new web server to host repositories

Create and configure a dedicated web server to host repositories for a disconnected environment. This procedure ensures local access to synchronized RPM packages and enables you to streamline content installation and updates on isolated systems.

#### About this task

#### Procedure

1.  Install prerequisites:


```
$ sudo dnf install httpd
```

2.  Configure httpd to serve the repo directory:


```
/etc/httpd/conf.d/repository.conf

DocumentRoot '/path/to/repos'

<LocationMatch "^/+$">
Options -Indexes
ErrorDocument 403 /.noindex.html
</LocationMatch>

<Directory '/path/to/repos'>
Options All Indexes FollowSymLinks
AllowOverride None
Require all granted
</Directory>
```

3.  Ensure that the directory is readable by an apache user:


```
$ sudo chown -R apache /path/to/repos
```

4.  Configure SELinux:


```
$ sudo semanage fcontext -a -t httpd_sys_content_t "/path/to/repos(/.*)?"
$ sudo restorecon -ir /path/to/repos
```

5.  Enable httpd:


```
$ sudo systemctl enable --now httpd.service
```

6.  Open firewall:


```
$ sudo firewall-cmd --zone=public --add-service=http –add-service=https --permanent
$ sudo firewall-cmd --reload
```

7.  On automation services, add a repo file at */etc/yum.repos.d/local.repo*, and add the optional repos if needed:


```
[Local-BaseOS]
name=Local BaseOS
baseurl=http://<webserver_fqdn>/rhel-8-for-x86_64-baseos-rpms
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release

[Local-AppStream]
name=Local AppStream
baseurl=http://<webserver_fqdn>/rhel-8-for-x86_64-appstream-rpms
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
```

### Access RPM repositories from a locally mounted DVD

In disconnected or air-gapped environments, you can install Ansible Automation Platform by using packages from a locally mounted RHEL DVD or ISO image. Learn how to mount the media and configure yum repositories to access BaseOS and AppStream packages for offline installation.

#### About this task

If you plan to access the repositories from the RHEL binary DVD, you must first set up a local repository.

#### Procedure

1.  Mount DVD or ISO:
1.  DVD


```
# mkdir /media/rheldvd && mount /dev/sr0 /media/rheldvd
```

2.  ISO


```
# mkdir /media/rheldvd && mount -o loop rhrhel-8.6-x86_64-dvd.iso /media/rheldvd
```

2.  Create yum repo file at `/etc/yum.repos.d/dvd.repo`


```
[dvd-BaseOS]
name=DVD for RHEL - BaseOS
baseurl=file:///media/rheldvd/BaseOS
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release

[dvd-AppStream]
name=DVD for RHEL - AppStream
baseurl=file:///media/rheldvd/AppStream
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
```

3.  Import the gpg key:


```
# rpm --import /media/rheldvd/RPM-GPG-KEY-redhat-release
```
Note:
If the key is not imported you will see an error similar to

```
# Curl error (6): Couldn't resolve host name for
https://www.redhat.com/security/data/fd431d51.txt [Could not resolve host:
www.redhat.com]
```

### Download and install the Ansible Automation Platform setup bundle

Choose the setup bundle to download Ansible Automation Platform for disconnected installations. This bundle includes the RPM content for Ansible Automation Platform and the default execution environment images that will be uploaded to your private automation hub during the installation process.

#### About this task

#### Procedure

1.  Download the Ansible Automation Platform setup bundle package by navigating to the [Red Hat Ansible Automation Platform download](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software) page and clicking Download Now for the Ansible Automation Platform 2.6 Setup Bundle.
2.  On control node, untar the bundle:


```
$ tar xvf \
ansible-automation-platform-setup-bundle-2.6-1.tar.gz
$ cd ansible-automation-platform-setup-bundle-2.6-1
```

3.  Edit the inventory file to include variables based on your host names and desired password values.
