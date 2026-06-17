+++
template = "docs/aem-title.html"
title = "New features and enhancements - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-aap_26"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-platform_intro/", "Release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-aap_26/aem-page/whats_new-aap_26.html"
last_crumb = "New features and enhancements"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "New features and enhancements"
oversized = "false"
page_slug = "whats_new-aap_26"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-aap_26"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-aap_26/toc/toc.json"
type = "aem-page"
+++

# New features and enhancements

Review the new features and enhancements in Red Hat Ansible Automation Platform 2.6 to maximize your automation capabilities. This release introduces the Ansible Lightspeed intelligent assistant, the Ansible automation portal, and unified role-based access control.

## General availability of Ansible Lightspeed intelligent assistant

The Ansible Lightspeed intelligent assistant is now generally available on Ansible Automation Platform 2.6 on OpenShift Container Platform. It is an intuitive chat interface embedded within the Ansible Automation Platform, utilizing generative artificial intelligence (AI) to answer questions about the Ansible Automation Platform.

The chat experience in the Ansible Lightspeed intelligent assistant interacts with users in their natural language prompts in English, and uses large language models (LLMs) to generate quick, accurate, and personalized responses. These responses empower users to work more efficiently, thereby improving productivity and the overall quality of their work.

To access and install Ansible Lightspeed intelligent assistant, you will need the following:

- Ansible Automation Platform 2.6 on OpenShift Container Platform
- An LLM service that is hosted on either Red Hat Enterprise Linux AI or Red Hat OpenShift AI


