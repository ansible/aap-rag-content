# 5. Managing access with role based access control
## 5.1. Organizations
### 5.1.3. Access to organizations




You can manage access to an organization by selecting an organization from the **Organizations** list view and selecting the associated tabs for providing access to [Users](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-controller-add-organization-user) , [Administrators](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-gw-add-admin-organization) or [Teams](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-gw-add-team-organization) .

#### 5.1.3.1. Adding a user to an organization




You can provide a user with access to an organization by adding them to the organization and managing the roles associated with the user. To add a user to an organization, the user must already exist. For more information, see [Creating a user](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-controller-creating-a-user) . To add roles for a user, the role must already exist. See [Creating a role](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-gw-create-roles) for more information.

The following tab selections are available when adding users to an organization. When user accounts from the automation controller organization have been migrated to Ansible Automation Platform 2.5 during the upgrade process, the **Automation Execution** tab shows content based on whether the users were added to the organization prior to migration.

New user memberships to an organization must be added at the platform level.

**Procedure**

1. From the navigation panel, selectAccess Management→Organizations.
1. From the **Organizations** list view, select the organization to which you want to add a user.
1. Click the **Users** tab to add users.
1. Select the **Ansible Automation Platform** tab and clickAdd usersto add user access to the team, or select the **Automation Execution** tab to view or remove user access from the team.
1. Select one or more users from the list by clicking the checkbox next to the name to add them as members.
1. ClickNext.
1. Select the roles you want the selected user to have. Scroll down for a complete list of roles.

Note
If you have multiple Ansible Automation Platform components installed, you will see selections for the roles associated with each component in the **Roles** menu bar. For example, Automation Execution for automation controller roles, Automation Decisions for Event-Driven Ansible roles.




1. ClickNextto review the roles settings.
1. ClickFinishto apply the roles to the selected users, and to add them as members. The **Add roles** dialog displays the updated roles assigned for each user.

Note
A user with associated roles retains them if they are reassigned to another organization.




1. To remove a particular user from the organization, select **Remove user** from the **More actions ⋮** list next to the user. This launches a confirmation dialog, asking you to confirm the removal.
1. To manage roles for users in an organization, click the **⚙** icon next to the user and select **Manage roles** .


#### 5.1.3.2. Adding an administrator to an organization




You can add administrators to an organization which allows them to manage the membership and settings of the organization. For example, they can create new users and teams within the organization, and grant permission to users within the organization. To add an administrator to an organization, the user must already exist.

**Procedure**

1. From the navigation panel, selectAccess Management→Organizations.
1. From the Organizations list view, select the organization to which you want to add a user, administrator, or team.
1. Click the **Administrators** tab.
1. ClickAdd administrators.
1. Select the users from the list by clicking the checkbox next to the name to assign the administrator role to them for this organization.
1. ClickAdd administrators.
1. To remove a particular administrator from the organization, select **Remove administrator** from the **More actions ⋮** list next to the administrator name. This launches a confirmation dialog, asking you to confirm the removal.

Note
If the user had previously been added as a member to this organization, they will continue to be a member of this organization. However, if they were added to the organization when the administrator assignment was made, they will be removed from the organization.






#### 5.1.3.3. Adding a team to an organization




You can provide team access to an organization by adding roles to the team. To add roles to a team, the team must already exist in the organization. For more information, see [Creating a team](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-controller-creating-a-team) . To add roles for a team, the role must already exist. See [Creating a role](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-gw-create-roles) for more information.

**Procedure**

1. From the navigation panel, selectAccess Management→Organizations.
1. From the Organizations list view, select the organization to which you want to add team access.
1. Click the **Teams** tab. If no teams exist, clickCreate teamto create a team and add it to this organization.
1. ClickAdd roles.
1. Select the roles you want the selected team to have. Scroll down for a complete list of roles.

Note
If you have multiple Ansible Automation Platform components installed, you will see selections for the roles associated with each component in the **Roles** menu bar. For example, Automation Execution for automation controller roles, Automation Decisions for Event-Driven Ansible roles.




1. ClickNextto review the roles settings.
1. ClickFinishto apply the roles to the selected teams. The Add roles dialog displays the updated roles assigned for each team.
1. ClickClose.

Note
A team with associated roles retains them if they are reassigned to another organization.




1. To manage roles for teams in an organization, click the **⚙** icon next to the user and select **Manage roles** .


#### 5.1.3.4. Deleting an organization




Before you can delete an organization, you must be an Organization administrator or System administrator. When you delete an organization, the organization, team, users and resources are permanently removed from Ansible Automation Platform.

Note
When you attempt to delete items that are used by other resources, a message is displayed warning you that the deletion might impact other resources and prompts you to confirm the deletion. Some screens contain items that are invalid or have been deleted previously, and will fail to run.



**Procedure**

1. From the navigation panel, selectAccess Management→Organizations.
1. Click the **⋮** icon next to the organization you want removed and select **Delete organization** .
1. Select the confirmation checkbox and clickDelete organizationsto proceed with the deletion. Otherwise, clickCancel.

Note
You can delete multiple organizations by selecting the checkbox next to each organization you want to remove, and selecting **Delete selected organizations** from the **More actions ⋮** list on the menu bar.






