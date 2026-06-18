+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2026_01_06"
template = "docs/aem-title.html"
title = "Ansible Automation Platform patch release January 6, 2026 - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-async_updates/", "Patch releases"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2026_01_06/aem-page/whats_new-aap_26_2026_01_06.html"
last_crumb = "Ansible Automation Platform patch release January 6, 2026"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Ansible Automation Platform patch release January 6, 2026"
oversized = "false"
page_slug = "whats_new-aap_26_2026_01_06"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2026_01_06"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2026_01_06/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform patch release January 6, 2026

The following release notes detail the updates for the Ansible Automation Platform patch released on January 6, 2026.

This release includes the following components and versions:

| Release Date        | Component versions                                                                                                                                                                                                                                                                                                                                               |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>January 6, 2026 | Automation controller 4.7.6Automation hub 4.11.4Event-Driven Ansible 1.2.3Container-based installer Ansible Automation Platform (bundle) 2.6-4.1Container-based installer Ansible Automation Platform (online) 2.6-4Receptor 1.6.2RPM-based installer Ansible Automation Platform (bundle) 2.6-3.2RPM-based installer Ansible Automation Platform (online) 2.6-3 |


CSV Versions in this release:

- Namespace: aap-operator.v2.6.0-0.1767630689
- Cluster: aap-operator.v2.6.0-0.1767630627

## CVE

With this update, the following CVEs have been addressed:

- [CVE-2025-14025](https://access.redhat.com/security/cve/cve-2025-14025)`automation-gateway`: Read-only Personal Access Token (PAT) bypasses write restrictions.(AAP-60068)
- [CVE-2025-68664](https://access.redhat.com/security/cve/cve-2025-68664)`ansible-automation-platform-26/lightspeed-rhel9: LangChain`: Arbitrary code execution via serialization injection.(AAP-61313)
