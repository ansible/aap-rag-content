# 2. Container topologies
## 2.2. Container enterprise topology
### 2.2.1. Infrastructure topology

The Red Hat tested infrastructure topology for this deployment model:

**Figure 2.2. Infrastructure topology diagram**

![Container enterprise topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Tested_deployment_models-en-US/images/704824d330eb8422156d4d7cf034ee52/cont-b-env-a.png)

Red Hat tests each VM with these requirements:

**Table 2.5. Virtual machine requirements**

| Requirement | Minimum requirement |
| --- | --- |
| <br>  RAM | <br>  16 GB |
| <br>  CPUs | <br>  4 |
| <br>  Local disk | <br>  Total available disk space: 60 GB   Installation directory: 15 GB (if on a dedicated partition) `/var/tmp` for online installations: 1 GB `/var/tmp` for offline or bundled installations: 3 GB   Temporary directory (defaults to `/tmp`) for offline or bundled installations: 10GB |
| <br>  Disk IOPS | <br>  3000 |

**Table 2.6. Infrastructure topology components**

| VM count | Purpose | Example VM group names |
| --- | --- | --- |
| <br>  2 | <br>  Platform gateway with colocated Redis | <br> `automationgateway` |
| <br>  2 | <br>  Automation controller | <br> `automationcontroller` |
| <br>  2 | <br>  Private automation hub with colocated Redis | <br> `automationhub` |
| <br>  2 | <br>  Event-Driven Ansible with colocated Redis | <br> `automationeda` |
| <br>  1 | <br>  Automation mesh hop node | <br> `execution_nodes` |
| <br>  2 | <br>  Automation mesh execution node | <br> `execution_nodes` |
| <br>  1 | <br>  Externally managed database service | <br>  N/A |
| <br>  1 | <br>  HAProxy load balancer in front of platform gateway (externally managed) | <br>  N/A |

Note

- 6 VMs are required for a Redis high availability (HA) compatible deployment. When installing Ansible Automation Platform with the containerized installer, Redis can be colocated on any Ansible Automation Platform component VMs of your choice except for execution nodes or the PostgreSQL database. They might also be assigned VMs specifically for Redis use.
- External Redis is not supported for containerized Ansible Automation Platform.

