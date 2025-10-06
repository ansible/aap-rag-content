# 4. Managing access with role-based access control
## 4.1. Organizations
### 4.1.3. Access to organizations




You can manage access to an organization by selecting an organization from the **Organizations** list view and selecting the associated tabs for providing access to [Users](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/access_management_and_authentication/index#proc-controller-add-organization-user) , [Administrators](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/access_management_and_authentication/index#proc-gw-add-admin-organization) or [Teams](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/access_management_and_authentication/index#proc-gw-add-team-organization) .

#### 4.1.3.1. Assigning a user to an organization




You can provide a user with access to an organization, and therefore the resources within the organization, by assigning them to the organization and managing the organization roles associated with the user.

You can view a list of users associated with an organization, along with the roles each user is directly assigned, in the organization’s **Users** tab. When you manage a user’s organization roles in the **Users** tab, you can also see how the user was assigned their roles, whether indirectly, through association with a team, or through direct user assignment by an administrator.

Note
If a user is assigned a "team member" role, this likely indicates that they have an indirectly-assigned role. To see a user’s indirectly-assigned roles, click the pencil icon![Edit page](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Access_management_and_authentication-en-US/images/e5cb7f9b0cfe60ab5ba421bd17ecbb6a/leftpencil.png)
to view and manage roles, and then click the link labeled **View indirectly-assigned organization roles** in the page banner.



To assign a user to an organization, the user must already exist. For more information, see [Creating a user](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access#proc-controller-creating-a-user) . To assign roles to a user, the role must already exist. See [Creating a role](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/assembly-gw-roles#proc-gw-create-roles) for more information.

**Procedure**

1. From the navigation panel, selectAccess Management→Organizations.
1. From the **Organizations** list view, select the organization to which you want to add a user.
1. Click the **Users** tab, then clickAssign Usersto add users.
1. Select one or more users from the list by clicking the checkbox next to the name to add them as members.
1. ClickNext.
1. Select the roles you want the selected user to have. Scroll down for a complete list of roles.

Note
Ensure that you are selecting the desired role within the correct component context, because resources like projects and credentials can be associated with both Automation Execution (automation controller) and Automation Decisions (Event-Driven Ansible).




1. ClickNextto review the roles settings.
1. ClickFinishto apply the roles to the selected users, and to add them as members. The **Add roles** dialog displays the updated roles assigned for each user.

Note
A user with roles associated with an organization loses those roles if they are removed from the organization.




1. To remove a particular user from the organization, select **Remove user** from theMore Actions **⋮** list next to the user. This launches a confirmation dialog, asking you to confirm the removal. Note that removing a user from an organization will also remove all organization roles that the user is indirectly assigned from that specific organization.
1. To manage roles for users in an organization, click the **⚙** icon next to the user and select **Manage roles** . You can manage organization roles that are directly assigned to a user by selecting or clearing the checkboxes. Double-check the component column to ensure you are selecting the desired role in the correct component context.


Tip
From this screen, you can view, but not manage, indirectly-assigned roles that a user has inherited from a team assignment. To view indirectly-assigned roles, along with the team assignment they originated from, click **View indirectly-assigned organization roles** link in the banner beneath the page heading. To manage roles indirectly assigned to a user through a team assignment, [manage that team’s role assignments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access#proc-controller-user-permissions) or [remove the user from that team](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access#proc-gw-team-remove-user) .



#### 4.1.3.2. Assigning an administrator to an organization




You can add administrators to an organization, which allows them to manage the membership and settings of the organization. For example, they can create new users and teams within the organization, and grant permission to users within the organization. To add an administrator to an organization, the user must already exist.

**Procedure**

1. From the navigation panel, selectAccess Management→Organizations.
1. From the Organizations list view, select the organization to which you want to add a user, administrator, or team.
1. Click the **Administrators** tab.
1. ClickAdd administrators.
1. Select the users from the list by clicking the checkbox next to the name to assign the administrator role to them for this organization.
1. ClickAdd administrators.
1. To remove a particular administrator from the organization, select **Remove administrator** from the **More actions ⋮** list next to the administrator name. This launches a confirmation dialog asking you to confirm the removal.

Note
If the user had previously been added as a member to this organization, they will continue to be a member of this organization. However, if they were added to the organization when the administrator assignment was made, they will be removed from the organization.






#### 4.1.3.3. Assigning a team to an organization




You can provide a team access to an organization, and to the resources within that organization, by assigning roles to the team in the organization’s **Teams** tab. All users who are part of a team assigned to the organization will inherit the team’s organization role assignments. To assign roles to a team, the team must already exist in the organization. For more information, see [Creating a team](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-managing-access#proc-controller-creating-a-team) . To assign roles for a team, the role must already exist. See [Creating a role](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/assembly-gw-roles#proc-gw-create-roles) for more information.

**Procedure**

1. From the navigation panel, selectAccess Management→Organizations.
1. From the Organizations list view, select the organization to which you want to assign team access.
1. Click the **Teams** tab. If no teams exist, clickCreate teamto create a team and assign it to this organization.
1. ClickAssign roles.
1. Select the roles you want the selected team to have. Scroll down for a complete list of roles.

Note
Ensure that you are selecting the desired role within the correct component context, because resources like projects and credentials can be associated with both Automation Execution (automation controller) and Automation Decisions (Event-Driven Ansible).




1. ClickNextto review the roles settings.
1. ClickFinishto apply the roles to the selected teams. The Assign roles dialog displays the updated roles assigned for each team.
1. ClickClose.

Note
A team with associated roles retains them if they are reassigned to another organization.




1. To manage roles for teams in an organization, click the **⚙** icon next to the user and select **Manage roles** .


#### 4.1.3.4. Deleting an organization




Before you can delete an organization, you must be an Organization administrator or System administrator. When you delete an organization, the organization, team, users and resources are permanently removed from Ansible Automation Platform.

Note
When you attempt to delete items that are used by other resources, a message is displayed warning you that the deletion might impact other resources and prompts you to confirm the deletion. Some screens contain items that are invalid or have been deleted previously, and will fail to run.



**Procedure**

1. From the navigation panel, selectAccess Management→Organizations.
1. Click the **⋮** icon next to the organization you want removed and select **Delete organization** .
1. Select the confirmation checkbox and clickDelete organizationsto proceed with the deletion. Otherwise, clickCancel.

Note
You can delete multiple organizations by selecting the checkbox next to each organization you want to remove, and selecting **Delete selected organizations** from the **More actions ⋮** list on the menu bar.






