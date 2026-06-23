# Pluggable authentication
## Define authentication mapping rules and triggers

Authentication map types can be used with any type of authenticator. Each map has a trigger that defines when the map should be evaluated as true.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  In the list view, select the authenticator name displayed in the **Name** column.
3.  Select the **Mapping** tab from the **Details** page of your authenticator.
4.  Click Create mapping.
5.  Select a map type from the **Authentication mapping** list. See [Authenticator map types](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-authenticator-map-types "Ansible Automation Platform supports the following rule types:") for detailed descriptions of the different map types. Choices include:

-  [Allow](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-allow-mapping "With allow mapping, you can control which users have access to the system by defining the conditions that must be met.")
-  [Organization](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#proc-controller-organization-mapping "You can control which users are placed into which Ansible Automation Platform organizations based on attributes such as their username and email address or based on groups provided from an authenticator.")
-  [Team](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#proc-controller-team-mapping "Team mapping is the mapping of team members (users) from authenticators.")
-  [Role](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-role-mapping "Role mapping is the mapping of a user either to a global role, such as Platform Auditor, or team or organization role.")
-  [Is Superuser](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-superuser-mapping "Superuser mapping is the mapping of a user to the superuser role, such as System Administrator.")

6.  Enter a unique rule **Name** to identify the rule.
7.  Select a **Trigger** from the list. See [Authenticator map triggers](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-authenticator-map-triggers "Each map has a trigger that defines when the map should be evaluated as true. Trigger types include the following:") for more details. Choices include:

-  **Always**
-  **Never**
-  **Group**
-  **Attribute**

8.  Click Create mapping.
9.  Repeat this procedure to create additional mapping rules and triggers for the authenticator.
10.  Proceed to [Adjust the Mapping order](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_gw_pluggable_authentication#gw-adjust-mapping-order "Adjust the execution order of your authenticator maps to control authorization rule precedence. As later maps override earlier ones, setting the correct sequence helps ensure users receive the intended permissions and team memberships.") to optionally reorder the mappings for your authenticator. Note:
The mapping order setting is only available if there is more than one authenticator map defined.

