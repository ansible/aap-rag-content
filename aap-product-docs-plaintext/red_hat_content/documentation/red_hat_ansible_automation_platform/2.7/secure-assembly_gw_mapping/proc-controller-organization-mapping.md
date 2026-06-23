# Map external authenticators to Ansible Automation Platform
## Map users to organizations

You can control which users are placed into which Ansible Automation Platform organizations based on attributes such as their username and email address or based on groups provided from an authenticator.

### About this task

When organization mapping is positively evaluated, a specified organization is created, if it does not exist if the authenticator tied to the map is allowed to create objects.

### Procedure

1.  After configuring the authentication details for your authentication method, select the **Mapping** tab.
2.  Select **Organization** from the **Add authentication mapping** list.
3.  Enter a unique rule **Name** to identify the rule.
4.  Select a **Trigger** from the list. See [Authenticator map triggers](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-authenticator-map-triggers "Each map has a trigger that defines when the map should be evaluated as true. Trigger types include the following:") for more information about map triggers.
5.  Select **Revoke** to remove the user’s access to the selected organization role when the trigger conditions are not matched.
6.  Select the **Organization** to which matching users are added or blocked.
7.  Select a **Role** to be applied or removed for matching users (for example, **Organization Admin** or **Organization Member**).
8.  Click Next.

### What to do next

1. You can manage the authentication mappings order by clicking Manage mappings.
2. Drag and drop the mapping up or down in the list.  Note:
The mapping precedence is determined by the order in which the mappings are listed.

3. Click Apply.

