+++
title = "What users see - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-con_auto_generated_what_users_see"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-con_auto_generated_what_users_see/aem-page/develop-con_auto_generated_what_users_see.html"
last_crumb = "What users see"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "What users see"
oversized = "false"
page_slug = "develop-con_auto_generated_what_users_see"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-con_auto_generated_what_users_see"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-con_auto_generated_what_users_see/toc/toc.json"
type = "aem-page"
+++

# What users see

Auto-generated templates appear in the template catalog alongside custom templates. Users browse or search the catalog and select a template to run.

When a user opens an auto-generated template, Ansible automation portal checks the Ansible Automation Platform Job Template for **Prompt on Launch** options and Survey questions. If the Job Template has **Prompt on Launch** options or Survey questions, Ansible automation portal displays a form. Users select Ansible Automation Platform resources by name (such as Inventories or Credentials) and answer survey questions (such as application name or environment). Ansible automation portal handles authentication automatically, so credentials are not visible on the form. If the Job Template has no **Prompt on Launch** options or Survey questions, the Job Template starts running automatically without displaying a form.

After the user submits the form or execution starts automatically, Ansible automation portal launches the Ansible Automation Platform Job Template and displays an output page. The output page shows the job ID, job status, and optional links such as a direct link to the job in Ansible Automation Platform.

Users do not need to understand YAML or the template structure. The form collects the required input, and the output page displays the results.
