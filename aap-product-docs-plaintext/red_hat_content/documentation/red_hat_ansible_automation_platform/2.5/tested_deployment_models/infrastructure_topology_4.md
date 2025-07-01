# 2. RPM topologies
## 2.4. RPM mixed enterprise topology
### 2.4.1. Infrastructure topology




The following diagram outlines the infrastructure topology that Red Hat has tested with this deployment model that customers can use when self-managing Ansible Automation Platform:


<span id="idm139891622704928"></span>
**Figure 2.4. Infrastructure topology diagram**

![RPM mixed enterprise topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Tested_deployment_models-en-US/images/9fbcca2154d5b59b78b09181fce08cb3/rpm-b-env-b.png)




Note
Here, automation controller and automation hub are at 2.4x while the Event-Driven Ansible and platform gateway components are at 2.5



Each VM has been tested with the following component requirements:


<span id="idm139891621457312"></span>
**Table 2.13. Virtual machine requirements**

| Requirement | Minimum requirement |
| --- | --- |
| RAM | 16 GB |
| CPUs | 4 |
| Local disk | 60 GB |
| Disk IOPS | 3000 |





<span id="idm139891618695024"></span>
**Table 2.14. Infrastructure topology**

| VM count | Purpose | Ansible Automation Platform version | Example VM group names |
| --- | --- | --- | --- |
| 3 | Platform gateway with colocated Redis | 2.5 |  `automationgateway` |
| 2 | Automation controller | 2.4 |  `automationcontroller` |
| 2 | Private automation hub | 2.4 |  `automationhub` |
| 3 | Event-Driven Ansible with colocated Redis | 2.5 |  `automationedacontroller` |
| 1 | Automation mesh hop node | 2.4 |  `execution_nodes` |
| 2 | Automation mesh execution node | 2.4 |  `execution_nodes` |
| 1 | Externally managed database service | N/A | N/A |
| 1 | HAProxy load balancer in front of platform gateway (externally managed) | N/A | N/A |




Note
6 VMs are required for a Redis high availability (HA) compatible deployment. Redis can be colocated on each Ansible Automation Platform 2.5 component VM except for automation controller, execution nodes, or the PostgreSQL database.



