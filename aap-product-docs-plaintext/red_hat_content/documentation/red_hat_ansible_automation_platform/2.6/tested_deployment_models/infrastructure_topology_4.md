# 3. Operator topologies
## 3.2. Operator enterprise topology
### 3.2.1. Infrastructure topology

The Red Hat tested infrastructure topology for this deployment model:

**Figure 3.2. Infrastructure topology diagram**

![Operator enterprise topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Tested_deployment_models-en-US/images/404830abca879783bdfe6a23434fd33a/ocp-b-env-a.png)

Important

While Redis and PostgreSQL can be installed as part of the operator-based installation process, the topology diagram represents a Red Hat supported topology where both Redis and PostgreSQL are external to Ansible Automation Platform.

This infrastructure topology describes an OpenShift Cluster with 3 primary nodes and 2 worker nodes.

Red Hat tests each OpenShift Worker node with these requirements: 16 GB RAM, 4 CPUs, 128 GB local disk, and 3000 IOPS.

**Table 3.4. Infrastructure topology components**

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
| <br>  2 | <br>  Event-Driven Ansible activation worker pod |
| <br>  2 | <br>  Event-Driven Ansible default worker pod |
| <br>  2 | <br>  Event-Driven Ansible event stream pod |
| <br>  1 | <br>  Event-Driven Ansible scheduler pod |
| <br>  1 | <br>  Platform gateway pod |
| <br>  2 | <br>  Mesh ingress pod |
| <br>  N/A | <br>  Externally managed database service |
| <br>  N/A | <br>  Externally managed Redis |
| <br>  N/A | <br>  Externally managed object storage service (for automation hub) |

