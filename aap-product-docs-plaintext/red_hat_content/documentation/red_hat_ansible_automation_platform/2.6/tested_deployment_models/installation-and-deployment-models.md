# 1. Tested deployment model types
## 1.1. Installation and deployment models




Ansible Automation Platform offers many installation and deployment options based on your infrastructure and organizational needs. Each installation type reference includes supported infrastructure types and links to tested topologies.

Note
The Ansible Automation Platform RPM installer was deprecated in 2.5 and will be removed in Ansible Automation Platform 2.7. The RPM installer will be supported for RHEL 9 during the lifecycle of Ansible Automation Platform 2.6 to support migrations to existing supported topologies. For more information on upgrade and migration paths, see the [Support matrix for upgrade scenarios](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/planning_your_upgrade/index#upgrade-support-matrix) .




<span id="idm140264427674736"></span>
**Table 1.1. Ansible Automation Platform installation and deployment models**

| Mode | Infrastructure | Description | Tested topologies |
| --- | --- | --- | --- |
| Containers | Virtual machines and bare metal | The containerized installer deploys Ansible Automation Platform on Red Hat Enterprise Linux by using Podman which runs the platform in containers on host machines. Customers manage the product and infrastructure lifecycle. | -  [Container growth topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/container-topologies#cont-a-env-a)
-  [Container enterprise topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/container-topologies#cont-b-env-a) |
| Operator | Red Hat OpenShift | The Operator uses Red Hat OpenShift Operators to deploy Ansible Automation Platform within Red Hat OpenShift. Customers manage the product and infrastructure lifecycle. | -  [Operator growth topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/ocp-topologies#ocp-a-env-a)
-  [Operator enterprise topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/ocp-topologies#ocp-b-env-a) |
| RPM | Virtual machines and bare metal | The RPM installer deploys Ansible Automation Platform on Red Hat Enterprise Linux by using RPMs to install the platform on host machines. Customers manage the product and infrastructure lifecycle. | -  [RPM growth topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/rpm-topologies#rpm-a-env-a)
-  [RPM enterprise topology](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/rpm-topologies#rpm-b-env-a) |




