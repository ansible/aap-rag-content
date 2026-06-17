# Ansible Automation Platform patch release January 21, 2026

The following release notes detail the updates for the Ansible Automation Platform patch released on January 21, 2026.

This release includes the following components and versions:

| Release Date         | Component versions                                                                                                                                                                                                                                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <br>January 21, 2026 | automation controller 4.7.8Automation hub 4.11.5Event-Driven Ansible 1.2.4Container-based installer Ansible Automation Platform (bundle) 2.6-5Container-based installer Ansible Automation Platform (online) 2.6-5Receptor 1.6.3RPM-based installer Ansible Automation Platform (bundle) 2.6-4RPM-based installer Ansible Automation Platform (online) 2.6-4 |


CSV Versions in this release:

- Namespace: aap-operator.v2.6.0-0.1768951397
- Cluster: aap-operator.v2.6.0-0.1768951413

## CVE

With this update, the following CVEs have been addressed:

- [CVE-2025-69223](https://access.redhat.com/security/cve/cve-2025-69223)`automation-controller`: AIOHTTP’s HTTP Parser auto_decompress feature is vulnerable to zip bomb.(AAP-61927)
- [CVE-2025-69223](https://access.redhat.com/security/cve/cve-2025-69223)`ansible-automation-platform-26/controller-rhel9`: AIOHTTP’s HTTP Parser auto_decompress feature is vulnerable to zip bomb.(AAP-61915)
- [CVE-2025-4565](https://access.redhat.com/security/cve/cve-2025-4565)`python3.11-protobuf`: Unbounded recursion in Python Protobuf.(AAP-60498)
- [CVE-2025-66031](https://access.redhat.com/security/cve/cve-2025-66031)`ansible-ai-connect-service`: `node-forge` ASN.1 Unbounded Recursion.(AAP-59983)
- [CVE-2025-66416](https://access.redhat.com/security/cve/cve-2025-66416)`ansible-automation-platform-26/mcp-tools-rhel9`: DNS Rebinding Protection Disabled by Default in Model Context Protocol PythonSDK.(AAP-59952)
- [CVE-2025-64459](https://access.redhat.com/security/cve/cve-2025-64459)`ansible-automation-platform-26/hub-rhel9`: Django SQL injection.(AAP-58111)
- [CVE-2025-53643](https://access.redhat.com/security/cve/cve-2025-53643)`automation-controller`: AIOHTTP HTTP Request/Response Smuggling.(AAP-54877)
- [CVE-2025-61729](https://access.redhat.com/security/cve/cve-2025-61729)`ansible-automation-platform-26/receptor-rhel9`: Excessive resource consumption when printing error string for host certificate validation in `crypto/x509`.(AAP-61230)
- [CVE-2025-64460](https://access.redhat.com/security/cve/cve-2025-64460)`python3.11-django`: `Django`: Algorithmic complexity in XML deserializer leads to denial of service.(AAP-61780)
- [CVE-2025-64460](https://access.redhat.com/security/cve/cve-2025-64460)`automation-controller`: `Django`: Algorithmic complexity in XML Deserializer leads to denial of service.(AAP-60961)
- [CVE-2026-21441](https://access.redhat.com/security/cve/cve-2026-21441)`ansible-automation-platform-26/lightspeed-rhel9`: `urllib3` vulnerable to decompression-bomb safeguard bypass when following HTTP redirects (streaming API).(AAP-62341)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471)`python3.11-urllib3`: `urllib3` streaming API improperly handles highly compressed data.(AAP-62290)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471)`python3.11-urllib3`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62290)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471)`automation-controller`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62090)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471)`ansible-automation-platform-26/controller-rhel9`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62068)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471)`ansible-automation-platform-25/lightspeed-rhel8`: `urllib3`: Streaming API improperly handles highly compressed data.(AAP-62030)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471)`ansible-automation-platform-26/mcp-tools-rhel9`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62085)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471)`ansible-automation-platform-26/lightspeed-rhel9-operator`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62084)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471)`ansible-automation-platform-26/lightspeed-rhel9`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62083)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471)`ansible-automation-platform-26/lightspeed-chatbot-rhel9`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62082)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471)`ansible-automation-platform-26/controller-rhel9-operator`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62069)
- [CVE-2025-61729](https://access.redhat.com/security/cve/cve-2025-61729)`receptor`: Excessive resource consumption when printing error string for host certificate validation in `crypto/x509`.(AAP-61235)
- [CVE-2025-62706](https://access.redhat.com/security/cve/cve-2025-62706)`ansible-automation-platform-26/lightspeed-chatbot-rhel9`: `Authlib`: JWE `zip=DEF` decompression bomb enables DoS.(AAP-60596)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471)``ansible-automation-platform-26/gateway-rhel9: `urllib3`` Streaming API improperly handles highly compressed data.(AAP-62077)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471)`ansible-automation-platform-26/eda-controller-rhel9`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62072)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471)`ansible-automation-platform-26/de-supported-rhel9`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62071)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471)`ansible-automation-platform-26/de-minimal-rhel9`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62070)
- [CVE-2026-21441](https://access.redhat.com/security/cve/cve-2026-21441)`ansible-automation-platform-26/gateway-rhel9`: `urllib3` vulnerable to decompression-bomb safeguard bypass when following HTTP redirects (streaming API).(AAP-62446)
- [CVE-2026-21441](https://access.redhat.com/security/cve/cve-2026-21441)`ansible-automation-platform-26/eda-controller-rhel9`: `urllib3` vulnerable to decompression-bomb safeguard bypass when following HTTP redirects (streaming API).(AAP-62443)
- [CVE-2026-21441](https://access.redhat.com/security/cve/cve-2026-21441)`ansible-automation-platform-26/de-minimal-rhel9`: `urllib3` vulnerable to decompression-bomb safeguard bypass when following HTTP redirects (streaming API).(AAP-62383)
- [CVE-2025-69223](https://access.redhat.com/security/cve/cve-2025-69223)`ansible-automation-platform-26/de-supported-rhel9`: AIOHTTP’s HTTP Parser `auto_decompress` feature is vulnerable to zip bomb.(AAP-61917)
- [CVE-2025-69223](https://access.redhat.com/security/cve/cve-2025-69223)`ansible-automation-platform-26/de-minimal-rhel9`: AIOHTTP’s HTTP Parser `auto_decompress` feature is vulnerable to zip bomb.(AAP-61916)

## Ansible Automation Platform

Features
- Page titles now reflect the current page content.(AAP-61754)
- Ansible Automation Platform now provides support for IPv6 single-stack and dual-stack (IPv4 and IPv6) deployments in container-based environments. IPv6 is now supported across all Ansible Automation Platform deployment methods. The `FEATURE_GATEWAY_IPV6_USAGE_ENABLED` feature flag has been removed and IPv6 support is enabled by default.(ANSTRAT-1575)
- Red Hat now collects anonymized telemetry data from the Ansible MCP server. The telemetry data includes metrics related to MCP server performance, adoption trends, and usage patterns. For more information, see the [Telemetry data collection for the Ansible MCP server](/documentation/en-us/red_hat_ansible_automation_platform/2.6/extend-assembly_deploying_ansible_mcp_server#deploying-ansible-mcp-server "As an organization administrator, you can deploy the Model Context Protocol (MCP) server for Red Hat Ansible Automation Platform on an operator-based installation or container-based installation of Ansible Automation Platform.").(ANSTRAT-1792)

Enhancements
Improves labels and descriptions for Authenticator Mappings details.(AAP-51295)

Updated modal warning message and layout when enabling a copied Rulebook Activation.(AAP-42574)

- Added dedicated aap.auth_audit logger with specialized formatters and handlers.   * Source IP address.
* User agent from HTTP requests.     + Introduced new logs for authentication events, all of which are both present in logs following their original patterns as well as logs under the `aap.auth_audit` logger, including all of the original information.


Important:

In a future release, all authentication logs introduced and moved from their existing logger to the aap.auth_audit logger will be removed from all but the `aap.auth_audit` logger.

- Specific log changes:
* `OAuth2` Token Lifecycle Tracking
+ Log token creation, modification, and usage with associated OAuth2 application.
+ Track authenticated API requests with user, method, path, and token details.
+ Improved activity stream with selective field diffing to reduce noise from trivial updates.
- SSO Authentication Logging
* Log SSO redirect initiation with authenticator identification and sanitized redirect URLs.
* Track social auth failures and exceptions.
* Enhanced SAML authenticator logging.
- Authentication Event Logging
* Log successful and failed authentication attempts.
* Track cases where no authenticator can validate a user.
* Include authenticator type in login success messages.
* Log access denials from claims processing.
- Improved Error Logging
* Enhanced Redis connection error messages to include underlying exceptions.

* Better diagnostic information for troubleshooting. (AAP-60364)

+ Reduce cognitive complexity `in _sync_user_superuser_flag`.(AAP-62771)

Bug Fixes
- Fixed an issue preventing gateway from working in a pure IPv4 single stack environment when IPv6 is enabled.(AAP-60478)
- Fixed an issue where the UI did not allow for full search in resource dropdowns.(AAP-57712)
- Fixed an issue that occasionally showed a bad request status when navigating between different pages in Ansible Automation Platform.(AAP-56701)
- Fixed an issue where searching for a collection by name returned incorrect results. Fixed the filtering by name in the **Collections** page.(AAP-56529)
- Fixed an issue where the user could not edit the **Client Certificate** and/or **Client Key** fields of a credential once set.(AAP-55296)
- Fixed an issue where the workflow job templates node credentials were missing after save for job template nodes that have a default credential that is promptable.(AAP-52638)
- Fixed an issue where the platform gateway UI reset the order of an authentication mapping when the entity was edited by the user.(AAP-52258)
- Fixed an issue where automation controller unavailability rendered the entire Ansible Automation Platform UI inaccessible. The UI now remains functional during automation controller outages, displaying a notification banner to alert users.(AAP-50106)
- Fixed an issue where the descriptions for the **Remotes** and **Remote Registries** were not accurate.(AAP-49838)
- Fixed an issue where the survey text area **Default Answer** field did not properly accept newlines when pressing Enter.(AAP-49820)
- Fixed an issue where the **Review** page of the add **Approval** node in workflow job template did not load.(AAP-49433)
- Fixed an issue where **Days of Data to Keep** is missing from **Edit Cleanup Job** schedule page.(AAP-48972)
- Fixed an issue where editing and saving credentials that use external credential lookup plugins (such as CyberArk) failed with an error message. Users can now successfully modify and save these credentials as expected.(AAP-44813)
- Fixed an issue where the SAML Service Provider extra configuration data field could not be cleared in the UI, as it would automatically reset to the default value. Users can now set this field to null, which is required for compatibility with certain identity providers.(AAP-43661)
- Fixed an issue where ad-hoc commands failed with a **Bad Request** error when using credentials configured with prompt on launch for password fields. The **Run Command** wizard now correctly displays a credential passwords step to collect required passwords before executing the command.(AAP-43603)

Deprecated
- Feature flag `FEATURE_GATEWAY_IPV6_USAGE_ENABLED` has been removed. IPv6 is now supported by default.(AAP-61805)

## Automation controller

Features
- Added runtime feature flags.(AAP-62686)

## Automation hub

Bug Fixes
- Fixed an issue where the password field on the automation hub Django REST framework authentication page was missing the autocomplete attribute. As a consequence, the field did not align with security best practices regarding browser autofill. With this update, the password field uses the autocomplete="new-password" attribute. As a result, the automation hub API authentication page now complies with recommended security settings.(AAP-59912)

## Container-based Ansible Automation Platform

Enhancements
- Added lTLS support to lightspeed chatbot service.(AAP-60900)

Bug Fixes
- Fixed an issue where the system-prompt optimized for granite and OpenAI models.(AAP-60898)
- Fixed an issue where the containerized installer could not properly configure Redis in the IPv6 only environment. Added IPv6 support for different Ansible Automation Platform components within the containerized installer collection.(AAP-60532)
- Fixed an issue where the ansiblemcp uninstall is failing to stop containers.

## Event-Driven Ansible

Features
- Added x-ai-description field to the activation PATCH method.(AAP-61969)
- With this update, activations in the "workers offline" status on the Event-Driven Ansible server are now protected from accidental deletion or disabling. This enhancement adds a warning banner to the User Interface (UI) for the "restart", "disable", and "delete" workflows, providing users with a clear warning before performing these actions. The feature also supports a force flag for the "disable" and "delete" operations, giving users the option to bypass the warning if necessary.(AAP-51378)

Bug Fixes
- Fixed an issue where the IPv6 support in the Event-Driven Ansible operator configmaps was missing the extra listen **NGINX** directive. We added the required directive so the event streams pod now has **NGINX** bound to its IPv6 interface.(AAP-62001)

## Red Hat Ansible Lightspeed

Enhancements
- Enabled chatbot authentication.(AAP-61015)
- Supports Red Hat Ansible Lightspeed chatbot authentication.(AAP-59478)
- Enabled chatbot authentication.(AAP-59476)
- The MCP service / endpoint now displays a banner that explains how to connect to the service, this banner replaces an error message.(AAP-59334)
- Implemented authentication between ansible-lightspeed and ansible-lightspeed-chatbot.(AAP-58796)
- Added chatbot authentication capabilities.(AAP-58794)
- Added Lightspeed chatbot TLS support.(AAP-54412)

Bug Fixes
- Fixed an issue where there was an error on the cursor editor. When the error occurred, the MCP server configuration on the Cursor Settings panel and Output view displayed error messages.(AAP-62002)
- Fixed an issue where the Lightspeed Chatbot `PROVIDER_VECTOR_DB_ID` set to literal string caused degraded responses in production.(AAP-61118)
- Fixed bug where VS Code would throw a warning when connecting to Ansible Automation Platform MCP servers due to a period character being in the tool name.(AAP-59293)
- Fixed an issue where Ansible Lightspeed intelligent assistant showed raw tool_call output in answers.(AAP-57513)
- Fixed an issue where long tool names in the Ansible Automation Platform MCP server exceeding the 60-character limit in Cursor’s MCP server resulted in the MCP server tools to being hidden in Cursor, impacting tool usage. With this release, the MCP server now supports tool names exceeding 60 characters, resolving the visibility and usability issues for all tools in the Ansible Automation Platform MCP server.(AAP-61149)
- Fixed an issue where ALIA was experiencing Database or Disk is Full errors.(AAP-53081)
- Fixed an issue where the `CHATBOT_API_KEY` environment variable was not passed to the container when the provider was azure/openai.(AAP-63292)

Deprecated
- Removed ansible-risk-insights dependency from ansible-ai-connect-service.(AAP-60336)
