# 3. Configuring authentication in the Ansible Automation Platform
## 3.6. Mapping
### 3.6.5. Allow mapping




With allow mapping, you can control which users have access to the system by defining the conditions that must be met.

**Procedure**

1. After configuring the authentication details for your authentication method, select the **Mapping** tab.
1. Select **Allow** from the **Add authentication mapping** list.
1. Enter a unique rule **Name** to identify the rule.
1. Select a **Trigger** from the list. See [Authenticator map triggers](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-authenticator-map-triggers) for more information about map triggers.
1. Select **Revoke** to deny user access to the system when the trigger conditions are not matched.
1. ClickNext.


**Next steps**

1. You can manage the authentication mappings order by clickingManage mappings.
1. Drag and drop the mapping up or down in the list.

Note
The mapping precedence is determined by the order in which the mappings are listed.




1. ClickApply.


