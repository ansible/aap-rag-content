# 2. Configuring authentication in the Ansible Automation Platform
## 2.5. Configuring an authentication type
### 2.5.17. Configuring RADIUS authentication




You can configure Ansible Automation Platform to centrally use RADIUS as a source for authentication information.

**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. ClickCreate authentication.
1. Enter a **Name** for this authentication configuration.
1. Select **Radius** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.
1. Enter the host or IP of the RADIUS server in the **RADIUS Server** field. If you leave this field blank, RADIUS authentication is disabled.
1. Enter the **Shared secret for authenticating to RADIUS server** .
1. Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator.

Note
Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.




1. To automatically create organizations, users, and teams upon successful login, select **Create objects** .
1. To enable this authentication method upon creation, select **Enabled** .
1. To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users** .
1. ClickCreate Authentication Method.


**Next steps**

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or to what groups they belong, continue to [Mapping](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/access_management_and_authentication/index#gw-mapping) .


