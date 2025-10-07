# 2. System requirements
## 2.1. Red Hat Ansible Automation Platform system requirements




Your system must meet the following minimum system requirements to install and run Red Hat Ansible Automation Platform. A resilient deployment requires 10 virtual machines with a minimum of 16 gigabytes (GB) of RAM and 4 virtual CPUs (vCPU). See [Tested deployment models](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models) for more information on topology options.


<span id="idm140151408809808"></span>
**Table 2.1. Base system**

| Type | Description | Notes |
| --- | --- | --- |
|  **Subscription** | Valid Red Hat Ansible Automation Platform subscription |  |
|  **Operating system** | - Red Hat Enterprise Linux 9.4 or later minor versions of Red Hat Enterprise Linux 9 | Red Hat Ansible Automation Platform are also supported on OpenShift, see [Installing on OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/installing_on_openshift_container_platform) for more information. |
|  **CPU architecture** | x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |  |
|  **Ansible-core** | Ansible-core version 2.16 or later | Ansible Automation Platform uses the system-wide ansible-core package to install the platform, but uses ansible-core 2.16 for both its control plane and built-in execution environments. |
|  **Browser** | A currently supported version of Mozilla Firefox or Google Chrome. |  |
|  **Database** | - For Ansible Automation Platform managed databases: PostgreSQL 15.
- For customer provided (external) databases: PostgreSQL 15, 16, or 17. | - External (customer supported) databases require ICU support.
- External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15. |





<span id="idm140151413814464"></span>
**Table 2.2. Virtual machine requirements**

| Component | RAM | VCPU | Disk IOPS | Storage |
| --- | --- | --- | --- | --- |
| Platform gateway | 16GB | 4 | 3000 | 60GB minimum |
| Control nodes | 16GB | 4 | 3000 | 80GB minimum with at least 20GB available under `/var/lib/awx` |
| Execution nodes | 16GB | 4 | 3000 | 60GB minimum |
| Hop nodes | 16GB | 4 | 3000 | 60GB minimum |
| Automation hub | 16GB | 4 | 3000 | 60GB minimum with at least 40GB allocated to `/var/lib/pulp` |
| Database | 16GB | 4 | 3000 | 100GB minimum allocated to `/var/lib/pgsql` |
| Event-Driven Ansible controller | 16GB | 4 | 3000 | 60GB minimum |




Note
These are minimum requirements and can be increased for larger workloads in increments of 2x (for example 16GB becomes 32GB and 4 vCPU becomes 8vCPU). See the horizontal scaling guide for more information.



