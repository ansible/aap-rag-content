+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_08_24"
template = "docs/aem-title.html"
title = "Ansible Automation Platform 2.7 patch release August 24, 2026 (2.7-6) - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-overview_of_redhat_ansible_intro/", "Ansible Automation Platform release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_08_24/aem-page/whats_new-aap_27_2026_08_24.html"
last_crumb = "Ansible Automation Platform 2.7 patch release August 24, 2026 (2.7-6)"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Ansible Automation Platform 2.7 patch release August 24, 2026 (2.7-6)"
oversized = "false"
page_slug = "whats_new-aap_27_2026_08_24"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_08_24"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_08_24/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform 2.7 patch release August 24, 2026 (2.7-6)

The following release notes detail the CVEs and Bug fixes for the Ansible Automation Platform patch released on August 24, 2026

This release includes the following components and versions:

| Release Date    | Component versions                                                                                                                                                                                       |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| August 24, 2026 | Automation controller 4.8.6Automation hub 4.12.5Event-Driven Ansible 1.3.8Container-based installer Ansible Automation Platform (bundle) 2.7-6Container-based installer Ansible Automation Platform (online) 2.7-6Receptor 1.6.7 |

CSV Versions in this release:

- namespace scoped: aap-operator.v2.7.0-0.1787240781
- cluster scoped: aap-operator.v2.7.0-0.1787240540

## Overview

This release of Ansible Automation Platform 2.7.20260824 includes 25 security updates, 16 performance and operational enhancements, and 31 bug fixes across 21 components. The release addresses critical vulnerabilities in Controller, Hub, Lightspeed, and execution environments, with significant performance improvements in RBAC query optimization, database connection management, and memory leak resolution.

## Features

## Aap Metrics

- Added a new Events Collector. (AAP-84990)

## Enhancements

## Aap Gateway

- When the database encryption key is not available or fails to decrypt the values, we now log a better message making that clear. (AAP-88859)

## Aap Metrics

- update pandas version to v3. (AAP-79053)

## Aap UI

- Updated label "Retained version count" to "Retained repository version count" in UI. (AAP-71927)

## Controller

- Fixed a significant per-call performance degradation on the team list RBAC query at scale. The OR-combined RBAC filter prevented PostgreSQL from using optimal per-branch index plans. Replaced with a UNION approach that gives each RBAC branch its own query plan, substantially reducing disk I/O per call. (AAP-83509)
- Fixed a pagination COUNT query regression introduced by the activity stream LEFT JOIN fix (AAP-81873). The RBAC-filtered subquery shape forced PostgreSQL to materialize all subquery results for `COUNT(*)`, causing extremely long query times on large activity stream tables. Replaced with an unfiltered table count for pagination headers while preserving RBAC-filtered page results. (AAP-83935)
- Performance: Web worker database connections now set PostgreSQL statement_timeout derived from the uwsgi harakiri timeout. This prevents abandoned queries from accumulating when uwsgi kills slow workers, reducing database CPU contention under load. The timeout can be overridden via the DATABASE_STATEMENT_TIMEOUT setting. (AAP-85170)
- Fixed a performance regression in the unified jobs list and dashboard endpoints where RBAC-filtered queries were up to 10x slower per database call due to a UNION-based query structure that forced PostgreSQL to materialize all accessible job IDs before applying pagination. The fix pre-computes the user’s role set once and uses single-pass OR filtering, restoring early query exit and eliminating redundant role table scans. (AAP-87313)
- Fixed a performance regression in the unified jobs list and dashboard endpoints where RBAC-filtered queries were up to 10x slower per database call due to a UNION-based query structure that forced PostgreSQL to materialize all accessible job IDs before applying pagination. The fix pre-computes the user’s role set once and uses single-pass OR filtering, restoring early query exit and eliminating redundant role table scans. (AAP-87315)
- Added awx-manage create_host_summary_index management command that creates a composite database index to improve host list page load performance. The command is safe to run on a live system (non-blocking) and can be re-run without side effects. (AAP-87861)

## Execution Environments

- ansible.controller collection: 4.8.5 → 4.8.6 ansible.platform collection: 2.7.20260630 → 2.7.20260805 (AAP-86927)
- ansible-controller-4.8.3→ ansible-controller-4.8.4 (AAP-88525)

## General

- This enhancement ensures the Automation Dashboard is ON by default at upgrade/installation (as per GA requirements) (AAP-81094)
- Added optional pkce_required field to oauth application model (AAP-83388)

## MCP Server for Red Hat Ansible Automation Platform

- AAP 2.7 adds OAuth 2.1 authentication with automatic discovery. (AAP-84895)
- The MCP server for Red Hat Ansible Automation Platform now includes an /mcp/discover endpoint that provides progressive tool discovery and reduces token consumption. Additionally, a new content_discovery toolset is available. This toolset bundles Galaxy content tools and the automation intelligent assistant search tool into a single toolset for content discovery workflows (AAP-81722)

## CVE

## Ansible Lightspeed

