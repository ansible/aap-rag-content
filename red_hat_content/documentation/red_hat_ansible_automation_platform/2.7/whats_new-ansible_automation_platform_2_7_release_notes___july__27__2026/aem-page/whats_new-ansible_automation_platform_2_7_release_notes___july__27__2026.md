+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-ansible_automation_platform_2_7_release_notes___july__27__2026"
title = "Ansible Automation Platform 2.7 Release Notes - July 27, 2026 (2.7-3) - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-overview_of_redhat_ansible_intro/", "Ansible Automation Platform release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-ansible_automation_platform_2_7_release_notes___july__27__2026/aem-page/whats_new-ansible_automation_platform_2_7_release_notes___july__27__2026.html"
last_crumb = "Ansible Automation Platform 2.7 Release Notes - July 27, 2026 (2.7-3)"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Ansible Automation Platform 2.7 Release Notes - July 27, 2026 (2.7-3)"
oversized = "false"
page_slug = "whats_new-ansible_automation_platform_2_7_release_notes___july__27__2026"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-ansible_automation_platform_2_7_release_notes___july__27__2026"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-ansible_automation_platform_2_7_release_notes___july__27__2026/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform 2.7 Release Notes - July 27, 2026 (2.7-3)

The following release notes detail the CVEs and Bug fixes for the Ansible Automation Platform patch released on July 27, 2026.

This release includes the following components and versions:

| Release Date  | Component versions                                                                                                                                                                                       |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| July 27, 2026 | Automation controller 4.8.3Automation hub 4.12.3Event-Driven Ansible 1.3.4Container-based installer Ansible Automation Platform (bundle) 2.7-3Container-based installer Ansible Automation Platform (online) 2.7-3Receptor 1.6.6 |

CSV Versions in this release:

- Namespace-scoped bundle: aap-operator.v2.7.0-0.1784907685
- Cluster-scoped bundle: aap-operator.v2.7.0-0.1784907698

## Overview

This hotfix release for Ansible Automation Platform 2.7 addresses proxy-related issues in the platform operator that caused authentication failures and component unavailability on proxy-configured OpenShift clusters.

## Bug fixes

## Platform operator

- Fixed an issue where, when a cluster-wide egress proxy was configured on OpenShift, the Ansible Automation Platform gateway operator propagated the `NO_PROXY` environment variable to operand containers verbatim, without including the internal service names that components use to communicate with each other. This caused internal traffic — including JWT key validation calls — to be routed through the corporate proxy, resulting in authentication failures and component unavailability on proxy-configured clusters. The operator now automatically augments `NO_PROXY` with the required internal cluster service exclusions before writing them to operand containers. (AAP-83822, AAP-84164)
