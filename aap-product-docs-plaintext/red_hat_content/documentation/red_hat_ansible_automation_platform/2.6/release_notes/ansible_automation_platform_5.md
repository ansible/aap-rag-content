# 9. Patch releases
## 9.4. Ansible Automation Platform patch release January 21, 2026
### 9.4.2. Ansible Automation Platform

#### 9.4.2.1. Features

- Page titles now reflect the current page content.(AAP-61754)
- Ansible Automation Platform now provides support for IPv6 single-stack and dual-stack (IPv4 and IPv6) deployments in container-based environments. IPv6 is now supported across all Ansible Automation Platform deployment methods. The `FEATURE_GATEWAY_IPV6_USAGE_ENABLED` feature flag has been removed and IPv6 support is enabled by default.(ANSTRAT-1575)
- Red Hat now collects anonymized telemetry data from the Ansible MCP server. The telemetry data includes metrics related to MCP server performance, adoption trends, and usage patterns. For more information, see the [Telemetry data collection for the Ansible MCP server](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/deploying-ansible-mcp-server#telemetry_data_collection_for_ansible_mcp_server).(ANSTRAT-1792)

#### 9.4.2.2. Enhancements

Improves labels and descriptions for Authenticator Mappings details.(AAP-51295)

Updated modal warning message and layout when enabling a copied Rulebook Activation.(AAP-42574)

- Added dedicated aap.auth_audit logger with specialized formatters and handlers.


- Source IP address.

- User agent from HTTP requests.


- Introduced new logs for authentication events, all of which are both present in logs following their original patterns as well as logs under the `aap.auth_audit` logger, including all of the original information.

Important

In a future release, all authentication logs introduced and moved from their existing logger to the aap.auth_audit logger will be removed from all but the `aap.auth_audit` logger.

- Specific log changes:


- `OAuth2` Token Lifecycle Tracking


- Log token creation, modification, and usage with associated OAuth2 application.
- Track authenticated API requests with user, method, path, and token details.
- Improved activity stream with selective field diffing to reduce noise from trivial updates.

- SSO Authentication Logging


- Log SSO redirect initiation with authenticator identification and sanitized redirect URLs.
- Track social auth failures and exceptions.
- Enhanced SAML authenticator logging.

- Authentication Event Logging


- Log successful and failed authentication attempts.
- Track cases where no authenticator can validate a user.
- Include authenticator type in login success messages.
- Log access denials from claims processing.

- Improved Error Logging


- Enhanced Redis connection error messages to include underlying exceptions.

- Better diagnostic information for troubleshooting.

(AAP-60364)


- Reduce cognitive complexity `in _sync_user_superuser_flag`.(AAP-62771)

#### 9.4.2.3. Bug Fixes

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

#### 9.4.2.4. Deprecated

- Feature flag `FEATURE_GATEWAY_IPV6_USAGE_ENABLED` has been removed. IPv6 is now supported by default.(AAP-61805)

