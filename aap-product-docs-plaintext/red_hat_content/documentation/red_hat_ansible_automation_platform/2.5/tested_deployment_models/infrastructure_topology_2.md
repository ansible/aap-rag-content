# 2. RPM topologies
## 2.2. RPM enterprise topology
### 2.2.1. Infrastructure topology




The following diagram outlines the infrastructure topology that Red Hat has tested with this deployment model that customers can use when self-managing Ansible Automation Platform:


<span id="idm139984996619248"></span>
**Figure 2.2. Infrastructure topology diagram**

![RPM enterprise topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Tested_deployment_models-en-US/images/f2f3c928085ce3b7b53a92d554fbc14d/rpm-b-env-a.png)




Each VM has been tested with the following component requirements:


<span id="idm139984996614448"></span>
**Table 2.5. Virtual machine requirements**

| Requirement | Minimum requirement |
| --- | --- |
| RAM | 16 GB |
| CPUs | 4 |
| Local disk | 60 GB |
| Disk IOPS | 3000 |





<span id="idm139984993273488"></span>
**Table 2.6. Infrastructure topology**

| VM count | Purpose | Example VM group names |
| --- | --- | --- |
| 2 | Platform gateway with colocated Redis |  `automationgateway` |
| 2 | Automation controller |  `automationcontroller` |
| 2 | Private automation hub with colocated Redis |  `automationhub` |
| 2 | Event-Driven Ansible with colocated Redis |  `automationedacontroller` |
| 1 | Automation mesh hop node |  `execution_nodes` |
| 2 | Automation mesh execution node |  `execution_nodes` |
| 1 | Externally managed database service | N/A |
| 1 | HAProxy load balancer in front of platform gateway (externally managed) | N/A |




Note
- 6 VMs are required for a Redis high availability (HA) compatible deployment. Redis can be colocated on each Ansible Automation Platform component VM except for automation controller, execution nodes, or the PostgreSQL database.
- External Redis is not supported for RPM-based deployments of Ansible Automation Platform.




