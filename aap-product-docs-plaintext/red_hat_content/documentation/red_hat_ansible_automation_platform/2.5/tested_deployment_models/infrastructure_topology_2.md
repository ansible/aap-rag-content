# 2. RPM topologies
## 2.2. RPM mixed growth topology
### 2.2.1. Infrastructure topology




The following diagram outlines the infrastructure topology that Red Hat has tested with this deployment model that customers can use when self-managing Ansible Automation Platform:


<span id="idm139891627351680"></span>
**Figure 2.2. Infrastructure topology diagram**

![RPM mixed growth topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Tested_deployment_models-en-US/images/24f65ee70c2611c625534226f66fae51/rpm-a-env-b.png)




Note
Here, automation controller and automation hub are at 2.4x while the Event-Driven Ansible and platform gateway components are at 2.5



Each VM has been tested with the following component requirements:


<span id="idm139891627345184"></span>
**Table 2.5. Virtual machine requirements**

| Requirement | Minimum requirement |
| --- | --- |
| RAM | 16 GB |
| CPUs | 4 |
| Local disk | 60 GB |
| Disk IOPS | 3000 |





<span id="idm139891628057136"></span>
**Table 2.6. Infrastructure topology**

| VM count | Purpose | Ansible Automation Platform version | Example VM group names |
| --- | --- | --- | --- |
| 1 | Platform gateway with colocated Redis | 2.5 |  `automationgateway` |
| 1 | Automation controller | 2.4 |  `automationcontroller` |
| 1 | Private automation hub | 2.4 |  `automationhub` |
| 1 | Event-Driven Ansible | 2.5 |  `automationedacontroller` |
| 1 | Automation mesh execution node | 2.4 |  `execution_nodes` |
| 1 | Ansible Automation Platform managed database | 2.4 |  `database` |




