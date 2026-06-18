# Ansible Automation Platform patch release December 10, 2025

The following release notes detail the updates for the Ansible Automation Platform patch released on December 10, 2025.

This release includes the following components and versions:

| Release Date          | Component versions                                                                                                                                                                                                                                                                                                                                             |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>December 10, 2025 | Automation controller 4.7.6Automation hub 4.11.4Event-Driven Ansible 1.2.3Container-based installer Ansible Automation Platform (bundle) 2.6-4Container-based installer Ansible Automation Platform (online) 2.6-4Receptor 1.6.2RPM-based installer Ansible Automation Platform (bundle) 2.6-3.1RPM-based installer Ansible Automation Platform (online) 2.6-3 |


CSV Versions in this release:

- namespace: aap-operator.v2.6.0-0.1764966733
- cluster: aap-operator.v2.6.0-0.1764966767

## General

**Stakeholder Notification: Ansible Lightspeed Release 2.6 Sign-Off Issue**
We are writing to inform you of an issue discovered during the final sign-off process for the Ansible Lightspeed 2.6 release that impacts a subset of customers.

Issue Description
Ansible Lightspeed customers who deploy using the Red Hat OpenShift Container Platform (RHOCP) installer will encounter a specific error when attempting to use the Chatbot feature to retrieve information about Ansible Automation Platform. This manifests as a **403 Forbidden error**.

A similar issue also affects customers who utilize the **containerized installer** with the **Enterprise topology**. Crucially, this issue **does not affect** customers using the containerized installer with the **Growth or All-in-One topology**.

Root Cause and Impact
The 403 error is caused by a Cross-Site Request Forgery (CSRF) protection mechanism not correctly recognizing the origin of the Chatbot’s request in the affected deployment configurations. This prevents the Chatbot from functioning as intended for these specific customer segments.

Workaround
We have identified a viable workaround that can be implemented by affected customers immediately:

Customers must edit their `AnsibleAutomationPlatform` kind value in the configuration to include a new `extra_setting` variable and wait for redeployment.

| Setting Name                | Value                                             | Action Required                                                                                          |
| --------------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| <br> `CSRF_TRUSTED_ORIGINS` | <br> `<Ansible Automation Platform Gateway FQDN>` | <br>Modify the `AnsibleAutomationPlatform` kind value and then wait for the changes to become effective. |


Example:

```python
kind: AnsibleAutomationPlatform
spec:
lightspeed:
extra_settings:
- setting: CSRF_TRUSTED_ORIGINS
value: 'https://gateway-onprem-signoff-26.apps.aap-test2.w6n5.p1.openshiftapps.com'
```


Note:

The `<Ansible Automation Platform Gateway FQDN>` should be replaced with the customer’s actual Fully Qualified Domain Name for the platform gateway.

Next Steps
Our engineering team is prioritizing a permanent fix for this issue, which will be included in a forthcoming patch release. We will provide updates on the timeline for the fix shortly.

Please disseminate this information to your relevant customer-facing and support teams so they can proactively assist customers encountering this issue with the provided workaround.

Thank you for your understanding and continued support.

## CVE

With this update, the following CVEs have been addressed:

