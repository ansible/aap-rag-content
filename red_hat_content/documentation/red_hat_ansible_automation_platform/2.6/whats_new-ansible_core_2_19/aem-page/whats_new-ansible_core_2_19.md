+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-ansible_core_2_19"
title = "ansible-core 2.19 - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-ansible_core_2_19/aem-page/whats_new-ansible_core_2_19.html"
last_crumb = "ansible-core 2.19"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "ansible-core 2.19"
oversized = "false"
page_slug = "whats_new-ansible_core_2_19"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-ansible_core_2_19"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-ansible_core_2_19/toc/toc.json"
type = "aem-page"
+++

# ansible-core 2.19

The ansible-core 2.19 release includes an overhaul of the templating system and a new feature labeled Data Tagging.

Note:

Ansible Automation Platform does not include ansible-core 2.19 by default, but it is compatible with 2.19. See related links for more information.

Changes in ansible-core enable reporting of numerous problematic behaviors that went undetected in previous releases, with wide-ranging positive effects on security, performance, and user experience. Backward compatibility has been preserved where practical, but some breaking changes were necessary. This section describes some common problem scenarios with example content, error messages, and suggested solutions.We recommend you test your playbooks and roles in a staging environment with this release to determine where you may need to make changes.
