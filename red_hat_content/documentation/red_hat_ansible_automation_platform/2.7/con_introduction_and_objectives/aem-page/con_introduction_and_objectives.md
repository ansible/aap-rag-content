+++
title = "Migrate from existing deployment topologies - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/con_introduction_and_objectives"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/con_introduction_and_objectives/aem-page/con_introduction_and_objectives.html"
last_crumb = "Migrate from existing deployment topologies"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Migrate from existing deployment topologies"
oversized = "false"
page_slug = "con_introduction_and_objectives"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/con_introduction_and_objectives"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/con_introduction_and_objectives/toc/toc.json"
type = "aem-page"
+++

# Migrate from existing deployment topologies

Learn about supported migration paths between RPM-based, container-based, OpenShift Container Platform, and Managed Ansible Automation Platform deployments, including step-by-step workflows and migration requirements.

Migration between different Ansible Automation Platform deployment types for Ansible Automation Platform 2.6 requires specific steps and considerations.

The supported migration paths include:

| Source environment                              | Target environment                                       |
| ----------------------------------------------- | -------------------------------------------------------- |
| <br>RPM-based Ansible Automation Platform       | <br>Container-based Ansible Automation Platform platform |
| <br>RPM-based Ansible Automation Platform       | <br>OpenShift Container Platform                         |
| <br>RPM-based Ansible Automation Platform       | <br>Managed Ansible Automation Platform                  |
| <br>Container-based Ansible Automation Platform | <br>OpenShift Container Platform                         |
| <br>Container-based Ansible Automation Platform | <br>Managed Ansible Automation Platform                  |


Migrations outside of those listed are not supported at this time.

Supported migration workflows:

- Document all components and configurations that require migration between Ansible Automation Platform platforms
- Provide step-by-step migration workflows for different deployment scenarios
- Identify potential challenges and unknowns that require further investigation