- Ansible Lightspeed (container image: ansible-automation-platform-27/gateway-rhel9)
  * [CVE-2026-46625](https://access.redhat.com/security/cve/CVE-2026-46625) – JavaScript Cookie: Cookie attribute manipulation via prototype pollution. AAP-85926
- Ansible Lightspeed (container image: ansible-automation-platform-27/lightspeed-rhel9)
  * [CVE-2026-59886](https://access.redhat.com/security/cve/CVE-2026-59886) – pyasn1: Denial of Service via crafted ASN.1 REAL values. AAP-83757
  * [CVE-2026-69244](https://access.redhat.com/security/cve/CVE-2026-69244) – AIOHTTP: Denial of Service via malformed HTTP responses. AAP-85553
  * [CVE-2026-69243](https://access.redhat.com/security/cve/CVE-2026-69243) – AIOHTTP: HTTP Request Smuggling via WebSocket Upgrade. AAP-85588
  * [CVE-2026-15307](https://access.redhat.com/security/cve/CVE-2026-15307) – Django: Remote code execution via GeoDjango spatial lookups. AAP-85798
  * [CVE-2026-27459](https://access.redhat.com/security/cve/CVE-2026-27459) – DTLS cookie callback buffer overflow. AAP-88249
  * [CVE-2026-27459](https://access.redhat.com/security/cve/CVE-2026-27459) – DTLS cookie callback buffer overflow. AAP-88257

## Automation controller

- Automation controller
  * [CVE-2026-52902](https://access.redhat.com/security/cve/CVE-2026-52902) – path traversal via YAML !include directive. AAP-80013
- Automation controller (container image: ansible-automation-platform-27/controller-rhel9)
  * [CVE-2026-44545](https://access.redhat.com/security/cve/CVE-2026-44545) – daphne: Denial of Service via excessive WebSocket message size. AAP-82613
  * [CVE-2026-71365](https://access.redhat.com/security/cve/CVE-2026-71365) – webhook status callback SSRF leaks the Git PAT. AAP-86687
  * [CVE-2026-44244](https://access.redhat.com/security/cve/CVE-2026-44244) – GitPython: Arbitrary code execution via injected newlines in Git configuration. AAP-88240
  * [CVE-2026-71366](https://access.redhat.com/security/cve/CVE-2026-71366)– notification backends allow SSRF and credential leakage. AAP-86683
  * [CVE-2026-71364](https://access.redhat.com/security/cve/CVE-2026-71364)– project archive extraction allows path traversal file writes. AAP-86690

## Automation gateway container

- Automation gateway container (container image: ansible-automation-platform-27/gateway-rhel9)
  * [CVE-2026-59886](https://access.redhat.com/security/cve/CVE-2026-59886) – pyasn1: Denial of Service via crafted ASN.1 REAL values. AAP-83748

## Automation platform UI

- Automation platform UI
  * [CVE-2026-39363](https://access.redhat.com/security/cve/CVE-2026-39363) – Vite: Information disclosure via WebSocket connection bypasses access control. AAP-74261
- Automation platform UI (container image: ansible-automation-platform-27/gateway-rhel9)
  * [CVE-2026-9595](https://access.redhat.com/security/cve/CVE-2026-9595) – webpack-dev-server: Information disclosure and denial of service via improper proxy configuration. AAP-84063
  * [CVE-2026-44705](https://access.redhat.com/security/cve/CVE-2026-44705) – path Traversal via unsanitized prefix/postfix enables directory escape. AAP-85822
  * [CVE-2026-12143](https://access.redhat.com/security/cve/CVE-2026-12143) – form-data: Form field override via CRLF injection. AAP-85902

## Ansible automation platform

- Ansible automation platform (container image:ansible-automation-platform-27/gateway-rhel9)
  * [CVE-2026-39363](https://access.redhat.com/security/cve/CVE-2026-39363) – Vite: Information disclosure via WebSocket connection bypasses access control. AAP-74261

## Event-Driven Ansible controller

- Event-Driven Ansible controller (container image: ansible-automation-platform-27/eda-controller-rhel9)
  * [CVE-2026-59886](https://access.redhat.com/security/cve/CVE-2026-59886) – pyasn1: Denial of Service via crafted ASN.1 REAL values. AAP-83747

## Execution environments

- Execution environments (container image: ansible-automation-platform-27/ee-minimal-rhel9)
  * [CVE-2026-69244](https://access.redhat.com/security/cve/CVE-2026-69244) – AIOHTTP: Denial of Service via malformed HTTP responses. AAP-85551
  * [CVE-2026-69243](https://access.redhat.com/security/cve/CVE-2026-69243) – AIOHTTP: HTTP Request Smuggling via WebSocket Upgrade. AAP-85586
- Execution environments (container image: ansible-automation-platform-27/ee-supported-rhel9)
  * [CVE-2026-59886](https://access.redhat.com/security/cve/CVE-2026-59886) – pyasn1: Denial of Service via crafted ASN.1 REAL values. AAP-83744
  * [CVE-2026-69244](https://access.redhat.com/security/cve/CVE-2026-69244) – AIOHTTP: Denial of Service via malformed HTTP responses. AAP-85552
  * [CVE-2026-69243](https://access.redhat.com/security/cve/CVE-2026-69243) – AIOHTTP: HTTP Request Smuggling via WebSocket Upgrade. AAP-85587
  * [CVE-2026-27459](https://access.redhat.com/security/cve/CVE-2026-27459) – DTLS cookie callback buffer overflow. AAP-88254
  * [CVE-2026-27459](https://access.redhat.com/security/cve/CVE-2026-27459) – DTLS cookie callback buffer overflow. AAP-88259

## Bug fixes

## Aap Gateway

- Fixed an issue where organization members can now discover and view teams within their organization when assigning permissions. (AAP-84972)
- Fixed an issue where envoy health check intervals and timeouts aligned to prevent timeouts and false node ejection under heavy load. (AAP-85105)
- Fixed an issue where an organization with a large number of role assignments would timeout. (AAP-85660)
- Fixed an issue where updated dependency libraries for jwcrypto to address CVE-2026-39373. (AAP-86141)

## Containerized Installer

- Fixed an issue where lightspeed Containerized installer Error when enabling mcp-tools on day-2 (AAP-86098)
- Fixed an issue where fixed issue with readiness probe that was causing memory leaks. (AAP-89092)

## Controller

- Fixed an issue where fixed an HTTP 500 error when assigning org-scoped roles (such as Organization JobTemplate Admin) to teams via POST /api/controller/v2/role_team_assignments/. The error was caused by a settings mismatch between Controller and Gateway for ANSIBLE_BASE_ALLOW_TEAM_ORG_MEMBER, which caused the Gateway to reject reverse-synced team role assignments containing the member_organization permission. Additionally, reverse-sync failures now log a warning instead of propagating as unhandled server errors. (AAP-85962)
- Fixed an issue where users with insufficient permissions were able to remove other users role assignments (AAP-86293)
- Fixed an issue where fixes an issue where unnecessary project syncs were triggered on multi node clusters (AAP-86621)
- Fixed an issue where fixed migration 0206_jobhostsummary_host_id_idx failing during 2.6→2.7 upgrade when the composite index had been created manually via awx-manage create_host_summary_index or raw SQL. The migration is now idempotent using CREATE INDEX IF NOT EXISTS. (AAP-87829)
- Fixed an issue where revert prior change that added member_organization permission to other organization-level controller roles. (AAP-88479)

## Dispatcherd

- Fixed an issue where now queue names longer than 63 characters will be transformed with UUID5 to work with pg_notify. (AAP-78938)

## Event Driven Ansible

- Fixed an issue where jWT Tokens generated are scoped to activation_instance_id to limit the acess to other activations (AAP-84857)

## General

- Fixed an issue where skip RBAC cached data rebuilding when no migrations were applied in order to speed up the migrate command. (AAP-83966)
- Fixed an issue where optimized N+1 queries in RBAC to optimize for scale. (AAP-85662)
- Fixed an issue where improve the logic used for saving user RBAC claims from Gateway to avoid 8 second or higher processing times at scale. (AAP-85664)
- Fixed an issue where fixed email enforcement edge cases from CVE-2026-6266 backport. (AAP-85715)
- Fixed an issue where improve system performance when creating an item inside of an organization with a lot of permissions assigned. (AAP-85717)
- Fixed an issue where added batched RBAC update support to improve performance of bulk operations. (AAP-85719)
- Fixed an issue where disabled reverse RBAC sync during JWT claims processing to avoid serial permission recomputation that negated bulk assignment improvements. (AAP-85852)
- Fixed an issue where replaced correlated subquery with a JOIN-based annotation for the ansible_id field on role assignment list endpoints, eliminating O(N²) query cost during paginated gateway sync. (AAP-86406)
- Fixed an issue where fixed 503/harakiri timeout on the role_user_access endpoint when listing access for organizations with many users (5000+) by replacing correlated EXISTS subqueries with a collect-IDs approach. (AAP-86408)

## Hub

- Fixed an issue where fixed High Memory Usage in Automation Hub (AAP-84630)

## Lightspeed

- Fixed Ansible Lighspeed OAuth2 Login with PKCE (AAP-86281)
- Fixed an issue where Http404 exception handler causing chatbot 503s (AAP-87903)

## Metrics Dashboard

- Fixed an issue where fixed the display and deduplication of labels in the Label filter (AAP-85445)
- Fixed an issue where fixed a bug where selecting a custom date range was disabling the Save report button in some timezones. (AAP-85644)

## Metrics Service

- Fixed an issue where prefer metrics.ms_awx_readonly_user_secret (the value explicitly set on the platform cr) over metrics_read_token_secret_name (AAP-83681)
- Fixed an issue where fixing minor issue where turning off anonymized did not stop a send to segment task if the timing was wrong (AAP-87824)
- Fixed an issue where auto-remove invalid Content Types potentially created from migrate_service_data command. (AAP-88482)

## Platform Operator

- Fixed an issue where reconciling while idled could leave the AutomationController CR with an empty spec, breaking controller API routing after un-idling (AAP-83609)
