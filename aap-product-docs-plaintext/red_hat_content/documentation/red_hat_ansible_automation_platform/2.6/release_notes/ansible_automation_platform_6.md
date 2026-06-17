# 9. Patch releases
## 9.6. Ansible Automation Platform patch release December 10, 2025
### 9.6.3. Ansible Automation Platform

#### 9.6.3.1. Features

- Ansible Automation Platform now provides support for IPv6 single-stack and dual-stack (IPv4 and IPv6) deployments in Red Hat OpenShift Container Platform, and RPM-based environments. Support for container-based environments will be introduced in a future patch release. To enable IPv6 in Ansible Automation Platform, set the `FEATURE_GATEWAY_IPV6_USAGE_ENABLED` feature flag to True. For more information about using feature flags, see [How to set feature flags for Red Hat Ansible Automation Platform](https://access.redhat.com/articles/7109282).(ANSTRAT-1575)

**Availability to deploy and configure Ansible MCP servers**

- Organization administrators can now deploy an Ansible Model Context Protocol (MCP) server on an Operator-based or containerized installation of Ansible Automation Platform 2.6. This functionality is available as a Technology Preview release.

- Model Context Protocol (MCP) is an open standard that enables AI models to use external AI tools and services via a unified interface.

- The following are the key capabilities:


- Using the Ansible MCP server, you can connect your Ansible Automation Platform with your preferred external AI tool (such as Claude, Cursor, or ChatGPT). The AI tools can access key information about your Ansible Automation Platform environment and perform tasks.
- Ansible users can query information, execute workflows, and perform automation tasks using natural language prompts directly within their preferred AI tool.

Note

Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview).

For more information about deploying the Ansible MCP server, see [Deploying an Ansible MCP server on Ansible Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/deploying-ansible-mcp-server). (ANSTRAT-1567)

#### 9.6.3.2. Enhancements

- Fixed an issue with missing Ansible Automation Platform 2.6 repositories for Red Hat Enterprise Linux 10, which previously prevented the successful build of devtools RPMs. This resulted in devtools failing to mirror Ansible Automation Platform 2.6 on Red Hat Enterprise Linux 10. With this release, we have built the devtools RPMs for Red Hat Enterprise Linux 10 on a dedicated channel which are now accessible to users.(AAP-53866)

#### 9.6.3.3. Bug Fixes

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

- Fixed an issue where there was a **404** error message on a validated repo sync on private automation hub.


- Introduces an **Options** section for the checkboxes **Signed collections only** and **Sync all dependencies**.
- Adds an info message about syncing dependencies outside the repository.(AAP-36592)

- Fixed an issue where there was an inconsistency in the task timestamps between the **Overview** and **Detail** views.(AAP-36588)

- Fixed an issue where an unchecked SSL verification caused `ImagePullBackOff` errors. This caused failed job launches due to SSL certificate verification issues. With this release, SSL certificate verification is bypassed for **Container Registry** type credentials.(AAP-33889)

- Fixed an issue where users were encountering an issue with `extra-vars` `number_list` containing more than 21 digits in non-quoted integer format, experiencing a UI display problem. Previously, the user interface incorrectly converted long numbers to scientific notation, making input difficult.(AAP-31805)

#### 9.6.3.4. Deprecated

- The following endpoints have been deprecated for Ansible Automation Platform, MCP, and MVP in the OpenAPI Specifications;


- `UserViewSet` and `DeprecatedRelatedUserViewSet` are deprecated.
- `UserTeamViewSet` and `UserOrganizationViewSet` are deprecated.
- `authenticators` and `authenticator_uid` fields are deprecated in `UserSerializer`.(AAP-58322)

