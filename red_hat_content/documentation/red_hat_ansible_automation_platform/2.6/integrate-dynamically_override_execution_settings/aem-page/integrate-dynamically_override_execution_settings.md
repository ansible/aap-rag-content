+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-dynamically_override_execution_settings"
title = "Dynamically override execution settings - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-assembly_terraform_introduction/", "Integrate with IBM HashiCorp Terraform"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/integrate-dynamically_override_execution_settings/aem-page/integrate-dynamically_override_execution_settings.html"
last_crumb = "Dynamically override execution settings"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Dynamically override execution settings"
oversized = "false"
page_slug = "integrate-dynamically_override_execution_settings"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/integrate-dynamically_override_execution_settings"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/integrate-dynamically_override_execution_settings/toc/toc.json"
type = "aem-page"
+++

# Dynamically override execution settings

As an administrator using Terraform provider, you can configure optional Prompt on Launch parameters in Ansible job and workflow templates to dynamically override default execution settings at runtime.placeholder.

This means that you can use one Ansible template with different Terraform `*.tf` files to deploy many environments. Terraform provides the values when the Ansible job or workflow runs.The Ansible playbooks and templates stored in Ansible Automation Platform remain reusable and independent of the specific Terraform configuration that provisioned them.

You must take the following steps to use Prompt on Launch:

- **Ansible UI:** Select the **Prompt on Launch** checkbox for any of the supported fields in the Ansible job or workflow template.
- **Terraform:** Set the values for the corresponding fields in the `*.tf` file that will launch jobs from that template. If the corresponding value is not set in the `*.tf` file, then the run fails and Ansible Automation Platform sends an error message.
The supported Prompt on Launch settings include:

- **Inventory:** Allows Terraform to specify the inventory that will be used by the Ansible job template.
- **Extra variables:** To use extra variables to pass data or trigger actionable workflows, provide either a JSON or YAML string.
- **Job tag:** Tags to include in the workflow job run.
- **Labels:** Labels can be used to describe a job template, such as dev or test. You can use labels to group and filter job templates and completed jobs in the display.
- **Limit:** The Prompt on Launch option restricts a job template to run against only a specific host or group of hosts within an inventory. Note:
  When running as part of a workflow, the workflow job template limit is used instead.

- **Skip tag:** Tags to ignore in the workflow job run.
