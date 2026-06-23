# Integrate with HashiCorp to secure sensitive data
## Configure Ansible Automation Platform to communicate with HashiCorp vault

In enterprise environments, managing secrets externally is vital. A recommended HashiCorp Vault method uses AppRoles. To use these secrets, configure a new Ansible Automation Platform credential using the [HashiCorp Vault Secret Lookup](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-integrate_third_party_secret_management_systems#ref-hashicorp-vault-lookup "The HashiCorp Vault secret lookup credential type allows you to retrieve secrets from a HashiCorp Vault server during playbook execution. This integration supports various authentication methods, including Token, AppRole, LDAP, Userpass, Kubernetes, and TLS Certificates.") type.

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

