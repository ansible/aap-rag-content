# 4. Infrastructure changes by deployment type
## 4.3. Operator-based deployments
### 4.3.2. Upgrading a 2.4 single automation controller and automation hub deployment to a 2.6 growth topology

Upgrade your 2.4 single-node deployment (automation controller and automation hub) to a 2.6 growth topology. Review the infrastructure changes and requirements needed to successfully plan your upgrade.

#### 4.3.2.1. 2.4 infrastructure topology diagram

This diagram outlines the 2.4 infrastructure topology for this deployment model.

**Figure 4.11. 2.4 infrastructure topology diagram**

![2.4 single controller and hub topology](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_upgrade-en-US/images/7c89a7bf265cf9281fe17b4245254573/ocp-a-controller-hub-2.4.png)

#### 4.3.2.2. 2.6 infrastructure topology diagram

This diagram outlines the 2.6 infrastructure topology that Red Hat has tested with this deployment model.

**Figure 4.12. 2.6 infrastructure topology diagram**

![2.6 growth topology](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_upgrade-en-US/images/21acc7a5d8cc4b5c8aa5937191468c3b/ocp-a-controller-hub-2.6.png)

#### 4.3.2.3. Requirements for upgrading a single automation controller and automation hub deployment

The following table highlights the requirements for upgrading from Ansible Automation Platform 2.4 to 2.6.

| Existing 2.4 topology | Tested 2.6 topology | Requirements for each pod |
| --- | --- | --- |
| <br>  Non-redundant automation controller and automation hub deployment:    <br>  One automation controller web pod   One automation controller task pod   One automation hub web pod   One automation hub API pod   Two automation hub content pods   Two automation hub worker pods   One database pod | <br>  Growth topology:    <br>  One automation controller web pod   One automation controller task pod   One automation hub web pod   One automation hub API pod   Two automation hub content pods   Two automation hub worker pods   One automation hub Redis pod   One Event-Driven Ansible controller API pod   One Event-Driven Ansible controller activation worker pod   One Event-Driven Ansible controller default worker pod   One Event-Driven Ansible controller event stream pod   One Event-Driven Ansible controller scheduler pod   One platform gateway pod   One database pod   One Redis pod | <br>  See the [Operator growth topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/ocp-topologies#ocp-a-env-a) section of the *Tested deployment models* guide. |

