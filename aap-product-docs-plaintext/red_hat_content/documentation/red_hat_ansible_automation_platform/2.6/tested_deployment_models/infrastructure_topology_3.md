# 3. Operator topologies
## 3.1. Operator growth topology
### 3.1.1. Infrastructure topology

The Red Hat tested infrastructure topology for this deployment model:

**Figure 3.1. Infrastructure topology diagram**

![Operator growth topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Tested_deployment_models-en-US/images/5d4c3ae79cc44b3dde002a9fe383192e/ocp-a-env-a.png)

Important

While Redis and PostgreSQL can be installed as part of the operator-based installation process, the topology diagram represents a Red Hat supported topology where both Redis and PostgreSQL are external to Ansible Automation Platform.

Red Hat tests a Single Node OpenShift (SNO) cluster with these requirements: 32 GB RAM, 16 CPUs, 128 GB local disk, and 3000 IOPS.

**Table 3.1. Infrastructure topology components**

| Count | Component |
| --- | --- |
| <br>  1 | <br>  Automation controller web pod |
| <br>  1 | <br>  Automation controller task pod |
| <br>  1 | <br>  Automation hub web pod |
| <br>  1 | <br>  Automation hub API pod |
| <br>  2 | <br>  Automation hub content pod |
| <br>  2 | <br>  Automation hub worker pod |
| <br>  1 | <br>  Automation hub Redis pod |
| <br>  1 | <br>  Event-Driven Ansible API pod |
| <br>  1 | <br>  Event-Driven Ansible activation worker pod |
| <br>  1 | <br>  Event-Driven Ansible default worker pod |
| <br>  1 | <br>  Event-Driven Ansible event stream pod |
| <br>  1 | <br>  Event-Driven Ansible scheduler pod |
| <br>  1 | <br>  Platform gateway pod |
| <br>  1 | <br>  Database pod |
| <br>  1 | <br>  Redis pod |

Note

You can deploy multiple isolated instances of Ansible Automation Platform into the same Red Hat OpenShift Container Platform cluster. To do this, use a namespace-scoped deployment model (isolated within a namespace).

This approach allows you to use the same cluster for several deployments.

