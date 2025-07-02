# 3. Configuring authentication in the Ansible Automation Platform
## 3.6. Mapping
### 3.6.7. Team mapping




Team mapping is the mapping of team members (users) from authenticators.

You can define the options for each team’s membership. For each team, you can specify which users are automatically added as members of the team and also which users can administer the team.

Team mappings can be specified separately for each account authentication.

When Team mapping is positively evaluated, a specified team and its organization are created, if they don’t exist if the related authenticator is allowed to create objects.

**Procedure**

1. After configuring the authentication details for your authentication method, select the **Mapping** tab.
1. Select **Team** from the **Add authentication mapping** list.
1. Enter a unique rule **Name** to identify the rule.
1. Select a **Trigger** from the list. See [Authenticator map triggers](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-authenticator-map-triggers) for more information about map triggers.
1. Select **Revoke** to remove the user’s access to the selected organization role and deny user access to the system when the trigger conditions are not matched.
1. Select the **Team** and **Organization** to which matching users are added or blocked.
1. Select a **Role** to be applied or removed for matching users (for example, **Team Admin** or **Team Member** ).
1. ClickNext.


**Next steps**

1. You can manage the authentication mappings order by clickingManage mappings.
1. Drag and drop the mapping up or down in the list.

Note
The mapping precedence is determined by the order in which the mappings are listed.




1. ClickApply.


