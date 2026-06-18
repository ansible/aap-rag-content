+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-con_terraform_provider_tf_actions_intro"
title = "About Terraform Actions and Ansible Automation Platform - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-assembly_terraform_introduction/", "Integrate with IBM HashiCorp Terraform"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-con_terraform_provider_tf_actions_intro/aem-page/integrate-con_terraform_provider_tf_actions_intro.html"
last_crumb = "About Terraform Actions and Ansible Automation Platform"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "About Terraform Actions and Ansible Automation Platform"
oversized = "false"
page_slug = "integrate-con_terraform_provider_tf_actions_intro"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/integrate-con_terraform_provider_tf_actions_intro"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/integrate-con_terraform_provider_tf_actions_intro/toc/toc.json"
type = "aem-page"
+++

# About Terraform Actions and Ansible Automation Platform

The Terraform (TF) Actions adds an imperative `action` block to the HCL language, letting you execute steps after infrastructure is provisioned without leaving the declarative Terraform workflow. This keeps the entire infrastructure and configuration process visible in your Terraform configuration.

TF Actions can be used to trigger Ansible automation for configuration management, such as sending an event and payload to Ansible Automation Platform to configure newly provisioned virtual machines.

There are two actions implemented with the Terraform provider for Ansible Automation Platform:

- **Launch a job directly:** Runs the job as a direct, immediate execution request to Ansible Automation Platform. You must explicitly define which specific Ansible Automation Platform job template the TF Action should call.
- **Use Event-Driven Ansible:** Sends an event to Ansible Automation Platform, which then uses rulebooks to intelligently decide which playbook to run based on the event’s payload. This allows for more dynamic, scalable and reactive automation.
