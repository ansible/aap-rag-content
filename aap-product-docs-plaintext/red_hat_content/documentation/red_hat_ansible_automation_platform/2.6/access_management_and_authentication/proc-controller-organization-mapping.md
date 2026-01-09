# 2. Configuring authentication in the Ansible Automation Platform
## 2.7. Mapping
### 2.7.6. Organization mapping




You can control which users are placed into which Ansible Automation Platform organizations based on attributes such as their username and email address or based on groups provided from an authenticator.

When organization mapping is positively evaluated, a specified organization is created, if it does not exist if the authenticator tied to the map is allowed to create objects.

**Procedure**

1. After configuring the authentication details for your authentication method, select the **Mapping** tab.
1. Select **Organization** from the **Add authentication mapping** list.
1. Enter a unique rule **Name** to identify the rule.
1. Select a **Trigger** from the list. See [Authenticator map triggers](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/access_management_and_authentication/index#gw-authenticator-map-triggers) for more information about map triggers.
1. Select **Revoke** to remove the user’s access to the selected organization role when the trigger conditions are not matched.
1. Select the **Organization** to which matching users are added or blocked.
1. Select a **Role** to be applied or removed for matching users (for example, **Organization Admin** or **Organization Member** ).
1. ClickNext.


**Next steps**

1. You can manage the authentication mappings order by clickingManage mappings.
1. Drag and drop the mapping up or down in the list.

Note
The mapping precedence is determined by the order in which the mappings are listed.




1. ClickApply.


