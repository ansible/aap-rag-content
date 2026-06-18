+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-oidc_authentication_for_hashicorp_vault"
title = "OIDC authentication for HashiCorp Vault - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-oidc_authentication_for_hashicorp_vault/aem-page/whats_new-oidc_authentication_for_hashicorp_vault.html"
last_crumb = "OIDC authentication for HashiCorp Vault"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "OIDC authentication for HashiCorp Vault"
oversized = "false"
page_slug = "whats_new-oidc_authentication_for_hashicorp_vault"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-oidc_authentication_for_hashicorp_vault"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-oidc_authentication_for_hashicorp_vault/toc/toc.json"
type = "aem-page"
+++

# OIDC authentication for HashiCorp Vault

Ansible Automation Platform supports zero trust access to HashiCorp Vault using OpenID Connect (OIDC)-based workload identity, eliminating the need to store Vault credentials in Ansible Automation Platform.

For each automation job configured with a Vault OIDC credential, Ansible Automation Platform issues a JSON Web Token (JWT) to authenticate the workload with HashiCorp Vault. Vault then validates this token via OIDC and applies your configured policies to either allow or deny access to the requested secrets.

JWTs are issued with an expiration time that matches the job timeout when available. When the timeout is not available, a configurable platform default is used.

To configure OIDC for your environment, follow this workflow:

1. Configure the HashiCorp Vault server to allow OIDC/JWT Authentication.
2. Configure credentials in Ansible Automation Platform to use either of these credential types: HashiCorp Vault Secret Lookup (OIDC) or HashiCorp Vault Signed SSH (OIDC).
