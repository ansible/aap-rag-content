+++
title = "Plan your upgrade to Ansible Automation Platform 2.6 - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-con_aap_upgrade_overview"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-con_aap_upgrade_overview/", "Plan your upgrade to Ansible Automation Platform 2.6"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-con_aap_upgrade_overview/aem-page/upgrade-con_aap_upgrade_overview.html"
last_crumb = "Plan your upgrade to Ansible Automation Platform 2.6"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Plan your upgrade to Ansible Automation Platform 2.6"
oversized = "false"
page_slug = "upgrade-con_aap_upgrade_overview"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/upgrade-con_aap_upgrade_overview"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/upgrade-con_aap_upgrade_overview/toc/toc.json"
type = "aem-page"
+++

# Plan your upgrade to Ansible Automation Platform 2.6

Ansible Automation Platform 2.6 includes changes that improve the overall platform upgrade experience.

-  **Upgrading from 2.5 to 2.6**
-  **Upgrading from 2.4 to 2.6**


Note:

You must be on the latest version of 2.4 or 2.5 before you upgrade to 2.6.

Upgrading from 2.5 to 2.6
Upgrading from 2.5 to 2.6 does not involve changes to the platform infrastructure requirements, architecture, or services. The improvements described in the 2.4 to 2.6 upgrade path are also present in the 2.5 to 2.6 upgrade path; however, the platform gateway service is already in place in 2.5.

Additionally, note the following:

- If you upgraded from 2.4 to 2.5, you must migrate your authentication methods and users before upgrading to 2.6 as that legacy authenticator functionality was removed.
- When you upgrade to 2.6, the system removes any users that the 2.4 to 2.5 upgrade did not fully migrate. The users that have previously merged their user records while on 2.5 will remain to function as is for 2.6.
- Upgrading to 2.6 prevents 2.4 automation controller users who never successfully logged into 2.5 from logging into the platform-gateway. These users retain backwards compatibility for direct Automation Execution access but cannot access the full platform. Ensure all users planning to use 2.6 have successfully logged into 2.5 before upgrading.
- Unified RBAC management across Ansible Automation Platform components: All Ansible Automation Platform collections, which support the Configuration-as-Code (CaC) approach, now use a standard global environment variable name and module variable name across Ansible Automation Platform components. For more details, see the **Release notes** for whats new around RBAC in 2.6, what’s changed around RBAC for users moving from 2.5 to 2.6

For more information about upgrading, see the upgrade document for your deployment type:

- Containerized
- RPM
- OpenShift Container Platform
  Note:
      Upgrades from the latest 2.5 version to 2.6 are supported with all deployment types: RPM, containerized, and OpenShift Container Platform deployments.

Upgrading from 2.4 to 2.6
Note the following when upgrading from 2.4 to 2.6:

- **Upgrades from 2.4**: Ansible Automation Platform supports upgrading directly from the latest 2.4 version to 2.6. Directly upgrading to 2.6 is the recommended upgrade path from 2.4, as several improvements in 2.6 simplify and improve the upgrade experience. Note:
      You can upgrade directly from the latest 2.4 version to 2.6 with RPM and OpenShift Container Platform deployments. However, upgrading Event-Driven Ansible 2.4 or from the 2.4 containerized deployment is not supported, as both features were Tech Preview in 2.4.

     For more information, see the upgrade document for your deployment type. Either RPM, or OpenShift Container Platform.

- **Infrastructure changes**: Ansible Automation Platform RPM deployments require additional infrastructure compared with 2.4, due to the addition of the platform gateway service. Infrastructure needs vary depending on factors such as whether you implement a growth or an enterprise deployment.

