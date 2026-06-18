+++
title = "Changed features - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-changed_feeatures"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-overview_of_redhat_ansible_intro/", "Ansible Automation Platform release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-changed_feeatures/aem-page/whats_new-changed_feeatures.html"
last_crumb = "Changed features"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Changed features"
oversized = "false"
page_slug = "whats_new-changed_feeatures"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-changed_feeatures"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-changed_feeatures/toc/toc.json"
type = "aem-page"
+++

# Changed features

The following release notes detail the changed features for the Ansible Automation Platform general availability release on June 3, 2026.

## Changed features

Ansible plug-ins for Red Hat Developer Hub

- **OCI container plug-in delivery**: OCI container delivery is now the recommended method for installing automation portal plug-ins. Set `pluginMode: oci` in the Helm chart configuration. The tarball delivery method is deprecated.
- **Templates and History menus require RBAC permissions**: The Templates and History navigation menus are now gated by role-based access control. After upgrading, these menus are hidden unless administrators grant the required permissions. For more information, see the automation portal upgrade documentation.
