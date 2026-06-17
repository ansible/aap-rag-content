# 4. RPM topologies
## 4.1. RPM growth topology
### 4.1.1. Infrastructure topology

The Red Hat tested infrastructure topology for this deployment model:

**Figure 4.1. Infrastructure topology diagram**

![RPM growth topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Tested_deployment_models-en-US/images/a6bab844df620cd5ae45fac1ec8f2b85/rpm-a-env-a.png)

Red Hat tests each VM with these requirements:

**Table 4.1. Virtual machine requirements**

| Requirement | Minimum requirement |
| --- | --- |
| <br>  RAM | <br>  16 GB |
| <br>  CPUs | <br>  4 |
| <br>  Local disk | <br>  60 GB |
| <br>  Disk IOPS | <br>  3000 |

**Table 4.2. Infrastructure topology components**

| VM count | Purpose | Example VM group names |
| --- | --- | --- |
| <br>  1 | <br>  Platform gateway with colocated Redis | <br> `automationgateway` |
| <br>  1 | <br>  Automation controller | <br> `automationcontroller` |
| <br>  1 | <br>  Private automation hub | <br> `automationhub` |
| <br>  1 | <br>  Event-Driven Ansible | <br> `automationedacontroller` |
| <br>  1 | <br>  Automation mesh execution node | <br> `execution_nodes` |
| <br>  1 | <br>  Ansible Automation Platform managed database | <br> `database` |

