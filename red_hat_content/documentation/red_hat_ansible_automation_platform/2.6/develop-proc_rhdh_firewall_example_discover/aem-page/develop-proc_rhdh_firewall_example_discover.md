+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-proc_rhdh_firewall_example_discover"
title = "Discover existing Ansible content for RHEL system roles - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_rhdh_using/", "Streamline development by integrating Red Hat Developer Hub plug-ins"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-proc_rhdh_firewall_example_discover/aem-page/develop-proc_rhdh_firewall_example_discover.html"
last_crumb = "Discover existing Ansible content for RHEL system roles"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Discover existing Ansible content for RHEL system roles"
oversized = "false"
page_slug = "develop-proc_rhdh_firewall_example_discover"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-proc_rhdh_firewall_example_discover"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-proc_rhdh_firewall_example_discover/toc/toc.json"
type = "aem-page"
+++

# Discover existing Ansible content for RHEL system roles

Red Hat recommends that you use trusted automation content that has been tested and approved by Red Hat or your organization.

## About this task

Automation hub is a central repository for discovering, downloading, and managing trusted content collections from Red Hat and its partners. Private automation hub provides an on-premise solution for managing content collections.

## Procedure

1.  Click on the Ansible `A` icon in the Red Hat Developer Hub navigation panel.
2.  Click **Discover existing collections**.
3.  Click **Go to Automation Hub**.   - If private automation hub has been configured in the Ansible plug-ins, you are redirected to your **PrivateHubName** instance.
  - If private automation hub has not been configured in the Ansible plug-ins installation configuration, you will be redirected to the Red Hat Hybrid Console (RHCC) automation hub.

    In this example, you are redirected to the RHCC automation hub.

4.  If you are prompted to log in, provide your Red Hat Customer Portal credentials.
5.  Filter the collections with the `rhel firewall` keywords. The search returns the `rhel_system_roles` collection.

    The RHEL System Roles collection contains certified Ansible content that you can reuse to configure your firewall.

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

### Create a new playbook to automate the firewall configuration

Create a new playbook and use the RHEL System Role collection to automate your Red Hat Enterprise Linux firewall configuration.

#### Procedure

1.  In your Dev Spaces instance, click File> (and then)New File.
2.  Enter `firewall.yml` for the filename and click **OK** to save it in the root directory.
3.  Add the following lines to your `firewall.yml` file:
  

```
---
- name: Open HTTPS and SSH on firewall
  hosts: rhel
  become: true
  tasks:
    - name: Use rhel system roles to allow https and ssh traffic
      vars:
        firewall:
          - service: https
            state: enabled
            permanent: true
            immediate: true
            zone: public
          - service: ssh
            state: enabled
            permanent: true
            immediate: true
            zone: public
      ansible.builtin.include_role:
        name: redhat.rhel_system_roles.firewall
```
  Note:
      You can use Ansible Lightspeed with IBM watsonx Code Assistant from the Ansible VS Code extension to help you generate playbooks. For more information, refer to the [Ansible Lightspeed with IBM watsonx Code Assistant User Guide](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index).

### Edit your firewall playbook project

The Ansible plug-ins integrate OpenShift Dev Spaces to edit your Ansible projects. OpenShift Dev Spaces provides on-demand, web-based Integrated Development Environments (IDEs).

#### About this task

Ansible Git projects provisioned using the Ansible plug-ins include best practice configurations for OpenShift Dev Spaces. These configurations include installing the Ansible VS Code extension and providing access from the IDE terminal to Ansible development tools, such as Ansible Navigator and Ansible Lint.

Note:

OpenShift Dev Spaces is optional and it is not required to run the Ansible plug-ins. It is a separate Red Hat product and it is not included in the Ansible Automation Platform or Red Hat Developer Hub subscription.

This example assumes that OpenShift Dev Spaces has been configured in the Ansible plug-ins installation.

#### Procedure

 In the **catalog item** view of your playbook project, click **Open Ansible project in OpenShift Dev Spaces**.

A VS Code instance of OpenShift Dev Spaces opens in a new browser tab. It automatically loads your new Ansible Playbook Git project.
