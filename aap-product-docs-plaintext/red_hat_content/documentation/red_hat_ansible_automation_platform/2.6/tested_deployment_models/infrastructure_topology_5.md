# 4. RPM topologies
## 4.1. RPM growth topology
### 4.1.1. Infrastructure topology




The Red Hat tested infrastructure topology for this deployment model:


<span id="idm140186614655264"></span>
**Figure 4.1. Infrastructure topology diagram**

![RPM growth topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Tested_deployment_models-en-US/images/a6bab844df620cd5ae45fac1ec8f2b85/rpm-a-env-a.png)




Red Hat tests each VM with these requirements:


<span id="idm140186614184672"></span>
**Table 4.1. Virtual machine requirements**

| Requirement | Minimum requirement |
| --- | --- |
| RAM | 16 GB |
| CPUs | 4 |
| Local disk | 60 GB |
| Disk IOPS | 3000 |





<span id="idm140186614161696"></span>
**Table 4.2. Infrastructure topology components**

| VM count | Purpose | Example VM group names |
| --- | --- | --- |
| 1 | Platform gateway with colocated Redis |  `automationgateway` |
| 1 | Automation controller |  `automationcontroller` |
| 1 | Private automation hub |  `automationhub` |
| 1 | Event-Driven Ansible |  `automationedacontroller` |
| 1 | Automation mesh execution node |  `execution_nodes` |
| 1 | Ansible Automation Platform managed database |  `database` |