For more information, see [Deploying the Ansible Lightspeed intelligent assistant on OpenShift Container Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.6/extend-assembly_deploying_alia#deploying-chatbot-operator "As a system administrator, you can deploy the automation intelligent assistant on Ansible Automation Platform on OpenShift Container Platform.") in Installing on OpenShift Container Platform.

## General availability of Ansible automation portal

Ansible automation portal is now generally available as part of the Ansible Automation Platform subscription. The new Ansible automation portal empowers platform admins to provide a streamlined “point-and-click” Ansible automation experience to a broader set of users within the organization. Users who are not Ansible experts now have a dedicated self-service portal from which they can launch a range of automation jobs.

- Installation: Deployment of Ansible automation portal requires Red Hat OpenShift Container Platform using a Helm chart. A future deployment of Ansible automation portal on Red Hat Enterprise Linux 10 is planned for Technology Preview in a future asynchronous release of Ansible Automation Platform 2.6.
- Synchronizes existing automation content: Extend the reach and impact of your automation job templates, while maintaining full control and compliance.
- Seamless Integration: Uses your existing Ansible Automation Platform configuration—same logins, same security controls, same automation logic.
- Simplified Interface: A distinct, user-friendly web interface designed for business users, not automation experts.
- Guided Workflows: Step-by-step forms that walk users through automation requests without technical complexity - automatically generated from your existing job templates.
- Smart Forms: Real-time field validation, conditional and dynamic forms, and dropdown fields for Ansible Automation Platform artifacts, such as Ansible Automation Platform inventories.

## General availability of Ansible automation dashboard

Automation dashboard is now generally available as part of the Ansible Automation Platform subscription. Automation dashboard is a utility you can connect to one or more Ansible Automation Platform deployments to visualize automation usage data, determine time savings, track ROI, and drive increased visibility into automation strategy, resource allocation, and prioritization of automation projects. Benefits include:

- Installation: Deployment of automation dashboard is via containerized installation only.
- Secure on-premise deployment: Simplified deployment as a self-contained, on-premise utility that runs on a dedicated RHEL 9 x86 and ARM host.
- Easy Integration: Integrates into Ansible Automation Platform 2.4, 2.5 and 2.6 instances with OAuth2 token for read-only access to pull data.
- Automated data sync: Once configured, the dashboard automatically syncs and visualizes data from connected Ansible Automation Platform instances.
- Flexible Reporting: Dashboard allows to generate and share customized PDF reports and export raw CSV data for flexible ingestion into BI tools.


For more information, see [Using automation dashboard](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_view_key_metrics#assembly-view-key-metrics "By effectively using automation dashboard, you can gain valuable insights into your Ansible Automation Platform usage and drive continuous improvement in your automation practices.").

## Configuration as Code

The [ansible.platform](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/platform/) collection now provides unified, platform-wide Role-Based Access Control (RBAC) management across Ansible Automation Platform components. New or enhanced modules include `Organization`, `Team`, `User`, `Role definitions`, `Role Assignments` (team/user). Additionally:

- You can declare the RBAC state as code and apply idempotently across services.
- Ansible collections now use a standard global environment variable prefix across components. Automation controller, Automation hub, and Event-Driven Ansible all use a new standard of “AAP_” instead of "COMPONENT_". For example, `aap_hostname`. See [the documentation](https://console.redhat.com/ansible/automation-hub/collections/published/ansible/platform/documentation/) in Automation hub for more information.

## Service accounts

- Service accounts, created in [console.redhat.com](https://console.redhat.com/), can now be used to manage subscriptions in Ansible Automation Platform. Manifest files and basic authentication may still be used for this purpose as well.
- Service accounts are now required in order to send data to automation analytics.

## Event-Driven Ansible (Automation decisions)

Event-Driven Ansible includes several key enhancements in the Ansible Automation Platform 2.6 release that improve performance, simplify operations, and expand the platform’s capabilities across security, networking, and event processing.

- **External secret management**: Event-Driven Ansible now supports external secret management systems, achieving parity with Automation controller. This includes support for HashiCorp Vault, CyberArk, Microsoft Azure Key Vault, and AWS Secrets Manager.
- **Editable project URLs**: You can now edit the source control URL for existing Event-Driven Ansible projects, providing greater flexibility to adapt to repository changes.
- **Improved job auditing**: A new label is automatically added to jobs triggered by Event-Driven Ansible, along with support for custom labels. This allows for more efficient tracing and auditing of event-triggered automations.
- **Kafka enhancements**: The Kafka source plugin now supports multiple topics and allows the use of regular expressions and wildcards. Additionally, it now supports GSSAPI for enhanced authentication.
- **New event filter**: A new filter plugin, `event_splitter`, is available to handle and process nested events more effectively.
- **Rulebook concurrency key**: Rulebooks now support a concurrency key, enabling you to group events by resource to ensure they are processed sequentially.

## Installation updates

Containerized installation
Updated system requirements for containerized installation of Ansible Automation Platform include:

- The Red Hat Enterprise Linux 9.2 operating system requirement was updated to 9.4 or later minor versions of Red Hat Enterprise Linux 9. Red Hat Enterprise Linux 10 system requirements are unchanged.
- PostgreSQL 15, 16, and 17 are now supported for customer provided (external) databases. Note:
      External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15.

For more information see [System requirements](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-ref_cont_aap_system_requirements "Use this information when planning your installation of containerized Ansible Automation Platform.") in *Containerized installation*.

Operator installation
Updated system requirements for Ansible Automation Platform Operator on Red Hat OpenShift Container Platform include:

- The Red Hat Enterprise Linux 9.2 operating system requirement was updated to 9.4 or later minor versions of Red Hat Enterprise Linux 9. Red Hat Enterprise Linux 10 system requirements are unchanged.
- PostgreSQL 16 and 17 are now supported for customer-provided (external) databases.


Note:

External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15.

For more information about the Ansible Automation Platform Operator system requirements, see [Choose a deployment method and topology](/documentation/en-us/red_hat_ansible_automation_platform/2.6/../plan/assembly-overview-tested-deployment-models.dita).

RPM installation
Updated system requirements for RPM installation of Ansible Automation Platform 2.6 include:

- Ansible Automation Platform RPM installer was deprecated in 2.5 and will be removed in Ansible Automation Platform 2.7. The RPM installer will be supported for RHEL 9 during the lifecycle of Ansible Automation Platform 2.6 to support migrations to existing supported topologies. See the [support matrix](/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_upgrade_support_matrix "Use these reference tables to find the supported upgrade paths for your Ansible Automation Platform deployment. Review Red Hat Enterprise Linux version compatibility and step-by-step processes for RPM, container, and OpenShift Container Platform deployment types.") for more information on upgrade and migration paths.
- Red Hat Enterprise Linux 9.2 operating system requirement was updated to 9.4 or later minor versions of Red Hat Enterprise Linux 9. Red Hat Enterprise Linux 8 is no longer supported.
- Red Hat Enterprise Linux 10 is not supported for RPM installations. See [support matrix](/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_upgrade_support_matrix "Use these reference tables to find the supported upgrade paths for your Ansible Automation Platform deployment. Review Red Hat Enterprise Linux version compatibility and step-by-step processes for RPM, container, and OpenShift Container Platform deployment types.") for more information on supported upgrade and migration paths.
- PostgreSQL 16 and 17 are now supported for customer-provided (external) databases. Note:
      External databases using PostgreSQL 16 or 17 must rely on external backup and restore processes. Backup and restore functionality is dependent on utilities provided with PostgreSQL 15.

For more information, see [System requirements](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_system_requirements#platform-system-requirements "Use this information when planning your Red Hat Ansible Automation Platform installations and designing automation mesh topologies that fit your use case.") in *RPM installation*.

## Upgrade paths

The following table outlines the supported upgrade paths for Ansible Automation Platform 2.6.

Note:

The RPM-based upgrade paths are deprecated and will be removed in Ansible Automation Platform 2.7.

| Starting Deployment                                                   | Upgrade Deployment           |
| --------------------------------------------------------------------- | ---------------------------- |
| <br>2.4 RPM single automation controller node                         | <br>2.6 RPM growth           |
| <br>2.4 RPM single node automation controller and automation hub      | <br>2.6 RPM growth           |
| <br>2.4 RPM multi node automation controller                          | <br>2.6 RPM enterprise       |
| <br>2.4 RPM multi node automation controller and automation hub       | <br>2.6 RPM enterprise       |
| <br>2.5 RPM growth                                                    | <br>2.6 RPM growth           |
| <br>2.5 RPM enterprise                                                | <br>2.6 RPM enterprise       |
| <br>2.5 Container growth                                              | <br>2.6 Container growth     |
| <br>2.5 Container enterprise                                          | <br>2.6 Container enterprise |
| <br>2.4 Operator single automation controller node                    | <br>2.6 Operator growth      |
| <br>2.4 Operator single node automation controller and automation hub | <br>2.6 Operator growth      |
| <br>2.4 Operator multi node automation controller                     | <br>2.6 Operator enterprise  |
| <br>2.4 Operator multi node automation controller and automation hub  | <br>2.6 Operator enterprise  |
| <br>2.5 Operator growth                                               | <br>2.6 Operator growth      |
| <br>2.5 Operator enterprise                                           | <br>2.6 Operator enterprise  |

## Migration paths

The following table outlines the supported migration paths for Ansible Automation Platform 2.6. Migration involves transitioning between deployment types, such as from an RPM to a containerized installation. This process is exclusively supported between identical versions (for example, 2.6 to 2.6).

| Source environment                              | Target environment                              |
| ----------------------------------------------- | ----------------------------------------------- |
| <br>RPM-based Ansible Automation Platform       | <br>Container-based Ansible Automation Platform |
| <br>RPM-based Ansible Automation Platform       | <br>OpenShift Container Platform                |
| <br>RPM-based Ansible Automation Platform       | <br>Managed Ansible Automation Platform         |
| <br>Container-based Ansible Automation Platform | <br>OpenShift Container Platform                |
| <br>Container-based Ansible Automation Platform | <br>Managed Ansible Automation Platform         |

## Overview of upgrade improvements

Changes in 2.6 improve the overall upgrade experience, as detailed in the following sections:

-  [Upgrading from 2.5 to 2.6](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-aap_26#new-features__from-2.5)
-  [Upgrading from 2.4 to 2.6](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-aap_26#new-features__from-2.4)


Note:

You must be on the latest version of 2.4 or 2.5 before you upgrade to 2.6.

Upgrading from 2.5 to 2.6
Upgrading from 2.5 to 2.6 does not involve changes to the platform infrastructure requirements, architecture, or services. The improvements described in the 2.4 to 2.6 upgrade path are also present in the 2.5 to 2.6 upgrade path; however, the platform gateway service is already in place in 2.5.

Additionally, note the following:

- If you upgraded from 2.4 to 2.5, you must migrate your authentication methods and users before upgrading to 2.6 as that legacy authenticator functionality was removed.
- When you upgrade to 2.6, the system removes any users that the 2.4 to 2.5 upgrade did not fully migrate. The users that have previously merged their user records while on 2.5 will remain to function as is for 2.6.
- Upgrading to 2.6 prevents 2.4 automation controller users who never successfully logged into 2.5 from logging into the platform-gateway. These users retain backwards compatibility for direct Automation Execution access but cannot access the full platform. Ensure all users planning to leverage 2.6 have successfully logged into 2.5 prior to upgrading.
- Unified RBAC management across Ansible Automation Platform components: All Ansible Automation Platform collections, which support the Configuration-as-Code (CaC) approach, now use a standard global environment variable name and module variable name across Ansible Automation Platform components. For more details, see [What’s new around RBAC in 2.6](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-platform_intro "Ansible Automation Platform unifies comprehensive automation capabilities, a robust ecosystem, and flexible deployment options into one strategic solution. It enables customers to automate and orchestrate workflows across domains for efficient, resilient, and consistent IT operations at scale."), [What’s changed around RBAC for users moving from 2.5 to 2.6](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-platform_intro "Ansible Automation Platform unifies comprehensive automation capabilities, a robust ecosystem, and flexible deployment options into one strategic solution. It enables customers to automate and orchestrate workflows across domains for efficient, resilient, and consistent IT operations at scale."), and [`ansible.platform`](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/platform/) documentation in automation hub.

For more information about upgrading, see the upgrade document for your deployment type:

-  [Containerized](/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-con_upgrade_infrastructure_container_deployments#upgrade-infrastructure-container-deployments "Container-based deployments require specific infrastructure changes during upgrade.")
-  [RPM](/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-con_upgrade_infrastructure_rpm_deployments "The following sections describe the tested infrastructure changes for RPM-based deployments.")
-  [OpenShift Container Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-con_upgrade_infrastructure_operator_deployments "Tested infrastructure changes are available for Operator-based deployments. To perform an upgrade, see Upgrading Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform.")
  Note:
      Upgrades from the latest 2.5 version to 2.6 are supported with all deployment types: RPM, containerized, and OpenShift Container Platform deployments.

Upgrading from 2.4 to 2.6
Note the following when upgrading from 2.4 to 2.6:

- **Upgrades from 2.4**: Ansible Automation Platform supports upgrading directly from the latest 2.4 version to 2.6. Directly upgrading to 2.6 is the recommended upgrade path from 2.4, as a number of improvements in 2.6 simplify and improve the upgrade experience. Note:
      You can upgrade directly from the latest 2.4 version to 2.6 with RPM and OpenShift Container Platform deployments. However, upgrading Event-Driven Ansible 2.4 or from the 2.4 containerized deployment is not supported, as both features were Tech Preview in 2.4.

     For more information, see the upgrade document for your deployment type. Either [RPM](/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-ref_upgrade_scenarios_rpm "Find the supported upgrade paths for your RPM-based Ansible Automation Platform deployment. This helps you plan the necessary steps for a smooth upgrade."), or [OpenShift Container Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-ref_upgrade_scenarios_openshift "Find the supported upgrade paths for Ansible Automation Platform deployments that use OpenShift Container Platform. This helps you plan the necessary steps for a smooth upgrade.").

- **Infrastructure changes**: Ansible Automation Platform RPM deployments require additional infrastructure compared with 2.4, due to the addition of the platform gateway service. Infrastructure needs vary depending on factors such as whether you implement a growth or an enterprise deployment. For details about infrastructure and inventory file changes in various upgrade scenarios, see [Infrastructure changes for RPM deployments](/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-con_upgrade_infrastructure_rpm_deployments "The following sections describe the tested infrastructure changes for RPM-based deployments.").

- **Authentication changes**: Enterprise authentication configuration and mappings, including SAML, LDAP, and OIDC, automatically move from automation controller 2.4 to platform gateway 2.6 during the upgrade. Although these settings migrate automatically within Ansible Automation Platform, you must update the callback URLs in your external Identity Provider (IdP) settings to point to platform gateway. For more information, see [Authentication provider migration behavior](/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_upgrade_authentication_movement_2_4_to_2_6#upgrade-authentication-movement-2.4-to-2.6 "During an upgrade from a version of Ansible Automation Platform that predates the platform gateway, only complete authentication provider configurations are migrated to the platform gateway."). See [Access management and authentication](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_configure_authentication "Configure authentication methods such as LDAP or SAML to simplify the user login experience. Providing the correct connection details for your chosen identity provider helps ensure seamless and secure access to Ansible Automation Platform.") for information about authentication options in general.

  Note:
      Authentication upgrade improvements apply to RPM and OpenShift Container Platform deployments. Upgrades from the 2.4 containerized deployment Tech Preview release are not supported. Additionally, upgrading Event-Driven Ansible 2.4 is not supported.

- **Identify access management changes**: All automation controller Identity Access Management (IAM) data moves from automation controller 2.4 to the platform gateway in 2.6 as part of the upgrade process. With automation controller 2.4 as the default source of IAM data for the platform gateway in 2.6, users retain their memberships and are assigned appropriate platform-level roles in 2.6. As part of the upgrade process:

  * Users, teams, organizations, their memberships, and common roles in 2.4 move from automation controller 2.4 to the platform gateway in 2.6.

  * Administrators in automation controller 2.4 become platform gateway administrators in 2.6.

  * Controller admins in 2.4 become platform gateway admins in 2.6. The more organizations, teams, and users being migrated during an upgrade, the longer the upgrade takes. As an example, upgrading and migrating 4,000 users, 400 teams, and 40 organizations may take close to two hours.

    Note:
            Identity access management changes apply to RPM and OpenShift Container Platform deployments. Upgrades from the 2.4 containerized deployment Tech Preview release are not supported.

         See [Data movement during upgrade to 2.6](/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_upgrade_data_movement "When upgrading from a version of Ansible Automation Platform that predates the platform gateway, Identity Access Management (IAM) data, including users, teams, organizations, their memberships, and associated roles, is migrated from automation controller and automation hub to platform gateway.") for more information.

- **API changes**: Some APIs are being deprecated in 2.6. See [API changes](/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_upgrade_api_changes#upgrade-api-changes "Ansible Automation Platform uses a platform gateway that provides centralized API access to all services. While APIs for automation controller, automation hub, and Event-Driven Ansible remain accessible directly for backward compatibility, this direct access will be removed in a future release.") for more information.

- **Unified RBAC management across Ansible Automation Platform components**: All Ansible Automation Platform collections, which support the Configuration-as-Code (CaC) approach, now use a standard global environment variable name and module variable name across Ansible Automation Platform components. For more details, see [What’s new around RBAC in 2.6](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-platform_intro "Ansible Automation Platform unifies comprehensive automation capabilities, a robust ecosystem, and flexible deployment options into one strategic solution. It enables customers to automate and orchestrate workflows across domains for efficient, resilient, and consistent IT operations at scale."), [What’s changed around RBAC for users moving from 2.5 to 2.6](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-platform_intro "Ansible Automation Platform unifies comprehensive automation capabilities, a robust ecosystem, and flexible deployment options into one strategic solution. It enables customers to automate and orchestrate workflows across domains for efficient, resilient, and consistent IT operations at scale."), and [`ansible.platform`](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/platform/) documentation in automation hub.

## Platform UI

Ansible Automation Platform 2.6 was delivered with the goal to simplify the UI, improve the relationship between user interface elements, and maintain the association between users, organizations, teams, and roles.

Within the Platform UI, the role based access controls (RBAC) have been centralized to give administrators control of users across the entire platform. The centralized RBAC has introduced additional APIs and expanded the scope of those APIs to allow the assignment of roles across any of the platform resources. The details of these changes are reflected within the [API changes](/documentation/en-us/red_hat_ansible_automation_platform/2.6/upgrade-assembly_upgrade_api_changes#upgrade-api-changes "Ansible Automation Platform uses a platform gateway that provides centralized API access to all services. While APIs for automation controller, automation hub, and Event-Driven Ansible remain accessible directly for backward compatibility, this direct access will be removed in a future release.").

The UI has also been updated to the latest version of Patternfly, which brings significant updates and refinements aiming to enhance user experience, performance, and developer efficiency.
