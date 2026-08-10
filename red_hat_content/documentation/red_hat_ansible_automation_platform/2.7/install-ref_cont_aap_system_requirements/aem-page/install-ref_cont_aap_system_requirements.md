+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_cont_aap_system_requirements"
title = "System requirements - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_aap_containerized_installation_intro/", "Install containerized Ansible Automation Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_cont_aap_system_requirements/aem-page/install-ref_cont_aap_system_requirements.html"
last_crumb = "System requirements"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "System requirements"
oversized = "false"
page_slug = "install-ref_cont_aap_system_requirements"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-ref_cont_aap_system_requirements"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_cont_aap_system_requirements/toc/toc.json"
type = "aem-page"
+++

# System requirements

Use this information when planning your installation of containerized Ansible Automation Platform.

## Prerequisites

- Configure a dedicated non-root user on the Red Hat Enterprise Linux host.   * This user requires `sudo` or other Ansible supported privilege escalation (`sudo` is recommended) to perform administrative tasks during the installation.
  * This user is responsible for the installation of containerized Ansible Automation Platform.
  * This user is also the service account for the containers running Ansible Automation Platform.
- For each Red Hat Enterprise Linux host in your containerized deployment, configure a dedicated user. The containerized installation program connects as this user to run tasks on the host. For more information about configuring a dedicated user on each host, see [Create the installation user](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_preparing_the_managed_nodes_for_containerized_installation "To ensure a secure containerized setup, create a dedicated user on each Red Hat Enterprise Linux host for the containerized installation program to use when connecting and running tasks.").
- For remote host installations, configure SSH public key authentication for the non-root user. For guidelines on setting up SSH public key authentication for the non-root user, see [How to configure SSH public key authentication for passwordless login](https://access.redhat.com/solutions/4110681).
- Ensure the Red Hat Enterprise Linux host has internet access if you are using the default online installation method.
- Open the appropriate network ports if you have a firewall in place. For more information about the ports to open, see [Container enterprise topology](/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-ref_cont_b_env_a "The container-based enterprise topology provides redundancy and higher compute for large volumes of automation.") in *Tested deployment models*.

Important:

Podman does not support storing container images on an NFS share. To use an NFS share for the user home directory, set up the Podman storage backend path outside of the NFS share. For more information, see [Rootless Podman and NFS](https://www.redhat.com/en/blog/rootless-podman-nfs).

## Ansible Automation Platform system requirements

Your system must meet the following minimum system requirements to install and run Red Hat Ansible Automation Platform.

*Table 1. System configuration*

| Type                 | Description                                                                                                                                                                                              | Notes                                                                                                                                                                                                    |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Subscription     | Valid Red Hat Ansible Automation Platform subscriptionValid Red Hat Enterprise Linux subscription (to consume the BaseOS and AppStream repositories)                                                     |                                                                                                                                                                                                          |
| <br>Operating system | Red Hat Enterprise Linux 9.6 or later minor versions of Red Hat Enterprise Linux 9.Red Hat Enterprise Linux 10 or later minor versions of Red Hat Enterprise Linux 10.                                   |                                                                                                                                                                                                          |
| <br>CPU architecture | <br>x86\_64, AArch64                                                                                                                                                                                     | <br>IBM Z (s390x) and IBM Power (ppc64le) are not supported in Ansible Automation Platform 2.7. For IBM architecture support, use Ansible Automation Platform 2.6.                                       |
| <br> `ansible-core`  | RHEL 9: installation program uses `ansible-core` 2.14, Ansible Automation Platform operation uses `ansible-core` 2.16.RHEL 10: installation program uses `ansible-core` 2.16, Ansible Automation Platform operation uses `ansible-core` 2.16. | The installation program uses the `ansible-core` package from the RHEL AppStream repository.Ansible Automation Platform bundles `ansible-core` 2.16 for operation, so you do not need to install it manually. |
| <br>Browser          | <br>A currently supported version of Mozilla Firefox or Google Chrome.                                                                                                                                   |                                                                                                                                                                                                          |
| <br>Database         | For Ansible Automation Platform managed databases: PostgreSQL 15.For customer provided (external) databases: PostgreSQL 15, 16, or 17.                                                                   | External (customer supported) databases require International Components for Unicode (ICU) support.External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15. |
| <br>IP version       | <br>IPv4, IPv6 (single-stack and dual-stack)                                                                                                                                                             |                                                                                                                                                                                                          |

Each virtual machine (VM) has the following system requirements:

*Table 2. Virtual machine requirements*

| Requirement    | Minimum requirement                                                                                                                                                                                      |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>RAM        | 16 GB32 GB required for growth topology bundled installations with `hub_seed_collections=true`. Seeding the collections can take 45 or more minutes.                                                     |
| <br>CPUs       | <br>4                                                                                                                                                                                                    |
| <br>Local disk | Total available disk space: 60 GBInstallation directory: 15 GB (if on a dedicated partition)`/var/tmp` for online installations: 1 GB`/var/tmp` for offline or bundled installations: 3 GBTemporary directory (defaults to `/tmp`) for offline or bundled installations: 10GB |
| <br>Disk IOPS  | <br>3000                                                                                                                                                                                                 |

## Database requirements

Ansible Automation Platform can work with two varieties of database:

1. Database installed with Ansible Automation Platform - This database consists of a PostgreSQL installation done as part of an Ansible Automation Platform installation using PostgreSQL packages that Red Hat provides.
2. Customer provided or configured database - This is an external database that the customer provides, whether on bare metal, virtual machine, container, or cloud hosted service.

Ansible Automation Platform requires a customer provided (external) database to have International Components for Unicode (ICU) support.
