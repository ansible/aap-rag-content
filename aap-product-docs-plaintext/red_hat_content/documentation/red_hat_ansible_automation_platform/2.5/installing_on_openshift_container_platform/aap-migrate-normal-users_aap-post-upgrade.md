# 6. Upgrading Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 6.7. Ansible Automation Platform post-upgrade steps
### 6.7.4. Migrating normal users




When you upgrade from Ansible Automation Platform 2.4 to 2.5, your existing user account is automatically migrated to a single platform account. However, if you have multiple component accounts (such as, automation controller, private automation hub and Event-Driven Ansible), your accounts must be linked to use the centralized features of the platform.

#### 6.7.4.1. Additional resources




- See [Creating a user](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-managing-access#proc-controller-creating-a-user) for more information on user types.


#### 6.7.4.2. Linking your account




Ansible Automation Platform 2.5 provides a centralized location for users, teams and organizations to access the platform’s services and features.

The first time you log in to Ansible Automation Platform 2.5, the platform searches through the existing services to locate a user account with the credentials you entered. When there is a match to an existing account, that account is registered and becomes centrally managed by the platform. Any subsequent component accounts in the system are orphaned and cannot be used to log into the platform.

To address this problem, use the account linking procedure to authenticate from any of your existing component accounts and still be recognized by the platform. Linking accounts associates existing component accounts with the same user profile.

**Prerequisites**

- You have completed the upgrade process and have a legacy Ansible Automation Platform account and credentials.


**Procedure**

If you have completed the upgrade process and have a legacy Ansible Automation Platform subscription, follow the account linking procedure below to migrate your account to Ansible Automation Platform 2.5.


1. Navigate to the login page for Ansible Automation Platform.
1. In the login modal, select either **I have an automation controller account** or **I have an automation hub account** based on the credentials you have.
1. On the next screen, enter the legacy credentials for the component account you selected and clickLog in.

Note
If you are logging in using OIDC credentials, see [How to fix broken OIDC redirect after upgrading to AAP 2.5](https://access.redhat.com/solutions/7092980) .




1. If you have successfully linked your account, the next screen shows your username with a green checkmark beside it. If you have other legacy accounts that you want to link, enter those account credentials and clickLinkto link them to your centralized platform gateway account.
1. ClickSubmitto complete linking your legacy accounts.
1. After your accounts are linked, depending on your authentication method, you might be prompted to create a new username and password. These credentials will replace your legacy credentials for each component account.


You can also link your legacy account manually by taking the following steps:

1. Select your user icon at the top right of your screen, and select **User details** .
1. Select theMore Actionsicon **⋮** > **Link user accounts** .
1. Enter the credentials for the account that you want to link.


If you encounter an error message telling you that your account could not be authenticated, contact your platform administrator.

Note
If you log into Ansible Automation Platform for the first time and are prompted to change your username, this is an indication that another user has already logged into Ansible Automation Platform with the same username. To proceed with account migration, follow the prompts to change your username. Ansible Automation Platform uses your password to authenticate which account or accounts belong to you.



**A diagram of the account linking flow**

![Account linking flow](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_on_OpenShift_Container_Platform-en-US/images/c69b6b34512d5fffe2613243f71fbbae/account-linking-flow.png)



After you have migrated your user account, you can manage your account from the **Access Management** menu. See [Managing access with role based access control](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/gw-managing-access) .

