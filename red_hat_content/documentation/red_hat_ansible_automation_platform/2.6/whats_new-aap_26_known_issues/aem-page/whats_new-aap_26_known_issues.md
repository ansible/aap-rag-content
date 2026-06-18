+++
title = "Known issues - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_known_issues"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-platform_intro/", "Release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_known_issues/aem-page/whats_new-aap_26_known_issues.html"
last_crumb = "Known issues"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Known issues"
oversized = "false"
page_slug = "whats_new-aap_26_known_issues"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_known_issues"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_known_issues/toc/toc.json"
type = "aem-page"
+++

# Known issues

This section provides information about known issues in Ansible Automation Platform 2.6.

- For role based authentication mappings, the role list includes all roles within the platform. Only the role assignments of Org Admin, Org Member, Team Admin, Team Member, and Platform Auditor are supported at this time. The list will be limited to only those that can be applied at a platform level in a subsequent release.

- If you have an existing deployment of Red Hat Ansible Lightspeed on Ansible Automation Platform 2.5, upgrading to Ansible Automation Platform 2.6 will cause your Red Hat Ansible Lightspeed deployment to fail. To avoid this failure, do not upgrade to Ansible Automation Platform 2.6 until a forthcoming patch is released on October 22, 2025. However, new deployments of Red Hat Ansible Lightspeed will work correctly on Ansible Automation Platform 2.6.(AAP-54064)     For more information, see [Ansible Lightspeed upgrade fails when upgrading Ansible Automation Platform 2.5 to 2.6](https://access.redhat.com/articles/7132132).

- Automation controller in Ansible Automation Platform 2.4 allowed customers to enter an encrypted private key in SAML configuration without raising an error. If request signing was not enabled in the authenticator and the SAML IdP, then the Ansible Automation Platform administrator would not know that encrypted keys were not supported. Encrypted keys not supported in Ansible Automation Platform 2.6 authenticators. The platform alerts users that encrypted keys are not supported. However, when upgrading from Ansible Automation Platform 2.4 to 2.6, customers must replace encrypted private keys with unencrypted private keys in their SAML authenticators to prevent migration errors for the authenticator to platform gateway. If you skip this step, the authenticator is not migrated as part of the upgrade. The SAML authenticator must then be recreated manually by a local administrator to re-enable authentication. This might delay SSO users from logging back into the platform after the upgrade.
