+++
title = "Ansible Automation Platform patch release November 5, 2025 - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2025_11_05"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-async_updates/", "Patch releases"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2025_11_05/aem-page/whats_new-aap_26_2025_11_05.html"
last_crumb = "Ansible Automation Platform patch release November 5, 2025"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Ansible Automation Platform patch release November 5, 2025"
oversized = "false"
page_slug = "whats_new-aap_26_2025_11_05"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2025_11_05"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2025_11_05/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform patch release November 5, 2025

The following release notes detail the updates for the Ansible Automation Platform patch released on November 5, 2025.

This release includes the following components and versions:

| Release Date         | Component versions                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <br>November 5, 2025 | Automation controller 4.7.4Automation hub 4.11.2Event-Driven Ansible 1.2.1Container-based installer Ansible Automation Platform (bundle) 2.6-2Container-based installer Ansible Automation Platform (online) 2.6-2Receptor 1.6.0RPM-based installer Ansible Automation Platform (bundle) 2.6-2RPM-based installer Ansible Automation Platform (online) 2.6-2 |


CSV Versions in this release:

- Namespace-scoped Bundle: aap-operator.v2.6.0-0.1761384532
- Cluster-scoped Bundle: aap-operator.v2.6.0-0.1761384578

## Red Hat Ansible Lightspeed

Bug Fixes
- A typo in the `containerfile` caused the **nginx** configuration file to be copied to a non-existent directory in operator-based installations, leading to the Lightspeed API service being unavailable due to incorrect port configuration. With this release, the typo has been fixed, ensuring the Lightspeed API service now listens on the correct port in operator-based installations, improving API endpoint accessibility.(AAP-56712)

## Technical note

Red Hat Ansible Lightspeed
RFC 2818 is now enforced between the lightspeed service and the identity provider (gateway) during the OAuth2 authorisation.

## Container-based Ansible Automation Platform

Bug Fixes
- Fixed an issue with the chatbot response about the latest Ansible Automation Platform version.(AAP-57385)
