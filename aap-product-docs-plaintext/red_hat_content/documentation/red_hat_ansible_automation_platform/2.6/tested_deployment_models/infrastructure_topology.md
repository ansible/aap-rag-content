# 2. Container topologies
## 2.1. Container growth topology
### 2.1.1. Infrastructure topology




The Red Hat tested infrastructure topology for this deployment model:


<span id="idm140264425244496"></span>
**Figure 2.1. Infrastructure topology diagram**

![Container growth topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Tested_deployment_models-en-US/images/02b948e9d139f9a478e80ba4164dceae/cont-a-env-a.png)




Red Hat tests a single VM with these requirements:


<span id="idm140264429621072"></span>
**Table 2.1. Virtual machine requirements**

| Requirement | Minimum requirement |
| --- | --- |
| RAM | - 16 GB
- 32 GB required for growth topology bundled installations with `    hub_seed_collections=true` . Seeding the collections can take 45 or more minutes. |
| CPUs | 4 |
| Local disk | - Total available disk space: 60 GB
- Installation directory: 15 GB (if on a dedicated partition)
-  `    /var/tmp` for online installations: 1 GB
-  `    /var/tmp` for offline or bundled installations: 3 GB
- Temporary directory (defaults to `    /tmp` ) for offline or bundled installations: 10GB |
| Disk IOPS | 3000 |





<span id="idm140264420410320"></span>
**Table 2.2. Infrastructure topology components**

| Purpose | Example group names |
| --- | --- |
| All Ansible Automation Platform components | -  `    automationgateway`
-  `    automationcontroller`
-  `    automationhub`
-  `    automationeda`
-  `    database` |




