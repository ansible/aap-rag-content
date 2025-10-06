# 2. Vault integration
## 2.1. About the Vault integration
### 2.1.1. Introduction




Vault lets you centrally store and manage secrets securely. The Ansible Automation Platform certified `hashicorp.vault` collection provides fully automated Key/Value V2 (KV2) secret lifecycle management for Vault. You can create, update, and delete secrets through playbooks.

-  **Existing `    community.hashi_vault` users:** The `    hashicorp.vault` solution is intended to replace unsupported `    community.hashi_vault` collection. Use the migration path to keep your existing playbooks. For more information about migrating, see [Migrating from community.hashi_vault](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_hashicorp_and_ansible_automation_platform/vault-product#vault-migrating-from-community-hashi-vault) .
-  **New Vault users:** The `    hashicorp.vault` collection is included in the supported execution environment from automation hub.


Note
Although the `hashicorp.vault` and `hashi.terraform` collections work independently of each other and are designed for different tasks, you can use them together in advanced workflows.



## 2.2. Authenticating to `hashicorp.vault`




After you install or migrate to the `hashicorp.vault` collection, authentication is configured in the Ansible Automation Platform user interface:

- An administrator creates a custom credential type to authenticate to Vault.
- Users create credentials (based on the credential type) to use with job templates in Ansible Automation Platform.


### 2.2.1. Authentication architecture




The `hashicorp.vault` collection manages authentication through environment variables and client initialization. This approach enhances security by preventing sensitive credentials from being passed directly as module parameters within playbook tasks. Instead, `hashicorp.vault` injects credentials into job templates with environment variables, so you get simpler, cleaner task definitions while ensuring that authentication details remain secure.

The following authentication types are supported:

-  **appRole authentication:** Use either one of the following methods when using appRole authentication:


- Set the `        VAULT_APPROLE_ROLE_ID` and `        VAULT_APPROLE_SECRET_ID` environment variables. When you use environment variables, you must also create a custom credential type and credentials that will be passed to the job template.
- Directly pass the `        role_id` and `        secret_id` parameters to the tasks, for example:


```
- name: Create a secret with AppRole authentication          hashicorp.vault.kv2_secret:            url: https://vault.example.com:8200            auth_method: approle            role_id: "{{ vault_role_id }}"            secret_id: "{{ vault_secret_id }}"            path: myapp/config            data:              api_key: secret-api-key
```



-  **Token authentication:** Set the `    VAULT_TOKEN` environment variable.

Optionally, you can configure parameters for the token. If parameters are not provided, then the module uses environment variables.




### 2.2.2. Creating a custom credential type




As an admin, you create a secure credential type in Ansible Automation Platform, which is used to authenticate to Vault.

You can configure role-based (appRole) authentication or allow users to directly provide a token.

**Prerequisites**

Do _one_ of the following:


-  **New users:** Install the Ansible Automation Platform certified `    hashicorp.vault` collection from [Automation hub](https://www.redhat.com/en/technologies/management/ansible/automation-hub) .
-  ** `    community.hashi_vault` collection users:** Migrate from `    community.hashi_vault` . For more information, see [Migrating from community.hashi_vault](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_hashicorp_and_ansible_automation_platform/vault-product#vault-migrating-from-community-hashi-vault) .


**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Execution→Infrastructure→Credential Types.
1. ClickCreate a credential type. The **Create Credential Type** page opens.
1. Enter a name and a description in the corresponding fields.
1. If you want to configure token authentication for individual users:


1. For **Input configuration** , enter:


```
fields:         - id: vault_token           type: string           label: Hashicorp Vault Token           secret: true
```


1. For **Injector configuration** , enter:


```
env:           VAULT_TOKEN: '{{ vault_token }}'
```



1. If you want to configure appRole authentication using `    role_id` and `    secret_id` :


1. For **Input configuration** , enter:


```
fields:          - id: vault_approle_role_id            type: string            label: Hashicorp Vault appRole Role ID            secret: true          - id: vault_approle_secret_id            type: string            label: Hashicorp Vault appRole Secret ID            secret: true
```


1. For **Injector configuration** , enter:


```
env:            VAULT_APPROLE_ROLE_ID: '{{ vault_approle_role_id }}'            VAULT_APPROLE_SECRET_ID: '{{ vault_approle_secret_id }}'
```



1. ClickCreate credential type.


**Next step**

-  [Creating a custom credential](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_hashicorp_and_ansible_automation_platform/vault-product#vault-creating-custom-credential)


**Additional resources**

-  [Vault API documentation](https://developer.hashicorp.com/vault/api-docs)


### 2.2.3. Creating a custom credential




Vault users must create a custom credential to use with job templates in Ansible Automation Platform.

**Prerequisite**

- Your administrator has created a Vault credential type.


**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Execution→Infrastructure→Credentials, and then selectCreate credential.
1. Enter a name and a description in the corresponding fields.
1. (Optional) From the **Organization** list, select an organization.
1. From the **Credential type** list, select a Vault credential type. The fields that display depend on the credential type.
1. Do _one_ of the following:


1. For the token authentication, add your Vault token and edit any fields as needed.
1. For the appRole authentication method, enter the IDs in the **appRole Role ID** and **appRole Secret ID** fields. Edit any other fields as needed.

1. ClickSave credential. You are ready to use the credential in a job template.


## 2.3. Migrating from `community.hashi_vault`




If you are using the `community.hashi_vault` collection, you can migrate your existing playbooks to the `hashicorp.vault` collection.

There are two modules for `hashicorp.vault` that you must configure:

-  ** `    hashicorp.vault.kv2_secret` ** - A unified module for CRUD operations on KV2 secrets.
-  ** `    hashicorp.vault.kv2_secret_get lookup` ** - A lookup plugin for reading KV2 secrets.


In the following procedures, you will replicate the parameters from the `community.hashi_vault` modules to these required `hashicorp.vault` modules.

### 2.3.1. Configuring the `hashicorp.vault.kv2_secret` module




The `hashicorp.vault.kv2_secret` module performs Create, Update, and Delete (CRUD) operations on KV2 secrets through a unified interface.

The corresponding `community.hashi_vault` modules are:

-  ** `    community.hashi_vault.vault_kv2_write` ** - Write KV2 secrets.
-  ** `    community.hashi_vault.vault_kv2_delete` ** - Delete KV2 secrets.


**Prerequisites**

- Install the Ansible Automation Platform certified `    hashicorp.vault` collection.


**Procedure**

1. Replicate your automation tasks from both of the `    community.hashi_vault` modules to the following `    hashicorp.vault.kv2_secret` parameters. The `    hashicorp.vault.kv2_secret` parameters are similar to `    community.hashi_vault` . For examples, see [Migration examples for the hashicorp.vault.kv2_secret module](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_hashicorp_and_ansible_automation_platform/vault-product#vault-migration-examples-secret-module) .


```
auth_method:     description: Authentication method to use     type: str     choices: [token, approle]     default: token     required: false        cas:     description: Perform a check-and-set operation.     type: int     required: false        data:     description: KV2 secret data to write.     type: dict     required: true        engine_mount_point:     description: The path where the secret backend is mounted.     type: str     default: secret     required: false     aliases: [secret_mount_path]        namespace:     description: Vault namespace where secrets reside.     type: str     default: admin     aliases: [vault_namespace]        path:     description: Vault KVv2 path to be written to.     type: str     required: true     aliases: [secret_path]        url:     description: URL of the Vault service     type: str     aliases: [vault_address]     required: true        versions:     description: One or more versions of the secret to delete.     type: list of int     required: false        state:     description: Desired state of the secret     type: str     choices: [present, absent]     default: present
```


1. You must add the `    state` parameter to the `    hashicorp.vault.kv2_secret` module, as shown above. Valid options are:


-  ** `        present` :** This is the equivalent of `        create` or `        update` in the `        community.hashi_vault.vault_kv2` modules.
-  ** `        absent` :** This is the equivalent of `        delete secret` in the `        community.hashi_vault.vault_kv2` modules.



**Next step**

-  [Configuring the hashicorp.vault.kv2_secret_get lookup plugin](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_hashicorp_and_ansible_automation_platform/vault-product#vault-configuring-kv2-secret-get-lookup) .


### 2.3.2. Configuring the `hashicorp.vault.kv2_secret_get` lookup plugin




The `hashicorp.vault.kv2_secret_get` lookup plugin module reads KV2 secrets.

The corresponding `community.hashi_vault` modules are:

-  ** `    community.hashi_vault.hashi_vault` :** Retrieves secrets from HashiCorp Vault.
-  ** `    community.hashi_vault.vault_kv2_get` lookup:** Gets secrets from the HashiCorp Vault KV version 2 secret store.


**Procedure**

1. Replicate the `    community.hashi_vault` modules to the following `    hashicorp.vault.kv2_secret_get` parameters. For examples, see [Migration examples for the hashicorp.vault.kv2_secret_get lookup plugin](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_hashicorp_and_ansible_automation_platform/vault-product#vault-migration-examples-secret-get-lookup) .


```
auth_method:     description: Authentication method to use     type: str     choices: [token, approle]     default: token     required: false        mount_point:     description: Vault mount point     type: str     required: false     aliases: [secret_mount_path]        namespace:     description: Vault namespace where secrets reside.     type: str     default: admin     aliases: [vault_namespace]    secret:     description: Vault path to the secret being requested in the format path[:field]     type: str     required: true     aliases: [secret_path]        url:     description: URL of the Vault service     type: str     aliases: [vault_address]     required: true        version:     description: Specifies the version to return. If not set the latest is returned.     type: int     required: false
```


1. Use the following guidance to configure the `    hashicorp.vault.kv2_secret_get` parameters:


-  ** `        auth_method` :** Maps identically to `        auth_method` in the `        community.hashi_vault.hashi_vault` modules.
-  ** `        mount_point` :** Maps to `        mount_point` in the `        community.hashi_vault.hashi_vault` modules. **Alias:**  `        secret_mount_path` .
-  ** `        namespace` :** Maps to `        namespace` in the `        community.hashi_vault.hashi_vault` modules. **Alias:**  `        vault_namespace` .
-  ** `        secret` :** Maps to `        secret` in the `        community.hashi_vault.hashi_vault` modules.
-  ** `        url` :** Maps to `        url` in the `        community.hashi_vault.hashi_vault` modules. Uses the same aliases as `        vault_address` .
-  ** `        version` :** Maps identically to `        version` in the `        community.hashi_vault.hashi_vault` modules.



**Next step**

-  [Creating a credential type](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_hashicorp_and_ansible_automation_platform/vault-product#vault-creating-a-credential-type)


### 2.3.3. Migration examples for the `hashicorp.vault.kv2_secret` module




The following examples show basic before and after configurations for the `hashicorp.vault.kv2_secret` module.

**Example: Basic Secret Write/Create**

Before ( `community.hashi_vault` ):


```
- name: Write/create a secret
community.hashi_vault.vault_kv2_write:
url: https://vault:8200
path: hello
data:
foo: bar
```

After ( `hashicorp.vault` ):

```
- name: Write/create a secret
hashicorp.vault.kv2_secret:
url: https://vault:8200
path: hello
data:
foo: bar
```

**Example 2: Basic Secret Delete**

Before ( `community.hashi_vault` ):


```
- name: Delete the latest version of the secret/mysecret secret.
community.hashi_vault.vault_kv2_delete:
url: https://vault:8201
path: secret/mysecret
```

After ( `hashicorp.vault` ):

```
- name: Delete the latest version of the secret/mysecret secret.
hashicorp.vault.kv2_secret:
url: https://vault:8201
path: secret/mysecret
state: absent
```

**Example 3: Secret Delete - specific version**

Before ( `community.hashi_vault` ):


```
- name: Delete versions 1 and 3 of the secret/mysecret secret.
community.hashi_vault.vault_kv2_delete:
url: https://vault:8201
path: secret/mysecret
versions: [1, 3]
```

After ( `hashicorp.vault` ):

```
- name: Delete versions 1 and 3 of the secret/mysecret secret.
hashicorp.vault.kv2_secret:
url: https://vault:8201
path: secret/mysecret
versions: [1, 3]
state: absent
```

### 2.3.4. Migration examples for the `hashicorp.vault.kv2_secret_get` lookup




**Example: KV2 secret lookup - latest version**

Before ( `community.hashi_vault` )


```
- name: Return latest KV v2 secret from path
ansible.builtin.debug:
msg: "{{ lookup('community.hashi_vault.hashi_vault', 'secret=secret/data/hello
token=my_vault_token
url=http://myvault_url:8200') }}"
```

After ( `hashicorp.vault` )

```
name: Return latest KV v2 secret from path
ansible.builtin.debug:
msg: "{{ lookup('hashicorp.vault.kv2_secret_get', 'secret=secret/data/hello
url=http://myvault_url:8200') }}"
```


<span id="idm140072282123696"></span>
# Legal Notice

Copyright© 2025 Red Hat, Inc.
The text of and illustrations in this document are licensed by Red Hat under a Creative Commons Attribution–Share Alike 3.0 Unported license ("CC-BY-SA"). An explanation of CC-BY-SA is available at [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/) . In accordance with CC-BY-SA, if you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, Red Hat Enterprise Linux, the Shadowman logo, the Red Hat logo, JBoss, OpenShift, Fedora, the Infinity logo, and RHCE are trademarks of Red Hat, Inc., registered in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
Java® is a registered trademark of Oracle and/or its affiliates.
XFS® is a trademark of Silicon Graphics International Corp. or its subsidiaries in the United States and/or other countries.
MySQL® is a registered trademark of MySQL AB in the United States, the European Union and other countries.
Node.js® is an official trademark of Joyent. Red Hat is not formally related to or endorsed by the official Joyent Node.js open source or commercial project.
TheOpenStack® Word Mark and OpenStack logo are either registered trademarks/service marks or trademarks/service marks of the OpenStack Foundation, in the United States and other countries and are used with the OpenStack Foundation's permission. We are not affiliated with, endorsed or sponsored by the OpenStack Foundation, or the OpenStack community.
All other trademarks are the property of their respective owners.





