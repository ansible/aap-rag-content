# 9. Upgrading Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 9.7. Ansible Automation Platform post-upgrade steps
### 9.7.5. Migrating Single Sign-On (SSO) users




When upgrading from Ansible Automation Platform 2.4 to 2.5, you must migrate your Single Sign-On (SSO) user accounts if you want to continue using SSO capabilities after the upgrade. Follow the steps in this procedure to ensure a smooth SSO user migration.

#### 9.7.5.1. Key considerations




**SSO configurations are not migrated automatically during upgrade to 2.5:** While the legacy authentication settings are carried over during the upgrade process and allow seamless initial access to the platform after upgrade, SSO configurations must be manually migrated over to a new Ansible Automation Platform 2.5 authentication configuration. The legacy configuration acts as a reference to preserve existing authentication capabilities and facilitate the migration process. The legacy authentication configuration should not be modified directly or used after migration is complete.

**SSO migration is supported in the UI:** Migration of legacy SSO accounts is supported in 2.5 UI, and is done by selecting your legacy authenticator from the **Auto migrate users from** list when you configure a new authentication method. This is the legacy authenticator from which to automatically migrate users to a new platform gateway authentication configuration.

**Migration of SSO must happen before users log in and start account linking:** You must enable the **Auto migrate users to** setting _after_ configuring SSO in 2.5 and _before_ any users log in.

Note
Ansible Automation Platform 2.4 SSO configurations are renamed during the upgrade process and are displayed in the **Authentication Methods** list view with a prefix to indicate a legacy configuration: for example, `legacy_sso-saml-&lt;entity id&gt;` . The **Authentication type** is also listed as **legacy sso** . These configurations can not be modified.



Once you set up the auto migrate functionality, you should be able to login with SSO in the platform gateway and it will automatically link any matching accounts from the legacy SSO authenticator.

**Additional resources**

[Ansible Automation Platform 2.4 to 2.5. Linking accounts post upgrade, and Setting up SAML authentication](https://interact.redhat.com/share/baxthgXBQZ3kSRKPLn5L)


