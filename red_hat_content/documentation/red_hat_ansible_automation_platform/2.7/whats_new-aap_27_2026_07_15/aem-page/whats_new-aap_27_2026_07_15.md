+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_07_15"
title = "Ansible Automation Platform 2.7 Release Notes - July 15, 2026 - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-overview_of_redhat_ansible_intro/", "Ansible Automation Platform release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_07_15/aem-page/whats_new-aap_27_2026_07_15.html"
last_crumb = "Ansible Automation Platform 2.7 Release Notes - July 15, 2026"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Ansible Automation Platform 2.7 Release Notes - July 15, 2026"
oversized = "false"
page_slug = "whats_new-aap_27_2026_07_15"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_07_15"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_07_15/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform 2.7 Release Notes - July 15, 2026

The following release notes detail the CVEs and Bug fixes for the Ansible Automation Platform patch released on July 15, 2026.

This release includes the following components and versions:

| Release Date      | Component versions                                                                                                                                                                                       |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>July 15, 2026 | Automation controller 4.8.3Automation hub 4.12.3Event-Driven Ansible 1.3.4Container-based installer Ansible Automation Platform (bundle) 2.7-3Container-based installer Ansible Automation Platform (online) 2.7-3Receptor 1.6.6 |

CSV Versions in this release:

- Namespace-scoped bundle: aap-operator.v2.7.0-0.1783928748
- Cluster-scoped bundle: aap-operator.v2.7.0-0.1783928796

## Overview

Red Hat Ansible Automation Platform 2.7.20260715 delivers a broad set of improvements across the platform, including new features for analytics export, Avro event support in Event-Driven Ansible, and configurable job variable prefixes in Automation Controller. This release also addresses multiple CVEs across Receptor, Lightspeed, and the metrics service, hardens security for execution environments and cookie handling, and resolves numerous bugs affecting the UI, containerized installer, operator deployments, and platform metrics. Performance optimizations to RBAC filtering, job output scrolling, and API call reduction improve responsiveness at scale.

## Highlights

- **Automation Dashboard CSV export** — Export dashboard data to CSV for offline analysis and reporting.
- **Avro & Schema Registry support in Event-Driven Ansible** — Rulebook activations can now consume Avro-encoded events with Schema Registry integration.
- **Configurable job variable prefixes** — New `INCLUDE_DEPRECATED_AWX_VAR_PREFIX` setting allows disabling the deprecated `awx_` prefix in job extra_vars.
- **Candlepin certificate integration** — Analytics authentication now supports Candlepin certificates.
- **Technical Marketing content in Intelligent Assistant** — The chatbot can now answer questions about AAP use cases and solution architectures from official Red Hat content.
- **Execution environment with ansible-core 2.20** — A new ee-minimal image tag provides ansible-core 2.20 alongside the existing 2.16-based image.
- **Pod affinity/anti-affinity for EDA operator** — Fine-grained scheduling control for EDA component pods on OpenShift.

## Features

## Controller

- The controller now logs the `request_id`, `account_number`, and `org_id` from the ingress API response after a successful `gather_analytics` tarball upload. Previously, this response data was silently discarded, requiring support engineers to manually patch the controller source code to trace analytics uploads through Kibana. The new log entry appears at INFO level in `task_system.log` and can be searched directly by `request_id` or `account_number` to correlate controller uploads with backend ingestion. (AAP-79940)
- The controller now logs the `request_id`, `account_number`, and `org_id` from the ingress API response after a successful `gather_analytics` tarball upload. Previously, this response data was silently discarded, requiring support engineers to manually patch the controller source code to trace analytics uploads through Kibana. The new log entry appears at INFO level in `task_system.log` and can be searched directly by `request_id` or `account_number` to correlate controller uploads with backend ingestion. (AAP-79937)
- The hardcoded JOB_VARIABLE_PREFIXES constant (['awx', 'tower']) has been replaced with a configurable INCLUDE_DEPRECATED_AWX_VAR_PREFIX boolean setting at /api/v2/settings/jobs/. When enabled (default), both awx_ and tower_ prefixed variables are injected into job extra_vars, preserving backward compatibility. When disabled, only the tower_ prefix is used, eliminating the duplicate variables. The awx_ prefix is deprecated and this setting will default to False in a future release. (AAP-76713)
- The hardcoded JOB_VARIABLE_PREFIXES constant (['awx', 'tower']) has been replaced with a configurable INCLUDE_DEPRECATED_AWX_VAR_PREFIX boolean setting at /api/v2/settings/jobs/. When enabled (default), both awx_ and tower_ prefixed variables are injected into job extra_vars, preserving backward compatibility. When disabled, only the tower_ prefix is used, eliminating the duplicate variables. The awx_ prefix is deprecated and this setting will default to False in a future release. (AAP-73395)
- Implement Candlepin certificate integration for analytics authentication. (AAP-72996)

