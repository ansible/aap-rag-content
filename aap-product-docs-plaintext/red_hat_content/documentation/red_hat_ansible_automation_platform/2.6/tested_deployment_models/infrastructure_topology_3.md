# 3. Operator topologies
## 3.1. Operator growth topology
### 3.1.1. Infrastructure topology




The Red Hat tested infrastructure topology for this deployment model:


<span id="idm140264421768688"></span>
**Figure 3.1. Infrastructure topology diagram**

![Operator growth topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Tested_deployment_models-en-US/images/5d4c3ae79cc44b3dde002a9fe383192e/ocp-a-env-a.png)




Important
While Redis and PostgreSQL can be installed as part of the operator-based installation process, the topology diagram represents a Red Hat supported topology where both Redis and PostgreSQL are external to Ansible Automation Platform.



Red Hat tests a Single Node OpenShift (SNO) cluster with these requirements: 32 GB RAM, 16 CPUs, 128 GB local disk, and 3000 IOPS.


<span id="idm140264421761936"></span>
**Table 3.1. Infrastructure topology components**

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
| 1 | Event-Driven Ansible activation worker pod |
| 1 | Event-Driven Ansible default worker pod |
| 1 | Event-Driven Ansible event stream pod |
| 1 | Event-Driven Ansible scheduler pod |
| 1 | Platform gateway pod |
| 1 | Database pod |
| 1 | Redis pod |




Note
You can deploy multiple isolated instances of Ansible Automation Platform into the same Red Hat OpenShift Container Platform cluster. To do this, use a namespace-scoped deployment model (isolated within a namespace).

This approach allows you to use the same cluster for several deployments.



