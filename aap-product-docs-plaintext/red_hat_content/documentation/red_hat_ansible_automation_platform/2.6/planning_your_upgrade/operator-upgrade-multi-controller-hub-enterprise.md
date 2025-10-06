# 4. Infrastructure changes by deployment type
## 4.3. Operator-based deployments
### 4.3.4. Upgrading a 2.4 multi node automation controller and automation hub deployment to a 2.6 enterprise topology




You can upgrade your 2.4 multi node automation controller and automation hub deployment to a 2.6 enterprise topology. This section outlines the infrastructure changes and requirements for upgrading.

#### 4.3.4.1. 2.4 infrastructure topology diagram




This diagram outlines the 2.4 infrastructure topology for this deployment model.


<span id="idm140440488109856"></span>
**Figure 4.15. 2.4 infrastructure topology diagram**

![2.4 multi controller and hub topology](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_upgrade-en-US/images/bac1cf6785af2b43d539d3d0db00af74/ocp-b-controller-hub-2.4.png)




#### 4.3.4.2. 2.6 infrastructure topology diagram




This diagram outlines the 2.6 infrastructure topology that Red Hat has tested with this deployment model.


<span id="idm140440488102800"></span>
**Figure 4.16. 2.6 infrastructure topology diagram**

![2.6 enterprise topology](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_upgrade-en-US/images/ef9d80ce5ca4d51d4ef247f2c27b6c8a/ocp-b-controller-hub-2.6.png)




#### 4.3.4.3. Requirements for upgrading a multi node automation controller and automation hub deployment




The following table highlights the requirements for upgrading from Ansible Automation Platform 2.4 to 2.6.

| Existing 2.4 topology | Tested 2.6 topology | Requirements for each pod |
| --- | --- | --- |
| Redundant deployment with automation controller and automation hub:

- One automation controller web pod
- One automation controller task pod
- Two automation mesh ingress pods
- One automation hub web pod
- One automation hub API pod
- Two automation hub content pods
- Two automation hub worker pods
- Externally managed database service | Enterprise topology:

- One automation controller web pod
- One automation controller task pod
- One automation hub web pod
- One automation hub API pod
- Two automation hub content pods
- Two automation hub worker pods
- One automation hub Redis pod
- One Event-Driven Ansible controller API pod
- Two Event-Driven Ansible controller activation worker pods
- Two Event-Driven Ansible controller default worker pods
- Two Event-Driven Ansible controller event stream pods
- One Event-Driven Ansible controller scheduler pod
- One platform gateway pod
- Two automation mesh ingress pods
- Externally managed database service
- Externally managed Redis
- Externally managed object storage service (for automation hub) | See the [Operator enterprise topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/ocp-topologies#ocp-b-env-a) section of the _Tested deployment models_ guide. |


