# 2. Upgrading to Red Hat Ansible Automation Platform 2.6
## 2.1. Upgrade prerequisites
### 2.1.2. System requirements




| Type | Description | Notes |
| --- | --- | --- |
|  **Subscription** | Valid Red Hat Ansible Automation Platform subscription |  |
|  **Operating system** | Red Hat Enterprise Linux 9.4 or later minor versions of Red Hat Enterprise Linux 9 | Red Hat Ansible Automation Platform are also supported on OpenShift, see [Installing on OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/installing_on_openshift_container_platform) for more information. |
|  **CPU architecture** | x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |  |
|  **Ansible-core** | Ansible-core version 2.16 or later | Ansible Automation Platform uses the system-wide ansible-core package to install the platform, but uses ansible-core 2.16 for both its control plane and built-in execution environments. |
|  **Browser** | A currently supported version of Mozilla Firefox or Google Chrome. |  |
|  **Database** | - For Ansible Automation Platform managed databases: PostgreSQL 15.
- For customer provided (external) databases: PostgreSQL 15, 16, or 17. | - External (customer supported) databases require ICU support.
- External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15. |


