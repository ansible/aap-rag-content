# View, create, or assign roles to users

A user is an individual or entity that can log in to the platform and perform tasks. Users are fundamental units to which roles can be assigned, either directly by an administrator or indirectly through a team.

Warning:

Ansible Automation Platform automatically creates a default system administrator user so they can log in and set up Ansible Automation Platformfor their organization. Do not delete this user.

The containerized installer uses this account to register services with platform gateway. Deleting the default system administrator user causes installation and upgrade operations to fail.

If you have already deleted the default system administrator user, you must set the `gateway_admin_user` variable in your installer inventory file to specify an alternative system administrator account before running the installation program.

You can sort or search the User list by **Username**, **First name**, **Last name**, or **Email**. Click the arrows in the header to toggle your sorting preference. You can view **User type** and **Email** beside the user name on the Users page.

## View the Users list

The **Users** page displays the existing users for your installation. From here, you can search for a specific user, filter the list of users, or change the sort order for the list.

### About this task

When user accounts have been migrated to Ansible Automation Platform 2.6 during the upgrade process, these accounts are also displayed in the **Users** list view. You can see whether these users have administrator privileges by editing the account. See [Editing a user](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_controller_users#gw-editing-a-user "You can change user account properties after creation, including password, user type, and organizational assignment. Only platform administrators and organization administrators can change a user's email address.") for instructions.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Users.
2.  In the **Search** bar, enter an appropriate keyword for the user you want to search for and click the arrow icon.
3.  From the menu bar, you can sort the list of users by using the arrows for **Username**, **Email**, **First name**, **Last name** or **Last login** to toggle your sorting preference.
4.  You can view user details by selecting a **Username** from the **Users** list view.

## Create a user

You can create three types of users in Ansible Automation Platform:

### About this task

Normal user
Normal users have read and write access limited to the resources (such as inventory, projects, and job templates) for which that user has been granted the appropriate roles and privileges. Normal users are the default type of user when no other **User type** is specified.

Ansible Automation Platform Administrator
An administrator (also known as a Superuser) has full system administration privileges, with full read and write privileges over the entire installation. An administrator is typically responsible for managing all aspects of and delegating responsibilities for day-to-day work to various users.

Ansible Automation Platform Auditor
Auditors have read-only capability for all objects within the environment.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Users.
2.  Click Create user.
3.  Enter the details about your new user in the fields on the **Create user** page. Fields marked with an asterisk (*) are required.
4.  Normal users are the default when no **User type** is specified. To define a user as an administrator or auditor, select a **User type** from the drop-down menu.  Note:
If you are modifying your own password, log out and log back in for the change to take effect.

5.  Select the **Organization** to be assigned for this user. For information about creating a new organization, see [Creating an organization](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_controller_create_organization#proc-controller-create-organization "Ansible Automation Platform automatically creates a default organization. If you have a self-support level license, you have only the default organization available and cannot delete it.").
6.  Click Create user. When the user is successfully created, the **User** details screen opens. From here, you can review and change the user’s teams, roles, tokens and other membership details.

Note:
If the user is not newly-created, the details screen displays the user’s last login activity.

### What to do next

If you log in as yourself, and view the details of your user profile, you can manage tokens from your user profile by selecting the **Tokens** tab. For more information, see [Adding a token](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-proc_controller_create_application#proc-controller-apps-create-tokens "You can view a list of users that have tokens to access an application by selecting the Tokens tab in the OAuth Applications details page.").

## Edit a user

You can change user account properties after creation, including password, user type, and organizational assignment. Only platform administrators and organization administrators can change a user's email address.

### About this task

To see whether a user had service level auditor privileges, you must refer to the API.

Note:

After upgrading to 2.6, users previously designated as automation controller administrators are labeled as platform administrators in the **User type** column in the [Users list view](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_controller_users#proc-gw-users-list-view "The Users page displays the existing users for your installation. From here, you can search for a specific user, filter the list of users, or change the sort order for the list."). Automation hub administrators are labeled as **Normal** in the **User Type** column.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Users.
2.  Click the **Pencil**![Edit page](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/leftpencil.png) icon next to the user you want to edit and select **Edit user**.
3.  The **Edit** user page is displayed where you can change user details such as **Password**, **Email**, **User type**, and **Organization**.
4.  After your changes are complete, click **Save user**.

## Delete a user

Before you can delete a user, you must have normal user or system administrator permissions. When you delete a user account, the name and email of the user are permanently removed from Ansible Automation Platform.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Users.
2.  To delete a single user, select the More Actions**⋮** icon next to the user you want to remove and select **Delete user**.
3.  To bulk delete users, select the checkbox next to each user you want to remove, and then from the More Actions**⋮** list, click **Delete users**.

## Assign roles to a user

You can grant users granular access to specific resources such as inventories, projects, or job templates by assigning users roles.

### About this task

You can view and manage roles that were assigned directly to a user by an administrator in the user’s **Roles** tab.

You can view roles that a user inherited from a team assignment in the **View indirectly assigned roles** link in the page banner. You cannot directly manage an indirectly-assigned role. You can only manage indirectly-assigned roles by [editing the team’s role assignments](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_controller_teams#proc-controller-user-permissions "You can grant a team granular access to specific resources such as inventories, projects, and job templates by assigning the team roles associated with those particular resources. You can also set permissions at the level of the organization from the Organizations view."), or by [removing the user from the team](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_controller_teams#proc-gw-team-remove-user "You can remove a user from a team from the Team list view.").

Note:

Users cannot be assigned to an organization through role assignment, nor can you assign users organization roles from this screen. Refer to the steps provided in [Adding a user to an organization](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_controller_access_organizations#proc-controller-add-organization-user "You can give a user with access to an organization, and therefore the resources within the organization, by assigning them to the organization and managing the organization roles associated with the user.") for detailed instructions on assigning a user to an organization.

Roles are labeled with their associated Ansible Automation Platform component and function. These components align with Ansible Automation Platform services and the side navigation structure in the user interface. Component labels can be understood as follows:

- **Automation Execution** refers to automation controller
- **Automation Decisions** refers to Event-Driven Ansible
- **Automation Content** refers to automation hub


When assigning roles, ensure that you are selecting the required resource in the correct component context, because resources such as projects and credentials can be associated with both Automation Execution and Automation Decisions.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Users.
2.  From the **Users** list view, click the user to which you want to add roles.
3.  Select the **Roles** tab to display the set of roles assigned to this user. These provide the ability to read, change, and administer resources.
4.  To add new roles, click Add roles.  Note:
Ensure that you are selecting the desired role within the correct component context, because resources like projects and credentials can be associated with both Automation Execution (automation controller) and Automation Decisions (Event-Driven Ansible).

5.  Select a Resource type and click Next.
6.  Select the resources that you want to give role-based access to and click Next.
7.  Select the roles that will be applied to the resources and click Next.  Tip:
If you are selecting more than one role, consider [creating a custom role](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_roles#proc-gw-create-roles "Ansible Automation Platform services provide a set of predefined roles with permissions enough for standard automation tasks. It is also possible to configure custom roles that define access permissions to a resource.") that includes all the permissions for this resource type so you can give your users the appropriate level of access.

8.  Review the settings and click Finish. The **Add roles** dialog displays indicating whether the role assignments were successfully applied. Click Close to close the dialog.

## Remove roles from a user

You can remove a user’s roles by editing the user information in the **Roles** tab.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Users.
2.  Select the user name whose role access you want to remove.
3.  Select the **Roles** tab.  Note:
Ensure that you are selecting the desired role within the correct component context, because resources like projects and credentials can be associated with both Automation Execution (automation controller) and Automation Decisions (Event-Driven Ansible).

4.  To remove a single role, click the **-** icon next to the role and confirm removal on the dialog that is displayed.
5.  To remove multiple roles, select the checkbox next to each role you want to remove and click **Remove selected roles** from the **More actions ⋮** list on the menu bar. On the dialog that is displayed, confirm removal of the selected roles and click Remove role.
