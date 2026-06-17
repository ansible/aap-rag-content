+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_fixed_issues"
template = "docs/aem-title.html"
title = "Fixed issues - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-platform_intro/", "Release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_fixed_issues/aem-page/whats_new-aap_26_fixed_issues.html"
last_crumb = "Fixed issues"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Fixed issues"
oversized = "false"
page_slug = "whats_new-aap_26_fixed_issues"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_fixed_issues"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_fixed_issues/toc/toc.json"
type = "aem-page"
+++

# Fixed issues

This section provides information about fixed issues in Ansible Automation Platform 2.6.

## Ansible Automation Platform

Note:

Ansible Automation Platform 2.6 also includes the fixes from the latest 2.5 patch release. For more information, see [Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/release_notes/patch_releases#aap-25-20250923) patch release September 23, 2025.

Ansible Automation Platform

- The `SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL` configuration parameter now functions as expected, allowing social auth logins to set the platform gateway username to the user’s email when enabled.(AAP-49736)


RPM-based Ansible Automation Platform

- Fixed an issue where installer managed CA certificates were discovered but not used by the installer.(AAP-53335)
