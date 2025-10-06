# 4. Operator topologies
## 4.2. Operator enterprise topology
### 4.2.1. Infrastructure topology




The following diagram outlines the infrastructure topology that Red Hat has tested with this deployment model that customers can use when self-managing Ansible Automation Platform:


<span id="idm139984993819392"></span>
**Figure 4.2. Infrastructure topology diagram**

![Operator enterprise topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Tested_deployment_models-en-US/images/0927062dc904a6d8a781db7124bbc41b/ocp-b-env-a.png)




Important
While Redis and PostgreSQL can be installed as part of the operator-based installation process, this diagram represents a Red Hat supported topology where both Redis and PostgreSQL are external to Ansible Automation Platform.



The following infrastructure topology describes an OpenShift Cluster with 3 primary nodes and 2 worker nodes.

Each OpenShift Worker node has been tested with the following component requirements: 16 GB RAM, 4 CPUs, 128 GB local disk, and 3000 IOPS.


<span id="idm139984993811696"></span>
**Table 4.4. Infrastructure topology**

| Count | Component |
| --- | --- |
| 1 | Automation controller web pod |
| 1 | Automation controller task pod |
| 1 | Automation hub web pod |
| 1 | Automation hub API pod |
| 2 | Automation hub content pod |
| 2 | Automation hub worker pod |
| 1 | Automation hub Redis pod |
| 1 | Event-Driven Ansible API pod |
| 2 | Event-Driven Ansible activation worker pod |
| 2 | Event-Driven Ansible default worker pod |
| 2 | Event-Driven Ansible event stream pod |
| 1 | Event-Driven Ansible scheduler pod |
| 1 | Platform gateway pod |
| 2 | Mesh ingress pod |
| N/A | Externally managed database service |
| N/A | Externally managed Redis |
| N/A | Externally managed object storage service (for automation hub) |




