# 5. Identity access management data movement
## 5.2. Upgrades from Ansible Automation Platform 2.5 to 2.6
### 5.2.2. Automation hub




The following apply:

- A private automation hub admin (Automation Content Administrator) in 2.5 will be removed in the upgraded version and for this user the permissions must be reassigned manually as part of the data movement process.


Important
If teams with the same name exist in both automation hub and within the platform-wide authentication gateway, users from automation hub will be automatically added to corresponding teams within the platform-wide authentication gateway, and new teams will be created if they do not exist. This approach aims to retain team memberships, but requires careful review of permissions post-upgrade.



- If you rely on automation hub _Single Sign-On_ (SSO) to access the automation hub user interface (UI), automation hub SSO logins will no longer function after the upgrade. However, API tokens will remain active. Therefore, automated processes or systems that use API tokens for authentication will continue to operate without interruption. If your workflows predominantly rely on API access, the impact might be minimal. However, if users primarily access the UI through SSO, they will need to take action post-upgrade.
- To restore UI access for users who previously relied on automation hub SSO, you need to reconfigure SSO within Ansible Automation Platform to be able to login. For further information, see [Configuring Ansible Automation Platform Central Authentication Generic OIDC Settings and Red Hat SSO/KEYCLOAK for Red Hat SSO and Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html-single/installing_and_configuring_central_authentication_for_the_ansible_automation_platform/index#configuring-central-auth-generic-oidc-settings) .
- Automation controller admins will become platform admins and can administer automation hub.
- If you upgraded from 2.4 to 2.6 with both automation controller and private automation hub, then a dialog appears in the product post upgrade that informs you that there are steps to take in order to reconfigure private automation hub. This dialog can either display information in-product, or link to a product doc or Knowledge Base article. In either case, you will be guided to take action from within the product and not be expected to find that information unprompted.
- If you upgraded from 2.4 to 2.6 from an automation controller-only environment, then the addition of private automation hub and Event-Driven Ansible services involves adding the necessary roles to a normal user account to grant access to those services.


