# Configure central authentication for Ansible Automation Platform

Configure authentication methods such as LDAP or SAML to simplify the user login experience. Providing the correct connection details for your chosen identity provider helps ensure seamless and secure access to Ansible Automation Platform.

Configuring authentication involves the following procedures:

- Selecting an authentication type, where you select the type of authenticator plugin you want to configure, including the authentication details for the authentication type selected.
- Mapping, where you define mapping rule types and triggers to control access to the system, and mapping order where you can define the mapping precedence.

Important:

- During an upgrade to Ansible Automation Platform 2.6, platform gateway uses a new central authentication service.
- After the upgrade, local users that used to exist in automation controller can be automatically converted into local platform gateway users. Other types of authentication from automation controller, such as LDAP, SAML, or OIDC, are migrated to platform gateway but platform gateway might need additional configuration before those users are ready for use.

Local user passwords are not automatically synchronized between automation controller and platform gateway after an upgrade. Platform gateway uses the following process to authenticate a local user for the first time:

- Platform gateway attempts to authenticate the user with the platform gateway password.
- If the attempt fails, platform gateway authenticates the user with the automation controller password.
- On successful authentication, platform gateway updates the user’s password in its database.
- The user is authenticated directly by platform gateway on subsequent logins.


