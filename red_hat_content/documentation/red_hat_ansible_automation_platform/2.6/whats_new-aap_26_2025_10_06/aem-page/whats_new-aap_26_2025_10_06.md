+++
title = "Ansible Automation Platform patch release October 6, 2025 - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2025_10_06"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-async_updates/", "Patch releases"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2025_10_06/aem-page/whats_new-aap_26_2025_10_06.html"
last_crumb = "Ansible Automation Platform patch release October 6, 2025"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Ansible Automation Platform patch release October 6, 2025"
oversized = "false"
page_slug = "whats_new-aap_26_2025_10_06"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2025_10_06"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2025_10_06/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform patch release October 6, 2025

The following release notes detail the updates for the Ansible Automation Platform patch released on October 6, 2025.

This release includes the following components and versions:

| Release Date        | Component versions                                                                                                                                                                                                                                                                                                                                           |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <br>October 6, 2025 | Automation controller 4.7.1Automation hub 4.11.0Event-Driven Ansible 1.2.0Container-based installer Ansible Automation Platform (bundle) 2.6-1Container-based installer Ansible Automation Platform (online) 2.6-1Receptor 1.5.7RPM-based installer Ansible Automation Platform (bundle) 2.6-1RPM-based installer Ansible Automation Platform (online) 2.6-1 |


CSV Versions in this release:

- Namespace-scoped Bundle: aap-operator.v2.6.0-0.1759764484
- Cluster-scoped Bundle: aap-operator.v2.6.0-0.1759764962

## Automation hub

- Fixed an issue where the automation hub collections in 2.6 could not be pulled with Ansible Galaxy due to incorrect dynamic http logic. This issue only affects the Red Hat Ansible Automation Platform Operator installation.(AAP-55099)
