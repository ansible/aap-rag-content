+++
title = "Ansible Automation Platform patch release March 25, 2026 - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2026_03_25"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-async_updates/", "Patch releases"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2026_03_25/aem-page/whats_new-aap_26_2026_03_25.html"
last_crumb = "Ansible Automation Platform patch release March 25, 2026"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Ansible Automation Platform patch release March 25, 2026"
oversized = "false"
page_slug = "whats_new-aap_26_2026_03_25"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2026_03_25"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2026_03_25/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform patch release March 25, 2026

The following release notes detail the updates for the Ansible Automation Platform patch released on March 25, 2026.

This release includes the following components and versions:

| Release Date   | Component versions                                                                                                                                                                                                                                                                                                                                            |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| March 25, 2026 | Automation controller 4.7.19Automation hub 4.11.7Event-Driven Ansible 1.2.7Container-based installer Ansible Automation Platform (bundle) 2.6-7Container-based installer Ansible Automation Platform (online) 2.6-7Receptor 1.6.4RPM-based installer Ansible Automation Platform (bundle) 2.6-6RPM-based installer Ansible Automation Platform (online) 2.6-6 |


CSV Versions in this release:

- Namespace-scoped bundle: aap-operator.v2.6.0-0.1774648945
- Cluster-scoped bundle: aap-operator.v2.6.0-0.1774648973

## Overview

This asynchronous update for Red Hat Ansible Automation Platform 2.6 (2.6.20260325) provides targeted enhancements, security updates, and bug fixes across automation controller, platform gateway, automation hub, Event-Driven Ansible, Lightspeed, execution environments, platform operators, and both platform and containerized installers.

This release focuses on expanding audit coverage for administrative actions, upgrading core services to Django 5.2 LTS, addressing multiple CVEs across the stack, and improving reliability, performance, and observability. It also refines user experience in the web UI and gateway and improves diagnostics through clearer logging and traceability.

## Highlights

Expanded audit and access logging

- Introduces and extends audit logging for users, teams, organizations, role assignments, dynamic preferences, and direct component access, improving traceability of administrative and configuration changes. AAP-67043, AAP-66919, AAP-66800, AAP-66668

Platform-wide move to Django 5.2 LTS

- Upgrades Django for gateway, hub, controller, and Lightspeed components to Django 5.2 LTS, aligning with a supported, more secure framework baseline. AAP-68587, AAP-68135, AAP-60155, AAP-59873, AAP-60388, AAP-64430

Security hardening through CVE remediation

- Resolves multiple vulnerabilities in UI, controller, gateway proxy, automation hub, Lightspeed, and packaging, including issues in Axios, Authlib, Pillow, pyasn1, cryptography, jsonpath, AIOHTTP, express-rate-limit, and Go’s `crypto/tls` and `net/url` libraries. AAP-69040, AAP-68686, AAP-68683, AAP-68529, AAP-68526, AAP-67735, AAP-67503, AAP-66903, AAP-66695, AAP-66655, AAP-66636, AAP-65713, AAP-65711, AAP-65695, AAP-65507, AAP-65506, AAP-65505, AAP-65475, AAP-65474, AAP-65473, AAP-65472, AAP-65412, AAP-65411, AAP-65410, AAP-65409, AAP-65224, AAP-64902, AAP-61921

Improved stability and performance across services

- Addresses issues impacting UI responsiveness, containerized installer behavior after Django upgrades, constructed inventory and facts handling, credential validation in Event-Driven Ansible, database restore flows in platform operators, and certificate handling in execution environments. AAP-69005, AAP-68843, AAP-68842, AAP-68841, AAP-68135, AAP-68079, AAP-67759, AAP-67749, AAP-67579, AAP-67552, AAP-67550, AAP-67549, AAP-67548, AAP-67498, AAP-67460, AAP-67371, AAP-67230, AAP-67081, AAP-67080, AAP-67079, AAP-67078, AAP-67038, AAP-66864, AAP-66845, AAP-66806, AAP-66706, AAP-66579, AAP-66400, AAP-66106, AAP-66105, AAP-66104, AAP-66102, AAP-65109, AAP-65081, AAP-64996, AAP-64630, AAP-64146, AAP-60313, AAP-60238, AAP-58769, AAP-58535, AAP-22149

- This update rebases the containerized installer to ansible.platform collection version 2.6.20260306, aligning the installer with the current Ansible Automation Platform 2.6 collection release. AAP-67548

Features
Controller

- This update improves compatibility with the receptor control tooling used by automation controller by updating the pinned `receptorctl` version for Tower 4.7 / Ansible Automation Platform 2.6. AAP-66806

Enhancements
Ansible Automation Platform

- This update extends audit logging for identity lifecycle operations in the gateway by recording creation, modification, and deletion of users, teams, and organizations. AAP-66919

- This update adds audit logging for dynamic preference changes so that updates to registered preferences and settings are tracked over time. AAP-66800

- This update refines the login experience by removing the “show password” eye icon so that the password field remains masked during entry. AAP-67230

- This update improves diagnostics for connectivity issues with automation controller by enhancing logging behind the “Error connecting to Controller API” banner. AAP-64146

