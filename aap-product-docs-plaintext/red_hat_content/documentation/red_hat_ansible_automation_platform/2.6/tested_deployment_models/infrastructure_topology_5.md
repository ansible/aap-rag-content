# 4. RPM topologies
## 4.1. RPM growth topology
### 4.1.1. Infrastructure topology




The following diagram outlines the infrastructure topology that Red Hat has tested with this deployment model that customers can use when self-managing Ansible Automation Platform:


<span id="idm140627609128464"></span>
**Figure 4.1. Infrastructure topology diagram**

![RPM growth topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Tested_deployment_models-en-US/images/a6bab844df620cd5ae45fac1ec8f2b85/rpm-a-env-a.png)




Each VM has been tested with the following component requirements:


<span id="idm140627609123664"></span>
**Table 4.1. Virtual machine requirements**

| Requirement | Minimum requirement |
| --- | --- |
| RAM | 16 GB |
| CPUs | 4 |
| Local disk | 60 GB |
| Disk IOPS | 3000 |





<span id="idm140627606668000"></span>
**Table 4.2. Infrastructure topology**

| VM count | Purpose | Example VM group names |
| --- | --- | --- |
| 1 | Platform gateway with colocated Redis |  `automationgateway` |
| 1 | Automation controller |  `automationcontroller` |
| 1 | Private automation hub |  `automationhub` |
| 1 | Event-Driven Ansible |  `automationedacontroller` |
| 1 | Automation mesh execution node |  `execution_nodes` |
| 1 | Ansible Automation Platform managed database |  `database` |