- **Authentication changes**: Enterprise authentication configuration and mappings (for example, SAML, LDAP, OIDC) move from automation controller 2.4 to platform gateway 2.6 as part of the upgrade process. You do not need to manually reconfigure these authentication methods after you upgrade. See **Access management and authentication** for information about authentication options in general.

  Note:
      Authentication upgrade improvements apply to RPM and OpenShift Container Platform deployments. Upgrades from the 2.4 containerized deployment Tech Preview release are not supported. Additionally, upgrading Event-Driven Ansible 2.4 is not supported.

- **Identify access management changes**: All automation controller Identity Access Management (IAM) data moves from automation controller 2.4 to the platform gateway in 2.6 as part of the upgrade process. With automation controller 2.4 as the default source of IAM data for the platform gateway in 2.6, users retain their memberships and are assigned appropriate platform-level roles in 2.6. As part of the upgrade process:

  * Users, teams, organizations, their memberships, and common roles in 2.4 move from automation controller 2.4 to the platform gateway in 2.6.

  * Administrators in automation controller 2.4 become platform gateway administrators in 2.6.

  * Controller admins in 2.4 become platform gateway admins in 2.6. The more organizations, teams, and users being migrated during an upgrade, the longer the upgrade takes. As an example, upgrading and migrating 4,000 users, 400 teams, and 40 organizations can take close to two hours.

    Note:
            Identity access management changes apply to RPM and OpenShift Container Platform deployments. Upgrades from the 2.4 containerized deployment Tech Preview release are not supported.

         See **Identity access management data movement** for more information.

- **API changes**: Some APIs are being deprecated in 2.6. See **API changes in Ansible Automation Platform 2.6** for more information.

- **Unified RBAC management across Ansible Automation Platform components**: All Ansible Automation Platform collections, which support the Configuration-as-Code (CaC) approach, now use a standard global environment variable name and module variable name across Ansible Automation Platform components. For more details, see the **Release notes** for what’s new around RBAC in 2.6, or what’s changed around RBAC for users moving from 2.5 to 2.6

## FAQs on upgrading to 2.6

Find concise answers to frequently asked questions about upgrading your system to quickly troubleshoot common issues and plan your migration effectively.

What are the supported installation topologies and operating systems for Ansible Automation Platform 2.6?
Red Hat has adopted a more definitive approach to installation topologies, categorizing them as "growth" or "enterprise" for production-ready setups:

- Growth topology: is intended for organizations that are getting started with Ansible Automation Platform and do not require redundancy or higher compute for large volumes of automation.
- Enterprise topology: is intended for organizations that require Ansible Automation Platform to be deployed with redundancy or higher compute for large volumes of automation.


For more information, see **Tested deployment models**.

Why did my authentication settings that were present in automation controller 2.4 not get imported?
If an authentication method is missing in Ansible Automation Platform 2.6, review the setup_log for migration warnings. These warnings indicate the reason authentication settings were not successfully created during the upgrade to version 2.6.

Why did my upgrade from Ansible Automation Platform 2.4 to 2.6 fail or encounter an error during the SAML authenticator migration?
A SAML authenticator migration fails if the configuration has an encrypted private key. While automation controller in Ansible Automation Platform 2.4 allowed input of an encrypted private key without error, Ansible Automation Platform 2.6 does not support this feature for authenticators and prevents the migration of any SAML configuration containing one.

To prevent migration failure and service disruption for SSO users, you must:

- **Before upgrading**: Replace the encrypted private key with an unencrypted one in the SAML authenticator settings on your Ansible Automation Platform 2.4 environment.
- **If the upgrade already failed**: Platform gateway did not migrate the authenticator. A local administrator must manually re-create the SAML authenticator in the new Ansible Automation Platform 2.6 environment to restore SSO functionality.

Which Red Hat Enterprise Linux versions are supported for RPM and containerized installations?
RPM installations will continue to be supported exclusively on Red Hat Enterprise Linux 9. Containerized installations support both Red Hat Enterprise Linux 9.6 or later versions of Red Hat Enterprise Linux 9 and Red Hat Enterprise Linux 10 or later versions of Red Hat Enterprise Linux 10 for enterprise topologies.

