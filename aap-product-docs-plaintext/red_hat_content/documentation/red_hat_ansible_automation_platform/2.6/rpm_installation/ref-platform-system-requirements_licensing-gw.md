# 2. System requirements
## 2.2. Red Hat Ansible Automation Platform system requirements

Your system must meet the following minimum system requirements to install and run Red Hat Ansible Automation Platform. A resilient deployment requires 10 virtual machines with a minimum of 16 gigabytes (GB) of RAM and 4 virtual CPUs (vCPU). See [Tested deployment models](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models) for more information on topology options.

**Table 2.1. Base system**

| Type | Description | Notes |
| --- | --- | --- |
| <br> **Subscription** | <br>  Valid Red Hat Ansible Automation Platform subscription |  |
| <br> **Operating system** | <br>  Red Hat Enterprise Linux 9.4 or later minor versions of Red Hat Enterprise Linux 9 | <br>  Red Hat Ansible Automation Platform are also supported on OpenShift, see [Installing on OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/installing_on_openshift_container_platform) for more information. |
| <br> **CPU architecture** | <br>  x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |  |
| <br> **Ansible-core** | <br>  Ansible-core version 2.16 or later | <br>  Ansible Automation Platform uses the system-wide ansible-core package to install the platform, but uses ansible-core 2.16 for both its control plane and built-in execution environments. |
| <br> **Browser** | <br>  A currently supported version of Mozilla Firefox or Google Chrome. |  |
| <br> **Database** | <br>  For Ansible Automation Platform managed databases: PostgreSQL 15.   For customer provided (external) databases: PostgreSQL 15, 16, or 17. | <br>  External (customer supported) databases require International Components for Unicode (ICU) support.   External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15. |
| <br> **IP version** | <br>  IPv4, IPv6 (single-stack and dual-stack) |  |

**Table 2.2. Virtual machine requirements**

| Component | RAM | vCPU | Disk IOPS | Storage |
| --- | --- | --- | --- | --- |
| <br>  Platform gateway | <br>  16GB | <br>  4 | <br>  3000 | <br>  60GB minimum |
| <br>  Control nodes | <br>  16GB | <br>  4 | <br>  3000 | <br>  80GB minimum with at least 20GB available under `/var/lib/awx` |
| <br>  Execution nodes | <br>  16GB | <br>  4 | <br>  3000 | <br>  60GB minimum |
| <br>  Hop nodes | <br>  16GB | <br>  4 | <br>  3000 | <br>  60GB minimum |
| <br>  Automation hub | <br>  16GB | <br>  4 | <br>  3000 | <br>  60GB minimum with at least 40GB allocated to `/var/lib/pulp` |
| <br>  Database | <br>  16GB | <br>  4 | <br>  3000 | <br>  100GB minimum allocated to `/var/lib/pgsql` |
| <br>  Event-Driven Ansible controller | <br>  16GB | <br>  4 | <br>  3000 | <br>  60GB minimum |

Note

These are minimum requirements and can be increased for larger workloads in increments of 2x (for example 16GB becomes 32GB and 4 vCPU becomes 8vCPU). See the horizontal scaling guide for more information.

