# Authenticate to hashicorp.vault
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
