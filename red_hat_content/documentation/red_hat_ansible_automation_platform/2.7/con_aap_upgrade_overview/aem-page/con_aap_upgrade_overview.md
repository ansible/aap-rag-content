+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/con_aap_upgrade_overview"
template = "docs/aem-title.html"
title = "Plan your upgrade to Ansible Automation Platform 2.6 - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/con_aap_upgrade_overview/aem-page/con_aap_upgrade_overview.html"
last_crumb = "Plan your upgrade to Ansible Automation Platform 2.6"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Plan your upgrade to Ansible Automation Platform 2.6"
oversized = "false"
page_slug = "con_aap_upgrade_overview"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/con_aap_upgrade_overview"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/con_aap_upgrade_overview/toc/toc.json"
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
