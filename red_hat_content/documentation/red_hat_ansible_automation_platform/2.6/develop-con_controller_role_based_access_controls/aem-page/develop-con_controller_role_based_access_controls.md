+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-con_controller_role_based_access_controls"
title = "Role-based access controls - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_ug_controller_workflow_job_templates/", "Orchestrate complex automation with workflow job templates"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-con_controller_role_based_access_controls/aem-page/develop-con_controller_role_based_access_controls.html"
last_crumb = "Role-based access controls"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Role-based access controls"
oversized = "false"
page_slug = "develop-con_controller_role_based_access_controls"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-con_controller_role_based_access_controls"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-con_controller_role_based_access_controls/toc/toc.json"
type = "aem-page"
+++

# Role-based access controls

Learn the specific roles required to create, edit, and run automation controller workflow job templates. Understanding these permissions help ensures that access is properly delegated among users and teams.

To edit and delete a workflow job template, you must have the administrator role. To create a workflow job template, you must be an organization administrator or a system administrator.

However, you can run a workflow job template that has job templates that you do not have permissions for. System administrators can create a blank workflow and then grant an `admin_role` to a low-level user, after which they can delegate more access and build the graph. You must have `execute` access to a job template to add it to a workflow job template.

You can also perform other tasks, such as making a duplicate copy or re-launching a workflow, depending on which permissions are granted to a user. You must have permissions to all the resources used in a workflow, such as job templates, before relaunching or making a copy.

For more information, see Managing access with role based access control.

For more information about performing the tasks described, see Workflow job templates.
