+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_06_23"
title = "Ansible Automation Platform 2.7 Release Notes - June 23, 2026 (2.7-2) - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-overview_of_redhat_ansible_intro/", "Ansible Automation Platform release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_06_23/aem-page/whats_new-aap_27_2026_06_23.html"
last_crumb = "Ansible Automation Platform 2.7 Release Notes - June 23, 2026 (2.7-2)"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Ansible Automation Platform 2.7 Release Notes - June 23, 2026 (2.7-2)"
oversized = "false"
page_slug = "whats_new-aap_27_2026_06_23"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_06_23"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_06_23/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform 2.7 Release Notes - June 23, 2026 (2.7-2)

The following release notes detail the CVEs and Bug fixes for the Ansible Automation Platform patch released on June 23, 2026.

This release includes the following components and versions:

| Release Date  | Component versions                                                                                                                                                                                       |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| June 23, 2026 | Automation controller 4.8.1Automation hub 4.12.2Event-Driven Ansible 1.3.3Container-based installer Ansible Automation Platform (bundle) 2.7-2Container-based installer Ansible Automation Platform (online) 2.7-2Receptor 1.6.5 |

CSV Versions in this release:

- Namespace-scoped bundle: aap-operator.v2.7.0-0.1781768237
- Cluster-scoped bundle: aap-operator.v2.7.0-0.1781768244

## CVE

- **Event-Driven Ansible**
  * [CVE-2026-11807](https://access.redhat.com/security/cve/cve-2026-11807) - A missing authorization vulnerability was found in the Event-Driven Ansible (EDA) websocket API. The websocket missing authorization allows credential theft via activation_id spoofing:
    + `eda-controller-rhel9`. AAP-78382
