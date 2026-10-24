+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_portal_permission_ref_for_job_templates"
title = "Permissions reference for Ansible Automation Platform job template access - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-install_automation_portal_on_openshift_container_platform/", "Install automation portal on OpenShift Container Platform"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_portal_permission_ref_for_job_templates/aem-page/install-ref_portal_permission_ref_for_job_templates.html"
last_crumb = "Permissions reference for Ansible Automation Platform job template access"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Permissions reference for Ansible Automation Platform job template access"
oversized = "false"
page_slug = "install-ref_portal_permission_ref_for_job_templates"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-ref_portal_permission_ref_for_job_templates"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_portal_permission_ref_for_job_templates/toc/toc.json"
type = "aem-page"
+++

# Permissions reference for Ansible Automation Platform job template access

Permissions for Ansible Automation Platform job templates

| Permission                           | Resource type       | Policy | Description                                                                                             |
| ------------------------------------ | ------------------- | ------ | ------------------------------------------------------------------------------------------------------- |
| `catalog.entity.read`                | catalog-entity      | read   | Users can view synchronized Ansible Automation Platform job templates in the Ansible automation portal. |
| `scaffolder.template.parameter.read` | scaffolder-template | read   | Users can read template parameters.                                                                     |
| `scaffolder.action.execute`          | scaffolder-action   | use    | Users can execute actions through templates.                                                            |
| `scaffolder.task.create`             |                     | create | Users can trigger the execution of Ansible Automation Platform job templates.                           |
| `scaffolder.task.read`               |                     | read   | Users can view task execution history and logs on the **History** page.                                 |
| `scaffolder.task.cancel`             |                     | use    | Users can cancel currently running templates.                                                           |
