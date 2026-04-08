# 3. Operator topologies
## 3.2. Operator enterprise topology
### 3.2.1. Infrastructure topology




The Red Hat tested infrastructure topology for this deployment model:


<span id="idm140264423583712"></span>
**Figure 3.2. Infrastructure topology diagram**

![Operator enterprise topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Tested_deployment_models-en-US/images/404830abca879783bdfe6a23434fd33a/ocp-b-env-a.png)




Important
While Redis and PostgreSQL can be installed as part of the operator-based installation process, the topology diagram represents a Red Hat supported topology where both Redis and PostgreSQL are external to Ansible Automation Platform.



This infrastructure topology describes an OpenShift Cluster with 3 primary nodes and 2 worker nodes.

Red Hat tests each OpenShift Worker node with these requirements: 16 GB RAM, 4 CPUs, 128 GB local disk, and 3000 IOPS.


<span id="idm140264423576048"></span>
**Table 3.4. Infrastructure topology components**

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




