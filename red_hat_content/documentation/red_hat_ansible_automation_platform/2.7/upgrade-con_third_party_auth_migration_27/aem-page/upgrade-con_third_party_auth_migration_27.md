+++
template = "docs/aem-title.html"
title = "Third-party authentication provider migration - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-con_third_party_auth_migration_27"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-con_third_party_auth_migration_27/", "Third-party authentication provider migration"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_third_party_auth_migration_27/aem-page/upgrade-con_third_party_auth_migration_27.html"
last_crumb = "Third-party authentication provider migration"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Third-party authentication provider migration"
oversized = "false"
page_slug = "upgrade-con_third_party_auth_migration_27"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-con_third_party_auth_migration_27"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_third_party_auth_migration_27/toc/toc.json"
type = "aem-page"
+++

# Third-party authentication provider migration

In Ansible Automation Platform 2.7, all third-party authentication provider configuration has moved to platform gateway. Configuration in automation controller has been removed.

This applies to:

- LDAP
- SAML
- RADIUS
- TACACS+
- OAuth providers (GitHub, Google, Azure AD, Generic OIDC)
