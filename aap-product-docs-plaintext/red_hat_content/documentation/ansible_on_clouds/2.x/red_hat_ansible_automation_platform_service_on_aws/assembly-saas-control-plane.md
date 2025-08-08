# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.2. Control plane




The Ansible Automation Platform control plane includes the application UIs, APIs, components, and services used for managing automation. Red Hat manages these within its own infrastructure.

Each customer deployment is fully isolated at the infrastructure layer. Every deployment provisions its own dedicated network, compute, and database resources, remaining entirely independent from all other customer environments. By enforcing this level of isolation, there is a reduce the risk of data leakage or unauthorized cross-deployment interactions, ensuring that actions and information remain confined within their designated environments.

![The diagram shows two customer deployments. Both deployments are identical](https://access.redhat.com/webassets/avalon/d/Ansible_on_Clouds-2.x-Red_Hat_Ansible_Automation_Platform_Service_on_AWS-en-US/images/f911b4ac0130963cd5c313ded8bebb12/AWS_tenant_isolation.png)


