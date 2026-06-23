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

