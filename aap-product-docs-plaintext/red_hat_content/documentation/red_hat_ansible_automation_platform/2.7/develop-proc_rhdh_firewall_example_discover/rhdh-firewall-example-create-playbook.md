# Discover existing Ansible content for RHEL system roles
## Create a new playbook project to configure a firewall

Create a new Ansible Playbook project quickly using the plug-in templates. This sets up the basic structure needed to configure your Red Hat Enterprise Linux firewall successfully.

### Procedure

1.  Click the Ansible `A` icon in the Red Hat Developer Hub navigation panel.
2.  From the **Create** dropdown menu on the landing page, select **Create Ansible Git Project**.
3.  Click **Choose** in the **Create Ansible Playbook Project** software template.
4.  Fill in the following information in the **Create Ansible Playbook Project** page:
| Field                                                    | Required | Description                                                                                                                | Example value                                                                 |
| -------------------------------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| <br>Source code repository organization name or username | <br>Yes  | <br>The name of your source code repository username or organization name.                                                 | <br> `my_github_username`                                                     |
| <br>Playbook repository name                             | <br>Yes  | <br>The name of your new Git repository.                                                                                   | <br> `rhel_firewall_config`                                                   |
| <br>Playbook description                                 | <br>No   | <br>A description of the new playbook project.                                                                             | <br> `This playbook configures firewalls on Red Hat Enterprise Linux systems` |
| <br>Playbook project’s collection namespace              | <br>Yes  | <br>The new playbook Git project creates an example collection folder for you. Enter a value for the collection namespace. | <br> `my_galaxy_username`                                                     |
| <br>Playbook project’s collection name                   | <br>Yes  | <br>This is the name of the example collection.                                                                            | <br> `rhel_firewall_config`                                                   |
| <br>Catalog Owner Name                                   | <br>Yes  | <br>The name of the Developer Hub catalog item owner. It is a Red Hat Developer Hub field.                                 | <br> `my_rhdh_username`                                                       |
| <br>System                                               | <br>No   | <br>This is a Red Hat Developer Hub field.                                                                                 | <br> `my_rhdh_linux_system`                                                   |

5.  Click **Review**.
6.  Click **Create** to provision your new playbook project.
7.  Click **Open in catalog** to view your project.

