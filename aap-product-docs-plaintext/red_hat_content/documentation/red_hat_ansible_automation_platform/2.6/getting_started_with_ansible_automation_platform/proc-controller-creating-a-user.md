# 2. Getting started as a platform administrator
## 2.7. Creating a user

You can create three types of users in Ansible Automation Platform:

Normal user
Normal users have read and write access limited to the resources (such as inventory, projects, and job templates) for which that user has been granted the appropriate roles and privileges. Normal users are the default type of user when no other **User type** is specified.

Ansible Automation Platform Administrator
An administrator (also known as a Superuser) has full system administration privileges, with full read and write privileges over the entire installation. An administrator is typically responsible for managing all aspects of and delegating responsibilities for day-to-day work to various users.

Ansible Automation Platform Auditor
Auditors have read-only capability for all objects within the environment.

**Procedure**

1. From the navigation panel, select Access Management → Users.

2. Click Create user.

3. Enter the details about your new user in the fields on the **Create user** page. Fields marked with an asterisk (*) are required.

4. Normal users are the default when no **User type** is specified. To define a user as an administrator or auditor, select a **User type** from the drop-down menu.


Note
If you are modifying your own password, log out and log back in for the change to take effect.

5. Select the **Organization** to be assigned for this user. For information about creating a new organization, see [Creating an organization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access#proc-controller-create-organization).

6. Click Create user.

When the user is successfully created, the **User** details screen opens. From here, you can review and change the user’s teams, roles, tokens and other membership details.


Note
If the user is not newly-created, the details screen displays the user’s last login activity.

**Next steps**

If you log in as yourself, and view the details of your user profile, you can manage tokens from your user profile by selecting the **Tokens** tab. For more information, see [Adding a token](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-token-based-authentication#proc-controller-apps-create-tokens).

