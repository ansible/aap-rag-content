# 2. Configuring authentication in the Ansible Automation Platform
## 2.5. Configuring an authentication type
### 2.5.3. Configuring local authentication




As a platform administrator, you can configure local system authentication. With local authentication, users and their passwords are checked against local system accounts.

Note
A local authenticator is automatically created by the Ansible Automation Platform installation process, and is configured with the specified admin credentials in the inventory file before installation. After successful installation, you can log in to the Ansible Automation Platform using those credentials.



**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. ClickCreate authentication.
1. Enter a **Name** for this Local configuration. The configuration name is required, must be unique across all authenticators, and must not be longer than 512 characters.
1. Select **Local** from the **Authentication type** list.
1. Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator.

Note
Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.




1. To automatically create organizations, users, and teams upon successful login, select **Create objects** .
1. To enable this authentication method upon creation, select **Enabled** .
1. To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users** .
1. ClickNext.


**Next steps**

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or to what groups they belong, continue to [Mapping](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/access_management_and_authentication/index#gw-mapping) .


