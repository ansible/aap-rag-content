+++
title = "Feature flag access - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/feature_flag_access"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/feature_flag_access/aem-page/feature_flag_access.html"
last_crumb = "Feature flag access"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Feature flag access"
oversized = "false"
page_slug = "feature_flag_access"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/feature_flag_access"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/feature_flag_access/toc/toc.json"
type = "aem-page"
+++

# Feature flag access

Access to the feature flags page is role-based; in other words, access depends on the level of access a user has.

When feature flags are enabled, the following access rules apply.

Superusers (administrators):

- Can view the feature flags section.
- Can toggle runtime feature flags on and off.
- Can access all editable feature flags.

Auditors:

- Can view the feature flags section.
- Can view all flag metadata and current states.
- **Cannot** toggle runtime feature flags, as they have read-only access

Normal users:

- Cannot view the feature flags section.
- Do not see the feature flags menu item in their UI navigation panel.
- Are blocked from direct URL access to the feature flags section.
