+++
title = "Authenticate to hashicorp.vault - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-assembly_vault_authenticating"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-assembly_vault_introduction/", "Integrate with IBM HashiCorp Vault"]]
category = "Integrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/integrate-assembly_vault_authenticating/aem-page/integrate-assembly_vault_authenticating.html"
last_crumb = "Authenticate to hashicorp.vault"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Authenticate to hashicorp.vault"
oversized = "false"
page_slug = "integrate-assembly_vault_authenticating"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/integrate-assembly_vault_authenticating"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/integrate-assembly_vault_authenticating/toc/toc.json"
type = "aem-page"
+++

# Authenticate to `hashicorp.vault`

After you install or migrate to the `hashicorp.vault` collection, authentication is configured in the Ansible Automation Platform user interface. An administrator creates a custom credential type to authenticate to Vault. Then users create credentials to use with job templates.

## About the Vault integration

Vault lets you centrally store and manage secrets securely. The Ansible Automation Platform certified `hashicorp.vault` collection provides fully automated lifecycle and operation management for Vault. You can create, update, and delete secrets through playbooks.

- **Existing `community.hashi_vault` users:** The `hashicorp.vault` solution is intended to replace unsupported `community.hashi_vault` collection. Use the migration path to keep your existing playbooks.
- **New Vault users:** The `hashicorp.vault` collection is included in the supported execution environment from automation hub.


Note:

Although the `hashicorp.vault` and `hashi.terraform` collections work independently of each other and are designed for different tasks, you can use them together in advanced workflows.

## Authentication architecture

The `hashicorp.vault` collection manages authentication through environment variables and client initialization. This approach enhances security by preventing sensitive credentials from being passed directly as module parameters within playbook tasks.

The `hashicorp.vault` collection injects credentials into job templates with environment variables, so you get simpler, cleaner task definitions while ensuring that authentication details remain secure.

The following authentication types are supported:

- **appRole authentication:** Use either one of the following methods when using appRole authentication:
  * Set the `VAULT_APPROLE_ROLE_ID` and `VAULT_APPROLE_SECRET_ID` environment variables. When you use environment variables, you must also create a custom credential type and credentials that will be passed to the job template.
  * Directly pass the `role_id` and `secret_id` parameters to the tasks, for example:

```
- name: Create a secret with AppRole authentication
  hashicorp.vault.kv2_secret:
    url: https://vault.example.com:8200
    auth_method: approle
    role_id: "{{ vault_role_id }}"
    secret_id: "{{ vault_secret_id }}"
    path: myapp/config
    data:
      api_key: secret-api-key
```

- **Token authentication:** Set the `VAULT_TOKEN` environment variable. Optionally, you can configure parameters for the token. If parameters are not provided, then the module uses environment variables.

## Create a custom credential type for Vault

As an admin, you create a secure credential type in Ansible Automation Platform, which is used to authenticate to Vault.

### Before you begin

Do *one* of the following:

- **New users:** Install the Ansible Automation Platform certified `hashicorp.vault` collection from Automation hub.
- **`community.hashi_vault` collection users:** Migrate from `community.hashi_vault`.

### About this task

You can configure role-based (appRole) authentication or allow users to directly provide a token.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select **Automation Execution> (and then)Infrastructure> (and then)Credential Types**.
3.  Click Create a credential type. The **Create Credential Type** page opens.
4.  Enter a name and a description in the corresponding fields.
5.  If you want to configure token authentication for individual users:
  1.  For **Input configuration**, enter:
  

```
fields:
 - id: vault_token
   type: string
   label: Hashicorp Vault Token
   secret: true
```

  2.  For **Injector configuration**, enter:
  

```
env:
   VAULT_TOKEN: '{{ vault_token }}'
```

6.  If you want to configure appRole authentication using `role_id` and `secret_id`:
  1.  For **Input configuration**, enter:
  

```
fields:
  - id: vault_approle_role_id
    type: string
    label: Hashicorp Vault appRole Role ID
    secret: true
  - id: vault_approle_secret_id
    type: string
    label: Hashicorp Vault appRole Secret ID
    secret: true
```

  2.  For **Injector configuration**, enter:
  

```
env:
    VAULT_APPROLE_ROLE_ID: '{{ vault_approle_role_id }}'
    VAULT_APPROLE_SECRET_ID: '{{ vault_approle_secret_id }}'
```

7.  Click Create credential type.

### What to do next

-  [Create a custom credential](/documentation/en-us/red_hat_ansible_automation_platform/2.6/integrate-assembly_vault_authenticating#vault-creating-custom-credential "Vault users must create a custom credential to use with job templates in Ansible Automation Platform.")

## Create a custom credential

Vault users must create a custom credential to use with job templates in Ansible Automation Platform.

### Before you begin

- Your administrator has created a Vault credential type.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select **Automation Execution> (and then)Infrastructure> (and then)Credentials**, and then select Create credential.
3.  Enter a name and a description in the corresponding fields.
4.  (Optional) From the **Organization** list, select an organization.
5.  From the **Credential type** list, select a Vault credential type. The fields that display depend on the credential type.
6.  Do *one* of the following:
  1.  For the token authentication, add your Vault token and edit any fields as needed.
  2.  For the appRole authentication method, enter the IDs in the **appRole Role ID** and **appRole Secret ID** fields. Edit any other fields as needed.
7.  Click Save credential. You are ready to use the credential in a job template.
