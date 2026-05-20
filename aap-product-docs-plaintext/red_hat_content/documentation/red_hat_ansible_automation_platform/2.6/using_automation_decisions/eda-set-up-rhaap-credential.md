# 6. Red Hat Ansible Automation Platform credential
## 6.2. Setting up a Red Hat Ansible Automation Platform credential

Set up the Red Hat Ansible Automation Platform credential to enable rulebook activations to securely communicate with and launch jobs on automation controller.

**Prerequisites**

- You have created a user.
- You have obtained the URL and the credentials to access automation controller.

**Procedure**

1. Log in to the Ansible Automation Platform Dashboard.

2. From the navigation panel, select Automation Decisions → Infrastructure → Credentials.

3. Click Create credential.

4. Insert the following:



Name
Insert the name.

Description
This field is optional.

Organization
Click the list to select an organization or select **Default**.

Credential type
Click the list and select **Red Hat Ansible Automation Platform**.


Note
When you select the credential type, the **Type Details** section is displayed with fields that are applicable for the credential type you chose.


Warning
If you plan to use a backup and restore operation to migrate your Ansible Automation Platform instance to a different cluster or new set of hostnames, the Red Hat Ansible Automation Platform credential will break, and your rulebook activation will fail. You must manually edit and update the automation controller URL and associated credentials after the restore operation is complete to restore connectivity.

5. In the required Red Hat Ansible Automation Platform field, enter your automation controller URL.


Note
For Event-Driven Ansible controller 2.6 with automation controller 2.4, use the following example: https://<your_controller_host>

For Ansible Automation Platform 2.6, use the following example: https://<your_gateway_host>/api/controller/

6. Enter a valid **Username** and **Password**, or **Oauth Token**.

7. Click Create credential.

**Next step**

After you create this credential, you can use it for configuring your rulebook activations.

