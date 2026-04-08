# 3. Example: Automate Red Hat Enterprise Linux firewall configuration
## 3.3. Create a new playbook project to configure a firewall




Create a new Ansible Playbook project quickly using the plug-in templates. This sets up the basic structure needed to configure your Red Hat Enterprise Linux firewall successfully.

**Procedure**

1. Click the Ansible `    A` icon in the Red Hat Developer Hub navigation panel.
1. From the **Create** dropdown menu on the landing page, select **Create Ansible Git Project** .
1. Click **Choose** in the **Create Ansible Playbook Project** software template.
1. Fill in the following information in the **Create Ansible Playbook Project** page:

| Field | Required | Description | Example value |
| --- | --- | --- | --- |
| Source code repository organization name or username | Yes | The name of your source code repository username or organization name. |  `my_github_username` |
| Playbook repository name | Yes | The name of your new Git repository. |  `rhel_firewall_config` |
| Playbook description | No | A description of the new playbook project. |  `This playbook configures firewalls on Red Hat Enterprise Linux systems` |
| Playbook project’s collection namespace | Yes | The new playbook Git project creates an example collection folder for you. Enter a value for the collection namespace. |  `my_galaxy_username` |
| Playbook project’s collection name | Yes | This is the name of the example collection. |  `rhel_firewall_config` |
| Catalog Owner Name | Yes | The name of the Developer Hub catalog item owner. It is a Red Hat Developer Hub field. |  `my_rhdh_username` |
| System | No | This is a Red Hat Developer Hub field. |  `my_rhdh_linux_system` |





1. Click **Review** .
1. Click **Create** to provision your new playbook project.
1. Click **Open in catalog** to view your project.


