# 3. Configuring authentication in the Ansible Automation Platform
## 3.2. Pluggable authentication




Authentication is the process of verifying a user’s identity to the Ansible Automation Platform (that is, to establish that a user is who they say they are). This can be done in a number of ways but would traditionally be associated with a `username` and `password` .

Ansible Automation Platform 2.5 uses a pluggable authentication system with a configuration wizard that provides a common, simplified method of configuring different types of authenticators such as LDAP and SAML. The pluggable system also allows you to configure multiple authenticators of the same type.

In the pluggable system we have a couple of concepts:

