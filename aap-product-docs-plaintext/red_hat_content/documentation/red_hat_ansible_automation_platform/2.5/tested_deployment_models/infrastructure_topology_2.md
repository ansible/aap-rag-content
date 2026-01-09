# 2. RPM topologies
## 2.2. RPM enterprise topology
### 2.2.1. Infrastructure topology




The Red Hat tested infrastructure topology for this deployment model:


<span id="idm139972756607216"></span>
**Figure 2.2. Infrastructure topology diagram**

![RPM enterprise topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Tested_deployment_models-en-US/images/f2f3c928085ce3b7b53a92d554fbc14d/rpm-b-env-a.png)




Red Hat tests each VM with these requirements:


<span id="idm139972765493264"></span>
**Table 2.5. Virtual machine requirements**

| Requirement | Minimum requirement |
| --- | --- |
| RAM | 16 GB |
| CPUs | 4 |
| Local disk | 60 GB |
| Disk IOPS | 3000 |





<span id="idm139972765789168"></span>
**Table 2.6. Infrastructure topology components**

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
- Redis high availability (HA) deployment requires 6 VMs. You can colocate Redis on each Ansible Automation Platform component VM except for automation controller, execution nodes, or the PostgreSQL database.
- RPM-based deployments of Ansible Automation Platform do not support external Redis.




