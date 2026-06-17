+++
title = "Pluggable authentication - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_gw_pluggable_authentication"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_gw_pluggable_authentication/aem-page/secure-con_gw_pluggable_authentication.html"
last_crumb = "Pluggable authentication"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Pluggable authentication"
oversized = "false"
page_slug = "secure-con_gw_pluggable_authentication"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-con_gw_pluggable_authentication"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-con_gw_pluggable_authentication/toc/toc.json"
type = "aem-page"
+++

# Pluggable authentication

Authentication verifies a user's identity to Red Hat Ansible Automation Platform. While users can authenticate through a username and password, configuring external sources like LDAP, SAML, or OIDC enables a single sign-on (SSO) experience using existing enterprise credentials.

Note:

When you log out of Ansible Automation Platform, only your session with the platform ends. Your session with the external Single Sign-On (SSO) provider stays active. To switch to a different account with the same provider, you must log out of the SSO provider’s website directly. This ensures that you can successfully sign in with a new account.

Ansible Automation Platform uses a pluggable authentication system with a configuration wizard that provides a common, simplified method of configuring different types of authenticators such as LDAP and SAML. The pluggable system also allows you to configure multiple authenticators of the same type.

In the pluggable system we have a couple of concepts:

Authenticator Plugin
A plugin allows Ansible Automation Platform to connect to a source system, such as, LDAP, or SAML. Ansible Automation Platform includes a variety of authenticator plugins. Authenticator plugins are similar to Ansible collections, in that all of the required code is in a package and can be versioned independently if needed.

Authenticator
An authenticator is an instantiation of an authenticator plugin and allows users from the specified source to log in. For example, the LDAP authenticator plugin defines a required LDAP server setting. When you instantiate an authenticator from the LDAP authentication plugin, you must provide the authenticator the LDAP server URL it needs to connect to.

Authenticator Map
Authenticator maps are applied to authenticators and tell Ansible Automation Platform what permissions to give a user logging into the system.

## Configure authentication

Configure authentication by connecting an identity provider to Ansible Automation Platform and then configuring it to fine tune user access.

Configuring authentication involves the following procedures:

- Selecting an authentication type, where you select the type of authenticator plugin you want to configure, including the authentication details for the authentication type selected.
- Mapping, where you define mapping rule types and triggers to control access to the system, and mapping order where you can define the mapping precedence. Note:
      Mapping order is only available if you have defined one or more authenticator maps.

## Enable and disable the local authenticator

As a platform administrator, you can enable or disable authenticators. However, disabling your local authenticator can have significant impacts and should only be done under specific circumstances. Before you disable your local authenticator, you must consider the following:

### Before you begin

- You have at least one other authenticator method configured.
- You have at least one administrator account that can authenticate using your alternate authenticator.


CAUTION:

Disabling the local authenticator without an alternative authentication in place can result in a locked environment.

### About this task

Local account inaccessibility
Disabling the local authenticator prevents all local accounts, including the default `admin` account from logging in.

Potential inaccessibility
Disabling the local authenticator without having at least one other configured authenticator can render the Ansible Automation Platform environment completely inaccessible.

Dependency on enterprise authentication provider
If the local authenticator is disabled and an issue occurs with the configured enterprise authentication provider, the platform will become inaccessible until the enterprise authentication provider issue is resolved.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Ensure that at least one other authenticator type is configured and enabled.
3.  Select your **Local Authenticator**.
4.  Toggle the **Enabled** switch to the off position to disable the local authenticator.

If the local authenticator is disabled without another authentication method configured, or if an issue arises with your configured enterprise authentication provider, making the Ansible Automation Platform inaccessible, you can re-enable the local authenticator from the command line as follows:

1. List the available authenticators and retrieve the ID of your local authenticator by running the following command:

```
aap-gateway-api authenticators --list
```

2. Enable the local authenticator using its ID:

```
aap-gateway-manage authenticators --enable :id
```
    where: `:id` is the ID of the local authenticator obtained from the previous step.

## Adjust the mapping order

Adjust the execution order of your authenticator maps to control authorization rule precedence. As later maps override earlier ones, setting the correct sequence helps ensure users receive the intended permissions and team memberships.

### About this task

For example, if the first authenticator map is of type `is_superuser` and the trigger is set to **never**, any user logging into the system would never be granted the `is_superuser` flag.

And, if the second map is of type `is_superuser` and the trigger is based on the user having a specific group, any user logging in would initially be denied the `is_superuser` permission. However, any user with the specified group would subsequently be granted the `is_superuser` permission by the second rule.

The order of rules is important beyond whether you want to process organizations, teams or roles first. They can also be used to refine access and careful consideration is needed to avoid login issues.

For example:

- Authenticator map A denies all users access to the system
- Authenticator map B allows the user `john` access to the system


When the mapping order is set to A, B; the first map denies access for all users, including `john`. The second map subsequently allows `john` access to the system and the result is that `john` is granted access and is able to log in to the platform.

However, when the mapping order is changed to B, A; the first map allows `john` access to the system. The second map subsequently denies all users access to the system (including `john`) and the result is that `john` is denied access and is unable to log in to the platform.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  In the list view, select the authenticator name displayed in the **Name** column.
3.  Select the **Mapping** tab from the **Details** page of your authenticator.
4.  Click Manage mappings.
5.  Adjust the mapping order by dragging and dropping the mappings up or down in the list using the icon. Note:
      The mapping precedence is determined by the order in which the mappings are listed.

6.  After your authenticator maps are in the correct order, click Apply.

## Define authentication mapping rules and triggers

