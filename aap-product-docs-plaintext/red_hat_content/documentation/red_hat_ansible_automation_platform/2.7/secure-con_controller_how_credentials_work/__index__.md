# How credentials work

Credentials in automation controller store the information required to authenticate to remote systems and services. Credentials include usernames and passwords, SSH keys, tokens, and other sensitive data. Automation controller encrypts sensitive credential data in the database to enhance security.

Automation controller uses SSH to connect to remote hosts. To pass the key from automation controller to SSH, the key must be decrypted before it can be written to a named pipe. Automation controller uses that pipe to send the key to SSH, so that the key is never written to disk. If passwords are used, automation controller handles them by responding directly to the password prompt and decrypting the password before writing it to the prompt.

The **Credentials** page shows credentials that are currently available. The default view is collapsed (Compact), showing the credential name, and credential type.

From this screen you can edit ![Edit](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftpencil.png), duplicate ![Copy](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/copy.png) or delete ⋮ a credential.

Note:

It is possible to create duplicate credentials with the same name and without an organization. However, it is not possible to create two duplicate credentials in the same organization.

**Example**

1. Create two machine credentials with the same name but without an organization.

2. Use the module `ansible.controller.export` to export the credentials.

3. Use the module `ansible.controller.import` in a different automation execution node.

4. Check the imported credentials. When you export two duplicate credentials and then import them in a different node, only one credential is imported.
