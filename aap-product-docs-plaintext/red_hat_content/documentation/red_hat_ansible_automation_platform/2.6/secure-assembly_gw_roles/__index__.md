# View, create, and assign roles to grant user access to resources

Assign roles to teams or users to grant them targeted access to Red Hat Ansible Automation Platform resources. Defining these permissions allows you to safely govern who can view, modify, or execute tasks on resources like projects and inventories.

Roles define permissions for a specific resource, centralizing all access to that resource through the role itself. This design makes roles reusable units that enable administrators to share defined behaviors among many resources or with different users.

As an administrator, you have the option of using default predefined roles, or you can create roles based on your organization’s needs.

## Display roles

You can display the roles assigned to each component resource from the Access Management menu.

### About this task

Roles are labeled with their associated Ansible Automation Platform component and function. These components align with Ansible Automation Platform services and the side navigation structure in the user interface. Component labels can be understood as follows:

- **Automation Execution** refers to automation controller
- **Automation Decisions** refers to Event-Driven Ansible
- **Automation Content** refers to automation hub


Roles created at the level of the organization can be associated with multiple components because they group together permissions from automation controller (Automation Execution) and Event-Driven Ansible (Automation Decisions). Only organization roles can span multiple components.

A similar role entity for Automation Content is a "system" role, which gives access to all of the specified resource types in Automation Content.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Roles.
2.  From the table header, you can sort the list of roles by using the arrows for **Name**, **Description**, **Component**, **Resource Type**, and **Role Creation**, or by making sort selections in the **Sort** list.
3.  You can filter the list of roles by selecting **Name**, **Editable**, or **Component** from the filter list and clicking the arrow.

## Create a role

Ansible Automation Platform services provide a set of predefined roles with permissions enough for standard automation tasks. It is also possible to configure custom roles that define access permissions to a resource.

### About this task

If the default predefined roles for a resource type do not give the necessary permissions, you can create custom roles for an organization. Creating a custom role reduces complexity by consolidating all required permissions into a single assignment per resource or resource type, eliminating the need to assign multiple roles to a user or team.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Roles.
2.  Click Create role.
3.  Provide a **Name** and a short **Description** for the role. The name and description should be unique and specific to the role’s intended use and permissions to give context when assigning the role.
4.  Select a **Resource Type**. Ensure that you are selecting the required resource in the correct component context, because resources such as projects and credentials can be associated with both Automation Execution and Automation Decisions.
5.  Select the **Permissions** you want assigned to this role from the drop-down menu.
6.  Click Create role to create your new role.

## Edit a role

Default roles are predefined in the platform and cannot be changed; however, you can modify custom roles from the **Roles** list view. The **Role Creation** column in the **Roles** list view indicates whether a role is a default role that cannot be changed, or a custom role that can be modified.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Roles.
2.  Click the **Edit role** icon ![Edit](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/leftpencil.png) next to the role you want and modify the role settings as needed.
3.  Click Save role to save your changes.

## Delete a role

You cannot delete default roles; however, you can delete custom roles from the **Roles** list view.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Roles.
2.  Click the More Actions icon **⋮** next to the role you want and select **Delete role**.
3.  To delete roles in bulk, select the roles you want to delete from the **Roles** list view, click the More Actions icon **⋮**, and select **Delete roles**.
