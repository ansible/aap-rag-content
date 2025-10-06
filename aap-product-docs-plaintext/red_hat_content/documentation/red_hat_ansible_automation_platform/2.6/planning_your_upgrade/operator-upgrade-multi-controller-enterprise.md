# 4. Infrastructure changes by deployment type
## 4.3. Operator-based deployments
### 4.3.3. Upgrading a 2.4 multi node automation controller deployment to a 2.6 enterprise topology




You can upgrade your 2.4 multi node automation controller deployment to a 2.6 enterprise topology. This section outlines the infrastructure changes and requirements for upgrading.

#### 4.3.3.1. 2.4 infrastructure topology diagram




This diagram outlines the 2.4 infrastructure topology for this deployment model.


<span id="idm140440484030688"></span>
**Figure 4.13. 2.4 infrastructure topology diagram**

![2.4 multi controller topology](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_upgrade-en-US/images/d977a11bcd47bd7c415beb03a58f71c2/ocp-b-controller-2.4.png)




#### 4.3.3.2. 2.6 infrastructure topology diagram




This diagram outlines the 2.6 infrastructure topology that Red Hat has tested with this deployment model.


<span id="idm140440484023632"></span>
**Figure 4.14. 2.6 infrastructure topology diagram**

![2.6 enterprise topology](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Planning_your_upgrade-en-US/images/daf6df62663bb2971afecec84977ef0c/ocp-b-controller-2.6.png)




#### 4.3.3.3. Requirements for upgrading a multi node automation controller deployment on OpenShift Container Platform




The following table highlights the requirements for upgrading from Ansible Automation Platform 2.4 to 2.6.

| Existing 2.4 topology | Tested 2.6 topology | Requirements for each pod |
| --- | --- | --- |
| Redundant automation controller-only deployment:

- One automation controller web pod
- One automation controller task pod
- Two automation mesh ingress pods
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


