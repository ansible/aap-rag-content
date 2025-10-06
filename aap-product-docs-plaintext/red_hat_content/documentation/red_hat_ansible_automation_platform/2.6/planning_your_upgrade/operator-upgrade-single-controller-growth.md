# 4. Infrastructure changes by deployment type
## 4.3. Operator-based deployments
### 4.3.1. Upgrading a 2.4 single automation controller node deployment to a 2.6 growth topology




You can upgrade your 2.4 single automation controller node deployment to a 2.6 growth topology. This section outlines the infrastructure changes and requirements for upgrading.

#### 4.3.1.1. 2.4 infrastructure topology diagram




This diagram outlines the 2.4 infrastructure topology for this deployment model.


<span id="idm140440485092192"></span>
**Figure 4.9. 2.4 infrastructure topology diagram**

![2.4 single controller topology](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_upgrade-en-US/images/939a71fba6d3b55d4095383016298a8b/ocp-a-controller-2.4.png)




#### 4.3.1.2. 2.6 infrastructure topology diagram




This diagram outlines the 2.6 infrastructure topology that Red Hat has tested with this deployment model.


<span id="idm140440487522496"></span>
**Figure 4.10. 2.6 infrastructure topology diagram**

![2.6 growth topology](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_upgrade-en-US/images/c5591346c88cb1a587f46c8e97fee020/ocp-a-controller-2.6.png)




#### 4.3.1.3. Requirements for upgrading a single automation controller node deployment




The following table highlights the requirements for upgrading from Ansible Automation Platform 2.4 to 2.6.

| Existing 2.4 topology | Tested 2.6 topology | Requirements for each pod |
| --- | --- | --- |
| Non-redundant automation controller-only deployment:

- One automation controller web pod
- One automation controller task pod
- One database pod | Growth topology:

- One automation controller web pod
- One automation controller task pod
- One automation hub web pod
- One automation hub API pod
- Two automation hub content pods
- Two automation hub worker pods
- One automation hub Redis pod
- One Event-Driven Ansible controller API pod
- One Event-Driven Ansible controller activation worker pod
- One Event-Driven Ansible controller default worker pod
- One Event-Driven Ansible controller event stream pod
- One Event-Driven Ansible controller scheduler pod
- One platform gateway pod
- One database pod
- One Redis pod | See the [Operator growth topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/ocp-topologies#ocp-a-env-a) section of the _Tested deployment models_ guide. |


