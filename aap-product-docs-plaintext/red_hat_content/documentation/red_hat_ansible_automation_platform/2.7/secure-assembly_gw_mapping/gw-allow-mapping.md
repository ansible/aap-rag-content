# Map external authenticators to Ansible Automation Platform
## Control user access to the system with allow mapping

With allow mapping, you can control which users have access to the system by defining the conditions that must be met.

### Procedure

1.  After configuring the authentication details for your authentication method, select the **Mapping** tab.
2.  Select **Allow** from the **Add authentication mapping** list.
3.  Enter a unique rule **Name** to identify the rule.
4.  Select a **Trigger** from the list. See [Authenticator map triggers](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-authenticator-map-triggers "Each map has a trigger that defines when the map should be evaluated as true. Trigger types include the following:") for more information about map triggers.
5.  Select **Revoke** to deny user access to the system when the trigger conditions are not matched.
6.  Click Next.

### What to do next

1. You can manage the authentication mappings order by clicking Manage mappings.
2. Drag and drop the mapping up or down in the list.  Note:
The mapping precedence is determined by the order in which the mappings are listed.

3. Click Apply.

