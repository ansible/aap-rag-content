# Manage access to organizations
## Assign a user to an organization

You can give a user with access to an organization, and therefore the resources within the organization, by assigning them to the organization and managing the organization roles associated with the user.

### About this task

You can view a list of users associated with an organization, along with the roles each user is directly assigned, in the organization’s **Users** tab. When you manage a user’s organization roles in the **Users** tab, you can also see how the user was assigned their roles, whether indirectly, through association with a team, or through direct user assignment by an administrator.

Note:

If a user is assigned a "team member" role, this likely indicates that they have an indirectly-assigned role. To see a user’s indirectly-assigned roles, click the pencil icon ![Edit page](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftpencil.png) to view and manage roles, and then click the link labeled **View indirectly-assigned organization roles** in the page banner.

To assign a user to an organization, the user must already exist. For more information, see [Creating a user](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_users#proc-controller-creating-a-user "You can create three types of users in Ansible Automation Platform:"). To assign roles to a user, the role must already exist. See [Creating a role](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_roles#proc-gw-create-roles "Ansible Automation Platform services provide a set of predefined roles with permissions enough for standard automation tasks. It is also possible to configure custom roles that define access permissions to a resource.") for more information.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Organizations.
2.  From the **Organizations** list view, select the organization to which you want to add a user.
3.  Click the **Users** tab, then click Assign Users to add users.
4.  Select one or more users from the list by clicking the checkbox next to the name to add them as members.
5.  Click Next.
6.  Select the roles you want the selected user to have. Scroll down for a complete list of roles.  Note:
Ensure that you are selecting the desired role within the correct component context, because resources like projects and credentials can be associated with both Automation Execution (automation controller) and Automation Decisions (Event-Driven Ansible).

7.  Click Next to review the roles settings.
8.  Click Finish to apply the roles to the selected users, and to add them as members. The **Add roles** dialog displays the updated roles assigned for each user.  Note:
A user with roles associated with an organization loses those roles if they are removed from the organization.

9.  To remove a particular user from the organization, select **Remove user** from the More Actions**⋮** list next to the user. This launches a confirmation dialog, asking you to confirm the removal. Note that removing a user from an organization will also remove all organization roles that the user is indirectly assigned from that specific organization.
10.  To manage roles for users in an organization, click the **⚙** icon next to the user and select **Manage roles**. You can manage organization roles that are directly assigned to a user by selecting or clearing the checkboxes. Double-check the component column to ensure you are selecting the desired role in the correct component context.  Tip:
From this screen, you can view, but not manage, indirectly-assigned roles that a user has inherited from a team assignment. To view indirectly-assigned roles, along with the team assignment they originated from, click **View indirectly-assigned organization roles** link in the banner beneath the page heading. To manage roles indirectly assigned to a user through a team assignment, [manage that team’s role assignments](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_teams#proc-controller-user-permissions "You can grant a team granular access to specific resources such as inventories, projects, and job templates by assigning the team roles associated with those particular resources. You can also set permissions at the level of the organization from the Organizations view.") or [remove the user from that team](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_teams#proc-gw-team-remove-user "You can remove a user from a team from the Team list view.").