## Event-driven Ansible

- Add Avro support. (AAP-67399)
- Add Avro support with Schema Registry. (AAP-67396)
- Add Avro support. (AAP-67395)

**AVRO support for the Kafka event source**

The Kafka source plugin in the `ansible.eda` collection now supports AVRO-encoded messages, enabling Event-Driven Ansible to process events from Kafka topics that use AVRO as their serialization format. You can provide the AVRO schema directly in your rulebook source configuration or retrieve it automatically from a Schema Registry URL. This feature supports integration with large-scale data platforms and data engineering pipelines where AVRO is the serialization standard.

## Metrics dashboard

- Adding CSV export for the Automation Dashboard data. (AAP-80914)
- Adding telemetry reporting for the Automation Dashboard. (AAP-80534)
- Adding the CSV export of the Automation Dashboard data. (AAP-72828)

## Enhancements

## General

- Resource sync now supports the following configurable settings: RESOURCE_SYNC_JWT_EXPIRATION — sets the JWT service token’s lifetime (default=60s). RESOURCE_SYNC_PAGE_SIZE — The number of role assignments fetched per page (default=50) during sync. Increasing this value reduces the overall number of API calls, and can help avoid pagination-related failures when there are a large number of assignments. Note that this value is capped by Gateway’s `MAX_PAGE_SETTING`. (AAP-74180)
- Added post logout redirect URI text box to the UI for setting allowed post logout redirect URIs, following the same rules as redirect URI. Enabled single log out in AAP at GET /o/logout, making the endpoint discoverable at the OIDC discovery endpoint. (AAP-76276)
- Resolved an issue in which related users (both from the User Access tab on resources and from within the User tab on Organizations) would not load. General performance of these related lists was also addressed. (AAP-80449)

## Aap-gateway, platform-operator

- Unifying collectors between the Automation Dashboard and the metrics service. (AAP-76646)

## Aap-ui

- Access Management page tooltips updated. (AAP-81789)
- Page header and descriptions are updated. (AAP-81788)
- Improved scrolling performance on the Job Output page. Scroll events are now throttled and consolidated, reducing unnecessary re-renders and providing smoother output viewing during job execution. (AAP-81786)
- Tooltips are updated in Settings area. (AAP-81385)
- Disabled counting to endpoints that didn’t require pagination to improve performance. (AAP-80376)
- Subscription banner is hidden for non-admin users. (AAP-74241)
- Optional analytics step removed from the subscription wizard. Analytics is now auto-enabled when using a Red Hat service account, Red Hat Satellite credentials or a Red Hat username and password. (AAP-72995)

## Containerized installer

- A new `postgresql_skip_data` variable allows skipping the PostgreSQL dump and restore steps during backup and restore operations. (AAP-79643)

## Controller

- Performance: Optimized RBAC permission filtering for non-superuser API requests to /api/v2/unified_jobs/ and /api/v2/unified_job_templates/. Replaced an inefficient 3-table JOIN in UnifiedJobTemplate.accessible_pk_qs() with a direct subquery using _actor_role_filter(), eliminating an unnecessary scan of the dab_rbac_objectrole table. This reduces query latency for non-superuser users, particularly at scale. (AAP-78350)

