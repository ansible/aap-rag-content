# 3. Configuring authentication in the Ansible Automation Platform
## 3.3. Creating an authentication method
### 3.3.3. Adjusting the Mapping order




If you have one or more authenticator maps defined, you can manage the order of the maps. Authenticator maps are run in order when logging in lowest order to highest. If one authenticator map determines a user should be a member of a team but a subsequent map determines the user should not be a member of the same team the ruling form the second map will take precedence over the result of the first map. Authenticator maps with the same order are executed in an undefined order.

For example, if the first authenticator map is of type `is_superuser` and the trigger is set to **never** , any user logging into the system would never be granted the `is_superuser` flag.

And, if the second map is of type `is_superuser` and the trigger is based on the user having a specific group, any user logging in would initially be denied the `is_superuser` permission. However, any user with the specified group would subsequently be granted the `is_superuser` permission by the second rule.

The order of rules is important beyond whether you want to process organizations, teams or roles first. They can also be used to refine access and careful consideration is needed to avoid login issues.

For example:

- Authenticator map A denies all users access to the system
- Authenticator map B allows the user `    john` access to the system


When the mapping order is set to A, B; the first map denies access for all users, including `john` . The second map subsequently allows `john` access to the system and the result is that `john` is granted access and is able to log in to the platform.

However, when the mapping order is changed to B, A; the first map allows `john` access to the system. The second map subsequently denies all users access to the system (including `john` ) and the result is that `john` is denied access and is unable to log in to the platform.

**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. In the list view, select the authenticator name displayed in the **Name** column.
1. Select the **Mapping** tab from the **Details** page of your authenticator.
1. ClickManage mappings.
1. Adjust the mapping order by dragging and dropping the mappings up or down in the list using the draggable icon.

Note
The mapping precedence is determined by the order in which the mappings are listed.




1. After your authenticator maps are in the correct order, clickApply.


