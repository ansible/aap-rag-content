# Chapter 3. Ansible Automation Platform post-upgrade steps




After a successful upgrade to Ansible Automation Platform 2.5, the next crucial step is migrating your users to the latest version of the platform.

User data and legacy authentication settings from automation controller and private automation hub are carried over during the upgrade process and allow seamless initial access to the platform after upgrade. Customers can log in without additional action.

However, to fully transition authentication to use all of the features and capabilities of the 2.5 platform gateway, a manual process is required post-upgrade to leverage the new authentication framework. In the context of upgrading to Ansible Automation Platform 2.5, this manual process is referred to as _migration_ .

There are important notes and considerations for each type of user migration, including the following:

- Admin users
- Normal users
- SSO users
- LDAP users


Be sure to read through the important notes highlighted for each user type to help make the migration process as smooth as possible.