Containerized-installer

- This update improves compatibility of the containerized installer after the Django 5.2 upgrade, preventing controller install failures caused by changes in Django behavior and output. AAP-68587

- This update keeps TLS configuration accurate by ensuring the gateway certificate is regenerated when certificate data changes so that gateway_main_url and related fields are updated. AAP-66579

- This update improves observability for direct component access in containerized deployments by adding nginx log markers for controller, hub, and Event-Driven Ansible in the containerized installer. AAP-66106

Controller

- This update increases observability for direct API access to automation controller by adding nginx log markers for requests containing `X-Trusted-Proxy` and `X-DAB-JW-TOKEN` headers. AAP-66102

- This update aligns automation controller with the supported framework baseline by upgrading its Django dependency to version 5.2 LTS. AAP-59873

Django-ansible-base

- This update extends audit logging coverage by adding audit entries for user and team role assignment changes, improving visibility into permission updates. AAP-67042

Event-driven-ansible

- This update improves observability for API traffic to Event-Driven Ansible by adding nginx log markers for direct API access. AAP-66105

Hub

- This update improves the robustness of the automation hub container registry by setting gunicorn and proxy timeouts to better handle varied workloads and network conditions. AAP-67759

- This update enhances logging parity across services by adding nginx log markers for direct API access to hub so that traffic bypassing the gateway can be detected. AAP-66104

- This update prepares for future token management changes by adding a deprecation warning for the ah_token module in the ansible.hub collection on AAP 2.6 (Hub 4.11) behind Ansible Automation Platform gateway. AAP-65109

- This update modernizes automation hub by upgrading its Django dependency to version 5.2 LTS. AAP-60388

CVE
Ansible Automation Platform UI

- CVE-2026-29074 – SVGO denial of service via XML entity expansion in:
  * `automation-platform-ui`. AAP-68529
  * `gateway-rhel9 image`. AAP-68526
- CVE-2026-27904 – Minimatch denial of service via catastrophic backtracking in glob expressions in:
  * `automation-platform-ui`. AAP-66695
- CVE-2025-69873 – Regular expression denial of service (ReDoS) via `$data` references in:
  * `automation-platform-ui` for Ansible Automation Platform 2.6. AAP-65713
  * `gateway-rhel9 image`. AAP-65711
  * `lightspeed-rhel9`. AAP-66655
- CVE-2026-25639 – Axios denial of service `via __proto__ handling` in `mergeConfig` in:
  * `automation-platform-ui`. AAP-65475
  * `gateway-rhel9 image`. AAP-65472
  * `lightspeed-rhel9`. AAP-65473


Automation gateway

- CVE-2025-68121 – Unexpected session resumption in Go crypto/tls in:
  * `automation-gateway-proxy` for Ansible Automation Platform 2.6. AAP-65695
- CVE-2025-61726 – Memory exhaustion via query parameter parsing in Go `net/url` in:
  * `automation-gateway-proxy` for Ansible Automation Platform 2.6. AAP-64902


Lightspeed / MCP / RAG

- CVE-2026-30922 – `pyasn1` denial of service via unbounded recursion in:
  * `lightspeed-chatbot-rhel9` image for Ansible Automation Platform 2.6. AAP-69040
- CVE-2026-28498 – `Authlib` authentication bypass via forged OpenID Connect ID tokens in:
  * `lightspeed-chatbot-rhel9` image for Ansible Automation Platform 2.6. AAP-68686
- CVE-2026-28802 – `Authlib` signature verification bypass allowing unauthorized access via malicious JWTs in:
  * `lightspeed-chatbot-rhel9` image. AAP-67503
- CVE-2026-25990 – Pillow out-of-bounds write via specially crafted PSD images in:
  * `lightspeed-chatbot-rhel9`. AAP-65506
  * hub-rhel9. AAP-65505
- CVE-2026-26007 – cryptography subgroup attack due to missing subgroup validation for SECT curves in:
  * `mcp-tools-rhel9`. AAP-65412
  * `lightspeed-rhel9`. AAP-65411
  * `lightspeed-chatbot-rhel9`. AAP-65410
- CVE-2026-1615 – jsonpath arbitrary code execution via unsafe JSON Path evaluation in:
  * `lightspeed-service-container`. AAP-65224
- CVE-2025-69223 – AIOHTTP HTTP parser `auto_decompress` vulnerability exploitable with zip bombs in:
  * `lightspeed-chatbot-rhel9`. AAP-61921
- CVE-2026-30827 – `express-rate-limit denial` of service for IPv4 clients due to incorrect IPv6 subnet masking in:
  * `aap-mcp-server-rhel9`. AAP-67735


Pillow / Image processing

- CVE-2026-25990 – Out-of-bounds write via specially crafted PSD images in:
  * `hub-rhel9`. AAP-65505


Bug fixes
Ansible Automation Platform

- Fixed an issue where the “Organization Admins Can Manage Users and Teams” setting did not correctly disable the create-team button in the UI when turned off, so organization admins now see the correct state. AAP-68843

