# Authenticate to hashicorp.vault
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

-  [Create a custom credential](/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-assembly_vault_authenticating#vault-creating-custom-credential "Vault users must create a custom credential to use with job templates in Ansible Automation Platform.")