- [CVE-2025-64459](https://access.redhat.com/security/cve/cve-2025-64459)`ansible-automation-platform-26/gateway-rhel9`: Django SQL injection.(AAP-58110)
- [CVE-2025-64459](https://access.redhat.com/security/cve/cve-2025-64459)`automation-controller`: Django SQL injection.(AAP-58117)
- [CVE-2025-64459](https://access.redhat.com/security/cve/cve-2025-64459)`ansible-automation-platform-26/controller-rhel9`: Django SQL injection.(AAP-58104)
- [CVE-2025-62727](https://access.redhat.com/security/cve/cve-2025-62727)`ansible-automation-platform-26/mcp-tools-rhel9`: Starlette DoS via Range header merging.(AAP-57017)
- [CVE-2025-62727](https://access.redhat.com/security/cve/cve-2025-62727)`ansible-automation-platform-26/lightspeed-chatbot-rhel9`: Starlette DoS via Range header merging.(AAP-57011)
- [CVE-2025-64459](https://access.redhat.com/security/cve/cve-2025-64459)`ansible-automation-platform-26/lightspeed-rhel9`: Django SQL injection.(AAP-58112)
- [CVE-2025-64459](https://access.redhat.com/security/cve/cve-2025-64459)`python3.11-django`: Django SQL injection.

## Ansible Automation Platform

Features
- Ansible Automation Platform now provides support for IPv6 single-stack and dual-stack (IPv4 and IPv6) deployments in Red Hat OpenShift Container Platform, and RPM-based environments. Support for container-based environments will be introduced in a future patch release. To enable IPv6 in Ansible Automation Platform, set the `FEATURE_GATEWAY_IPV6_USAGE_ENABLED` feature flag to True. For more information about using feature flags, see [How to set feature flags for Red Hat Ansible Automation Platform](https://access.redhat.com/articles/7109282).(ANSTRAT-1575)

**Availability to deploy and configure Ansible MCP servers**

- Organization administrators can now deploy an Ansible Model Context Protocol (MCP) server on an Operator-based or containerized installation of Ansible Automation Platform 2.6. This functionality is available as a Technology Preview release.
- Model Context Protocol (MCP) is an open standard that enables AI models to use external AI tools and services via a unified interface.
- The following are the key capabilities:
* Using the Ansible MCP server, you can connect your Ansible Automation Platform with your preferred external AI tool (such as Claude, Cursor, or ChatGPT). The AI tools can access key information about your Ansible Automation Platform environment and perform tasks.
* Ansible users can query information, execute workflows, and perform automation tasks using natural language prompts directly within their preferred AI tool.


Note:

Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview).

For more information about deploying the Ansible MCP server, see [Deploy the MCP server on Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server#deploying-ansible-mcp-server "As an organization administrator, you can deploy the Model Context Protocol (MCP) server for Red Hat Ansible Automation Platform on an operator-based installation or container-based installation of Ansible Automation Platform."). (ANSTRAT-1567)

Enhancements
- Fixed an issue with missing Ansible Automation Platform 2.6 repositories for Red Hat Enterprise Linux 10, which previously prevented the successful build of devtools RPMs. This resulted in devtools failing to mirror Ansible Automation Platform 2.6 on Red Hat Enterprise Linux 10. With this release, we have built the devtools RPMs for Red Hat Enterprise Linux 10 on a dedicated channel which are now accessible to users.(AAP-53866)

Bug Fixes
- Fixed an issue where the python build dependencies wheel files were stored in container images.(AAP-59254)
- Fixed an issue where the job template did not remain editable after the associated project was deleted.(AAP-58467)
- Fixed a server error that could happen when assigning permissions via the `/api/eda/` or `/api/controller/` endpoints.(AAP-58622)
- Fixed an issue where the job template did not remain editable after the associated project was deleted.(AAP-58467)
- Fixed an issue where the project status update link on the job details page was broken.(AAP-57215)
- Fixed an issue where the brand logo was missing in the **About** page when accessing it from the **Overview** page.(AAP-57133)
- Fixed an issue where the **Resource Type** filter in the **Roles** page did not correctly filter by resource types like Credential, Project, and Execution Environment, that are found in both Automation Execution and Automation Decisions.(AAP-56691)
- Fixed an issue where the **Launched by** field appeared blank in the UI when the project update is triggered automatically, such as through **Update revision on launch** or other automated conditions.(AAP-56643)
- Fixed an issue where the playbook select dropdown did not automatically select a playbook if there was only one in the project.(AAP-56279)
- Fixed an issue where the source control **Branch** option was missing from the Inventory source.(AAP-56149)
- Fixed an issue where the Azure AD name was inconsistently called **Azuread** in the user interface. This has been corrected to **Azure AD**.(AAP-55677)
- Fixed an issue where the OpenAPI specification for the platform gateway REST API was not providing comprehensive documentation and detailed request/response schemas.(AAP-53643)
- Fixed an issue where the edit form for a survey would not display in the UI if the survey was created without a default value using the ansible.controller collection.(AAP-51548)
- Fixed an issue where the text on **Remotes** and **Remote Registries** pages was not accurate.(AAP-49838)
- Fixed an issue where the source control branch for the **Project Sync Job Details** was missing.(AAP-49450)
- Fixed an issue where the collection hyperlink was broken in card view in private automation hub.(AAP-49006)
- Fixed an issue where the **Search** function failed to narrow results when adding host to group.(AAP-47510)
- Fixed an issue where the custom login text had poor legibility and did not allow for HTML markup such as links.(AAP-47462)
- Fixed an issue where the filtering by host name did not work as expected in the **Add Existing Host** dialog.(AAP-45534)
- Fixed an issue where the email notification URL for the workflow job template displayed a blank page.(AAP-43796)
- Fixed an issue where creating a new template from **Project** or **Inventory** did not auto-populate the Project field.(AAP-41725)
- Fixed an issue where the **Permission Denied** message on the templates tab, when the user has permission, was misleading. Updated the messaging when job template creation is not available: Job template creation requires project access and the user is not currently assigned to any projects.(AAP-40800)
- Fixed an issue where the repository URL in the **Details** page was incorrect.(AAP-40160)
- Fixed a survey validation issue where the minimum length value of a question could be set to greater than the maximum length value.(AAP-39932)
- Fixed a survey validation issue where text was being treated as a number when evaluating its length.(AAP-39931)
- Fixed an issue where the user was unable to create a schedule for **Constructed inventory** synchronization. The **Create Schedule** UI no longer presents the option to select a constructed inventory when the resource type is Inventory source.(AAP-38660)
- Fixed an issue where the survey answers were not being saved when editing or creating a schedule.(AAP-37923)
- Fixed an issue where the instance groups on a schedule could not be edited.(AAP-37872)
- Fixed an issue where there was a **404** error message on a validated repo sync on private automation hub.   * Introduces an **Options** section for the checkboxes **Signed collections only** and **Sync all dependencies**.
* Adds an info message about syncing dependencies outside the repository.(AAP-36592)
- Fixed an issue where there was an inconsistency in the task timestamps between the **Overview** and **Detail** views.(AAP-36588)
- Fixed an issue where an unchecked SSL verification caused `ImagePullBackOff` errors. This caused failed job launches due to SSL certificate verification issues. With this release, SSL certificate verification is bypassed for **Container Registry** type credentials.(AAP-33889)
- Fixed an issue where users were encountering an issue with `extra-vars``number_list` containing more than 21 digits in non-quoted integer format, experiencing a UI display problem. Previously, the user interface incorrectly converted long numbers to scientific notation, making input difficult.(AAP-31805)

Deprecated
- The following endpoints have been deprecated for Ansible Automation Platform, MCP, and MVP in the OpenAPI Specifications;
* `UserViewSet` and `DeprecatedRelatedUserViewSet` are deprecated.
* `UserTeamViewSet` and `UserOrganizationViewSet` are deprecated.
* `authenticators` and `authenticator_uid` fields are deprecated in `UserSerializer`.(AAP-58322)

## Ansible Automation Platform Operator

Enhancements
- Event-Driven Ansible event-stream mTLS configuration has been added to the installer.(AAP-58343)
- Added `spec_overrides` field to the restore CR spec:
* Added support for overriding Controller-specific settings via `spec_overrides.controller`.
* Added support for overriding automation hub specific settings via `spec_overrides.hub`.
* Added support for overriding Event-Driven Ansible specific settings via `spec_overrides.eda`.
* Added support for overriding database-specific settings via `spec_overrides.database`.(AAP-60024)

Bug Fixes
- Fixed an issue with object storage secrets that were not included in the Automation Hub backup.(AAP-59610)
- Fixed the conditional failure for `AnsibleWorkflow` job launch when using the `AnsibleWorkflow` CR in Ansible Automation Platform 2.6.(AAP-59106)
- Fixed an issue where there was an OpenShift Container Platform resource runner python library dependency missing from the container image.(AAP-59032)
- Fixed a server error that could happen when assigning permissions via the `/api/eda/` or `/api/controller/` endpoints.(AAP-58622)

## Automation controller

Features
- Receptor collection version bumped to 2.0.8, which is compatible with Red Hat Enterprise Linux 10.(AAP-58421)
- Added `x-ai-description` to controller schema to provide AI friendly description of each endpoint.(AAP-59819)

Bug Fixes
- Fixed an issue where project update failed with no output, and project deletions failed. Automation controller now uses the force flag when syncing a project which has **Allow branch override** enabled.(AAP-58533)
- In this update, users attempting to install a software package on an unsupported architecture may encounter issues due to incorrect data in reminders. This has been resolved.(AAP-59728)
- Fixed an issue where the project update failed with no output and project deletions also failed.(AAP-58533)
- Fixed an issue where the OpenAPI specification for the Automation controller was incomplete, impeding MCP server integration development. This limited the seamless MCP server integration with the Ansible Automation Platform. The Automation controller’s REST API is now complete and accessible.(AAP-53640)

## Automation hub

Bug Fixes
- Fixed an issue with Automation hub authentication failure for users with the **Team Admin** role:
* Users assigned the **Team Admin** role can now successfully authenticate to Automation hub. Previously, these users would receive a **401** error when accessing Automation hub API endpoints due to an incompatibility between the **Team Admin** role and Automation hub’s internal permission system.(AAP-58898)
- Fixed an issue where the password field on the Automation hub Django REST framework authentication page was missing the autocomplete attribute. As a consequence, the field did not align with security best practices regarding browser autofill. With this update, the password field uses the `autocomplete="new-password"` attribute. As a result, the Automation hub API authentication page complies with recommended security settings.(AAP-59910)
- Previously, upgrades from Ansible Automation Platform 2.5 to 2.6 failed when API access logging was enabled. This occurred due to an incorrect import path in the galaxy-ng package. This release corrects the import path.(AAP-59886)

## Container-based Ansible Automation Platform

Enhancements
- Configured podman PID limits, `sysctls` for `inotify` and kernel keys, and ulimit `nofile` for user running Ansible Automation Platform service containers based on system resources.(AAP-59438)

Bug Fixes
- Fixed an issue where after uninstall/re-install of receptor jobs were unable to start due to stale exited containers with the same name were still present.(AAP-59609)

## Event-Driven Ansible

Enhancements
- Added concise descriptions to API endpoints for Ansible Automation Platform MCP MVP endpoints (`x-ai-description`).(AAP-58431)

Bug Fixes
- Fixed an issue where the OpenAPI specification for Event-Driven Ansible was not offering comprehensive documentation and detailed request/response schemas. Previously, developers integrating with Event-Driven Ansible via the MCP server had to manually explore APIs and format API calls without proper guidance, which impeded seamless integration. With this release, the OpenAPI specification for the Event-Driven Ansible REST API is now complete and well-documented. This enhancement enables seamless integration with the MCP server using Event-Driven Ansible.(AAP-53642)

## Lightspeed

Technical Preview
- This developer preview introduces support for Ansible MCP Servers.(AAP-57303)
- This new feature enables users to access the Ansible Automation Platform 2.6 API directly from AI tools like Claude Code.(AAP-57217)

Features
Added the new Ansible Automation Platform MCP Server to the 2.6 stream.(AAP-58863)

Bug Fixes
- Fixed an issue of Ansible Automation Platform Multi-Channel Platform (MCP) servers crashing due to incomplete Epic and System Design Plan (SDP) creation, leading to unclear work requirements. As a result, the Ansible Automation Platform MCP Servers have created the System Design Plan and related tasks, addressing ANSTRAT-1567. This enhancement improves the efficiency of feature development for end users by completing the Ansible Automation Platform MCP Servers system design plan in an active manner.(AAP-53087)

## Receptor

Features
- Receptor collection version bumped to 2.0.8, which supports Red Hat Enterprise Linux 10 mesh nodes.(AAP-57987)

Bug Fixes
- Fixed an issue where the receptor-collection was not up to date with Automation hub standards. There is now an up to date Changelog included in receptor-collection.(AAP-58434)
