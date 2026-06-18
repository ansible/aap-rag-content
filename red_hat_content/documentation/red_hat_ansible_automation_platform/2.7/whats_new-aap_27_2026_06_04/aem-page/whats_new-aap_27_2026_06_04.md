+++
title = "Ansible Automation Platform patch release June 4, 2026 - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_06_04"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-overview_of_redhat_ansible_intro/", "Ansible Automation Platform release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_06_04/aem-page/whats_new-aap_27_2026_06_04.html"
last_crumb = "Ansible Automation Platform patch release June 4, 2026"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Ansible Automation Platform patch release June 4, 2026"
oversized = "false"
page_slug = "whats_new-aap_27_2026_06_04"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_06_04"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_06_04/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform patch release June 4, 2026

The following release notes detail the CVEs and Bug fixes for the Ansible Automation Platform patch released on June 4, 2026

This release includes the following components and versions:

| Release Date     | Component versions                                                                                                                                                                                                                 |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>June 4, 2026 | Automation controller 4.8.0Automation hub 4.12.1Event-Driven Ansible 1.3.1Container-based installer Ansible Automation Platform (bundle) 2.7-1.1Container-based installer Ansible Automation Platform (online) 2.7-1Receptor 1.6.5 |


CSV Versions in this release:

- Namespace-scoped bundle: aap-operator.v2.7.0-0.1780540119
- Cluster-scoped bundle: aap-operator.v2.7.0-0.1780540580

## CVE

## Lightspeed

- [CVE-2026-24486](https://access.redhat.com/security/cve/cve-2026-48710) – Starlette: Security restriction bypass via malformed HTTP Host header

## Bug fixes

## Automation hub

- Fixed an issue where execution environment (EE) container images that existed in automation hub before a 2.6 to 2.7 upgrade failed to sync or pull with errors such as "unexpected end of JSON input" or "manifest unknown." The upgrade did not fully populate some manifest records for pre-existing EE images. New EE images pushed after the upgrade and collections were not affected. (AAP-77470)
