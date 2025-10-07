# Chapter 6. Authentication movement




During an upgrade from Ansible Automation Platform 2.4 to 2.6, only complete authentication provider configurations are migrated to the new platform gateway.

A configuration is considered complete when it meets the following criteria:

-  **LDAP** : You must specify a server URL.
-  **GitHub and Microsoft Azure AD** : You must specify both a key and a secret.
-  **OIDC** : You must define a key, a secret, and an OIDC endpoint.
-  **RADIUS** and **TACACS+** : You must specify the host.


Before proceeding with the upgrade, ensure that you complete the following steps:

-  **Create a local administrator account** and verify that you can log in to the environment using local authentication. You can also use the default administrator account from the inventory file.
-  **Enable the local authenticator** in the target environment to ensure a fallback login method is available.
-  **Perform a full backup** of your existing environment.

Important
This is a critical step for data recovery in case any issues occur during the migration process.






**Post upgrade**

-  **Update the callback URLs** in your _Identity Provider_ (IdP) configurations after the movement. This is necessary for OAuth and SSO providers to function correctly with the new platform gateway architecture. For more information, see [Updating callback URLs for OAuth and SSO providers](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-configure-authentication#gw-update-callback-urls) .
-  **Reestablish custom certificates for LDAPS** if your LDAP authentication uses custom certificates in the system’s trust store. This configuration is not automatically migrated and you must manually reestablish it.


The movement of existing authentication configurations from a Red Hat Ansible Automation Platform 2.4 automation controller to the new 2.6 platform gateway is automated. The following tables show how settings and mappings from the old automation controller schema are transformed to fit the new platform gateway API schema.