- Fixed an issue where organization administrators were still able to delete or modify teams when “Organization Admins Can Manage Users and Teams” was disabled, so this setting now enforces the intended restrictions. AAP-68842

- Fixed an issue where teams from other organizations were not visible to organization administrators as expected when organization-wide visibility was enabled. AAP-68841

- Fixed an issue where an organization administrator could not assign team access to projects in Ansible Automation Platform 2.6, preventing proper delegation of permissions. AAP-65081

- Fixed an issue where list views in the gateway UI loaded slowly because of excessive duplicate API requests and aggressive polling intervals, improving responsiveness. AAP-67460

- Fixed an issue where redirects using the next URL parameter failed when the value included a plus sign (+), whether encoded or unencoded, so redirects now work correctly. AAP-64996

- Fixed an issue where creating Event-Driven Ansible projects concurrently from multiple users could result in server errors when handling project creation. AAP-67749

- Fixed an issue where general project creation flows in Django Ansible Base could lead to errors when invoked by multiple users, improving stability. AAP-60238

Containerized-installer

- Fixed an issue where containerized controller installs could fail after the Django 5.2 upgrade because Django output changed and broke parsing in the installer. AAP-68135

- Fixed an issue where Podman’s pids_limit could be set to an extremely large value on nodes with large memory, exceeding system-supported limits, by capping the value. AAP-67579

Controller

- Fixed an issue where facts could become inconsistent when running job templates with fact storage enabled, particularly when multiple inventories had same-name hosts or concurrent jobs updated facts. AAP-67371

- Fixed an issue where constructed inventories could not be saved when verbosity was greater than 2, so higher verbosity levels are now supported. AAP-66864

- Fixed an issue where job events missing an event type caused uncaught exceptions in the job events children summary view, improving reliability. AAP-64630

Event-driven-ansible

- Fixed an issue where Decision Environment credential validation rejected container registry credentials when the password came from an external credential provider unless placeholder text was used, allowing those credentials to be attached without workarounds. AAP-69005
- Fixed an issue where Jinja2 variable substitution in rule names failed in Event-Driven Ansible controller worker mode even though the same variables worked in action `extra_vars`, aligning behavior with the CLI. AAP-67038
- Fixed an issue where Event-Driven Ansible server could not sync git projects using `ssh://` or `git+ssh://` URL schemes, restoring project sync behavior. AAP-66353


Execution-environments

- Fixed an issue where a change in the `certifi` package affected default trust store paths in Ansible Automation Platform 2.6 execution environments by switching to `system-certifi` to restore expected behavior. AAP-58769


Hub

- Fixed an issue where the X-Forwarded-Proto header could be incorrectly set in conjunction with the `alter_hostname_settings` configuration on Azure when passing traffic from gateway to hub. AAP-66706


Lightspeed

- Fixed an issue where OAuth2 authentication on containerized installer deployments could fail when the Lightspeed port was set to 443 because of incorrect URL handling and default port logic. `AAP-66845`

- Fixed an issue where the platform configuration MCP server exposed the `settings_list` tool twice, causing API errors in clients, by renaming the tools to `controller-settings_list` and `gateway-settings_list`. AAP-66400

- Fixed an issue where the /check endpoint of the Ansible Lightspeed API container reported an incorrect commit version and SHA, improving diagnostics. AAP-60313

Platform-operator

- Fixed an issue where deleting a restored Ansible Automation Platform object did not delete the associated deployment or pods, leaving orphaned resources. AAP-68079

- Fixed an issue where IRSA-based S3 authentication support from galaxy-operator was not available in automation hub operator for stable-2.6, allowing S3 access-key fields to be optional. AAP-67498

- Fixed an issue where Galaxy operator restores with `force_drop_db` failed due to missing `CREATEDB` privileges and partitioned index handling, causing `pg_restore` to fail during restores. AAP-67081

- Fixed an issue where Event-Driven Ansible operator restores with `force_drop_db` failed because the managed PostgreSQL user lacked permissions to recreate databases, causing failures on restore. AAP-67080

- Fixed an issue where gateway operator restores with `force_drop_db` failed because required privileges were missing and partitioned indexes caused errors during `pg_restore`. AAP-67079

- Fixed an issue where AWX operator restores with `force_drop_db` were ignored, preventing databases from being dropped and recreated as expected. AAP-67078

Receptor

- Fixed an issue where receptor reported “Error locating unit” when running in controller because cancelled work units were deleted prematurely across restarts. AAP-22149

Known issues
Lightspeed

- This update documents that validation of Lightspeed enablement in related ATF pipelines is part of ongoing work, with pipelines verified for coverage. AAP-66885

Developer preview
Controller

- This update introduces a developer preview of the dispatcherd feature flag for automation controller in Ansible Automation Platform 2.6, allowing early evaluation of the new task system engine ahead of general availability. AAP-58535

Rebase
Platform-installer

- This update rebases the platform installer to `ansible.platform` collection version 2.6.20260306, aligning installer content with the current collection version. AAP-67549

Platform-operator

- This update rebases the platform operator to `ansible.platform` collection version 2.6.20260306, ensuring operator-managed resources use the current collection baseline. AAP-67550
