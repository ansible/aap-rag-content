+++
template = "docs/aem-title.html"
title = "Ansible Automation Platform 2.7 hotfix patch release September 25, 2026 - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_09_21_hotfixs"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-overview_of_redhat_ansible_intro/", "Ansible Automation Platform release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_09_21_hotfixs/aem-page/whats_new-aap_27_2026_09_21_hotfixs.html"
last_crumb = "Ansible Automation Platform 2.7 hotfix patch release September 25, 2026"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Ansible Automation Platform 2.7 hotfix patch release September 25, 2026"
oversized = "false"
page_slug = "whats_new-aap_27_2026_09_21_hotfixs"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_09_21_hotfixs"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_09_21_hotfixs/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform 2.7 hotfix patch release September 25, 2026

The following release notes detail a hotfix for the Ansible Automation Platform hotfix patch released on September 25, 2026

This release includes the following components and versions:

| Release Date       | Component versions                                                                                                                                                                                       |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| September 25, 2026 | Automation controller 4.8.9Automation hub 4.12.7Event-Driven Ansible 1.3.11Container-based installer Ansible Automation Platform (bundle) 2.7-9Container-based installer Ansible Automation Platform (online) 2.7-9Receptor 1.6.8 |

Operator bundle

- namespace: aap-operator.v2.7.0-0.1790279930
- cluster: aap-operator.v2.7.0-0.1790279903

## Overview

This release of Ansible Automation Platform 2.7 includes a critical bug fix for the Platform Operator component. This patch addresses an intermittent service availability issue affecting the gateway’s internal health-check endpoint under concurrent user load.

## Bug fixes

## Platform Operator

- Fixed an issue where the gateway could intermittently return 503 errors on its internal health-check endpoint during periods of concurrent user activity. This was caused by an overly restrictive connection limit, which has now been removed. (AAP-93604)
