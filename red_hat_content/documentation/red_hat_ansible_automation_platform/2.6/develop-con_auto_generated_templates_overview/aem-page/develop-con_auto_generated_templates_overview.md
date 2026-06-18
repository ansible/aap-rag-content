+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-con_auto_generated_templates_overview"
title = "Understanding auto-generated templates - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-con_auto_generated_templates_overview/aem-page/develop-con_auto_generated_templates_overview.html"
last_crumb = "Understanding auto-generated templates"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Understanding auto-generated templates"
oversized = "false"
page_slug = "develop-con_auto_generated_templates_overview"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-con_auto_generated_templates_overview"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-con_auto_generated_templates_overview/toc/toc.json"
type = "aem-page"
+++

# Understanding auto-generated templates

Ansible automation portal automatically generates templates from Ansible Automation Platform Job Templates. Each Ansible Automation Platform Job Template with the appropriate configuration becomes a template that users can execute from Ansible automation portal.

Note:

Templates in Ansible automation portal use Backstage Software Templates as the underlying technology. For details on supported usage, see the Ansible automation portal support policy.

Auto-generated templates include:

- Form fields generated from Ansible Automation Platform Job Template Surveys and "Prompt on Launch" options.
- Metadata (name, description, labels) mapped from Ansible Automation Platform Job Template properties.
- A single step that launches the Ansible Automation Platform Job Template using the `rhaap:launch-job-template` action.
- Output that displays the job execution results to the user.


Users only see and execute templates for Ansible Automation Platform Job Templates they have Job Template Execute permission in Ansible Automation Platform.
