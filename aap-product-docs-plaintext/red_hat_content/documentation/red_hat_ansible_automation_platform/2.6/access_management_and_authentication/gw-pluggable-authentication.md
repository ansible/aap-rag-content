# 2. Configuring authentication in the Ansible Automation Platform
## 2.2. Pluggable authentication




Authentication is the process of verifying a user’s identity to the Ansible Automation Platform, that is, to establish that a user is who they say they are. This can be done in several ways and is traditionally associated with a `username` and `password` . Configuring external authentication sources such as LDAP, SAML, and OIDC enables a Single Sign-On (SSO) experience. SSO allows users to access platform gateway by using the same credentials from other enterprise services.

Note
When you log out of Ansible Automation Platform, only your session with the platform ends. Your session with the external Single Sign-On (SSO) provider stays active. To switch to a different account with the same provider, you must log out of the SSO provider’s website directly. This ensures that you can successfully sign in with a new account.



Ansible Automation Platform 2.6 uses a pluggable authentication system with a configuration wizard that provides a common, simplified method of configuring different types of authenticators such as LDAP and SAML. The pluggable system also allows you to configure multiple authenticators of the same type.

In the pluggable system we have a couple of concepts:

