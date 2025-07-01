# 2. Ansible Automation Platform containerized installation
## 2.2. System requirements
### 2.2.1. Ansible Automation Platform system requirements




Your system must meet the following minimum system requirements to install and run Red Hat Ansible Automation Platform.


<span id="idm140359471030208"></span>
**Table 2.1. Base system requirements**

| Type | Description |
| --- | --- |
| Subscription | - Valid Red Hat Ansible Automation Platform subscription
- Valid Red Hat Enterprise Linux subscription (to consume the BaseOS and AppStream repositories) |
| Operating system | Red Hat Enterprise Linux 9.2 or later minor versions of Red Hat Enterprise Linux 9 |
| CPU architecture | x86_64, AArch64, s390x (IBM Z), ppc64le (IBM Power) |
| Ansible-core | Ansible-core version 2.16 or later |
| Browser | A currently supported version of Mozilla Firefox or Google Chrome. |
| Database | PostgreSQL 15 |




Each virtual machine (VM) has the following system requirements:


<span id="idm140359479287152"></span>
**Table 2.2. Virtual machine requirements**

| Requirement | Minimum requirement |
| --- | --- |
| RAM | 16 GB |
| CPUs | 4 |
| Local disk | - 60 GB
- Minimum of 15 GB dedicated to the installation directory if it is in a dedicated partition. |
| Disk IOPS | 3000 |




Note
If performing a bundled installation of the growth topology with `hub_seed_collections=true` , then 32 GB RAM is recommended. Note that with this configuration the install time is going to increase and can take 45 or more minutes alone to complete seeding the collections.



