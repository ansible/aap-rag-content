# 6. Red Hat Ansible Automation Platform credential
## 6.2. Setting up a Red Hat Ansible Automation Platform credential




You can create a Red Hat Ansible Automation Platform credential type to run your rulebook activations.

**Prerequisites**

- You have created a user.
- You have obtained the URL and the credentials to access automation controller.


**Procedure**

1. Log in to the Ansible Automation Platform Dashboard.
1. From the navigation panel, selectAutomation Decisions→Infrastructure→Credentials.
1. ClickCreate credential.
1. Insert the following:


1. In the required Red Hat Ansible Automation Platform field, enter your automation controller URL.

Note
For Event-Driven Ansible controller 2.5 with automation controller 2.4, use the following example: https://<your_controller_host>

For Ansible Automation Platform 2.5, use the following example: https://<your_gateway_host>/api/controller/




1. Enter a valid **Username** and **Password** , or **Oauth Token** .
1. ClickCreate credential.


After you create this credential, you can use it for configuring your rulebook activations.

