+++
title = "Create a credential using a Vault OIDC credential type - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-create_a_credential_using_a_vault_oidc_credential_type"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-create_a_credential_using_a_vault_oidc_credential_type/aem-page/whats_new-create_a_credential_using_a_vault_oidc_credential_type.html"
last_crumb = "Create a credential using a Vault OIDC credential type"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Create a credential using a Vault OIDC credential type"
oversized = "false"
page_slug = "whats_new-create_a_credential_using_a_vault_oidc_credential_type"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-create_a_credential_using_a_vault_oidc_credential_type"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-create_a_credential_using_a_vault_oidc_credential_type/toc/toc.json"
type = "aem-page"
+++

# Create a credential using a Vault OIDC credential type

Configure an OIDC credential to enable Ansible Automation Platform to authenticate with HashiCorp Vault using short-lived tokens instead of static credentials, reducing the risk of credential exposure.

## Before you begin

- You have configured the HashiCorp Vault Server with the OIDC Discovery URL.
- You have set your install time feature flag, `FEATURE_OIDC_WORKLOAD_IDENTITY_ENABLED`, to `True`.
- You have created a JWT role and appropriate access policies in Vault.

## Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Credentials, and then select .
3.  Click Create credential.
4.  Edit the following fields:
  

Name
The name of your credential.

Description
Optional field describing your credential.

Organization
Select an organization or choose Default.

Credential type
Select either HashiCorp Vault Secret Lookup or HashiCorp Vault Signed SSH. Depending on your selection, relevant fields are displayed.

Server URL
The URL used to communicate with the HashiCorp Vault secret management system. Note:
  This value is also used as the **JSON Web Token (JWT) audience**. Ensure that the `bound_audiences` parameter in your Vault JWT role matches this URL exactly to achieve successful authentication.

CA Certificate
Optional CA certificate used to verify connections to the HashiCorp Vault server.

Path to auth
Path to the authentication method in HashiCorp Vault. Use the default `jwt` unless you used a custom path when you ran `vault auth enable jwt`.

JWT role
JWT role name that is configured in HashiCorp Vault.

Namespace Name (Vault Enterprise only)
Name of the Vault Enterprise namespace where your secrets and authentication methods are configured. Namespaces provide tenant isolation within a shared Vault instance, allowing teams or environments to manage secrets independently. If your Vault server does not use namespaces, leave this field blank.

API version
- The version of the Vault KV secrets engine used for secret lookups. Valid values are `v1` (for KV version 1) or `v2` (for KV version 2).

5.  Click Test to verify connection to the secret management system.
6.  In the **Test external credential** dialog, edit the fields:
  - For HashiCorp Vault Secret Lookup (OIDC)

Name of secret backend
The unique identifier or name assigned to your secret engine instance in HashiCorp Vault.

Path to secret
The database or storage path to the specific secret inside the Vault engine (for example, `secret/data/myapp`).

Path to auth
The endpoint path where the JWT/OIDC authentication method is enabled in Vault (defaults to `jwt` if not customized).

Key name
The specific key within the secret payload whose value you want to retrieve.

Secret version (v2 only)
The specific version number of the secret to fetch. Leave blank to retrieve the latest version.

  - For HashiCorp Vault Signed SSH (OIDC)

Unsigned public key
Paste the raw, unsigned public SSH key that requires a signature from the HashiCorp Vault SSH secrets engine.

Path to secret
The storage path configured for the SSH secrets engine in Vault (for example, `ssh-client-signer`).

Path to auth
The endpoint path where the JWT/OIDC authentication method is enabled in Vault.

Role name
The specific role name configured within the Vault SSH secrets engine that dictates signing permissions.

Valid principals
A comma-separated list of valid usernames or hosts allowed to use the signed certificate.

7.  Click Run.
  A success or error message displays, showing the claims associated with the job template you selected.   - For errors, click Retry to correct your input in the Test external credential dialog, or click Cancel to return to the Details screen of your target credential. Review the displayed claims and Vault logs to troubleshoot any errors.
  - For successful tests, click Close. You are returned to the Details screen of your target credential.

8.  Click Create credential.
