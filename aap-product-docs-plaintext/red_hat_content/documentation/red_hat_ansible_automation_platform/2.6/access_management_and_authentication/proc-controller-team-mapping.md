# 2. Configuring authentication in the Ansible Automation Platform
## 2.7. Mapping
### 2.7.7. Team mapping

Team mapping is the mapping of team members (users) from authenticators.

You can define the options for each team’s membership. For each team, you can specify which users are automatically added as members of the team and also which users can administer the team.

You can specify Team mappings separately for each account authentication.

When Team mapping is positively evaluated, a specified team and its organization are created, if they do not exist if the related authenticator is allowed to create objects.

Important

When configuring team mappings with an Attribute trigger, use the `or` operation. The `and` operation requires every single value in a list to match the comparison criteria for the trigger to be successful. This is rarely the intended behavior, as you typically want a match on at least one value in the list.

**Procedure**

1. After configuring the authentication details for your authentication method, select the **Mapping** tab.
2. Select **Team** from the **Add authentication mapping** list.
3. Enter a unique rule **Name** to identify the rule.
4. Select a **Trigger** from the list. See [Authenticator map triggers](#gw-authenticator-map-triggers "2.7.3.&nbsp;Authenticator map triggers") for more information about map triggers.
5. Select **Revoke** to remove the user’s access to the selected organization role and deny user access to the system when the trigger conditions are not matched.
6. Select the **Team** and **Organization** to which matching users are added or blocked.
7. Select a **Role** to be applied or removed for matching users (for example, **Team Admin** or **Team Member**).
8. Click Next.

**Next steps**

1. You can manage the authentication mappings order by clicking Manage mappings.

2. Drag and drop the mapping up or down in the list.


Note
The mapping precedence is determined by the order in which the mappings are listed.

3. Click Apply.

