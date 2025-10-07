# 4. Overview of tested deployment models
## 4.1. Installation and deployment models




The following table outlines the different ways to install or deploy Ansible Automation Platform:


<span id="idm140410396533472"></span>
**Table 4.1. Ansible Automation Platform installation and deployment models**

| Mode | Infrastructure | Description | Tested topologies |
| --- | --- | --- | --- |
| Containers | Virtual machines and bare metal | The containerized installer deploys Ansible Automation Platform on Red Hat Enterprise Linux by using Podman which runs the platform in containers on host machines. Customers manage the product and infrastructure lifecycle. | -  [Container growth topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/container-topologies#cont-a-env-a)
-  [Container enterprise topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/container-topologies#cont-b-env-a) |
| Operator | Red Hat OpenShift | The Operator uses Red Hat OpenShift Operators to deploy Ansible Automation Platform within Red Hat OpenShift. Customers manage the product and infrastructure lifecycle. | -  [Operator growth topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/ocp-topologies#ocp-a-env-a)
-  [Operator enterprise topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/ocp-topologies#ocp-b-env-a) |
| RPM | Virtual machines and bare metal | The RPM installer deploys Ansible Automation Platform on Red Hat Enterprise Linux by using RPMs to install the platform on host machines. Customers manage the product and infrastructure lifecycle. | -  [RPM growth topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/rpm-topologies#rpm-a-env-a)
-  [RPM enterprise topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/rpm-topologies#rpm-b-env-a) |




