# 2. Ansible Automation Platform containerized installation
## 2.2. System requirements
### 2.2.2. Ansible Automation Platform system requirements




Your system must meet the following minimum system requirements to install and run Red Hat Ansible Automation Platform.


<span id="idm140679173416416"></span>
**Table 2.1. System configuration**

| Type | Description | Notes |
| --- | --- | --- |
| Subscription | - Valid Red Hat Ansible Automation Platform subscription
- Valid Red Hat Enterprise Linux subscription (to consume the BaseOS and AppStream repositories) |  |
| Operating system | - Red Hat Enterprise Linux 9.2 or later minor versions of Red Hat Enterprise Linux 9.
- Red Hat Enterprise Linux 10 or later minor versions of Red Hat Enterprise Linux 10 for enterprise topologies. |  |
| CPU architecture | x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |  |
|  `ansible-core` | - For the installation: `    ansible-core` version 2.14.
- For Ansible Automation Platform operation: `    ansible-core` version 2.16. | - The installation program uses the `    ansible-core` 2.14 package from the RHEL 9 AppStream repository.
- Ansible Automation Platform bundles `    ansible-core` version 2.16 for its operation, so you do not need to install it manually. |
| Browser | A currently supported version of Mozilla Firefox or Google Chrome. |  |
| Database | PostgreSQL 15 | External (customer supported) databases require ICU support. |




Each virtual machine (VM) has the following system requirements:


<span id="idm140679173639712"></span>
**Table 2.2. Virtual machine requirements**

| Requirement | Minimum requirement |
| --- | --- |
| RAM | 16 GB |
| CPUs | 4 |
| Local disk | - Total available disk space: 60 GB
- Installation directory: 15 GB (if on a dedicated partition)
-  `    /var/tmp` for online installations: 1 GB
-  `    /var/tmp` for offline or bundled installations: 3 GB
- Temporary directory (defaults to `    /tmp` ) for offline or bundled installations: 10GB |
| Disk IOPS | 3000 |




Note
If performing a bundled installation of the growth topology with `hub_seed_collections=true` , then 32 GB RAM is recommended. Note that with this configuration the install time is going to increase and can take 45 or more minutes alone to complete seeding the collections.



