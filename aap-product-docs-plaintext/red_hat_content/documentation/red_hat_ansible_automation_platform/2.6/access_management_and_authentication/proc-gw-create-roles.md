# 5. Roles
## 5.2. Creating a role




Ansible Automation Platform services provide a set of predefined roles with permissions enough for standard automation tasks. It is also possible to configure custom roles that define access permissions to a resource.

If the default predefined roles for a resource type do not give the necessary permissions, you can create custom roles for an organization. Creating a custom role reduces complexity by consolidating all required permissions into a single assignment per resource or resource type, eliminating the need to assign multiple roles to a user or team.

**Procedure**

1. From the navigation panel, selectAccess Management→Roles.
1. ClickCreate role.
1. Provide a **Name** and a short **Description** for the role. The name and description should be unique and specific to the role’s intended use and permissions to give context when assigning the role.
1. Select a **Resource Type** . Ensure that you are selecting the required resource in the correct component context, because resources such as projects and credentials can be associated with both Automation Execution and Automation Decisions.
1. Select the **Permissions** you want assigned to this role from the drop-down menu.
1. ClickCreate roleto create your new role.


