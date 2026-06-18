# Integrate with HashiCorp to secure sensitive data

You can integrate HashiCorp Vault with Ansible Automation Platform to manage and retrieve sensitive data.

## Configure Ansible Automation Platform to communicate with HashiCorp vault

In enterprise environments, managing secrets externally is vital. A recommended HashiCorp Vault method uses AppRoles. To use these secrets, configure a new Ansible Automation Platform credential using the [HashiCorp Vault Secret Lookup](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-integrate_third_party_secret_management_systems#ref-hashicorp-vault-lookup "The HashiCorp Vault secret lookup credential type allows you to retrieve secrets from a HashiCorp Vault server during playbook execution. This integration supports various authentication methods, including Token, AppRole, LDAP, Userpass, Kubernetes, and TLS Certificates.") type.

### About this task

Enter relevant information such as an identifiable credential name, organization, and the URL of the vault server, for example, <https://vault.domain.com:8200>.

Populate the necessary fields with your information such as Token, AppRole role_id, and AppRole secret_id, then select v2 for the API version.

To test the credential to test for functionally and operation, use the following procedure:

### Procedure

1.  Before clicking on **Create Credential**, click Test.
2.  In the pop-up box, enter the **Path to Secret** and the **Key Name**.  Note:
The **Path to Secret** will be prefixed by `kv` if storing a key-value pair, for example, `kv/key_name`.

3.  Click Run.
4.  When the test is successful, click Create Credential.
5.  When complete, Ansible Automation Platform is properly configured to use HashiCorp Vault as an external secret source.

## Use HashiCorp Vault credentials within Ansible Automation Platform

To use HashiCorp vault credentials within Ansible Automation Platform, create a new credential with the type **Machine Credential**. Enter relevant information such as an identifiable credential name and an organization.

### About this task

To configure the use of HashiCorp Vault credentials, use the following procedure:

### Procedure

1.  To configure the **Username**, click the ![Key](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/leftkey.png) icon.
2.  Select the HashiCorp Vault credentials that were created in step 1.
3.  Populate **Path to Secret** and the **Key Name**.
4.  Optionally, click Test. Otherwise, click Finish.

## Configure the machine credential’s SSH private key

Link your machine credential's SSH private key to HashiCorp Vault. Retrieving this key from an external secret management system helps ensure that sensitive authentication details are securely injected into your automation workflows.

### Procedure

1.  To configure the **Username**, click the ![Key](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/leftkey.png) icon.
2.  Select the HashiCorp Vault credentials that you created.
3.  Populate the **Path to Secret** and the **Key Name**.
4.  Select the name of the private key as the **Key Name**.
5.  Optionally, click Test. Otherwise, click Finish.
