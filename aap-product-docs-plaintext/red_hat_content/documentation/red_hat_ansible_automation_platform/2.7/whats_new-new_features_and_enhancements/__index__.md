# New features and enhancements

The following release notes detail the new features and enhancements for the Ansible Automation Platform general availability release on June 3, 2026.

## Automation portal Red Hat Enterprise Linux appliance

Ansible automation portal is now available as a pre-built RHEL 9 virtual machine appliance. The appliance packages automation portal as a QCOW2 or VMDK disk image that you deploy on your existing virtualization infrastructure.

- Key capabilities include:
* Multi-platform deployment: Deploy on RHEL with KVM, Red Hat OpenShift Virtualization, or VMware vSphere.
* Automated first-boot configuration: Provide SSH keys and AAP OAuth credentials in a cloud-init user-data file. The appliance configures itself on first boot with no manual steps.
* Atomic upgrades and rollback: Built on RHEL 9 image mode (bootc). Upgrade the appliance atomically while preserving configuration and data, and roll back to the previous version if needed.


For more information, see the Ansible automation portal documentation.

## Automation portal self-service enhancements

**Role-based access control**: Automation portal now supports RBAC-based navigation menus. Administrators can control which users can access Templates, History, execution environment definitions, collections, Git repositories, and synchronization actions. Configure permitted roles in the portal administration section.

**GitHub Apps authentication**: Configure GitHub Apps as an authentication method for source control integration, in addition to personal access tokens. GitHub Apps provide fine-grained repository permissions and higher API rate limits.

**Disconnected environment support**: Additional disconnected environment support for registries and self-signed certificates.

**Job template filtering**: Use the excludeLabels Helm chart setting to filter which job templates are visible in automation portal. Templates with matching labels are excluded from the catalog.

## General availability of execution environment builder

Execution environment (EE) builder in Ansible automation portal is now generally available. Use the web UI to define execution environments (collections, Python and system packages, custom build steps), push definitions to Git source control, and build images with GitHub Actions.

- Key capabilities in this release include:
* **Guided wizard**: Step through presets or a blank definition. AAP administrators can publish custom wizards for other teams.
* **Collections**: Pull from private automation hub or Git and browse the configured catalog.
* **Packages and build steps**: Add Python and system packages by entry or file upload and inject custom steps at build phases.
* **Git export**: Push EE definitions to GitHub or GitLab.
* **GitHub builds**: Trigger image builds from connected GitHub repositories.
* **Portable definitions**: Download a `.tar` without committing to Git, or import a template from a URL for reuse.
* **Catalogs**: Search and filter EE definitions and collections with parsed content, metadata, dependencies, and source links.


For more information, see *Using execution environment builder* in the Ansible automation portal documentation.

## Installation and Upgrades

- Only containerized and operator supported installation methods (RPM install method removed)
* NOTE: Ansible Development Tools will continue to be available via RPM
- Must be on AAP 2.6 to upgrade to 2.7. Therefore, any AAP 2.4 or 2.5 installs must first upgrade to AAP 2.6 prior to upgrading to AAP 2.7.
- Migrating from one installation method to another must occur on the same AAP version.
- Removal of direct external routes/ingress in automation controller, EDA and AutomationHub API

## The MCP server for Red Hat Ansible Automation Platform