## Event-driven Ansible

- Provide the EDA API endpoint parity to expose local EDA roles. (AAP-79305)
- Implement encryption key rotation mechanism for Event-Driven Ansible. (AAP-77158)
- Performance tests. (AAP-73124)
- Performance testing. (AAP-73122)

## Execution environments

Collection updates:

| Collection                       | Version change  |
| -------------------------------- | --------------- |
| ansible.controller               | 4.8.2 → 4.8.3   |
| ansible.hub                      | 1.0.6 → 1.1.0   |
| ansible.netcommon                | 8.5.0 → 8.5.3   |
| ansible.posix                    | 2.1.0 → 2.2.0   |
| ansible.utils                    | 6.0.1 → 6.0.3   |
| ansible.windows                  | 3.5.0 → 3.6.1   |
| cisco.intersight                 | 2.17.0 → 2.20.0 |
| hashicorp.vault                  | 1.1.1 → 1.2.0   |
| kubernetes.core                  | 6.3.0 → 6.4.0   |
| microsoft.ad                     | 1.10.0 → 1.11.0 |
| microsoft.hyperv                 | 1.0.0 → 1.1.0   |
| microsoft.iis                    | 1.1.0 → 1.2.0   |
| redhat.amq\_broker               | 2.3.5 → 2.3.6   |
| redhat.jws                       | 2.1.2 → 2.1.4   |
| redhat.openshift\_virtualization | 2.2.4 → 2.3.0   |
| redhat.rhbk                      | 3.0.1 → 3.0.2   |
| redhat.runtimes\_common          | 1.2.3 → 1.2.5   |
| redhat.sap\_install              | 1.8.0 → 1.9.2   |
| redhat.satellite                 | 5.10.0 → 5.11.0 |
| servicenow.itsm                  | 2.13.2 → 2.15.1 |
| vmware.vmware\_rest              | 4.10.0 → 4.11.0 |

(AAP-81480)

## Execution environments

- AAP 2.7 now provides an additional ee-minimal image using ansible-core 2.20. To use this image, select the 2.20 tag from the AAP 2.7 ee-minimal container in Software Catalog. This does not impact your use of the existing AAP 2.7 ee-minimal, which continues to use ansible-core 2.16. (AAP-77755)

## Lightspeed

- Technical Marketing Content Support on Automation Intelligent Assistant. Automation Intelligent Assistant can now answer questions about AAP use cases and solution architectures by drawing on official Red Hat Technical Marketing content (solution guides and reference architectures). This content is ingested automatically during the build process; no user action is needed. (AAP-74445)
- Technical Marketing Content Support on Automation Intelligent Assistant. Automation Intelligent Assistant can now answer questions about AAP use cases and solution architectures by drawing on official Red Hat Technical Marketing content (solution guides and reference architectures). This content is ingested automatically during the build process; no user action is needed. (AAP-74287)
- AAP gateway server metadata to advertise the revocation_endpoint and code_challenge_methods_supported. (AAP-80508)
- MCP telemetry HMAC key, installer ID, internal email domains, and backup/restore. (AAP-73481)

## Metrics dashboard, metrics service

- Unifying job collectors between the Automation Dashboard and the metrics service. (AAP-76651)

## Metrics dashboard

- Adding the currency sign to all the appropriate Automation Dashboard values. (AAP-74365)

## Metrics service

- Improved handling of failed tasks. Tasks will now log as warning instead of error unless the task can’t be retried. (AAP-77933)

## Platform operator

- Added pod affinity and anti-affinity configuration support to EDA operator component deployments (API, default worker, activation worker, event stream, and UI), enabling users to control pod scheduling placement across cluster nodes. (AAP-82329)
- Added the postgres_skip_data option to the Backup and Restore custom resources, allowing users to back up and restore the database schema without including the data. (AAP-80276)
- Lowered Ansible log verbosity to the default (0) and documented how to increase through the Ansible Operator SDK. (AAP-74950)
- Added proxy variables for operator deployments. Enabled proxy-aware for the AAP operator bundle. (AAP-74859)