Authentication map types can be used with any type of authenticator. Each map has a trigger that defines when the map should be evaluated as true.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  In the list view, select the authenticator name displayed in the **Name** column.
3.  Select the **Mapping** tab from the **Details** page of your authenticator.
4.  Click Create mapping.
5.  Select a map type from the **Authentication mapping** list. See [Authenticator map types](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_mapping#gw-authenticator-map-types "Ansible Automation Platform supports the following rule types:") for detailed descriptions of the different map types. Choices include:

  -  [Allow](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_mapping#gw-allow-mapping "With allow mapping, you can control which users have access to the system by defining the conditions that must be met.")
  -  [Organization](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_mapping#proc-controller-organization-mapping "You can control which users are placed into which Ansible Automation Platform organizations based on attributes such as their username and email address or based on groups provided from an authenticator.")
  -  [Team](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_mapping#proc-controller-team-mapping "Team mapping is the mapping of team members (users) from authenticators.")
  -  [Role](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_mapping#gw-role-mapping "Role mapping is the mapping of a user either to a global role, such as Platform Auditor, or team or organization role.")
  -  [Is Superuser](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_mapping#gw-superuser-mapping "Superuser mapping is the mapping of a user to the superuser role, such as System Administrator.")

6.  Enter a unique rule **Name** to identify the rule.
7.  Select a **Trigger** from the list. See [Authenticator map triggers](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_mapping#gw-authenticator-map-triggers "Each map has a trigger that defines when the map should be evaluated as true. Trigger types include the following:") for more details. Choices include:

  -  **Always**
  -  **Never**
  -  **Group**
  -  **Attribute**

8.  Click Create mapping.
9.  Repeat this procedure to create additional mapping rules and triggers for the authenticator.
10.  Proceed to [Adjust the Mapping order](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_gw_pluggable_authentication#gw-adjust-mapping-order "Adjust the execution order of your authenticator maps to control authorization rule precedence. As later maps override earlier ones, setting the correct sequence helps ensure users receive the intended permissions and team memberships.") to optionally reorder the mappings for your authenticator. Note:
      The mapping order setting is only available if there is more than one authenticator map defined.

## Select an authentication type

On the **Authentication Methods** page you can select the type of authenticator plugin you want to configure.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Click Create authentication.
3.  Enter a unique **Name** for the authenticator. The name is required, must be unique across all authenticators, and must not be longer than 512 characters. This becomes the unique identifier generated for the authenticator. Note:
      Changing the name does not update the unique identifier of the authenticator. For example, if you create an authenticator with the name `My Authenticator` and later change it to `My LDAP Authenticator` you will not be able to create another authenticator with the name `My Authenticator` because the unique identifier is still in use.

4.  Select the authenticator type from the **Authentication type** list. See [Configuring an authentication type](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_config_authentication_type#gw-config-authentication-type "Ansible Automation Platform provides multiple authenticator plugins that you can configure to simplify the login experience for your organization.") for the complete list of authentication plugins available.
5.  The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type. See the relevant sections in Configuring an authentication type for the required details. For all authentication types you can enter a **Name**, **Additional Authenticator Fields** and **Create Objects**.

6.  Enable or disable **Enabled** to specify if the authenticator should be enabled or disabled. If enabled, users are able to login from the authenticator. If disabled, users will not be allowed to login from the authenticator.
7.  Enable or disable **Create Object** to specify whether the authenticator should create teams and organizations in the system when a user logs in.

Enabled
Teams and organizations defined in the authenticator maps are created and the users added to them.

Disabled
Organizations and teams defined in the authenticator maps will not be created automatically in the system. However, if they already exist, for example, created by a superuser, users who trigger the maps are granted access to them.

8.  Enable or disable **Remove Users**. If enabled, any access previously granted to a user is removed when they authenticate from this source. If disabled, permissions are only added or removed from the user based on the results of this authenticator’s authenticator mappings. For example, assume a user has been granted the `is_superuser` permission in the system. And that user will log in to an authenticator whose maps will not formulate an opinion as to whether or not the user should be a superuser. If **Remove Users** is enabled, the `is_superuser` permission will be removed from the user, the authenticator maps will not have an opinion as to whether it should be there or not so, after login the user will not have the `is_superuser` permission.

    If **Remove Users** is disabled, the `is_superuser` permission *will not* be removed from the user. The authenticator maps will not have an opinion as to whether it should be there or not so after login the user *will* have the `is_superuser` permission.

9.  Click Create Authentication Method and proceed to [Define authentication mapping rules and triggers](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_gw_pluggable_authentication#gw-define-rules-triggers "Authentication map types can be used with any type of authenticator. Each map has a trigger that defines when the map should be evaluated as true.").

### What to do next

Important:

Before you enable an external authenticator, verify that your identity provider enforces email verification and restricts self-service email changes. The platform accepts email claims from identity providers without verifying email ownership.

Ansible Automation Platform uses email addresses to link external identities to existing platform accounts. If an identity provider permits unverified email addresses or unrestricted email changes, this can result in unintended account linking.

When you select an identity provider:

- Confirm that the provider verifies email addresses during user registration.
- Confirm that the provider requires administrator approval for email changes, or that email changes trigger re-verification.
- If the provider does not meet these requirements, use a different provider or implement compensating controls.


For more information about how the platform links external identities to accounts, see [User association and attribute synchronization](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-con_gw_user_association_and_attr_sync "Ansible Automation Platform manages user accounts and synchronizes attributes by centralizing user identification around a matching email address. You can sign in with existing accounts from different sources while maintaining a consistent user profile and access permissions.").
