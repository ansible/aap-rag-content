# 10. Disconnected installation
## 10.1. Obtaining and configuring RPM source dependencies
### 10.1.1. Configuring a local repository using reposync

With the `reposync` command you can to synchronize the BaseOS and AppStream repositories to a local directory on a Red Hat Enterprise Linux host with an active internet connection. You can then transfer the repositories to your disconnected environment.

**Prerequisites**

- A Red Hat Enterprise Linux host with an active internet connection.

**Procedure**

1. Attach the BaseOS and AppStream repositories using `subscription-manager`, replacing `<RHEL_VERSION>` with your RHEL version number:

$ sudo subscription-manager repos \
--enable rhel-<RHEL_VERSION>-baseos-rhui-rpms \
--enable rhel-<RHEL_VERSION>-appstream-rhui-rpms

2. Install the `yum-utils` package:

$ sudo dnf install yum-utils

3. Synchronize the repositories with the `reposync` command. Replace `<path_to_download>` with a suitable value.

$ sudo reposync -m --download-metadata --gpgcheck \
-p <path_to_download>

For example:

$ sudo reposync -m --download-metadata --gpgcheck \
-p rhel-repos


- Use reposync with the `--download-metadata` option and without the `--newest-only` option for optimal download time.

4. After the `reposync` operation is complete, compress the directory:

$ tar czvf rhel-repos.tar.gz rhel-repos

5. Move the compressed archive to your disconnected environment.

6. On the disconnected environment, create a directory to store the repository files:

$ sudo mkdir /opt/rhel-repos

7. Extract the archive into the `/opt/rhel-repos` directory. The following command assumes the archive file is in your home directory:

$ sudo tar xzvf ~/rhel-repos.tar.gz -C /opt

8. Create a Yum repository file at `/etc/yum.repos.d/rhel.repo` with the following content, replacing `<RHEL_VERSION>` with your RHEL version number:

[RHEL-BaseOS]
name=Red Hat Enterprise Linux BaseOS
baseurl=file:///opt/rhel-repos/rhel-<RHEL_VERSION>-baseos-rhui-rpms
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release

[RHEL-AppStream]
name=Red Hat Enterprise Linux AppStream
baseurl=file:///opt/rhel-repos/rhel-<RHEL_VERSION>-appstream-rhui-rpms
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release

9. Import the gpg key to allow the system to verify the packages, replacing `<RHEL_VERSION>` with your RHEL version number:

$ sudo rpm --import /opt/rhel-repos/rhel-<RHEL_VERSION>-baseos-rhui-rpms/RPM-GPG-KEY-redhat-release

10. Verify the repository configuration:

$ sudo yum repolist