What is the difference between "upgrade" and "migration" in Ansible Automation Platform 2.6?
An upgrade is an application action, such as updating Ansible Automation Platform 2.5 to 2.6. A migration involves moving data, such as from an RPM-based 2.6 installation to a container-based 2.6 installation. New service components are not explicitly required between versions 2.5 and 2.6.

Can I upgrade from 2.4 to 2.6 or must I upgrade to 2.5 first?
Yes you can upgrade directly to 2.6. However note that there might be new system requirements you must update before upgrading.

How will managed cloud customers be upgraded to Ansible Automation Platform 2.6?
All managed cloud customers on Microsoft Azure and Amazon Web Services will be upgraded to 2.6. Two upgrade window options will be available following the platform upgrade: non-production or production environments. Communications will be ongoing from mid-July until late September.

Will migrations be fully supported in Ansible Automation Platform 2.6?
Yes, migrations are fully supported, enabling customers to move from RPM installations to containerized or OpenShift Container Platform environments, or to the managed offering. Customers must be on the latest version of Ansible Automation Platform for their current installation before migrating. The installation program manages new components introduced in version 2.5 for direct 2.4 to 2.6 upgrades.

When upgrading from 2.4 to 2.6 (applies only to RPM or OpenShift Container Platform), what is different about the upgrade process compared with the 2.4 to 2.5 process?
See the **Overview of upgrade improvements** section.

I’m using Event-Driven Ansible in 2.4, can I upgrade Event-Driven Ansible to 2.6?
If you are using Ansible Automation Platform 2.4 with the technical preview of Event-Driven Ansible controller but want to upgrade to the Ansible Automation Platform 2.6 with Event-Driven Ansible, you must install a new instance of Ansible Automation Platform 2.6 and manually re-create your Event-Driven Ansible configurations in the new, fully integrated environment.

Will my existing 2.4 or 2.5 OAuth Applications/Tokens, Credentials/Customer Credentials, and Personal Access Tokens still work after upgrading to 2.6?
For upgrades from Ansible Automation Platform 2.4 or 2.5 to Ansible Automation Platform 2.6, some manual configuration is required:

- OAuth applications:
  * Automation controller: You can view and edit existing automation controller applications, but you cannot create new ones. They still function, but they might be removed in a future release. You should plan to migrate to platform OAuth applications.
  * Ansible Automation Platform: Platform OAuth applications provide an updated interface and are the standard for future use. You will move to these applications.
- Tokens:
  * Automation controller: Automation controller personal access tokens (PATs) are deprecated. You will move to platform gateway PATs.
  * Ansible Automation Platform: Platform tokens provide an updated interface and are the standard for future use. You will move to these tokens.
- Authenticator configurations:
  * Ansible Automation Platform 2.4 to Ansible Automation Platform 2.6: The migration of all authenticator configurations from the automation controller to the platform gateway is automated. This includes third-party authentication configurations and sensitive data such as SAML private keys or OAuth secret keys. If you use custom LDAP certificates, you must manually migrate them.
  * Ansible Automation Platform 2.5 to Ansible Automation Platform 2.6: Authenticator configurations are not automatically migrated. LDAP settings configured in Ansible Automation Platform 2.5 remain as they were after upgrading to 2.6.

What RBAC (platform gateway and/or automation controller) control permissions will be missing in version 2.6?
- **For 2.4 to 2.6 upgrades:** During the upgrade, authenticators and their mappings from the controller are imported into the gateway; therefore, you don’t need to manually migrate authenticators.
- **For 2.5 to 2.6 upgrades:** Authenticators and their mappings in the platform gateway continue to function as is, because no changes are imported.

Which version of PostgreSQL does Ansible Automation Platform 2.6 support?
Ansible Automation Platform 2.6 supports PostgreSQL 15 for its managed databases and additionally supports PostgreSQL 15, 16, and 17 for external databases.
