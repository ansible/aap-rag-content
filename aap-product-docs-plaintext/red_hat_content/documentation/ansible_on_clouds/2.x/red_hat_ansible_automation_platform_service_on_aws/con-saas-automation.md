# 2. Red Hat Ansible Automation Platform Service on AWS PULL and PUSH models
## 2.1. Automation using the Red Hat Ansible Automation Platform Service on AWS control plane




The Red Hat Ansible Automation Platform Service on AWS offers a deployment of Ansible Automation Platform deployment purchased through AWS Marketplace. Red Hat configures and provisions an Ansible Automation Platform. The Red Hat team handles the setup and maintenance of the Ansible Automation Platform, ensuring reliability and security.

While Red Hat manages the control plane, the execution plane is implemented in your network using automation mesh hop nodes and execution nodes. For help with configuring execution nodes see _ [Automation mesh for managed cloud or operator environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/automation_mesh_for_managed_cloud_or_operator_environments) _ .

There are two ways to configure the communication between control nodes and execution nodes:

- The PULL connectivity model (recommended)
- The PUSH connectivity model


