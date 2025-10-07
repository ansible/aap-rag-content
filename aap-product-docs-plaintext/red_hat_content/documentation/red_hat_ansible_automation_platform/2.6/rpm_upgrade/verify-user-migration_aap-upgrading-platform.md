# 2. Upgrading to Red Hat Ansible Automation Platform 2.6
## 2.7. Verifying user migration




During the upgrade to Ansible Automation Platform 2.6, controller user accounts are converted into platform user accounts. Controller administrators retain their administrative privileges, but they are converted into platform administrator privileges.

Other controller accounts become platform users, and their existing permissions are mapped over appropriately after an initial password reset. Users with existing accounts associated with other components (like private automation hub and Event-Driven Ansible) must have their passwords reset by their administrator before they can log in.

Authenticator configurations are automatically migrated. SSO and LDAP accounts do not require any manual migration steps, including password resets, with the exception of accounts that use a certificate from the trust store. See [Configuring authentication in the Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade) for more information on migrating authentication configurations that use a custom certificate.

After your upgrade to Ansible Automation Platform 2.6 is complete, verify that you can log in to the upgraded platform.

**Procedure**

- If you have a controller account that has been converted to a platform gateway account for Ansible Automation Platform 2.6:


- Log into your upgraded platform instance with your controller credentials.

- If you have a component-level account (such as an account associated with private automation hub or Event-Driven Ansible):


- Request a password reset from your administrator and log into the upgraded platform with your new password.



