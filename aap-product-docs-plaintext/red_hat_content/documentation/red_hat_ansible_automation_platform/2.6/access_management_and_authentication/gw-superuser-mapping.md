# 2. Configuring authentication in the Ansible Automation Platform
## 2.7. Mapping
### 2.7.9. Superuser mapping




Superuser mapping is the mapping of a user to the superuser role, such as System Administrator.

**Procedure**

1. After configuring the authentication details for your authentication method, select the **Mapping** tab.
1. Select **Superuser** from the **Add authentication mapping** list.
1. Enter a unique rule **Name** to identify the rule.
1. Select a **Trigger** from the list. See [Authenticator map triggers](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/access_management_and_authentication/index#gw-authenticator-map-triggers) for more information about map triggers.
1. Select **Revoke** to remove the superuser role from the user when none of the trigger conditions are matched.
1. ClickNext.


**Next steps**

1. You can manage the authentication mappings order by clickingManage mappings.
1. Drag and drop the mapping up or down in the list.

Note
The mapping precedence is determined by the order in which the mappings are listed.




1. ClickApply.


