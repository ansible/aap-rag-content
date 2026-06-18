+++
template = "docs/aem-title.html"
title = "Ansible plug-ins for Red Hat Developer Hub - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-rhdh_ansible_plugins_overview"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_rhdh_intro/", "Ansible plug-ins for Red Hat Developer Hub"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-rhdh_ansible_plugins_overview/aem-page/extend-rhdh_ansible_plugins_overview.html"
last_crumb = "Ansible plug-ins for Red Hat Developer Hub"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Ansible plug-ins for Red Hat Developer Hub"
oversized = "false"
page_slug = "extend-rhdh_ansible_plugins_overview"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-rhdh_ansible_plugins_overview"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-rhdh_ansible_plugins_overview/toc/toc.json"
type = "aem-page"
+++

# Ansible plug-ins for Red Hat Developer Hub

Ansible plug-ins for Red Hat Developer Hub deliver an Ansible-first user experience that simplifies the automation experience for Ansible users of all skill levels.

The Ansible plug-ins provide:

- A customized home page and navigation tailored to Ansible users.
- Software templates for creating Ansible playbook and collection projects that follow best practices.
- Curated Ansible learning paths to help users new to Ansible.
- Links to supported development environments and tools with opinionated configurations.


The `automation-portal` OCI bundle includes the following plug-ins:

*Table 1. Ansible plug\-ins for Red Hat Developer Hub*

| Plug-in                                                    | Type     | Purpose                                                                 |
| ---------------------------------------------------------- | -------- | ----------------------------------------------------------------------- |
| `ansible-plugin-backstage-rhaap`                           | Frontend | Ansible landing page, navigation, and UI components                     |
| `ansible-plugin-backstage-self-service`                    | Frontend | Scaffolder field extensions for AAP token and resource picker           |
| `ansible-plugin-scaffolder-backend-module-backstage-rhaap` | Backend  | Scaffolder actions for creating Ansible content                         |
| `ansible-backstage-plugin-catalog-backend-module-rhaap`    | Backend  | Catalog entity provider for syncing AAP organizations, users, and teams |
