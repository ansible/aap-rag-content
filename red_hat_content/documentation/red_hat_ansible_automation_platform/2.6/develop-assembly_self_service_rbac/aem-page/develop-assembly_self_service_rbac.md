+++
title = "Set up permissions for custom self-service templates - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_rbac"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_rbac/aem-page/develop-assembly_self_service_rbac.html"
last_crumb = "Set up permissions for custom self-service templates"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Set up permissions for custom self-service templates"
oversized = "false"
page_slug = "develop-assembly_self_service_rbac"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_rbac"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_rbac/toc/toc.json"
type = "aem-page"
+++

# Set up permissions for custom self-service templates

Custom self-service templates that you set up in Ansible automation portal use a different set of RBAC rules than the RBAC rules for auto-generated self-service templates that are synchronized from Ansible Automation Platform.

- **Auto-generated self-service templates**: The RBAC settings for these templates are synchronized from Ansible Automation Platform.
- **Custom self-service templates**: You must set up RBAC for these templates in Ansible automation portal.

## Set up RBAC for custom self-service templates

By default, Ansible Automation Platform administrators can define Ansible automation portal RBAC roles.

### Before you begin

- You have created a user, for example `example-user`.
- You have added this user as a member of a team, for example `example-team`.

### About this task

This procedure describes how to create a role in Ansible automation portal that allows only a selected team to view and execute particular custom self-service templates.

Custom self-service templates in Ansible automation portal are associated with job templates in Ansible Automation Platform. This association is set in the `steps.actions` section of the YAML file for the custom self-service template.

If you assign permissions to a particular team to launch a custom self-service template from Ansible automation portal, then you must make sure that that team has permission to run the associated job templates in Ansible Automation Platform.

### Procedure

1.  In a browser, log in to your Ansible automation portal instance as an Ansible Automation Platform user with Ansible Automation Platform administrator privileges.
2.  In the navigation panel, select Administration> (and then)RBAC.
3.  In the **RBAC** view, click **Create**. The **Create Role** view appears.

  1.  Enter a name for the role.
  2.  In the **Users and Groups** section, select the Ansible Automation Platform teams and users to assign to this role.
  
![Select users and groups table showing Members column](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/self-service-rbac-select-users-groups.png)  
     Note:
            The **Members** column displays the total count of users in each team, including both regular team members and administrators.

  3.  In the **Add Permission policies** section, select the plug-ins that you want to enable for the role.
  4.  Select **Permission** in the list of plug-ins to configure the fine-grained permission policies for the role.

4.  Click **Next**.
5.  Review the settings that you have selected for the role.
6.  Click **Create** to create the role.

## Verify RBAC

This procedure describes how to verify that the role you set up is working correctly.

### Procedure

1.  Verify that users with permissions can use a template:
  1.  Log in to Ansible automation portal as a user who is a member of a team that has been enabled to use a role.
  2.  Verify that RBAC is applied and that the user can use the templates that you enabled for the role.
2.  Log out of Ansible automation portal.
3.  Verify that users without permissions can not see or use a template:
  1.  Log in to Ansible automation portal as a user who is not a member of the new team that has been enabled to use the role.
  2.  Verify that RBAC is applied and that the user cannot use the templates that you enabled for the role.
4.  Log out of Ansible automation portal.

## Deregister custom self-service templates

You can deregister custom self-service templates. Deregistering templates deletes them from the **Templates** view in the Ansible automation portal console.

### Procedure

1.  In a browser, log in to Ansible automation portal as a user with administrative privileges.
2.  Select **Templates** to display the self-service templates.
3.  For each custom self-service template that you want to delete, execute the following steps:
  1.  Click a custom self-service template to open the **Template detail** view. The navigation bar contains the **Unregister Template** option.
  2.  Click **Unregister Template**.  
![Unregister template option](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/self-service-unregister-template.png)  
  3.  In the dialog, confirm that you want to deregister the template.
  4.  Click **Delete Entity** to unregister the template.

### Results

In a browser, navigate to the **Templates** view for your Ansible automation portal instance. Verify that the custom self-service templates that you deregistered have been deleted.