## Deprecated functionality

## Platform operator

- Deprecated postgres_keep_pvc_after_upgrade for the automation hub operator. (AAP-78558)
- Deprecated postgres_keep_pvc_after_upgrade for lightspeed operator. (AAP-78556)
- Deprecated postgres_keep_pvc_after_upgrade for the EDA controller operator. (AAP-78554)
- Deprecated postgres_keep_pvc_after_upgrade for the controller operator. (AAP-78552)

## CVE

## Ansible-core

- [CVE-2026-11332](http://access.redhat.com/security/cve/CVE-2026-11332) – ansible-core: Argument injection in ansible-galaxy role install leads to arbitrary code execution in:
  * `ansible-core`. AAP-78066

## Automation Hub

- [CVE-2026-12701](https://access.redhat.com/security/cve/cve-2026-12701) - A path traversal vulnerability was found in pulpcore's relative_path_validator:
  * `hub-rhel9`. AAP-80306

## Ansible Automation Platform Gateway

- Gateway: JWCrypto memory exhaustion via crafted compressed JWE tokens
  * [CVE-2026-39373](http://access.redhat.com/security/cve/CVE-2026-39373) – JWCrypto: Memory exhaustion via crafted compressed JWE tokens in:
    + `gateway-rhel9`. AAP-76360
  * [CVE-2026-12382](https://access.redhat.com/security/cve/cve-2026-12382) - Missing requestHeadersToRemove allows mTLS bypass via Subject header spoofing.     + `gateway-rhel9`. AAP-79212

## Ansible Automation Platform Lightspeed

- Lightspeed: python-multipart denial of service and vLLM authentication bypass
  * [CVE-2026-42561](http://access.redhat.com/security/cve/CVE-2026-42561) – python-multipart: Denial of Service via excessive multipart part headers in:
    + `mcp-tools-rhel9`. AAP-81778
    + `lightspeed-chatbot-rhel9`. AAP-81685
  * [CVE-2026-48746](http://access.redhat.com/security/cve/CVE-2026-48746) – vLLM: Critical authentication bypass allows unauthorized API access in:
    + `mcp-tools-rhel9`. AAP-80311
- Lightspeed: Guardrail bypass via system_prompt parameter injection
  * [CVE-2026-XXXXX](http://access.redhat.com/security/cve/CVE-2026-XXXXX) – Guardrail bypass via system_prompt parameter injection in:
    + `lightspeed-chatbot-rhel9`. AAP-65101

## Ansible Automation Platform Metrics service

- Metrics service: PyJWT authentication bypass and urllib3 vulnerabilities
  * [CVE-2026-48526](http://access.redhat.com/security/cve/CVE-2026-48526) – PyJWT: Authentication bypass due to forged JSON Web Tokens; bumped to 2.13.0 in:
    + `metrics-service`. AAP-78040
  * [CVE-2026-44431](http://access.redhat.com/security/cve/CVE-2026-44431) – urllib3: Information disclosure via cross-origin redirects; bumped to 2.7.0 in:
    + `metrics-service`. AAP-76519
  * [CVE-2026-44432](http://access.redhat.com/security/cve/CVE-2026-44432) – urllib3: Denial of Service due to excessive HTTP response decompression; bumped to 2.7.0 in:
    + `metrics-service`. AAP-76267

## Ansible Automation Platform Receptor

- Receptor: Go dependency vulnerabilities addressed
  * [CVE-2026-27136](http://access.redhat.com/security/cve/CVE-2026-27136) – golang.org/x/net/html: Cross-Site Scripting via HTML parsing bypass in:
    + `receptor`. AAP-81360
    + `receptor-rhel9`. AAP-81359
  * [CVE-2026-27145](http://access.redhat.com/security/cve/CVE-2026-27145) – golang crypto/x509: Denial of Service via excessive processing of DNS SAN entries in:
    + `receptor`. AAP-80904
    + `receptor-rhel9`. AAP-80903
  * [CVE-2026-39821](http://access.redhat.com/security/cve/CVE-2026-39821) – golang.org/x/net/idna: Privilege escalation via incorrect Punycode label processing; dependency updated to v0.55.0 in:
    + `receptor-rhel9`. AAP-78516
    + `receptor`. AAP-78502

## Bug fixes

## General

- Fixed an issue where GitHub OAuth2 login failed on first attempt and did not use the proper GitHub username. (AAP-77967)
- Fixed an issue where the activity stream did not accurately reflect changes made to the oauth2accesstoken model. (AAP-75584)

## Aap-gateway, platform-operator

- Fixed an issue where setting a component to disabled broke the gateway operator. (AAP-80463)
- Fixed an issue where the AAP operator did not correctly restore deployment replicas after `idle_aap` was toggled from `true` back to `false`. Child custom resources retained `idle_deployment: true` permanently, keeping all deployments scaled to zero replicas even after un-idling. (AAP-79036)

## Aap-gateway, aap-security

- Fixed an issue where the Subject header could be spoofed on mTLS Event Streams connections; Envoy now always strips client-provided values. (AAP-79247)

## Aap-ui

- Fixed an issue where the job output view switched from flat mode to tree mode after a running job completed, causing an unexpected layout change and loss of scroll position. (AAP-82278)
- Fixed an issue where filtering by user dropdown caused a page crash. (AAP-82269)
- Fixed an issue where filtering by user dropdown did not work correctly. (AAP-82104)
- Fixed an issue where UI warnings were not handled gracefully when Controller was unavailable. (AAP-81791)
- Fixed an issue where the "launched by" filter was missing from the jobs list. (AAP-81679)
- Fixed an issue where excessive API calls were made from the Jobs page. (AAP-81211)
- Fixed an issue where user search was case sensitive. (AAP-80466)
- Fixed an issue where false values were not handled correctly in the external credential test modal. (AAP-80377)
- Fixed an issue where stale prompt values persisted in the Workflow Visualizer when switching a workflow node’s job template, which could cause save failures or incorrect job configuration. (AAP-79858)
- Fixed an issue where the Inventory "Add Group" modal search functionality was broken. (AAP-79102)
- Fixed an issue where the brand logo in the "About" modal did not appear correctly when accessed from certain pages. (AAP-72839)
- Fixed an issue where polling retries did not work correctly upon timeout. (AAP-73647)

## Aap-ui, lightspeed

- Fixed an issue where the AAP chatbot CSRF usage was not properly enhanced. (AAP-79676)

## Containerized installer

- Fixed an issue where multi-node restore failed because pg_dump assertion failed on secondary nodes. (AAP-82404)
- Fixed an issue where Podman pull operations could hang indefinitely; a configurable timeout is now enforced. (AAP-79696)
- Fixed an issue where containerized uninstall failed on automationmetrics firewalld task with `_automationmetrics_ports` undefined. (AAP-79624)
- Fixed an issue where Automation Controller backup included non-manual project directories, increasing backup size unnecessarily. (AAP-79525)
- Fixed an issue where the Strict-Transport-Security header was missing from nginx responses. (AAP-76048)
- Fixed an issue where certain containerized installer operations failed. (AAP-79055)

## Containerized installer, metrics service

- Fixed an issue where the service_index_path was missing. (AAP-82225)
- Fixed an issue where the metrics service did not default to the name set for the Controller database name. (AAP-80786)

## Controller

- Fixed an issue where constructed inventories increased the host count in the dashboard. (AAP-80065)
- Fixed an issue where instances reporting cpu=0 or memory=0 with no errors were transitioned to READY state with non-zero capacity, making them appear healthy and schedulable. Zero cpu/memory is now treated as an error condition so the node is marked offline until a valid health check is received. (AAP-79735)
- Fixed an issue where health check returned with 0 cpu and 0 memory but the node was marked as healthy with 1 capacity instead of re-running the health check. (AAP-79733)
- Fixed an issue where custom credential types with file injectors failed to set environment variables during job execution after the 2.7 upgrade. File injection now uses a two-pass approach to ensure all paths are available for cross-references. (AAP-78147)
- Fixed an issue where raw SQL was used in the stdout copy query; replaced with psycopg composable SQL using sql.Identifier/sql.Literal for safe construction. (AAP-77740)
- Fixed an issue where giving a user admin permission to a notification template caused a server error. (AAP-77108)

## Controller, platform-collection

- Fixed an issue where the collection did not automatically retry transient HTTP errors. The collection now retries with exponential backoff for 502, 503, 500, or 504 errors. (AAP-72706)

## Event-driven Ansible

- Fixed an issue where transient Kubernetes API errors could cause rulebook activations to enter an unrecoverable error state, leading to orphaned activation pods and duplicate pod spawning. Activations now retry on transient errors and automatically recover. (AAP-80939)
- Fixed an issue where health checks were included in activation create and enable actions; removed to restore prior behavior. (AAP-80331)
- Fixed an issue where health checks targeted the wrong activation queue in multi-node podman deployments. (AAP-75771)
- Fixed an issue where certain EDA operations failed unexpectedly. (AAP-75150)

## Execution environments

- Fixed an issue where CVE-2025-57847 allowed exploitation via a writable /etc/passwd; hardened to read-only (644) with nss_wrapper for user identity resolution. (AAP-80787)
- Fixed an issue where CVE-2025-57847 allowed exploitation via a writable /etc/passwd; hardened to read-only (644) with nss_wrapper for user identity resolution. (AAP-66952)

## Lightspeed

- Fixed an issue where the intelligent assistant chatbot displayed raw tool call tokens instead of executing tools when using non-Granite LLM providers. (AAP-81979)
- Fixed an issue where cookie security was not sufficiently hardened. (AAP-78305)
- Fixed an issue where raw tool calls were showing in the UI when using Azure model provider. (AAP-73593)
- Fixed an issue where cookie security was not sufficiently hardened. (AAP-61711)
- Fixed an issue where certain Lightspeed operations failed. (See AAP-78467) (AAP-60942)
- MCP servers now automatically inherit custom CA certificates configured at the platform level (bundle_cacert_secret), enabling proper SSL certificate validation for self-signed or internal certificates without requiring manual configuration or disabling certificate validation. (AAP-78387)

## Metrics service, platform operator

- Fixed an issue where metrics-service tasks failed on startup. (AAP-80668)

## Metrics service, platform installer

- Fixed an issue where backup and restore operations failed for the metrics service. (AAP-76638)

## Metrics service

- Fixed an issue where the datestyle variable was incorrectly passed to the metrics service. (AAP-79828)
- Fixed an issue where Metrics Feature Enablement did not work with environment variables; previous DB settings now correctly interact with environment variables. (AAP-78063)
- Fixed an issue where dispatcherd hourly collector tasks were permanently orphaned when a pg_notify message was lost during container restart. (AAP-74311)

## Performance and scale

- Fixed an issue where the dispatcher minimum worker pool was not configurable; set minimum to 4 and added new setting DISPATCHER_MIN_WORKERS. (AAP-76982)

## Platform operator

- Fixed an issue where the Automation Controller liveness probe was configured with an incorrect supervisord configuration filename. (AAP-76616)
- Fixed an issue where general operator bugs caused unexpected behavior. (AAP-75642)
- Fixed an issue where the gateway operator could reference a stale pod name during upgrades, causing a 7.5 minute timeout per reconciliation loop. The operator now refreshes the gateway pod name variable before post-install operations. (AAP-74954)

## Known issues

*(No known issues reported for this release.)*
