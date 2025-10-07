# Chapter 2. Configuring authentication in the Ansible Automation Platform




Using the authentication settings in Ansible Automation Platform, you can set up a simplified login through several authentication methods, such as LDAP and SAML. Depending on the authentication method you select, you will be required to enter different information to complete the configuration. Be sure to include all the information required for your configuration needs.

Important
- During an upgrade to Ansible Automation Platform 2.6, platform gateway uses a new central authentication service.
- After the upgrade, local users that used to exist in automation controller can be automatically converted into local platform gateway users. Other types of authentication from automation controller, such as LDAP, SAML, or OIDC, are migrated to platform gateway but platform gateway might need additional configuration before those users are ready for use.




Local user passwords are not automatically synchronized between automation controller and platform gateway after an upgrade. Platform gateway uses the following process to authenticate a local user for the first time:

- Platform gateway attempts to authenticate the user with the platform gateway password.
- If the attempt fails, platform gateway authenticates the user with the automation controller password.
- On successful authentication, platform gateway updates the user’s password in its database.
- The user is authenticated directly by platform gateway on subsequent logins.


For more information, see [RPM upgrade and migration](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_upgrade) .

