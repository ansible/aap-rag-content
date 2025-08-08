# 2. New features and enhancements
## 2.2. Deployment topologies




Red Hat tests Ansible Automation Platform 2.5 with a defined set of topologies to give you opinionated deployment options. Deploy all components of Ansible Automation Platform so that all features and capabilities are available for use without the need to take further action.

It is possible to install Ansible Automation Platform on different infrastructure topologies and with different environment configurations. Red Hat does not fully test topologies outside of published reference architectures. Red Hat recommends using a tested topology for all new deployments and provides commercially reasonable support for deployments that meet minimum requirements.

At the time of the Ansible Automation Platform 2.5 GA release, a limited set of topologies are fully tested. Red Hat will regularly add new topologies to iteratively expand the scope of fully tested deployment options. As new topologies roll out, we will include them in the release notes.

The following table shows the tested topologies for Ansible Automation Platform 2.5:

| Mode | Infrastructure | Description | Tested topologies |
| --- | --- | --- | --- |
| RPM | Virtual Machines/Bare Metal | The RPM installer deploys the Ansible Automation Platform on Red Hat Enterprise Linux using RPMs to install the platform on host machines. Customers manage the product and infrastructure lifecycle. | - RPM growth topology
- RPM enterprise topology |
| Containers | Virtual Machines/Bare Metal | The containerized installer deploys the Ansible Automation Platform on Red Hat Enterprise Linux by using Podman that runs the platform in containers on host machines. Customers manage the product and infrastructure lifecycle. | - Container growth topology
- Container enterprise topology |
| Operator | Red Hat OpenShift | The operator uses Red Hat OpenShift operators to deploy the Ansible Automation Platform within Red Hat OpenShift. Customers manage the product and infrastructure lifecycle. | - Operator growth topology
- Operator enterprise topology |


For more information, see [Tested deployment models](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models) .

