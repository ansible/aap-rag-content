# Map external authenticators to Ansible Automation Platform
## Map users to roles

Role mapping is the mapping of a user either to a global role, such as Platform Auditor, or team or organization role.

### About this task

When a Team or Organization is specified together with the appropriate Role, the behavior is the same with Organization mapping or Team mapping.

You can specify role mapping separately for each account authentication.

### Procedure

1.  After configuring the authentication details for your authentication method, select the **Mapping** tab.
2.  Select **Role** from the **Add authentication mapping** list.
3.  Enter a unique rule **Name** to identify the rule.
4.  Select a **Trigger** from the list. See [Authenticator map triggers](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-authenticator-map-triggers "Each map has a trigger that defines when the map should be evaluated as true. Trigger types include the following:") for more information about map triggers.
5.  Select **Revoke** to remove the role for the user when none of the trigger conditions are matched.
6.  Select a **Role** to be applied or removed for matching users.
7.  Click Next.

### What to do next

1. You can manage the authentication mappings order by clicking Manage mappings.
2. Drag and drop the mapping up or down in the list.  Note:
The mapping precedence is determined by the order in which the mappings are listed.

3. Click Apply.

