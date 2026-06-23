# Pluggable authentication
## Adjust the mapping order

Adjust the execution order of your authenticator maps to control authorization rule precedence. As later maps override earlier ones, setting the correct sequence helps ensure users receive the intended permissions and team memberships.

### About this task

For example, if the first authenticator map is of type `is_superuser` and the trigger is set to **never**, any user logging into the system would never be granted the `is_superuser` flag.

And, if the second map is of type `is_superuser` and the trigger is based on the user having a specific group, any user logging in would initially be denied the `is_superuser` permission. However, any user with the specified group would subsequently be granted the `is_superuser` permission by the second rule.

The order of rules is important beyond whether you want to process organizations, teams or roles first. They can also be used to refine access and careful consideration is needed to avoid login issues.

For example:

- Authenticator map A denies all users access to the system
- Authenticator map B allows the user `john` access to the system


When the mapping order is set to A, B; the first map denies access for all users, including `john`. The second map subsequently allows `john` access to the system and the result is that `john` is granted access and is able to log in to the platform.

However, when the mapping order is changed to B, A; the first map allows `john` access to the system. The second map subsequently denies all users access to the system (including `john`) and the result is that `john` is denied access and is unable to log in to the platform.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  In the list view, select the authenticator name displayed in the **Name** column.
3.  Select the **Mapping** tab from the **Details** page of your authenticator.
4.  Click Manage mappings.
5.  Adjust the mapping order by dragging and dropping the mappings up or down in the list using the icon. Note:
The mapping precedence is determined by the order in which the mappings are listed.

6.  After your authenticator maps are in the correct order, click Apply.

