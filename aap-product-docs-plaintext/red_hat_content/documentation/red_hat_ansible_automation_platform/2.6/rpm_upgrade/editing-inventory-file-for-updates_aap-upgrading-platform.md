# 2. Upgrading to Red Hat Ansible Automation Platform 2.6
## 2.3. Setting up the inventory file

Before upgrading your Red Hat Ansible Automation Platform installation, edit the `inventory` file so that it matches your required configuration. You can keep the same parameters from your existing Ansible Automation Platform deployment or you can update the parameters to match any changes to your environment.

You can find sample inventory files in the [Test topologies](https://github.com/ansible/test-topologies/) GitHub repository, or in our [Tested deployment models](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models) guide.

**Procedure**

1. Navigate to the installation program directory.



Bundled installer
$ cd ansible-automation-platform-setup-bundle-2.6-4-x86_64

Online installer
$ cd ansible-automation-platform-setup-2.6-4

2. Open the `inventory` file for editing.

3. Modify the `inventory` file to provision new nodes, deprovision nodes or groups, and import or generate automation hub API tokens.

You can use the same `inventory` file from an existing Ansible Automation Platform installation if there are no changes to the environment.


Note
Provide a reachable IP address or fully qualified domain name (FQDN) for all hosts to ensure that users can synchronize and install content from Ansible automation hub from a different node. Do not use `localhost`. If `localhost` is used, the upgrade will be stopped as part of preflight checks.

4. Provision new nodes in a cluster, by adding new nodes alongside existing nodes in the `inventory` file as follows:

[automationcontroller]
clusternode1.example.com
clusternode2.example.com
clusternode3.example.com

[all:vars]
admin_password='password'

pg_host='<host_name>'

pg_database='<database_name>'
pg_username='<your_username>'
pg_password='<your_password>'

