# Bulk-assign roles to users with teams
## Remove roles from a team

Remove roles from a team to revoke access to specific Ansible Automation Platform resources. Updating these permissions helps ensure that team members only keep the necessary access for their tasks within the correct component context.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Teams.
2.  Select the team **Name** from which you want to remove roles.
3.  Select the **Roles** tab.
4.  To remove a single role, click the minus icon next to the resource and confirm removal on the dialog that is displayed. Note:
Ensure that you are selecting the desired role within the correct component context, because resources like projects and credentials can be associated with both Automation Execution (automation controller) and Automation Decisions (Event-Driven Ansible).

5.  To remove roles in bulk, select the checkbox next to each resource you want to remove and click **Delete selected roles** from the More Actions**⋮** list on the menu bar, then confirm removal and click **Delete role**.

