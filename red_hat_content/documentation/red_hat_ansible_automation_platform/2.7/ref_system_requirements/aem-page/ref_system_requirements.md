+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/ref_system_requirements"
title = "Red Hat Ansible Automation Platform system requirements - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/ref_system_requirements/aem-page/ref_system_requirements.html"
last_crumb = "Red Hat Ansible Automation Platform system requirements"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Red Hat Ansible Automation Platform system requirements"
oversized = "false"
page_slug = "ref_system_requirements"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/ref_system_requirements"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/ref_system_requirements/toc/toc.json"
type = "aem-page"
+++

# Red Hat Ansible Automation Platform system requirements

Your system must meet the following minimum system requirements to install and run Red Hat Ansible Automation Platform.

A resilient deployment requires 10 virtual machines with a minimum of 16 gigabytes (GB) of RAM and 4 virtual CPUs (vCPU). See [Choose a deployment method and topology](/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-assembly_overview_tested_deployment_models "Red Hat tests Ansible Automation Platform with a defined set of topologies to give you opinionated deployment options. Deploy all components of Ansible Automation Platform so that all features and capabilities are available for use without the need to take further action.") for more information on topology options.

*Table 1. Base system*

| Type                 | Description                                                                                                                            | Notes                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>Subscription     | <br>Valid Red Hat Ansible Automation Platform subscription                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <br>Operating system | Red Hat Enterprise Linux 9.6 or later minor versions of Red Hat Enterprise Linux 9                                                     | <br>Red Hat Ansible Automation Platform are also supported on OpenShift, see [Installing on OpenShift Container Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_operator_install_operator "As a system administrator, you can use Ansible Automation Platform Operator to deploy new Ansible Automation Platform instances in your OpenShift environment.") for more information. |
| <br>CPU architecture | <br>x86\_64, AArch64, s390x (IBM Z), ppc64le (IBM Power)                                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <br>Ansible-core     | <br>Ansible-core version 2.16 or later                                                                                                 | <br>Ansible Automation Platform uses the system-wide ansible-core package to install the platform, but uses ansible-core 2.16 for both its control plane and built-in execution environments.                                                                                                                                                                                                                             |
| <br>Browser          | <br>A currently supported version of Mozilla Firefox or Google Chrome.                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <br>Database         | For Ansible Automation Platform managed databases: PostgreSQL 15.For customer provided (external) databases: PostgreSQL 15, 16, or 17. | External (customer supported) databases require International Components for Unicode (ICU) support.External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15.                                                                                                                               |
| <br>IP version       | <br>IPv4, IPv6 (single-stack and dual-stack)                                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                           |

*Table 2. Virtual machine requirements*

| Component                           | RAM      | vCPU  | Disk IOPS | Storage                                                            |
| ----------------------------------- | -------- | ----- | --------- | ------------------------------------------------------------------ |
| <br>Platform gateway                | <br>16GB | <br>4 | <br>3000  | <br>60GB minimum                                                   |
| <br>Control nodes                   | <br>16GB | <br>4 | <br>3000  | <br>80GB minimum with at least 20GB available under `/var/lib/awx` |
| <br>Execution nodes                 | <br>16GB | <br>4 | <br>3000  | <br>60GB minimum                                                   |
| <br>Hop nodes                       | <br>16GB | <br>4 | <br>3000  | <br>60GB minimum                                                   |
| <br>Automation hub                  | <br>16GB | <br>4 | <br>3000  | <br>60GB minimum with at least 40GB allocated to `/var/lib/pulp`   |
| <br>Database                        | <br>16GB | <br>4 | <br>3000  | <br>100GB minimum allocated to `/var/lib/pgsql`                    |
| <br>Event-Driven Ansible controller | <br>16GB | <br>4 | <br>3000  | <br>60GB minimum                                                   |


Note:

These are minimum requirements and can be increased for larger workloads in increments of 2x (for example 16GB becomes 32GB and 4 vCPU becomes 8vCPU). See [Horizontally scale tested deployment models to improve performance](/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-con_horizontal_scaling_for_performance "Horizontal scaling involves increasing the number of replicas (pods or virtual machines) for a given service. Similar to vertical scaling, this approach is useful for high resource utilization or workload scaling.") for more information.

## Repository requirements

Enable the following repositories only when installing Red Hat Ansible Automation Platform:

- RHEL BaseOS
- RHEL AppStream


Note:

If you enable repositories besides those mentioned above, the Red Hat Ansible Automation Platform installation could fail unexpectedly.

The following are necessary for you to work with project updates and collections:

- Ensure that the [Network ports and protocols table](/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-assembly_network_ports_protocols#network-ports-protocols_table "The following table indicates the destination port and the direction of network traffic:") are available for successful connection and download of collections from automation hub or Ansible Galaxy server.

## Additional notes for Red Hat Ansible Automation Platform requirements

- The Ansible Automation Platform database backups are staged on each node at `/var/backups/automation-platform` through the variable `backup_dir`. You might need to mount a new volume to `/var/backups` or change the staging location with the variable `backup_dir` to prevent issues with disk space before running the `./setup.sh -b` script.
- If performing a bundled Ansible Automation Platform installation, the installation setup.sh script attempts to install ansible-core (and its dependencies) from the bundle for you.
- If you have installed Ansible-core manually, the Ansible Automation Platform installation setup.sh script detects that Ansible has been installed and does not attempt to reinstall it.


Note:

You must use Ansible-core, which is installed by using DNF. Ansible-core version 2.16 is required for versions 2.6 and later.
