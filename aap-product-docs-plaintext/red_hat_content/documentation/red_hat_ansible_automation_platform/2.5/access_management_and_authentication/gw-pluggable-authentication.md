# 2. Configuring authentication in the Ansible Automation Platform
## 2.2. Pluggable authentication




Authentication is the process of verifying a user’s identity to the Ansible Automation Platform (that is, to establish that a user is who they say they are). You can do this in several ways but would traditionally be associated with a `username` and `password` .

Note
When you log out of Ansible Automation Platform, only your session with the platform ends. Your session with the external Single Sign-On (SSO) provider stays active. To switch to a different account with the same provider, you must log out of the SSO provider’s website directly. This ensures that you can successfully sign in with a new account.



Ansible Automation Platform 2.5 uses a pluggable authentication system with a configuration wizard that provides a common, simplified method of configuring different types of authenticators such as LDAP and SAML. With the pluggable system you can configure many authenticators of the same type.

In the pluggable system we have a couple of concepts:

