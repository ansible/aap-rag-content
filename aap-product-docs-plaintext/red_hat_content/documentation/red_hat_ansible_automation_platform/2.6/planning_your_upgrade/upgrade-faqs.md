# Chapter 2. FAQs related to upgrading

Find concise answers to frequently asked questions about upgrading your system to quickly troubleshoot common issues and plan your migration effectively.

What are the supported installation topologies and operating systems for Ansible Automation Platform 2.6?
Red Hat has adopted a more definitive approach to installation topologies, categorizing them as "growth" or "enterprise" for production-ready setups:

- Growth topology: is intended for organizations that are getting started with Ansible Automation Platform and do not require redundancy or higher compute for large volumes of automation.
- Enterprise topology: is intended for organizations that require Ansible Automation Platform to be deployed with redundancy or higher compute for large volumes of automation.

For more information, see [Tested deployment models](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/index).

Why did my authentication settings that were present in automation controller 2.4 not get imported?
If an authentication method is missing in Ansible Automation Platform 2.6, review the setup_log for migration warnings. These warnings indicate the reason authentication settings were not successfully created during the upgrade to version 2.6.

Why did my upgrade from Ansible Automation Platform 2.4 to 2.6 fail or encounter an error during the SAML authenticator migration?
A SAML authenticator migration fails if the configuration has an encrypted private key. While automation controller in Ansible Automation Platform 2.4 allowed input of an encrypted private key without error, Ansible Automation Platform 2.6 does not support this feature for authenticators and prevents the migration of any SAML configuration containing one.

To prevent migration failure and service disruption for SSO users, you must:

- **Before upgrading**: Replace the encrypted private key with an unencrypted one in the SAML authenticator settings on your Ansible Automation Platform 2.4 environment.

- **If the upgrade already failed**: Platform gateway did not migrate the authenticator. A local administrator must manually re-create the SAML authenticator in the new Ansible Automation Platform 2.6 environment to restore SSO functionality.



Which Red Hat Enterprise Linux versions are supported for RPM and containerized installations?
RPM installations will continue to be supported exclusively on Red Hat Enterprise Linux 9. Containerized installations support both Red Hat Enterprise Linux 9.4 or later versions of Red Hat Enterprise Linux 9 and Red Hat Enterprise Linux 10 or later versions of Red Hat Enterprise Linux 10 for enterprise topologies.

What is the difference between "upgrade" and "migration" in Ansible Automation Platform 2.6?
An upgrade is an application action, such as updating Ansible Automation Platform 2.5 to 2.6. A migration involves moving data, such as from an RPM-based 2.6 installation to a container-based 2.6 installation. New service components are not explicitly required between versions 2.5 and 2.6.

Can I upgrade from 2.4 to 2.6 or must I upgrade to 2.5 first?
Yes you can upgrade directly to 2.6. However note that there might be new system requirements you must update before upgrading.

How will managed cloud customers be upgraded to Ansible Automation Platform 2.6?
All managed cloud customers on Microsoft Azure and Amazon Web Services will be upgraded to 2.6. Two upgrade window options will be available following the platform upgrade: non-production or production environments. Communications will be ongoing from mid-July until late September.

Will migrations be fully supported in Ansible Automation Platform 2.6?
Yes, migrations are fully supported, enabling customers to move from RPM installations to containerized or OpenShift Container Platform environments, or to the managed offering. Customers must be on the latest version of Ansible Automation Platform for their current installation before migrating. The installation program manages new components introduced in version 2.5 for direct 2.4 to 2.6 upgrades.

When upgrading from 2.4 to 2.6 (applies only to RPM or OpenShift Container Platform), what is different about the upgrade process compared with the 2.4 to 2.5 process?
See the [Overview of upgrade improvements](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/planning_your_upgrade/index#con-upgrade-improvements-overview) section.

I’m using Event-Driven Ansible in 2.4, can I upgrade Event-Driven Ansible to 2.6?
If you are using Ansible Automation Platform 2.4 with the technical preview of Event-Driven Ansible controller but want to upgrade to the Ansible Automation Platform 2.6 with Event-Driven Ansible, you must install a new instance of Ansible Automation Platform 2.6 and manually re-create your Event-Driven Ansible configurations in the new, fully integrated environment.

Will my existing 2.4 or 2.5 OAuth Applications/Tokens, Credentials/Customer Credentials, and Personal Access Tokens still work after upgrading to 2.6?
For upgrades from Ansible Automation Platform 2.4 or 2.5 to Ansible Automation Platform 2.6, some manual configuration is required:

- OAuth applications:


- Automation controller: You can view and edit existing automation controller applications, but you cannot create new ones. They still function, but they might be removed in a future release. You should plan to migrate to platform OAuth applications.
- Ansible Automation Platform: Platform OAuth applications provide an updated interface and are the standard for future use. You will move to these applications.

- Tokens:


- Automation controller: Automation controller personal access tokens (PATs) are deprecated. You will move to platform gateway PATs.
- Ansible Automation Platform: Platform tokens provide an updated interface and are the standard for future use. You will move to these tokens.

- Authenticator configurations:


- Ansible Automation Platform 2.4 to Ansible Automation Platform 2.6: The migration of all authenticator configurations from the automation controller to the platform gateway is automated. This includes third-party authentication configurations and sensitive data such as SAML private keys or OAuth secret keys. If you use custom LDAP certificates, you must manually migrate them.

- Ansible Automation Platform 2.5 to Ansible Automation Platform 2.6: Authenticator configurations are not automatically migrated. LDAP settings configured in Ansible Automation Platform 2.5 remain as they were after upgrading to 2.6.



What RBAC (platform gateway and/or automation controller) control permissions will be missing in version 2.6?

- **For 2.4 to 2.6 upgrades:** During the upgrade, authenticators and their mappings from the controller are imported into the gateway; therefore, you don’t need to manually migrate authenticators.

- **For 2.5 to 2.6 upgrades:** Authenticators and their mappings in the platform gateway continue to function as is, because no changes are imported.



Which version of PostgreSQL does Ansible Automation Platform 2.6 support?
Ansible Automation Platform 2.6 supports PostgreSQL 15 for its managed databases and additionally supports PostgreSQL 15, 16, and 17 for external databases.

