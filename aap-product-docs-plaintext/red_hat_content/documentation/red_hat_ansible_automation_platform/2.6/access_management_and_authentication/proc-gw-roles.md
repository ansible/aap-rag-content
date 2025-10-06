# 5. Roles
## 5.1. Displaying roles




You can display the roles assigned to each component resource from theAccess Managementmenu.

Roles are labeled with their associated Ansible Automation Platform component and function. These components align with Ansible Automation Platform services and the side navigation structure in the user interface. Component labels can be understood as follows:

-  **Automation Execution** refers to automation controller
-  **Automation Decisions** refers to Event-Driven Ansible
-  **Automation Content** refers to automation hub


Roles created at the level of the organization can be associated with multiple components because they group together permissions from automation controller (Automation Execution) and Event-Driven Ansible (Automation Decisions). Only organization roles can span multiple components.

A similar role entity for Automation Content is a "system" role, which gives access to all of the specified resource types in Automation Content.

**Procedure**

1. From the navigation panel, selectAccess Management→Roles.
1. From the table header, you can sort the list of roles by using the arrows for **Name** , **Description** , **Component** , **Resource Type** , and **Role Creation** , or by making sort selections in the **Sort** list.
1. You can filter the list of roles by selecting **Name** , **Editable** , or **Component** from the filter list and clicking the arrow.


