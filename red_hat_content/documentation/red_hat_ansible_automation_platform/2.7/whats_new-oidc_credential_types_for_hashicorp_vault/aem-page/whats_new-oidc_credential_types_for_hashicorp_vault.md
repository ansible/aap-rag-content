+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-oidc_credential_types_for_hashicorp_vault"
title = "OIDC credential types for HashiCorp Vault - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-oidc_credential_types_for_hashicorp_vault/aem-page/whats_new-oidc_credential_types_for_hashicorp_vault.html"
last_crumb = "OIDC credential types for HashiCorp Vault"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "OIDC credential types for HashiCorp Vault"
oversized = "false"
page_slug = "whats_new-oidc_credential_types_for_hashicorp_vault"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-oidc_credential_types_for_hashicorp_vault"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-oidc_credential_types_for_hashicorp_vault/toc/toc.json"
type = "aem-page"
+++

# OIDC credential types for HashiCorp Vault

Ansible Automation Platform supports OIDC credential types for HashiCorp Vault that use short-lived JSON Web Tokens instead of static credentials, providing secure, automatic authentication without the need to store or rotate Vault secrets.

You can configure credentials using one of the following OIDC credential types:

-      **HashiCorp Vault Secret Lookup (OIDC):**Fetches arbitrary Key/Value (KV) secrets from HashiCorp Vault that are needed for Ansible automation, such as passwords, private keys, and API keys.

-      **HashiCorp Vault Signed SSH (OIDC):**HashiCorp Vault digitally signs a certificate that Ansible Automation Platform uses to authenticate to a remote host and run automation.

Instead of relying on long-lived credentials that must be stored, rotated, and protected, OIDC credential types use short-lived JSON Web Tokens (JWTs) that are issued per job and expire automatically. This reduces the risk of credential exposure and removes the operational burden of manual credential rotation.

## **JWT expiration and timeout behavior**

When issuing JWTs for OIDC credentials, Ansible Automation Platform uses the job's configured timeout to determine the token's expiration time, aligning it with the expected duration of the job. If the job has no configured timeout, a platform default of 5 minutes (plus 1 minute for clock skew) is used.

This time is intentionally short but generally sufficient because the JWT is only used by the control plane to access HashiCorp Vault and retrieve secrets before automation begins executing. This value is configurable and can be adjusted if jobs fail due to an expired JWT or if a shorter time is needed.
