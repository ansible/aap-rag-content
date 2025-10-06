# 2. Configuring authentication in the Ansible Automation Platform
## 2.3. Creating an authentication method
### 2.3.1. Selecting an authentication type




On the **Authentication Methods** page you can select the type of authenticator plugin you want to configure.

**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. ClickCreate authentication.
1. Enter a unique **Name** for the authenticator. The name is required, must be unique across all authenticators, and must not be longer than 512 characters. This becomes the unique identifier generated for the authenticator.

Note
Changing the name does not update the unique identifier of the authenticator. For example, if you create an authenticator with the name `    My Authenticator` and later change it to `    My LDAP Authenticator` you will not be able to create another authenticator with the name `    My Authenticator` because the unique identifier is still in use.




1. Select the authenticator type from the **Authentication type** list. See [Configuring an authentication type](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-config-authentication-type) for the complete list of authentication plugins available.
1. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type. See the respective sections in Configuring an authentication type for the required details.

For all authentication types you can enter a **Name** , **Additional Authenticator Fields** and **Create Objects** .


1. Enable or disable **Enabled** to specify if the authenticator should be enabled or disabled. If enabled, users are able to login from the authenticator. If disabled, users will not be allowed to login from the authenticator.
1. Enable or disable **Create Object** to specify whether the authenticator should create teams and organizations in the system when a user logs in.


1. Enable or disable **Remove Users** . If enabled, any access previously granted to a user is removed when they authenticate from this source. If disabled, permissions are only added or removed from the user based on the results of this authenticator’s authenticator mappings.

For example, assume a user has been granted the `    is_superuser` permission in the system. And that user will log in to an authenticator whose maps will not formulate an opinion as to whether or not the user should be a superuser. If **Remove Users** is enabled, the `    is_superuser` permission will be removed from the user, the authenticator maps will not have an opinion as to whether it should be there or not so, after login the user will not have the `    is_superuser` permission.

If **Remove Users** is disabled, the `    is_superuser` permission _will not_ be removed from the user. The authenticator maps will not have an opinion as to whether it should be there or not so after login the user _will_ have the `    is_superuser` permission.


1. ClickCreate Authentication Methodand proceed to [Define authentication mapping rules and triggers](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-define-rules-triggers) .


