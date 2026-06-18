+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_aap_containerized_disconnected_installation"
template = "docs/aem-title.html"
title = "Install in a disconnected environment - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_aap_containerized_disconnected_installation/aem-page/install-assembly_aap_containerized_disconnected_installation.html"
last_crumb = "Install in a disconnected environment"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Install in a disconnected environment"
oversized = "false"
page_slug = "install-assembly_aap_containerized_disconnected_installation"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-assembly_aap_containerized_disconnected_installation"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-assembly_aap_containerized_disconnected_installation/toc/toc.json"
type = "aem-page"
+++

# Install in a disconnected environment

You can install containerized Ansible Automation Platform in an environment that does not have an active internet connection. To do this you need to obtain and configure the RPM source dependencies before performing the disconnected installation.

## Obtain and configure RPM source dependencies

The Ansible Automation Platform containerized setup bundle installation program does not include RPM source dependencies from the BaseOS and AppStream repositories. It relies on the host system’s package manager to resolve these dependencies.

### Procedure

 Use one of the following methods to access these dependencies in a disconnected environment:

- Use [Red Hat Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html/installing_satellite_server_in_a_disconnected_network_environment/index) to synchronize repositories in your disconnected environment.
- Use a local repository that you create with the `reposync` command on a Red Hat Enterprise Linux host that has an active internet connection.
- Use a local repository that you create from a mounted Red Hat Enterprise Linux Binary DVD ISO image.

### Configure a local repository using reposync

With the `reposync` command you can to synchronize the BaseOS and AppStream repositories to a local directory on a Red Hat Enterprise Linux host with an active internet connection. You can then transfer the repositories to your disconnected environment.

#### Before you begin

- A Red Hat Enterprise Linux host with an active internet connection.

#### Procedure

1.  Attach the BaseOS and AppStream repositories using `subscription-manager`, replacing `<RHEL_VERSION>` with your RHEL version number:
  

```
$ sudo subscription-manager repos \
    --enable rhel-<RHEL_VERSION>-baseos-rhui-rpms \
    --enable rhel-<RHEL_VERSION>-appstream-rhui-rpms
```

2.  Install the `yum-utils` package:
  

```
$ sudo dnf install yum-utils
```

3.  Synchronize the repositories with the `reposync` command. Replace `<path_to_download>` with a suitable value.

```
$ sudo reposync -m --download-metadata --gpgcheck \
    -p <path_to_download>
```
    For example:

```
$ sudo reposync -m --download-metadata --gpgcheck \
    -p rhel-repos
```
  - Use reposync with the `--download-metadata` option and without the `--newest-only` option for optimal download time.

4.  After the `reposync` operation is complete, compress the directory:
  

```
$ tar czvf rhel-repos.tar.gz rhel-repos
```

5.  Move the compressed archive to your disconnected environment.
6.  On the disconnected environment, create a directory to store the repository files:
  

```
$ sudo mkdir /opt/rhel-repos
```

7.  Extract the archive into the `/opt/rhel-repos` directory. The following command assumes the archive file is in your home directory:
  

```
$ sudo tar xzvf ~/rhel-repos.tar.gz -C /opt
```

8.  Create a Yum repository file at `/etc/yum.repos.d/rhel.repo` with the following content, replacing `<RHEL_VERSION>` with your RHEL version number:
  

```
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
```

9.  Import the gpg key to allow the system to verify the packages, replacing `<RHEL_VERSION>` with your RHEL version number:
  

```
$ sudo rpm --import /opt/rhel-repos/rhel-<RHEL_VERSION>-baseos-rhui-rpms/RPM-GPG-KEY-redhat-release
```

10.  Verify the repository configuration:
  

```
$ sudo yum repolist
```

### Configure a local repository from a mounted ISO

You can use a Red Hat Enterprise Linux Binary DVD image to access the necessary RPM source dependencies in a disconnected environment.

#### Before you begin

- You have downloaded the Red Hat Enterprise Linux Binary DVD image from the [Red Hat Enterprise Linux downloads page](https://access.redhat.com/downloads/content/rhel) and moved it to your disconnected environment.

#### Procedure

1.  In your disconnected environment, create a mount point directory to serve as the location for the ISO file:
  

```
$ sudo mkdir /media/rhel
```

2.  Mount the ISO image to the mount point. Replace `<version_number>` and `<arch_name>` with suitable values:
  

```
$ sudo mount -o loop rhel-<version_number>-<arch_name>-dvd.iso /media/rhel
```
  Note:
  The ISO is mounted in a read-only state.

3.  Create a Yum repository file at `/etc/yum.repos.d/rhel.repo` with the following content:
  

```
[RHEL-BaseOS]
name=Red Hat Enterprise Linux BaseOS
baseurl=file:///media/rhel/BaseOS
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release

    [RHEL-AppStream]
name=Red Hat Enterprise Linux AppStream
baseurl=file:///media/rhel/AppStream
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
```

4.  Import the gpg key to allow the system to verify the packages:
  

```
$ sudo rpm --import /media/rhel/RPM-GPG-KEY-redhat-release
```

5.  Verify the repository configuration:
  

```
$ sudo yum repolist
```

### Perform a disconnected installation

A disconnected installation installs containerized Ansible Automation Platform without requiring network access to external registries.

#### Before you begin

- You have prepared the Red Hat Enterprise Linux host
- You have obtained and configured the RPM source dependencies. The installation program uses your host system’s `dnf` package manager to resolve these dependencies.
- You have prepared the managed nodes
- You have downloaded the containerized Ansible Automation Platform setup bundle from the [Ansible Automation Platform download page](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software).

#### Procedure

1.  Log in to the Red Hat Enterprise Linux host as your non-root user.
2.  Update the inventory file by following the steps in [Configure the inventory file](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-ref_configuring_inventory_file#configuring-inventory-file___inventory_file_for_online_installation_for_containerized_enterprise_topology). Note:
      Do not include `registry_username` or `registry_password` in your inventory file for disconnected installations. These variables are only required for online installations. All container images are pre-packaged in the setup bundle.

3.  Ensure you include the following variables in your inventory file under the `[all:vars]` group:
  

```
bundle_install=true
# The bundle directory must include /bundle in the path
bundle_dir='{{ lookup("ansible.builtin.env", "PWD") }}/bundle'
```

4.  Follow the steps in [Install containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_installing_containerized_aap#installing-containerized-aap "Run the install playbook to install containerized Ansible Automation Platform after preparing the Red Hat Enterprise Linux host, downloading the installation program, and configuring the inventory file.") to install containerized Ansible Automation Platform and verify your installation.
