# 2. Configuring authentication in the Ansible Automation Platform
## 2.7. Mapping
### 2.7.9. Superuser mapping

Superuser mapping is the mapping of a user to the superuser role, such as System Administrator.

**Procedure**

1. After configuring the authentication details for your authentication method, select the **Mapping** tab.
2. Select **Superuser** from the **Add authentication mapping** list.
3. Enter a unique rule **Name** to identify the rule.
4. Select a **Trigger** from the list. See [Authenticator map triggers](#gw-authenticator-map-triggers "2.7.3.&nbsp;Authenticator map triggers") for more information about map triggers.
5. Select **Revoke** to remove the superuser role from the user when none of the trigger conditions are matched.
6. Click Next.

**Next steps**

1. You can manage the authentication mappings order by clicking Manage mappings.

2. Drag and drop the mapping up or down in the list.


Note
The mapping precedence is determined by the order in which the mappings are listed.

3. Click Apply.

