+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_preparing_the_rhel_host_for_containerized_installation"
template = "docs/aem-title.html"
title = "Prepare the Red Hat Enterprise Linux host - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_preparing_the_rhel_host_for_containerized_installation/aem-page/install-proc_preparing_the_rhel_host_for_containerized_installation.html"
last_crumb = "Prepare the Red Hat Enterprise Linux host"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Prepare the Red Hat Enterprise Linux host"
oversized = "false"
page_slug = "install-proc_preparing_the_rhel_host_for_containerized_installation"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/install-proc_preparing_the_rhel_host_for_containerized_installation"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/install-proc_preparing_the_rhel_host_for_containerized_installation/toc/toc.json"
type = "aem-page"
+++

# Prepare the Red Hat Enterprise Linux host

Containerized Ansible Automation Platform runs the component services as Podman based containers on top of a Red Hat Enterprise Linux host. Prepare the Red Hat Enterprise Linux host to ensure a successful installation.

## Procedure

1.  Log in to the Red Hat Enterprise Linux host as your non-root user.
2.  Ensure that the hostname of your host uses a fully qualified domain name (FQDN).   1.  To check the hostname of your host, run the following command:
  

```
hostname -f
```
        Example output:

```
aap.example.org
```

  2.  If the hostname is not a FQDN, you can set it with the following command:
  

```
$ sudo hostnamectl set-hostname <your_hostname>
```

3.  Register your Red Hat Enterprise Linux host with `subscription-manager`:
  

```
$ sudo subscription-manager register
```

4.  Verify that only the BaseOS and AppStream repositories are enabled on the host:
  

```
$ sudo dnf repolist
```
    Example output for RHEL 9:

```
Updating Subscription Management repositories.
repo id                                                    repo name
rhel-9-for-x86_64-appstream-rpms                           Red Hat Enterprise Linux 9 for x86_64 - AppStream (RPMs)
rhel-9-for-x86_64-baseos-rpms                              Red Hat Enterprise Linux 9 for x86_64 - BaseOS (RPMs)
```
    Example output for RHEL 10:

```
Updating Subscription Management repositories.
repo id                                                    repo name
rhel-10-for-x86_64-appstream-rpms                          Red Hat Enterprise Linux 10 for x86_64 - AppStream (RPMs)
rhel-10-for-x86_64-baseos-rpms                             Red Hat Enterprise Linux 10 for x86_64 - BaseOS (RPMs)
```
  - For disconnected installations, follow the steps in [Obtain and configure RPM source dependencies](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_aap_containerized_disconnected_installation#obtaining-and-configuring-rpm-dependencies "The Ansible Automation Platform containerized setup bundle installation program does not include RPM source dependencies from the BaseOS and AppStream repositories. It relies on the host system’s package manager to resolve these dependencies.") to access these repositories.

5.  Ensure the host can resolve host names and IP addresses using DNS. This is essential to ensure services can talk to one another.
6.  Install `ansible-core`:
  

```
$ sudo dnf install -y ansible-core
```

7.  Optional: Install additional utilities that are useful for troubleshooting purposes, for example `wget`, `git-core`, `rsync`, and `vim`:
  

```
$ sudo dnf install -y wget git-core rsync vim
```

8.  Optional: To have the installation program automatically pick up and apply your Ansible Automation Platform subscription manifest license, follow the steps in [Obtain a manifest file](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_aap_manifest_files#assembly-aap-obtain-manifest-files "You can obtain a subscription manifest in the Subscription Allocations section of Red Hat Subscription Management.").
