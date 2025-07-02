# 3. Container topologies
## 3.1. Container growth topology
### 3.1.1. Infrastructure topology




The following diagram outlines the infrastructure topology that Red Hat has tested with this deployment model that customers can use when self-managing Ansible Automation Platform:


<span id="idm139891619084448"></span>
**Figure 3.1. Infrastructure topology diagram**

![Container growth topology diagram](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Tested_deployment_models-en-US/images/02b948e9d139f9a478e80ba4164dceae/cont-a-env-a.png)




A single VM has been tested with the following component requirements:


<span id="idm139891619856592"></span>
**Table 3.1. Virtual machine requirements**

| Requirement | Minimum requirement |
| --- | --- |
| RAM | 16 GB |
| CPUs | 4 |
| Local disk | - 60 GB
- Minimum of 15 GB dedicated to the installation directory if it is in a dedicated partition. |
| Disk IOPS | 3000 |




Resources, such as storage, can be increased based on the needs of the deployment.

Note
If performing a bundled installation of the growth topology with `hub_seed_collections=true` , then 32 GB RAM is recommended. Note that with this configuration the install time is going to increase and can take 45 or more minutes alone to complete seeding the collections.




<span id="idm139891618796400"></span>
**Table 3.2. Infrastructure topology**

| Purpose | Example group names |
| --- | --- |
| All Ansible Automation Platform components | -  `    automationgateway`
-  `    automationcontroller`
-  `    automationhub`
-  `    automationeda`
-  `    database` |




