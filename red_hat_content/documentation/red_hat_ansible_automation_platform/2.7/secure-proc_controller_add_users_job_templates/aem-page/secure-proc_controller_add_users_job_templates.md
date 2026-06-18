+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_controller_add_users_job_templates"
title = "Add new users and job templates to existing credentials - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials/", "Configure credentials to authenticate remote systems and services"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-proc_controller_add_users_job_templates/aem-page/secure-proc_controller_add_users_job_templates.html"
last_crumb = "Add new users and job templates to existing credentials"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Add new users and job templates to existing credentials"
oversized = "false"
page_slug = "secure-proc_controller_add_users_job_templates"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-proc_controller_add_users_job_templates"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-proc_controller_add_users_job_templates/toc/toc.json"
type = "aem-page"
+++

# Add new users and job templates to existing credentials

You can add new users and job templates to existing credentials in automation controller.

## Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Credentials.
2.  Select the credential that you want to assign to additional users.
3.  Click the **User Access** tab. You can see users and teams associated with this credential and their roles. If no users exist, add them from the **Users** menu. For more information, see [Users](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_users#assembly-controller-users "A user is an individual or entity that can log in to the platform and perform tasks. Users are fundamental units to which roles can be assigned, either directly by an administrator or indirectly through a team.").
4.  Click Add roles.
5.  Select the user(s) that you want to give access to the credential and click Next.
6.  From the **Select roles to apply** page, select the roles you want to add to the User.
7.  Click Next.
8.  Review your selections and click Finish to add the roles or click Back to make changes. The **Add roles** window displays stating whether the action was successful.

    If the action is not successful, a warning displays.

9.  Click Close.
10.  The **User Access** page displays the summary information.
11.  Select the **Job templates** tab to select a job template to which you want to assign this credential.
12.  Chose a job template or select **Create job template** from the **Create template** list to assign the credential to additional job templates. For more information about creating new job templates, see [Job templates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_job_templates "You can create both Job templates and Workflow job templates from Automation Execution > Templates .").
