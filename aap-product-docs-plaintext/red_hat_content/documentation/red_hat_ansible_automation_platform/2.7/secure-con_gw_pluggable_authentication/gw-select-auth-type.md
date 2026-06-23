# Pluggable authentication
## Select an authentication type

On the **Authentication Methods** page you can select the type of authenticator plugin you want to configure.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Click Create authentication.
3.  Enter a unique **Name** for the authenticator. The name is required, must be unique across all authenticators, and must not be longer than 512 characters. This becomes the unique identifier generated for the authenticator. Note:
Changing the name does not update the unique identifier of the authenticator. For example, if you create an authenticator with the name `My Authenticator` and later change it to `My LDAP Authenticator` you will not be able to create another authenticator with the name `My Authenticator` because the unique identifier is still in use.

4.  Select the authenticator type from the **Authentication type** list. See [Configuring an authentication type](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_config_authentication_type#gw-config-authentication-type "Ansible Automation Platform provides multiple authenticator plugins that you can configure to simplify the login experience for your organization.") for the complete list of authentication plugins available.
5.  The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type. See the relevant sections in Configuring an authentication type for the required details. For all authentication types you can enter a **Name**, **Additional Authenticator Fields** and **Create Objects**.

6.  Enable or disable **Enabled** to specify if the authenticator should be enabled or disabled. If enabled, users are able to login from the authenticator. If disabled, users will not be allowed to login from the authenticator.
7.  Enable or disable **Create Object** to specify whether the authenticator should create teams and organizations in the system when a user logs in.

Enabled
Teams and organizations defined in the authenticator maps are created and the users added to them.

Disabled
Organizations and teams defined in the authenticator maps will not be created automatically in the system. However, if they already exist, for example, created by a superuser, users who trigger the maps are granted access to them.

8.  Enable or disable **Remove Users**. If enabled, any access previously granted to a user is removed when they authenticate from this source. If disabled, permissions are only added or removed from the user based on the results of this authenticator’s authenticator mappings. For example, assume a user has been granted the `is_superuser` permission in the system. And that user will log in to an authenticator whose maps will not formulate an opinion as to whether or not the user should be a superuser. If **Remove Users** is enabled, the `is_superuser` permission will be removed from the user, the authenticator maps will not have an opinion as to whether it should be there or not so, after login the user will not have the `is_superuser` permission.

If **Remove Users** is disabled, the `is_superuser` permission *will not* be removed from the user. The authenticator maps will not have an opinion as to whether it should be there or not so after login the user *will* have the `is_superuser` permission.

9.  Click Create Authentication Method and proceed to [Define authentication mapping rules and triggers](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_gw_pluggable_authentication#gw-define-rules-triggers "Authentication map types can be used with any type of authenticator. Each map has a trigger that defines when the map should be evaluated as true.").

### What to do next

Important:

Before you enable an external authenticator, verify that your identity provider enforces email verification and restricts self-service email changes. The platform accepts email claims from identity providers without verifying email ownership.

Ansible Automation Platform uses email addresses to link external identities to existing platform accounts. If an identity provider permits unverified email addresses or unrestricted email changes, this can result in unintended account linking.

When you select an identity provider:

- Confirm that the provider verifies email addresses during user registration.
- Confirm that the provider requires administrator approval for email changes, or that email changes trigger re-verification.
- If the provider does not meet these requirements, use a different provider or implement compensating controls.


For more information about how the platform links external identities to accounts, see [User association and attribute synchronization](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_gw_user_association_and_attr_sync "Ansible Automation Platform manages user accounts and synchronizes attributes by centralizing user identification around a matching email address. You can sign in with existing accounts from different sources while maintaining a consistent user profile and access permissions.").