- The MCP server has moved from technical preview to general availability.
- Extending Red Hat maintained content use cases via the MCP plugin.
- Adding the ability to include MCP servers into Execution Environments.
- Deliver reference examples (AWS, Azure, GitHub) as Dev Preview, unsupported samples demonstrating integration patterns.
- [Knowledgebase for running the AAP MCP Server as a standalone container](https://access.redhat.com/articles/7139698).

## AIOps integrations

- Solution Guides for integrating Ansible Automation Platform with IBM Instana, ServiceNow and Splunk

## Automation coding assistant

- Added support for RHEL AI hosted models, no longer requiring WatsonX

## Automation intelligent assistant

- BYOK (bring-your-own-knowledge) to automation intelligent assistant RAG pipeline
* Customers can inject their own documentation into the automation intelligent assistant RAG pipeline
* The intelligent assistant can now reference a 2nd RAG image/repo when producing answers to the end-user
* The BYOK RAG image is the highest priority data to utilize as context, where the Ansible-documentation-based RAG image is the second priority data.
* The BYOK RAG image is built outside of the AAP deployment (build tool supports text and markdown files)
* Admins can manage BYOK images over time (update, replace, or remove)

## Security and Compliance

- Added support for AAP OpenID Connect provider configuration endpoints (OIDC) for sharing identity to 3rd party systems, eliminating the need for static service accounts during playbook execution.   * Added concept of “workload identities” for playbook generated access. (Tech Preview)
* AAP as an OIDC Authentication Provider for HashiCorp Vault. (Tech Preview)
* Added general support for “user identity” with OIDC well-known configuration.

## Removal of direct API access to platform components

- External/third-party authentication providers removed in automation controller, Automation Hub.
- Disabling of basic authentication and personal access tokens for automation controller, Automation Hub, and EDA.
- New CLI utility (aap-detect-direct-component-access) for identifying legacy direct-API usage/scripts (containerized and operator only).

## Accessibility

- Unified UI meets Web Content Accessibility Guidelines (WCAG) 2.2.
- Usability Enhancements
- Enable or disable feature flags directly from the user interface during runtime (no longer only at installation).

## Usability Enhancements

- Enable or disable feature flags directly from the user interface during runtime (no longer only at installation).

## Developer Experience

- Content discovery and catalog to support EE-Builder.
- Added support for Google Vertex in the VS Code Ansible plugin.
- Added support for RHEL AI in the VS Code Ansible plugin.
- Provide a single, searchable view of Ansible collections aggregated from multiple sources.
- Enable automated creation of the Execution Environment image eliminating the need for manual build configuration or command-line execution.
- Supportability upgrade from Tech Preview to GA for Ansible Workspace image for Red Hat OpenShift Dev Spaces.

## Ansible plug-ins for Red Hat Developer Hub

New features and enhancements

- **OCI-based plug-in delivery**: Ansible plug-ins for Red Hat Developer Hub are now delivered as OCI artifacts from `registry.redhat.io`. Red Hat Developer Hub pulls plug-ins directly from the container registry during startup. This replaces the HTTP plug-in registry method as the primary installation path.
- **Red Hat Developer Hub 1.9** compatibility: Plug-in installation and configuration validated against Red Hat Developer Hub 1.9. Documentation references updated to RHDH 1.9.

## Ansible Automation Dashboard (Tech Preview)

- Integration with Ansible Automation Platform native experience (off by default), Separate utility continues to exist.
- Part of Metrics Service database for simplified deployment, running on 6-hour schedule.

## Self-service automation

- Added support for deployment on RHEL by providing appliance-based (VMDK and QCOW2) installation.
- The OpenShift Helm chart now supports installing the Ansible plugins directly from registry.redhat.io as OCI images, improving the current installation experience.
- Configurable "Support" link in the global header bar. Defaults to <https://access.redhat.com/support>. Customers override it to point to their own support portal (e.g. ServiceNow, internal help desk).
- Playbook authors can use ansible.builtin.debug messages to communicate results directly to self-service users (URLs, guidance, etc) displayed in the self-service portal template log output.
- AAP Job Template sync filtering now supports excludeLabels, allowing admins to exclude specific AAP Job Templates from being available in the automation portal using Ansible Automation Platform labels without needing to curate an explicit inclusion list.

## Scalability, Reliability, and Resilience

- More reliable Ansible rulebook executions: Ensure previous events persist if required by the Event-driven Ansible rule engine.
- Automating re-syncing of an automation controller project after a rulebook update in a git repository.

## Event-Driven Ansible (Automation decisions)

- Event-Driven Ansible includes several key enhancements in the Ansible Automation Platform 2.7 release that improve performance, simplify operations, and expand the platform’s capabilities across security, networking, and event processing.

## Highlighted Content Collections

- hashicorp.vault
* Supports Vault KV secret lookups and is compatible with AAP’s existing Vault credential plugin workflows.
* The collection includes content for managing Vault policies, authentication methods, dynamic secrets (e.g., database, cloud), and PKI workflows.
* Enterprise Vault features such as namespaces and multi-tenant configurations are supported and documented.
* Event-Driven Ansible can trigger rulebook workflows based on Vault events via webhook or polling mechanisms.
* Migration documentation is available to help users transition from `community.hashi_vault` to `hashicorp.vault` with minimal disruption.
* Solution guides and examples are published for common Vault use cases, including dynamic credentials, short-lived SSH keys, and secure application integration.
- microsoft.mecm
* Brand New Certified Collection: Officially launched as a Red Hat Certified Collection (v1.0.0) with 26 new modules acting as a bridge between Ansible and Microsoft Endpoint Configuration Manager.
* Patch Management & Zero-Downtime: Features granular modules like software_update_group, software_update_deployment, and install_updates to orchestrate zero-downtime Windows Server patching.
* Client Management: Added a client_action module to trigger immediate actions on client devices (e.g., forcing machine policy retrievals) without waiting for standard polling cycles.
* Health Status Retrieval: Features several info modules (dp_status_info, wsus_sync_status_info) to verify MECM infrastructure health before kicking off deployments.
- microsoft.scom
* New Certified Release: Reached v1.0.1 as a newly certified collection.
* SCOM Infrastructure Management: Provides a suite of modules for automating Microsoft System Center Operations Manager infrastructure.
* Event-Driven Hooks: Designed to route SCOM alerts (via webhooks or event streams) into Event-Driven Ansible for automated remediations to Windows Server alerts.

## Execution environment updates

- Ee-minimal
* Removed `ansible-lint`. If your infrastructure depends on
* , migrate to the Ansible Automation Platform Development Tools container.
* Removed :latest: convention for ee-minimal images. Users now need to identify the specific image and version to download.
- Ee-supported
* Removed `ansible-lint`. If your infrastructure depends on `ansible-lint`, migrate to the Ansible Automation Platform Development Tools container.
* Added microsoft.mecm and microsoft.hyperv collections.
* Updated existing collections to the most recent compatible versions.
* Removed the cloud.common, cloud.terraform, redhat.csp_download , redhat.rhv, and trendmicro.deepsec collections.
* Removed the junipernetworks-junos collection. Use the juniper.device collection instead.

## Event-Driven Ansible ansible.eda and ansible-rulebook changes

- New ansible-rulebook built-in modules The following event sources and event filters will be available as built-in modules in 'ansible-rulebook', and removed from 'ansible.collection'.


The following is the list of new built-in modules:

'eda.builtin.dashes_to_underscores'(filter) 'eda.builtin.generic'(source) 'eda.builtin.insert_hosts_to_meta'(filter) 'eda.builtin.json_filter'(filter) 'eda.builtin.normalize_keys'(filter) 'eda.builtin.pg_listener'(source) 'eda.builtin.range'(source) 'eda.builtin.webhook'(source)

For backwards compatibility, these plugins remain available in the ansible.eda namespace and are automatically mapped to eda.builtin. However, they are no longer actively maintained in the ansible.eda collection. If you currently have rulebooks that use these filters or sources, update your rulebooks to use the eda.builtin namespace instead of the ansible.eda namespace.

AWS and Azure event sources movement to the cloud collections The following list of event sources is being deprecated in ansible.eda collection and moving to the corresponding certified cloud collections. The DE-supported decision environments have been updated to incorporate amazon.aws and azure.azcollection. If you update the DE-supported decision environment, make sure to update your ansible-rulebooks namespace to refer to the updated namespace as mentioned below:

'ansible.eda.aws_cloudtrail to amazon.aws.aws_cloudtrail' 'ansible.eda.aws_sqs_queue to amazon.aws.aws_sqs_queue' 'ansible.eda.azure_service_bus' 'azure.azcollection.azure_service_bus'

## Event sources transitioning from ansible.eda to community.eda

The following list of event sources is being removed from the certified ansible.eda collection, will not be supported by Red Hat engineering, but they will have community maintenance, and are available as part of the community.eda collection. If you are using any of these filters, make sure to update your ansible-rulebooks to use the community.eda namespace, and you will need a custom decision environment in order to keep running your rulebooks.

You can also keep your existing rulebooks with an older version of DE-supported or DE-minimal, while you update your rulebooks.

'ansible.eda.file to community.eda.file' 'ansible.eda.file_watch to community.eda.file_watch' 'ansible.eda.journald to community.eda.journald' 'ansible.eda.tick to use either eda.builtin.generic or eda.builtin.range' 'ansible.eda.url_check to community.eda.url_check'

## Bring-Your-Own-Knowledge with the Ansible Lightspeed intelligent assistant

Ansible Lightspeed intelligent assistant uses retrieval-augmented generation (RAG) to provide contextual answers grounded in Red Hat Ansible Automation Platform (AAP) documentation. With the upcoming Bring Your Own Knowledge (BYOK) capability, administrators can extend the intelligent assistant’s knowledge by adding their organization’s own documentation, such as internal AAP policies, operational procedures, and best practices, into the RAG pipeline. When users ask the intelligent assistant a question, responses are informed by both the organization’s custom content and Red Hat’s AAP documentation, with organizational content taking priority when relevant.

BYOK is designed for both OpenShift Operator and containerized installer deployments of Ansible Automation Platform. Administrators build a custom knowledge image externally using provided tooling, import it into their AAP environment, and configure the intelligent assistant to use it. The image can be updated or replaced over time as organizational documentation evolves.
