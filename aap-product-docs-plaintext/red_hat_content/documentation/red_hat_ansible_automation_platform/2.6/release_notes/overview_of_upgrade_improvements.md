# 2. New features and enhancements
## 2.10. Overview of upgrade improvements




Changes in 2.6 improve the overall upgrade experience, as detailed in the following sections:

-  [Upgrading from 2.5 to 2.6](#from-2.5)
-  [Upgrading from 2.4 to 2.6](#from-2.4)


Note
You must be on the latest version of 2.4 or 2.5 before you upgrade to 2.6.



<span id="from-2.5"></span>For more information about upgrading, see the upgrade document for your deployment type:

-  [Containerized](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-infrastructure-changes#container_based_deployments)
-  [RPM](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-infrastructure-changes#rpm_based_deployments)
-  [OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-infrastructure-changes#operator_based_deployments)

Note
Upgrades from the latest 2.5 version to 2.6 are supported with all deployment types: RPM, containerized, and OpenShift Container Platform deployments.







<span id="from-2.4"></span>## 2.11. Platform UI




Ansible Automation Platform 2.6 was delivered with the goal to simplify the UI, improve the relationship between user interface elements, and maintain the association between users, organizations, teams, and roles.

Within the Platform UI, the role based access controls (RBAC) have been centralized to give administrators control of users across the entire platform. The centralized RBAC has introduced additional APIs and expanded the scope of those APIs to allow the assignment of roles across any of the platform resources. The details of these changes are reflected within the [API changes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/planning_your_upgrade/index#upgrade-api-changes) .

The UI has also been updated to the latest version of Patternfly, which brings significant updates and refinements aiming to enhance user experience, performance, and developer efficiency.

# Chapter 3. Technology preview




## 3.1. Technology Preview




### 3.1.1. Ansible Lightspeed intelligent assistant integration with MCP




Ansible Lightspeed intelligent assistant integration with the Model Context Protocol (MCP) server is now available as a Technology Preview release. This integration enhances the user experience by delivering relevant, dynamically sourced data results to your queries. For information about how to access and use the Ansible Lightspeed intelligent assistant, see [Deploying the Ansible Lightspeed intelligent assistant on OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/installing_on_openshift_container_platform/deploying-chatbot-operator) .

### 3.1.2. Ansible development workspaces




A supported Ansible development workspace container image is now available as a Technology Preview release. The container image is used with Red Hat OpenShift Dev Spaces to create an in-browser instance of VS Code with the Ansible extension installed, so that you can use Ansible development tools to develop automation content.

For information about installing and using Ansible dev spaces, see [Using Ansible development workspaces for automation content development](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_ansible_development_workspaces_for_automation_content_development) .

### 3.1.3. ansible-core 2.19




Note
Ansible Automation Platform 2.6 does not include ansible-core 2.19 by default, but it is compatible with 2.19. See [Red Hat Ansible Automation Platform Life Cycle](https://access.redhat.com/support/policy/updates/ansible-automation-platform) for more information about compatibility.



This [technical preview](https://access.redhat.com/articles/7128367) includes an overhaul of the templating system and a new feature labeled Data Tagging. These changes enable reporting of numerous problematic behaviors that went undetected in previous releases, with wide-ranging positive effects on security, performance, and user experience.

Backward compatibility has been preserved where practical, but some breaking changes were necessary. This guide describes some common problem scenarios with example content, error messages, and suggested solutions.

We recommend you test your playbooks and roles in a staging environment with this release to determine where you may need to make changes.

For further information see the [Ansible Porting Guide](https://ansible.readthedocs.io/projects/ansible-core/devel/porting_guides/porting_guide_core_2.19.html#id3) .

# Chapter 4. Deprecated features




Deprecated functionality is still included in Ansible Automation Platform and continues to be supported during this version’s support cycle. However, the functionality will be removed in a future release of Ansible Automation Platform and is not recommended for new deployments.

The following table provides information about features that were deprecated in Ansible Automation Platform 2.5:

| Component | Feature |
| --- | --- |
| Access to service APIs for automation controller,
automation hub,
and Event-Driven Ansible | With the addition of platform gateway, a number of service-specific API endpoints are deprecated because their functionality will be removed or superseded with other capabilities in a future release.

Ansible Automation Platform 2.5 and 2.6 expose API access to individual services (automation controller, private automation hub, Event-Driven Ansible) to maintain compatibility with existing REST API integrations. This access will be removed in a future release.

For detailed information, see [API changes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-api-changes) in _Planning your upgrade_ . |
| Installer | The Ansible Automation Platform installer using Red Hat Enterprise Linux RPMs was deprecated (announced) in 2.5 and will be removed in Ansible Automation Platform 2.7.

The RPM installer will be supported for Red Hat Enterprise Linux 9 during the lifecycle of Ansible Automation Platform 2.6 to support migrations to existing supported topologies. Users are encouraged to migrate to the containerized topology on Red Hat Enterprise Linux or to the OpenShift Container Platform Operator installation method. See the [support matrix](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/planning_your_upgrade/upgrade-support-matrix) for more information on upgrade and migration paths. |
| Ansible-core | ```
uri module:
- Using 'yes' or 'no' for 'follow_redirects' parameter is deprecated.
yum_repository:
- deprecated parameters:
- 'keepcache'
- 'async'
- "deltarpm_metadata_percentage"
- "gpgcakey"
- "http_caching"
- "keepalive"
- "metadata_expire_filter"
- "mirrorlist_expire"
- "protect"
- "ssl_check_cert_permissions"
- "ui_repoid_vars"`
url lookup:
- Using `yes` or `no` for `follow_redirects` parameter is deprecated.
``` |
| Execution environment | Removing `cisco.asa` from ee-supported as it is being deprecated

Removing `ibm.qradar` from ee-supported as it is being deprecated |
| Certified Collections | An `ansible.platform` collection is available as the preferred collection to replace the service-specific `ansible.controller` , `ansible.hub` , and `ansible.eda` collections. These service-specific collections will be replaced by `ansible.platform` after 2.6. |
| Ansible code bot code bot | The code bot (as described in the [Red Hat Ansible Lightspeed with IBM watsonx Code Assistant](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#using-code-bot-for-suggestions_lightspeed-user-guide) user guide) is being deprecated, and will be retired on December 31, 2025. |
| Ansible Content | Deprecation of the Notification Service for ServiceNow, which will not be supported on the ServiceNow Zurich and later releases. Support will end when the Yokohama release is end-of-life. |


# Chapter 5. Removed features




Removed features are those that were deprecated in earlier releases. They are now removed from the Ansible Automation Platform 2.5, and will no longer be supported.

| Component | Feature |
| --- | --- |
| Event-Driven Ansible controller | Removal of `max_running_activations setting in eda-controller` |
| Platform gateway | Legacy Authenticators that were added during an upgrade from 2.4 to 2.5 will no longer be present |


# Chapter 6. Changed features




Changed features are not deprecated and will continue to be supported until further notice.

The following table provides information about features that are changed in Ansible Automation Platform 2.6:

| Component | Feature |
| --- | --- |
| Platform gateway | The determination for matching to existing user records upon login has changed from previous versions. The new process leverages email address as the primary matching criteria for existing user accounts across multiple authentication methods. See [Access Management](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/index) for more details. Within 2.5, each authentication method would result in a user record being created regardless of the email matching from the different IdP sources. |
| Platform-operator,
Ansible Automation Platform Hub Operator | Added `postgres_extra_settings` to Ansible Automation Platform operators to apply PostgreSQL configuration file level changes to managed Postgres. |
| Platform-operator,
Event-Driven Ansible | Added `postgres_extra_settings` to Ansible Automation Platform operators to apply PostgreSQL configuration file level changes to managed Postgres. |
| Platform-operator,
gateway-operator | Added `postgres_extra_settings` to Ansible Automation Platform operators to apply PostgreSQL configuration file level changes to managed Postgres. |


# Chapter 7. Known issues




This section provides information about known issues in Ansible Automation Platform 2.6.

- For role based authentication mappings, the role list includes all roles within the platform. Only the role assignments of Org Admin, Org Member, Team Admin, Team Member, and Platform Auditor are supported at this time. The list will be limited to only those that can be applied at a platform level in a subsequent release.
- If you have an existing deployment of Red Hat Ansible Lightspeed on Ansible Automation Platform 2.5, upgrading to Ansible Automation Platform 2.6 will cause your Red Hat Ansible Lightspeed deployment to fail. To avoid this failure, do not upgrade to Ansible Automation Platform 2.6 until a forthcoming patch is released on October 22, 2025. However, new deployments of Red Hat Ansible Lightspeed will work correctly on Ansible Automation Platform 2.6.(AAP-54064)

For more information, see [Ansible Lightspeed upgrade fails when upgrading Ansible Automation Platform 2.5 to 2.6](https://access.redhat.com/articles/7132132) .


- Automation controller in Ansible Automation Platform 2.4 allowed customers to enter an encrypted private key in SAML configuration without raising an error. If request signing was not enabled in the authenticator and the SAML IdP, then the Ansible Automation Platform administrator would not know that encrypted keys were not supported. Encrypted keys not supported in Ansible Automation Platform 2.6 authenticators. The platform alerts users that encrypted keys are not supported. However, when upgrading from Ansible Automation Platform 2.4 to 2.6, customers must replace encrypted private keys with unencrypted private keys in their SAML authenticators to prevent migration errors for the authenticator to platform gateway. If you skip this step, the authenticator is not migrated as part of the upgrade. The SAML authenticator must then be recreated manually by a local administrator to re-enable authentication. This might delay SSO users from logging back into the platform after the upgrade.


# Chapter 8. Fixed issues




This section provides information about fixed issues in Ansible Automation Platform 2.6.

## 8.1. Ansible Automation Platform




Note
Ansible Automation Platform 2.6 also includes the fixes from the latest 2.5 patch release. For more information see [Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/release_notes/patch_releases#aap-25-20250923) patch release September 23, 2025.



Ansible Automation Platform

- The `    SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL` configuration parameter now functions as expected, allowing social auth logins to set the platform gateway username to the user’s email when enabled.(AAP-49736)


RPM-based Ansible Automation Platform

- Fixed an issue where installer managed CA certificates were discovered but not used by the installer.(AAP-53335)


# Chapter 9. Patch releases




Security, bug fixes, and enhancements for Ansible Automation Platform 2.6 are released as asynchronous erratas. All Ansible Automation Platform erratas are available on the [Download Red Hat Ansible Automation Platform](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software) page.

As a Red Hat Customer Portal user, you can enable errata notifications in the account settings for Red Hat Subscription Management (RHSM). When errata notifications are enabled, you receive notifications through email whenever new erratas relevant to your registered systems are released.

Note
Red Hat Customer Portal user accounts must have systems registered and consuming Ansible Automation Platform entitlements for Ansible Automation Platform errata notification emails to generate.



The patch releases section of the release notes will be updated over time to give notes on enhancements and bug fixes for patch releases of Ansible Automation Platform 2.6.

**Additional resources**

- For more information about asynchronous errata support in Ansible Automation Platform, see [Red Hat Ansible Automation Platform Life Cycle](https://access.redhat.com/support/policy/updates/ansible-automation-platform) .
- For information about Common Vulnerabilities and Exposures (CVEs), see [What is a CVE?](https://www.redhat.com/en/topics/security/what-is-cve) and [Red Hat CVE Database](https://access.redhat.com/security/security-updates/cve) .


## 9.1. Ansible Automation Platform patch release December 10, 2025




This release includes the following components and versions:

| Release Date | Component versions |
| --- | --- |
| December 10, 2025 | - Automation controller 4.7.6
- Automation hub 4.11.4
- Event-Driven Ansible 1.2.3
- Container-based installer Ansible Automation Platform (bundle) 2.6-4
- Container-based installer Ansible Automation Platform (online) 2.6-4
- Receptor 1.6.2
- RPM-based installer Ansible Automation Platform (bundle) 2.6-3.1
- RPM-based installer Ansible Automation Platform (online) 2.6-3 |


CSV Versions in this release:

- namespace: aap-operator.v2.6.0-0.1764966733
- cluster: aap-operator.v2.6.0-0.1764966767


### 9.1.1. General




#### 9.1.1.1. **Stakeholder Notification: Ansible Lightspeed Release 2.6 Sign-Off Issue**




We are writing to inform you of an issue discovered during the final sign-off process for the Ansible Lightspeed 2.6 release that impacts a subset of customers.

#### 9.1.1.2. Issue Description




Ansible Lightspeed customers who deploy using the Red Hat OpenShift Container Platform (OCP) installer will encounter a specific error when attempting to use the Chatbot feature to retrieve information about Ansible Automation Platform. This manifests as a **403 Forbidden error** .

A similar issue also affects customers who utilize the **containerized installer** with the **Enterprise topology** . Crucially, this issue **does not affect** customers using the containerized installer with the **Growth or All-in-One topology** .

#### 9.1.1.3. Root Cause and Impact




The 403 error is caused by a Cross-Site Request Forgery (CSRF) protection mechanism not correctly recognizing the origin of the Chatbot’s request in the affected deployment configurations. This prevents the Chatbot from functioning as intended for these specific customer segments.

#### 9.1.1.4. Workaround




We have identified a viable workaround that can be implemented by affected customers immediately:

Customers must edit their `AnsibleAutomationPlatform` kind value in the configuration to include a new `extra_setting` variable and wait for redeployment.

| Setting Name | Value | Action Required |
| --- | --- | --- |
|  `CSRF_TRUSTED_ORIGINS` |  `&lt;Ansible Automation Platform Gateway FQDN&gt;` | Modify the `AnsibleAutomationPlatform` kind value and then wait for the changes to become effective. |


Example:

```
kind: AnsibleAutomationPlatform
spec:
lightspeed:
extra_settings:
- setting: CSRF_TRUSTED_ORIGINS
value: 'https://gateway-onprem-signoff-26.apps.aap-test2.w6n5.p1.openshiftapps.com'
```

Note
The `&lt;Ansible Automation Platform Gateway FQDN&gt;` should be replaced with the customer’s actual Fully Qualified Domain Name for the platform gateway.



#### 9.1.1.5. Next Steps




Our engineering team is prioritizing a permanent fix for this issue, which will be included in a forthcoming patch release. We will provide updates on the timeline for the fix shortly.

Please disseminate this information to your relevant customer-facing and support teams so they can proactively assist customers encountering this issue with the provided workaround.

Thank you for your understanding and continued support.

### 9.1.2. CVE




With this update, the following CVEs have been addressed:

-  [CVE-2025-64459](https://access.redhat.com/security/cve/cve-2025-64459\)  `    ansible-automation-platform-26/gateway-rhel9` : Django SQL injection.(AAP-58110)
-  [CVE-2025-64459](https://access.redhat.com/security/cve/cve-2025-64459\)  `    automation-controller` : Django SQL injection.(AAP-58117)
-  [CVE-2025-64459](https://access.redhat.com/security/cve/cve-2025-64459\)  `    ansible-automation-platform-26/controller-rhel9` : Django SQL injection.(AAP-58104)
-  [CVE-2025-62727](https://access.redhat.com/security/cve/cve-2025-62727)  `    ansible-automation-platform-26/mcp-tools-rhel9` : Starlette DoS via Range header merging.(AAP-57017)
-  [CVE-2025-62727](https://access.redhat.com/security/cve/cve-2025-62727)  `    ansible-automation-platform-26/lightspeed-chatbot-rhel9` : Starlette DoS via Range header merging.(AAP-57011)
-  [CVE-2025-64459](https://access.redhat.com/security/cve/cve-2025-64459)  `    ansible-automation-platform-26/lightspeed-rhel9` : Django SQL injection.(AAP-58112)
-  [CVE-2025-64459](https://access.redhat.com/security/cve/cve-2025-64459)  `    python3.11-django` : Django SQL injection.


### 9.1.3. Ansible Automation Platform




#### 9.1.3.1. Features




- Ansible Automation Platform now provides support for IPv6 single-stack and dual-stack (IPv4 and IPv6) deployments in Red Hat OpenShift Container Platform, and RPM-based environments. Support for container-based environments will be introduced in a future patch release. To enable IPv6 in Ansible Automation Platform, set the `    FEATURE_GATEWAY_IPV6_USAGE_ENABLED` feature flag to True. For more information about using feature flags, see [How to set feature flags for Red Hat Ansible Automation Platform](https://access.redhat.com/articles/7109282) .(ANSTRAT-1575)


**Availability to deploy and configure Ansible MCP servers**

- Organization administrators can now deploy an Ansible Model Context Protocol (MCP) server on an Operator-based or containerized installation of Ansible Automation Platform 2.6. This functionality is available as a Technology Preview release.
- Model Context Protocol (MCP) is an open standard that enables AI models to use external AI tools and services via a unified interface.
- The following are the key capabilities:


- Using the Ansible MCP server, you can connect your Ansible Automation Platform with your preferred external AI tool (such as Claude, Cursor, or ChatGPT). The AI tools can access key information about your Ansible Automation Platform environment and perform tasks.
- Ansible users can query information, execute workflows, and perform automation tasks using natural language prompts directly within their preferred AI tool.



Note
Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview) .

For more information about deploying the Ansible MCP server, see [Deploying an Ansible MCP server on Ansible Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/deploying-ansible-mcp-server) . (ANSTRAT-1567)



#### 9.1.3.2. Enhancements




- Fixed an issue with missing Ansible Automation Platform 2.6 repositories for Red Hat Enterprise Linux 10, which previously prevented the successful build of devtools RPMs. This resulted in devtools failing to mirror Ansible Automation Platform 2.6 on Red Hat Enterprise Linux 10. With this release, we have built the devtools RPMs for Red Hat Enterprise Linux 10 on a dedicated channel which are now accessible to users.(AAP-53866)


#### 9.1.3.3. Bug Fixes




- Fixed an issue where the python build dependencies wheel files were stored in container images.(AAP-59254)
- Fixed an issue where the job template did not remain editable after the associated project was deleted.(AAP-58467)
- Fixed a server error that could happen when assigning permissions via the `    /api/eda/` or `    /api/controller/` endpoints.(AAP-58622)
- Fixed an issue where the job template did not remain editable after the associated project was deleted.(AAP-58467)
- Fixed an issue where the project status update link on the job details page was broken.(AAP-57215)
- Fixed an issue where the brand logo was missing in the **About** page when accessing it from the **Overview** page.(AAP-57133)
- Fixed an issue where the **Resource Type** filter in the **Roles** page did not correctly filter by resource types like Credential, Project, and Execution Environment, that are found in both Automation Execution and Automation Decisions.(AAP-56691)
- Fixed an issue where the **Launched by** field appeared blank in the UI when the project update is triggered automatically, such as through **Update revision on launch** or other automated conditions.(AAP-56643)
- Fixed an issue where the playbook select dropdown did not automatically select a playbook if there was only one in the project.(AAP-56279)
- Fixed an issue where the source control **Branch** option was missing from the Inventory source.(AAP-56149)
- Fixed an issue where the Azure AD name was inconsistently called **Azuread** in the user interface. This has been corrected to **Azure AD** .(AAP-55677)
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


- Introduces an **Options** section for the checkboxes **Signed collections only** and **Sync all dependencies** .
- Adds an info message about syncing dependencies outside the repository.(AAP-36592)

- Fixed an issue where there was an inconsistency in the task timestamps between the **Overview** and **Detail** views.(AAP-36588)
- Fixed an issue where an unchecked SSL verification caused `    ImagePullBackOff` errors. This caused failed job launches due to SSL certificate verification issues. With this release, SSL certificate verification is bypassed for **Container Registry** type credentials.(AAP-33889)
- Fixed an issue where users were encountering an issue with `    extra-vars`  `    number_list` containing more than 21 digits in non-quoted integer format, experiencing a UI display problem. Previously, the user interface incorrectly converted long numbers to scientific notation, making input difficult.(AAP-31805)


#### 9.1.3.4. Deprecated




- The following endpoints have been deprecated for Ansible Automation Platform, MCP, and MVP in the OpenAPI Specifications;


-  `        UserViewSet` and `        DeprecatedRelatedUserViewSet` are deprecated.
-  `        UserTeamViewSet` and `        UserOrganizationViewSet` are deprecated.
-  `        authenticators` and `        authenticator_uid` fields are deprecated in `        UserSerializer` .(AAP-58322)



### 9.1.4. Ansible Automation Platform Operator




#### 9.1.4.1. Enhancements




- Event-Driven Ansible event-stream mTLS configuration has been added to the installer.(AAP-58343)
- Added `    spec_overrides` field to the restore CR spec:


- Added support for overriding Controller-specific settings via `        spec_overrides.controller` .
- Added support for overriding automation hub specific settings via `        spec_overrides.hub` .
- Added support for overriding Event-Driven Ansible specific settings via `        spec_overrides.eda` .
- Added support for overriding database-specific settings via `        spec_overrides.database` .(AAP-60024)



#### 9.1.4.2. Bug Fixes




- Fixed an issue with object storage secrets that were not included in the Automation Hub backup.(AAP-59610)
- Fixed the conditional failure for `    AnsibleWorkflow` job launch when using the `    AnsibleWorkflow` CR in Ansible Automation Platform 2.6.(AAP-59106)
- Fixed an issue where there was an OpenShift Container Platform resource runner python library dependency missing from the container image.(AAP-59032)
- Fixed a server error that could happen when assigning permissions via the `    /api/eda/` or `    /api/controller/` endpoints.(AAP-58622)


### 9.1.5. Automation controller




#### 9.1.5.1. Features




- Receptor collection version bumped to 2.0.8, which is compatible with Red Hat Enterprise Linux 10.(AAP-58421)
- Added `    x-ai-description` to controller schema to provide AI friendly description of each endpoint.(AAP-59819)


#### 9.1.5.2. Bug Fixes




- Fixed an issue where project update failed with no output, and project deletions failed. Automation controller now uses the force flag when syncing a project which has **Allow branch override** enabled.(AAP-58533)
- In this update, users attempting to install a software package on an unsupported architecture may encounter issues due to incorrect data in reminders. This has been resolved.(AAP-59728)
- Fixed an issue where the project update failed with no output and project deletions also failed.(AAP-58533)
- Fixed an issue where the OpenAPI specification for the Automation controller was incomplete, impeding MCP server integration development. This limited the seamless MCP server integration with the Ansible Automation Platform. The Automation controller’s REST API is now complete and accessible.(AAP-53640)


### 9.1.6. Automation hub




#### 9.1.6.1. Bug Fixes




- Fixed an issue with Automation hub authentication failure for users with the **Team Admin** role:


- Users assigned the **Team Admin** role can now successfully authenticate to Automation hub. Previously, these users would receive a **401** error when accessing Automation hub API endpoints due to an incompatibility between the **Team Admin** role and Automation hub’s internal permission system.(AAP-58898)

- Fixed an issue where the password field on the Automation hub Django REST framework authentication page was missing the autocomplete attribute. As a consequence, the field did not align with security best practices regarding browser autofill. With this update, the password field uses the `    autocomplete="new-password"` attribute. As a result, the Automation hub API authentication page complies with recommended security settings.(AAP-59910)
- Previously, upgrades from Ansible Automation Platform 2.5 to 2.6 failed when API access logging was enabled. This occurred due to an incorrect import path in the galaxy-ng package. This release corrects the import path.(AAP-59886)


### 9.1.7. Container-based Ansible Automation Platform




#### 9.1.7.1. Enhancements




- Configured podman PID limits, `    sysctls` for `    inotify` and kernel keys, and ulimit `    nofile` for user running Ansible Automation Platform service containers based on system resources.(AAP-59438)


#### 9.1.7.2. Bug Fixes




- Fixed an issue where after uninstall/re-install of receptor jobs were unable to start due to stale exited containers with the same name were still present.(AAP-59609)


### 9.1.8. Event-Driven Ansible




#### 9.1.8.1. Enhancements




- Added concise descriptions to API endpoints for Ansible Automation Platform MCP MVP endpoints ( `    x-ai-description` ).(AAP-58431)


#### 9.1.8.2. Bug Fixes




- Fixed an issue where the OpenAPI specification for Event-Driven Ansible was not offering comprehensive documentation and detailed request/response schemas. Previously, developers integrating with Event-Driven Ansible via the MCP server had to manually explore APIs and format API calls without proper guidance, which impeded seamless integration. With this release, the OpenAPI specification for the Event-Driven Ansible REST API is now complete and well-documented. This enhancement enables seamless integration with the MCP server using Event-Driven Ansible.(AAP-53642)


### 9.1.9. Lightspeed




#### 9.1.9.1. Technical Preview




- This developer preview introduces support for Ansible MCP Servers.(AAP-57303)
- This new feature enables users to access the Ansible Automation Platform 2.6 API directly from AI tools like Claude Code.(AAP-57217)


#### 9.1.9.2. Features




Added the new Ansible Automation Platform MCP Server to the 2.6 stream.(AAP-58863)

#### 9.1.9.3. Bug Fixes




- Fixed an issue of Ansible Automation Platform Multi-Channel Platform (MCP) servers crashing due to incomplete Epic and System Design Plan (SDP) creation, leading to unclear work requirements. As a result, the Ansible Automation Platform MCP Servers have created the System Design Plan and related tasks, addressing ANSTRAT-1567. This enhancement improves the efficiency of feature development for end users by completing the Ansible Automation Platform MCP Servers system design plan in an active manner.(AAP-53087)


### 9.1.10. Receptor




#### 9.1.10.1. Features




- Receptor collection version bumped to 2.0.8, which supports Red Hat Enterprise Linux 10 mesh nodes.(AAP-57987)


#### 9.1.10.2. Bug Fixes




- Fixed an issue where the receptor-collection was not up to date with Automation hub standards. There is now an up to date Changelog included in receptor-collection.(AAP-58434)


## 9.2. Ansible Automation Platform patch release November 19, 2025




This release includes the following components and versions:

| Release Date | Component versions |
| --- | --- |
| November 19, 2025 | - Automation controller 4.7.5
- Automation hub 4.11.3
- Event-Driven Ansible 1.2.2
- Container-based installer Ansible Automation Platform (bundle) 2.6-3
- Container-based installer Ansible Automation Platform (online) 2.6-3
- Receptor 1.6.2
- RPM-based installer Ansible Automation Platform (bundle) 2.6-3
- RPM-based installer Ansible Automation Platform (online) 2.6-3 |


CSV Versions in this release:

- Namespace: aap-operator.v2.6.0-0.1763137334
- Cluster: aap-operator.v2.6.0-0.1763137355


### 9.2.1. CVE




With this update, the following CVEs have been addressed:

-  [CVE-2025-9909](https://access.redhat.com/security/cve/cve-2025-9909)  `    automation-gateway` : improper path validation in gateway allows credential exfiltration.(AAP-53584)
-  [CVE-2025-59530](https://access.redhat.com/security/cve/cve-2025-59530)  `    receptor` : `    quic-go` crash due to premature `    HANDSHAKE_DONE` frame.(AAP-55973)


### 9.2.2. Ansible Automation Platform




#### 9.2.2.1. Features




- Allows for Event-Driven Ansible to add CA Certificates in gateway which can then be used by **Envoy** to do certificate based authorization for mTLS `    EventStreams` .(AAP-56770)


#### 9.2.2.2. Enhancements




- Red Hat Ansible Lightspeed section has been removed from the left navigation bar.(AAP-53006)
- Added fallback-authenticator feature, which allows users to configure `    fallback_authentication` for running custom logic in the event local authentication fails.


- Set all existing local authenticators and those created on initial install to fallback to controller credentials.
- The ability to clear the preset if the user does not want to fallback to controller authorization anymore.(AAP-56919)

- Ansible Lightspeed intelligent assistant has expanded its support for third-party Large Language Model (LLM) providers, and now includes OpenAI and Microsoft Azure. Third-party LLM support is available for both OpenShift Container Platform operator installation and containerized installation.


- For more information, see [Deploying the Ansible Lightspeed intelligent assistant on Red Hat OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/installing_on_openshift_container_platform/deploying-chatbot-operator) and [Deploying the Ansible Lightspeed intelligent assistant on containerized installation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/deploying-lightspeed-containerized-install) .(ANSTRAT-1673)



#### 9.2.2.3. Bug Fixes




- Fixed a significant performance regression in response time for GET requests to _/role_definitions/_ and related endpoints.(AAP-56868)
- Fixed an issue where users who existed in Ansible Automation Platform 2.5 with controller legacy authentication, but never logged in were unable to attempt authentication with controller in Ansible Automation Platform 2.6, and were left in an unusable state.(AAP-56388)
- Fixed issue in which superuser status would sync from platform gateway to other components if set to `    True` , but not if set to `    False` , where administrator privileges were not removed from the other components in all cases.(AAP-56296)
- Fixed an issue where platform auditors were not able to view all platform level settings.(AAP-55608)
- Fixed an issues where the **Team** input field on the authentication mapping form was not hidden when an organization role was selected.(AAP-55602)
- Fixed an issue where the workflow visualizer CSS was displaying the incorrect height.(AAP-55164)
- Fixed an issue using the and condition with multiple attributes. Previously the authentication map would skip the missing attributes, now, the map will be applied only if all attributes are present and the condition(s) are met.(AAP-53612)
- Fixed an issue where the `    LOGIN_REDIRECT_OVERRIDE` did not allow for a bypass URL. A login page has been added at _/login_ to bypass the `    LOGIN_REDIRECT_OVERRIDE` setting when it is misconfigured.(AAP-53471)
- Fixed the Subscription Usage chart where it did not always display at full height.(AAP-52218)
- Fixed an issue that was preventing users from viewing complete survey question choices that contained a colon.(AAP-50290)
- Fixed an issue where a warning message was not available when a user tried to restart an activation in the **workers offline** status.(AAP-24009)
- Fixed an issue where filtering platform resources by special characters did not work as expected.(AAP-52360)
- Fixed an issue where, applying a domains filter on the Jobs tab and navigating to the **Projects** section, then selecting a project with multiple templates, caused the system to display only the job template that was filtered by the domain, hiding other templates and showing a misleading message.(AAP-48031)
- Fixed an issue where there was no limit filtering to the jobs page.(AAP-45218)
- Fixed a form validation issue on the **Login redirect override** field in platform gateway settings.(AAP-40517)
- Fixed an execution environment deletion warning.(AAP-55135)


### 9.2.3. Red Hat Ansible Lightspeed




#### 9.2.3.1. Features




- Added support for 3rd party model providers OpenAI.(AAP-58291)
- Added support for 3rd party model providers Azure.(AAP-58290)


#### 9.2.3.2. Enhancements




- Upgraded Lightspeed Core Stack to 0.3.0.(AAP-55681)
- Added ALIA support `    lightspeed-stack` 0.3.0 and `    llama-stack` 0.2.22.(AAP-58136)
- Upgraded Ansible Lightspeed intelligent assistant to `    Lightspeed-core` 0.3.0.(AAP-56629)
- Added ALIA support for Azure provider.(AAP-56511)
- Added ALIA support for OpenAI provider.(AAP-56509)
- Made changes required to support `    llama-stack` 0.2.22.(AAP-58361)


#### 9.2.3.3. Bug Fixes




- Fixes an issue where the Red Hat Ansible Lightspeed assistant returned raw `    tool_call` JSON instead of natural language answers due to improper processing in Ansible Automation Platform 2.6 with granite-3.3-8b. This compromised user experience by exposing internal details.(AAP-57513)
- Fixed an issue where the user would be scrolled to the bottom of the chat history if they clicked **thumbs up/thumbs down** on a previous message.(AAP-58438)
- Fixed an issue where during the upgrade of `    chatbot-api` , the new one is stuck in pending state waiting until PVC is removed.(AAP-57376)


#### 9.2.3.4. Known Issues




- If you are using an IBM Granite 3.3 AI model series in your Ansible Lightspeed intelligent assistant deployment, there may be a delay of ~1 minute in receiving a chat response. As a workaround, restart the chat session.(AAP-58186)


### 9.2.4. Automation controller




#### 9.2.4.1. Features




- Receptor collection version updated to 2.0.6, which is compatible with ansible-core 2.19.(AAP-42617)


#### 9.2.4.2. Bug Fixes




- Fixed an issue where the migrating team mappers which did not include a users field is now supported.(AAP-56395)
- Fixed the following migration error for the migration `    0200_template_name_constraint.py` when there was a job template or project with duplicate name in the same organization.(AAP-56222)


**Error Message**

```
django.db.utils.ProgrammingError: column main_unifiedjobtemplate.org_unique does not exist
```


- Fixed an issue where some edge cases caused JSON to fail to parse a line from the worker stream with the error: **Expecting value: line 1 column 1 (char 0) Line with invalid JSON data: b** . Updated the pinned version for `    receptorctl` in automation controller to address this issue. This effects Tower 4.7.(AAP-58412)
- Fixed an issue where some edge cases caused JSON to fail to parse a line from the worker stream with the error: **Expecting value: line 1 column 1 (char 0) Line with invalid JSON data: b** . Updated the pinned version for `    receptorctl` in automation controller to address this issue. This effects Tower 4.6.(AAP-58415)
- Fixed an issue where there was not a meaningful error message whenever the streaming of logs was aborted. Update `    ansble-runner` to 2.4.2 to address this issue.(AAP-58390)
- Fixes an issue where jobs failed on `    fapolicyd` enabled systems where python3.9 was not installed by default. Updates `    automation-controller-fapolicyd` from python3.9 to python3.11 to address this issue.(AAP-55790)


### 9.2.5. Automation hub




#### 9.2.5.1. Bug Fixes




- Fixed an upgrade error, `    AttributeError` or `    ValueError` , **content type mismatch** in the migration that happens when upgrading if any role is assigned to a group globally before the migration.(AAP-58299)


### 9.2.6. Container-based Ansible Automation Platform




#### 9.2.6.1. Enhancements




- Added ALIA support lightspeed-stack 0.3.0 and llama-stack 0.2.22.(AAP-58295)
- Added ALIA support for Azure provider.(AAP-58206)
- Added ALIA support for OpenAI provider.(AAP-58197)


#### 9.2.6.2. Bug Fixes




- Fixed a compatibility issue with PostgreSQL 17 when using an external database and admin credentials.(AAP-57431)
- Fixed an issue with the chatbot response about the latest Ansible Automation Platform version.(AAP-57385)
- Fixed an issue with the monitoring image on Red Hat Ansible Lightspeed nodes when using the bundle deployment.(AAP-57167)


### 9.2.7. RPM-based Ansible Automation Platform




#### 9.2.7.1. Enhancements




Event-Driven Ansible event-stream mTLS configuration added to installer.(AAP-46070)

#### 9.2.7.2. Bug Fixes




- Fixed an issue where the installer failed during the execution environment image upload when there was no automation hub node in inventory.(AAP-56892)
- Fixed an issue with extra log content. platform gateway logs in _/var/log/ansible-automation-platform/gateway_ have been refactored, there is now more separation of the logs for various components:


-  _control-plane-supervisor.log_ ← Messages from `        supervisorctl` about the control-plane (new)
-  _control-plane.log_ ← Django logs for the control-plane (new, extracted from gateway.log)
-  _gateway.log_ ← Django logs for gateway (existing, had items removed)
-  _uwsgi.log_ ← UWSGI logs for the {Gateeway} (new, extracted from gateeay.log)
-  _envoy.log_ ← The proxy log (existing, unchanged).(AAP-30549)



### 9.2.8. Event-Driven Ansible




#### 9.2.8.1. Features




- Enhancement to support mTLS event streams.(AAP-57375)
- Added the ca_certificates module and the enable_mtls attribute to route objects.(AAP-48345)
- Added a credential type for mTLS event stream.(AAP-46054)


#### 9.2.8.2. Enhancements




- Event-Driven Ansible event-stream mTLS configuration added to the installer,(AAP-57434)


### 9.2.9. Receptor




#### 9.2.9.1. Features




- Addresses edge cases that could cause JSON failure to parse a line from the worker stream. It also raises the versions of go dependencies and other minor functionality changes.(AAP-57253)


## 9.3. Ansible Automation Platform patch release November 5, 2025




This release includes the following components and versions:

| Release Date | Component versions |
| --- | --- |
| November 5, 2025 | - Automation controller 4.7.4
- Automation hub 4.11.2
- Event-Driven Ansible 1.2.1
- Container-based installer Ansible Automation Platform (bundle) 2.6-2
- Container-based installer Ansible Automation Platform (online) 2.6-2
- Receptor 1.6.0
- RPM-based installer Ansible Automation Platform (bundle) 2.6-2
- RPM-based installer Ansible Automation Platform (online) 2.6-2 |


CSV Versions in this release:

- Namespace-scoped Bundle: aap-operator.v2.6.0-0.1761384532
- Cluster-scoped Bundle: aap-operator.v2.6.0-0.1761384578


### 9.3.1. Red Hat Ansible Lightspeed




#### 9.3.1.1. Bug Fixes




- A typo in the `    containerfile` caused the **nginx** configuration file to be copied to a non-existent directory in operator-based installations, leading to the Lightspeed API service being unavailable due to incorrect port configuration. With this release, the typo has been fixed, ensuring the Lightspeed API service now listens on the correct port in operator-based installations, improving API endpoint accessibility.(AAP-56712)


### 9.3.2. Technical note




#### 9.3.2.1. Red Hat Ansible Lightspeed




RFC 2818 is now enforced between the lightspeed service and the identity provider (gateway) during the OAuth2 authorisation.

### 9.3.3. Container-based Ansible Automation Platform




#### 9.3.3.1. Bug Fixes




- Fixed an issue with the chatbot response about the latest Ansible Automation Platform version.(AAP-57385)


## 9.4. Ansible Automation Platform patch release October 28, 2025




This release includes the following components and versions:

| Release Date | Component versions |
| --- | --- |
| October 28, 2025 | - Automation controller 4.7.4
- Automation hub 4.11.2
- Event-Driven Ansible 1.2.1
- Container-based installer Ansible Automation Platform (bundle) 2.6-2
- Container-based installer Ansible Automation Platform (online) 2.6-2
- Receptor 1.6.0
- RPM-based installer Ansible Automation Platform (bundle) 2.6-2
- RPM-based installer Ansible Automation Platform (online) 2.6-2 |


CSV Versions in this release:

- Namespace: aap-operator.v2.6.0-0.1762261205
- Cluster: aap-operator.v2.6.0-0.1762261209


### 9.4.1. CVE




With this update, the following CVEs have been addressed:

[CVE-2025-59682](https://access.redhat.com/security/cve/cve-2025-59682)  `python-django` : Potential partial directory-traversal via archive.extract().(AAP-54755)

[CVE-2025-9908](https://access.redhat.com/security/cve/cve-2025-9908)  `event-driven-ansible` : Sensitive internal headers disclosure in Ansible Automation Platform Event-Driven Ansible event streams.(AAP-53582)

[CVE-2025-9907](https://access.redhat.com/security/cve/cve-2025-9907)  `event-driven-ansible` : Event stream test mode exposes sensitive headers in Ansible Automation Platform Event-Driven Ansible.(AAP-53580)

[CVE-2025-59343](https://access.redhat.com/security/cve/cve-2025-59343)  `automation-platform-ui` : tar-fs symlink validation bypass.(AAP-54392)

[CVE-2025-58754](https://access.redhat.com/security/cve/cve-2025-58754)  `automation-platform-ui` : Axios DoS via lack of data size check.(AAP-53718)

### 9.4.2. Ansible Automation Platform




#### 9.4.2.1. Features




- Added a step in the subscription wizard that allows the user to configure automation analytics.(AAP-55094)
- Added two new toggle options on the subscription wizard to allow for fetching subscriptions using basic authentication.(AAP-47865)


#### 9.4.2.2. Bug Fixes




- Fixed an issue where the `    ansible-builder` and `    ansible-navigator` did not use execution environment images from ansible-automation-platform-26 namespace by default.(AAP-54934)
- Fixed an issue where the settings did not display **Red Hat** consistently in the API and UI.(AAP-54276)
- Fixed an issue where the decision environment dropdown was broken. Replaced the dropdown type for decision environments in the rulebook activation form so that when there are no decision environments available, the dropdown displays No results found instead of an empty dropdown.(AAP-53844)
- Fixed an issue where creating resources with `    cookie/xcrf` token failed. Aligned dependency versions between Konflux build and component repository.(AAP-53561)
- Fixed an issue where the component label for the Platform Auditor role did not display all components.(AAP-53551)
- Fixed an issue where empty strings were displayed in the extra variables field on the **Jobs > Details** page.(AAP-49448)
- Fixed an issue where the **Load More** in authentication mapping role dropdown did not work.(AAP-54049) HubName
- Fixed an issue where the user was unable to create Event-Driven Ansible or automation hub roles when creating a custom role and selecting the **Automation Decisions** project or credential types because the UI displayed only the automation controller permissions.(AAP-54756) ControllerName
- Fixed an issue where the PatternFly 6 Upgrade broke the Ansible Automation Platform topology layout and fullscreen mode.(AAP-51106)
- Fixed an issue where some fields were missing `    autocomplete = new-password` setting.(AAP-55783)
- Fixed an issue where the user was unable to select the default execution environment in the automation settings page.(AAP-39321)
- Fixed an issue where the LDAP Group Type parameters failed to save user preferences when the language was initially set to `    es_ES` , resulting in a wrong version displayed on the user interface due to an uninitialized translation object.(AAP-56356)
- Fixed an issue that prevented SAML and AzureAD authentication when local user accounts share the same email address.(AAP-56518)


#### 9.4.2.3. Deprecated




- Subscription credentials can no longer be viewed/edited from the system settings page.(AAP-55014)


### 9.4.3. Ansible Automation Platform Operator




#### 9.4.3.1. Bug Fixes




- Fixed an issue where the Ansible Lightspeed API version did not work during Ansible Automation Platform idle.(AAP-54174)
- Fixed an issue that caused a failure to gather the job data from the controller API.(AAP-55632)
- Fixed a bug where the user could set an image without the respective version, causing the installation to enter an error loop.(AAP-55642)
- Fixed an issue where the backup and restore Ansible Automation Platform instance failed, from cluster A to cluster B, when restoring an upgraded AAP environment from 2.4.(AAP-55648)


### 9.4.4. Red Hat Ansible Lightspeed




#### 9.4.4.1. Features




**Ability to deploy Red Hat Ansible Lightspeed on new containerized installations of Ansible Automation Platform 2.6**

You can deploy and use Red Hat Ansible Lightspeed when you install or upgrade to a containerized installation of Ansible Automation Platform 2.6.

Red Hat Ansible Lightspeed includes two main components that enhance your automation experience with generative artificial intelligence (AI):

**Ansible Lightspeed intelligent assistant** , which is an AI-powered, intuitive chat interface embedded within the Ansible Automation Platform.

The integration of Red Hat Ansible Lightspeed intelligent assistant with the Model Context Protocol (MCP) server is available as a Technology Preview release. This integration enhances the user experience by delivering relevant, dynamically sourced data results to your queries.

Note
Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/) .



**Ansible Lightspeed coding assistant** , which is a generative AI service that works with IBM watsonx Code Assistant to help developers create and maintain Ansible content more efficiently.

For more information, see [Deploying Red Hat Ansible Lightspeed on containerized Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/deploying-lightspeed-containerized-install) in the containerized install user guide.

#### 9.4.4.2. Enhancements




- Added `    postgres_extra_settings` to Ansible Automation Platform operators to apply PostgreSQL configuration file level changes to managed postgres.(AAP-55053)


### 9.4.5. Automation controller




#### 9.4.5.1. Enhancements




- Added support for Red Hat username and password for the subscription management API.(AAP-54975)


#### 9.4.5.2. Bug Fixes




- Fixes the `    system_administrator` role creation race condition which most commonly happened on new Openshift deployments resulting in the default instance group not being created.(AAP-54963)
- Fixed an issue where the Controller container file was missing the metrics utility in version 2.6.(AAP-54948)
- Fixed an issue where the `    awx.awx.license` appeared to succeed when given an invalid _pool/subscription_ .(AAP-54768)
- Fixed an issue where the `    ansible.platform` collection did not work with the default Red Hat Ansible Automation Platform credential type.(AAP-41000)
- Fixed an issue where there was a duplicate value ( `    subsystem_metrics_pipe_execute_seconds` ) detected under _api/controller/v2/metrics/_ on Ansible Automation Platform 2.5.(AAP-55621)
- Fixed an issue where the platform auditor did not have access to controller settings.(AAP-55607)


### 9.4.6. Automation hub




#### 9.4.6.1. Enhancements




- Fixed an **HTTP 500** error when getting _/api/galaxy/_ui/v2/users/3/_ .(AAP-54260)


#### 9.4.6.2. Bug Fixes




- Fixed an HTTP 500 error when getting /api/galaxy/_ui/v2/users/3/.(AAP-54260)


### 9.4.7. Container-based Ansible Automation Platform




#### 9.4.7.1. Enhancements




- Implemented preflight ansible-core version validation.(AAP-54932)


#### 9.4.7.2. Bug Fixes




- Fixed an issue where `    REDHAT_CANDLEPIN_VERIFY` was not being used for the correct CA permissions so that the controller could not make requests to **subscription.rhsm.redhat.com** .(AAP-55180)


### 9.4.8. RPM-based Ansible Automation Platform




#### 9.4.8.1. Bug Fixes




- Fixed an issue where setting `    automationgateway_disable_https=false` resulted in install failure.(AAP-55466)
- Fixed an issue where `    RESOURCE_KEY SECRET_KEY` was not updated when restoring from a different environment.(AAP-54942)
- Fixed an issue where Event-Driven Ansible DE credentials failed to populate on initial installation.(AAP-54519)


Fixed an issue where the `envoy.log` for automation gateway did not receive logs after it was rotated.(AAP-51779)

Fixed an issue where `REDHAT_CANDLEPIN_VERIFY` was not being used for the correct CA permissions so that the controller could not make requests to **subscription.rhsm.redhat.com** .(AAP-55183)

### 9.4.9. Event-Driven Ansible




#### 9.4.9.1. Features




- Changes in the deployment and nginx configuration now allow for gunicorn and daphne to bind to :: as well, essentially allowing for seamlessly binding to IPv4 and IPv6 (dual-stack) addresses, while also enabling the operator to run in single-stack IPv6 or IPv4 scenarios.(AAP-56192)


### 9.4.10. Receptor




#### 9.4.10.1. Bug Fixes




Fixed an issue where there was stability issue on long-running jobs, clusters under heavy load, and network flakiness.(AAP-53742)

## 9.5. Ansible Automation Platform patch release October 16, 2025




This release includes the following components and versions:

| Release Date | Component versions |
| --- | --- |
| October 16, 2025 | - Automation controller 4.7.2
- Automation hub 4.11.1
- Event-Driven Ansible 1.2.0
- Container-based installer Ansible Automation Platform (bundle) 2.6-1.1
- Container-based installer Ansible Automation Platform (online) 2.6-1
- Receptor 1.5.7
- RPM-based installer Ansible Automation Platform (bundle) 2.6-1.1
- RPM-based installer Ansible Automation Platform (online) 2.6-1 |


CSV Versions in this release:

- Namespace-scoped Bundle: aap-operator.v2.6.0-0.1760139263
- Cluster-scoped Bundle: aap-operator.v2.6.0-0.1760139657


### 9.5.1. Ansible Automation Platform




#### 9.5.1.1. Bug Fixes




- Fixed an issue where the claims processing failed to migrate services during the post-migrate upgrade process.(AAP-55631)


### 9.5.2. Automation controller




#### 9.5.2.1. Bug Fixes




- Fixed an issue where the Ansible Automation Platform upgrade would be marked as failed if a single authenticator failed to migrate.(AAP-55629)


### 9.5.3. Automation hub




#### 9.5.3.1. Bug Fixes




- Fixed a global galaxy team role migration issue that could occur during the post-migrate upgrade process.(AAP-55304)
- Fixed an issue caused by a constraint violation during migrations.(AAP-55309)
- Fixed an issue from `    aap-gateway-manage,`  `    migrate_service_data` , that states **Role definition content type must be null to assign globally** , which was due to permissions in hub that failed validation.(AAP-55639)


## 9.6. Ansible Automation Platform patch release October 6, 2025




This release includes the following components and versions:

| Release Date | Component versions |
| --- | --- |
| October 6, 2025 | - Automation controller 4.7.1
- Automation hub 4.11.0
- Event-Driven Ansible 1.2.0
- Container-based installer Ansible Automation Platform (bundle) 2.6-1
- Container-based installer Ansible Automation Platform (online) 2.6-1
- Receptor 1.5.7
- RPM-based installer Ansible Automation Platform (bundle) 2.6-1
- RPM-based installer Ansible Automation Platform (online) 2.6-1 |


CSV Versions in this release:

- Namespace-scoped Bundle: aap-operator.v2.6.0-0.1759764484
- Cluster-scoped Bundle: aap-operator.v2.6.0-0.1759764962


### 9.6.1. Automation hub




- Fixed an issue where the automation hub collections in 2.6 could not be pulled with Ansible Galaxy due to incorrect dynamic http logic. This issue only affects the Red Hat Ansible Automation Platform Operator installation.(AAP-55099)



<span id="idm140711326443472"></span>
# Legal Notice

Copyright© 2025 Red Hat, Inc.
The text of and illustrations in this document are licensed by Red Hat under a Creative Commons Attribution–Share Alike 3.0 Unported license ("CC-BY-SA"). An explanation of CC-BY-SA is available at [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/) . In accordance with CC-BY-SA, if you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, Red Hat Enterprise Linux, the Shadowman logo, the Red Hat logo, JBoss, OpenShift, Fedora, the Infinity logo, and RHCE are trademarks of Red Hat, Inc., registered in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
Java® is a registered trademark of Oracle and/or its affiliates.
XFS® is a trademark of Silicon Graphics International Corp. or its subsidiaries in the United States and/or other countries.
MySQL® is a registered trademark of MySQL AB in the United States, the European Union and other countries.
Node.js® is an official trademark of Joyent. Red Hat is not formally related to or endorsed by the official Joyent Node.js open source or commercial project.
TheOpenStack® Word Mark and OpenStack logo are either registered trademarks/service marks or trademarks/service marks of the OpenStack Foundation, in the United States and other countries and are used with the OpenStack Foundation's permission. We are not affiliated with, endorsed or sponsored by the OpenStack Foundation, or the OpenStack community.
All other trademarks are the property of their respective owners.





