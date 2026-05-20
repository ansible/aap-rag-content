# 4. RPM topologies
## 4.2. RPM enterprise topology
### 4.2.1. Infrastructure topology

The Red Hat tested infrastructure topology for this deployment model:

**Figure 4.2. Infrastructure topology diagram**

![RPM enterprise topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Tested_deployment_models-en-US/images/f2f3c928085ce3b7b53a92d554fbc14d/rpm-b-env-a.png)

Red Hat tests each VM with these requirements:

**Table 4.5. Virtual machine requirements**

| Requirement | Minimum requirement |
| --- | --- |
| <br>  RAM | <br>  16 GB |
| <br>  CPUs | <br>  4 |
| <br>  Local disk | <br>  60 GB |
| <br>  Disk IOPS | <br>  3000 |

**Table 4.6. Infrastructure topology components**

| VM count | Purpose | Example VM group names |
| --- | --- | --- |
| <br>  2 | <br>  Platform gateway with colocated Redis | <br> `automationgateway` |
| <br>  2 | <br>  Automation controller | <br> `automationcontroller` |
| <br>  2 | <br>  Private automation hub with colocated Redis | <br> `automationhub` |
| <br>  2 | <br>  Event-Driven Ansible with colocated Redis | <br> `automationedacontroller` |
| <br>  1 | <br>  Automation mesh hop node | <br> `execution_nodes` |
| <br>  2 | <br>  Automation mesh execution node | <br> `execution_nodes` |
| <br>  1 | <br>  Externally managed database service | <br>  N/A |
| <br>  1 | <br>  HAProxy load balancer in front of platform gateway (externally managed) | <br>  N/A |

Note

- Redis high availability (HA) deployment requires 6 VMs. You can colocate Redis on each Ansible Automation Platform component VM except for automation controller, execution nodes, or the PostgreSQL database.
- RPM-based deployments of Ansible Automation Platform do not support external Redis.

