# 2. Configuring authentication in the Ansible Automation Platform
## 2.5. Configuring an authentication type
### 2.5.4. Configuring TACACS+ authentication




Terminal Access Controller Access-Control System Plus (TACACS+) is a protocol that handles remote authentication and related services for networked access control through a centralized server. TACACS+ provides authentication, authorization and accounting (AAA) services, in which you can configure Ansible Automation Platform to use as a source for authentication.

Note
This feature is deprecated and will be removed in a future release.



**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. ClickCreate authentication.
1. Enter a **Name** for this authentication configuration.
1. Select **TACACS+** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.
1. Select a legacy authenticator method from the **Auto migrate users from** list. After upgrading from 2.4 to 2.5, this is the legacy authenticator from which to automatically migrate users to this new authentication configuration. Refer to [Ansible Automation Platform post-upgrade steps](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_upgrade_and_migration/aap-post-upgrade) in the RPM upgrade and migration guide for important information about migrating users.
1. Enter the following information:


- Hostname of TACACS+ Server: Provide the hostname or IP address of the TACACS+ server with which to authenticate. If you leave this field blank, TACACS+ authentication is disabled.
- TACACS+ Authentication Protocol: The protocol used by the TACACS+ client. The options are ascii or pap.
- Shared secret for authenticating to TACACS+ server: The secret key for TACACS+ authentication server.

1. The **TACACS+ client address sending enabled** is disabled by default. To enable client address sending, select the checkbox.
1. Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator.

Note
Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.




1. To automatically create organizations, users, and teams upon successful login, select **Create objects** .
1. To enable this authentication method upon creation, select **Enabled** .
1. To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users** .

ClickCreate Authentication Method.




**Next steps**

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (like username and email address) or to what groups they belong, continue to [Mapping](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-mapping) .


