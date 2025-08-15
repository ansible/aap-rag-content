# 3. Container topologies
## 3.2. Container enterprise topology
### 3.2.1. Infrastructure topology




The following diagram outlines the infrastructure topology that Red Hat has tested with this deployment model that customers can use when self-managing Ansible Automation Platform:


<span id="idm139937750980464"></span>
**Figure 3.2. Infrastructure topology diagram**

![Container enterprise topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Tested_deployment_models-en-US/images/704824d330eb8422156d4d7cf034ee52/cont-b-env-a.png)




Each VM has been tested with the following component requirements:


<span id="idm139937750975520"></span>
**Table 3.5. Virtual machine requirements**

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





<span id="idm139937751709696"></span>
**Table 3.6. Infrastructure topology**

| VM count | Purpose | Example VM group names |
| --- | --- | --- |
| 2 | Platform gateway with colocated Redis |  `automationgateway` |
| 2 | Automation controller |  `automationcontroller` |
| 2 | Private automation hub with colocated Redis |  `automationhub` |
| 2 | Event-Driven Ansible with colocated Redis |  `automationeda` |
| 1 | Automation mesh hop node |  `execution_nodes` |
| 2 | Automation mesh execution node |  `execution_nodes` |
| 1 | Externally managed database service | N/A |
| 1 | HAProxy load balancer in front of platform gateway (externally managed) | N/A |




Note
- 6 VMs are required for a Redis high availability (HA) compatible deployment. When installing Ansible Automation Platform with the containerized installer, Redis can be colocated on any Ansible Automation Platform component VMs of your choice except for execution nodes or the PostgreSQL database. They might also be assigned VMs specifically for Redis use.
- External Redis is not supported for containerized Ansible Automation Platform.




