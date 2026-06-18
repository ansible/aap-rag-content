+++
title = "Ansible Automation Platform patch release June 3, 2026 - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-2.6_2026_06_03"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-async_updates/", "Patch releases"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-2.6_2026_06_03/aem-page/whats_new-2.6_2026_06_03.html"
last_crumb = "Ansible Automation Platform patch release June 3, 2026"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Ansible Automation Platform patch release June 3, 2026"
oversized = "false"
page_slug = "whats_new-2.6_2026_06_03"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-2.6_2026_06_03"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-2.6_2026_06_03/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform patch release June 3, 2026

The following release notes detail the CVEs and Bug fixes for the Ansible Automation Platform patch released on June 3, 2026

This release includes the following components and versions:

| Release Date     | Component versions                                                                                                                                                                                                                                                                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>June 3, 2026 | Automation controller 4.7.12Automation hub 4.11.9Event-Driven Ansible 1.2.8Container-based installer Ansible Automation Platform (bundle) 2.6-9Container-based installer Ansible Automation Platform (online) 2.6-9Receptor 1.6.5RPM-based installer Ansible Automation Platform (bundle) 2.6-7RPM-based installer Ansible Automation Platform (online) 2.6-7 |


CSV Versions in this release:

- namespace - aap-operator.v2.6.0-0.1780320900 2.6
- cluster - aap-operator.v2.6.0-0.1780320904


This release includes important security updates, bug fixes, and enhancements across Ansible Automation Platform components. Notable updates include fixes for multiple CVEs affecting cryptography dependencies, performance improvements for database queries and resource synchronization, enhanced proxy support for operators, and various UI improvements. This release also updates the minimum RHEL version requirement to 9.6 for both RPM and containerized installations.

## Enhancements

## Automation controller

- Installed collections and ansible version are now available in the database even when the Indirect counting feature flag is off. (AAP-76808)

## Containerized installer

- The containerized installer now requires RHEL 9.6 as the minimum version. (AAP-69789)

## Django-ansible-base

- Resource sync now supports the following configurable settings: `RESOURCE_SYNC_JWT_EXPIRATION` — sets the JWT service token’s lifetime (default==60s); `RESOURCE_SYNC_PAGE_SIZE` — the number of role assignments fetched per page (default==50) during sync. Increasing this value reduces the overall number of API calls and can help avoid pagination-related failures when there are a large number of assignments. Note that this value is capped by Gateway’s `MAX_PAGE_SETTING`. (AAP-74179)

## Platform operator

- Added proxy variables for operator deployments. (AAP-73664)
- Added proxy variables for operator deployments. (AAP-73662)

## Platform UI

- Subscription banner is hidden for non-admin users since they cannot act on it. (AAP-74243)

## Deprecated

## Lightspeed

- CVE Bucket - ansible-chatbot-stack 2.6. (AAP-74118)

## CVE

## Automation controller

- [CVE-2026-39892](https://access.redhat.com/security/cve/cve-2026-39892) – Cryptography: Buffer overflow via non-contiguous buffer in API:
  * `automation-controller` for Ansible Automation Platform 2.6. AAP-75026
- [CVE-2026-33154](https://access.redhat.com/security/cve/cve-2026-33154) – Dynaconf: Arbitrary code execution via Server-Side Template Injection:
  * `controller-rhel9` for Ansible Automation Platform 2.6. AAP-69464
- [CVE-2026-30922](https://access.redhat.com/security/cve/cve-2026-30922) – pyasn1: Denial of service via unbounded recursion:
  * `automation-controller` for Ansible Automation Platform 2.6. AAP-69044

## Event-driven Ansible

- CVE – PGNotify SQL Injection via Dollar-Quote Escape in Unauthenticated Event Stream Payload:
  * `event-driven-ansible` for Ansible Automation Platform 2.6. AAP-77313
- [CVE-2026-39892](https://access.redhat.com/security/cve/cve-2026-39892) – Cryptography: Buffer overflow via non-contiguous buffer in API:
  * `eda-controller-rhel9` for Ansible Automation Platform 2.6. AAP-75028

## Execution environments

- [CVE-2026-39892](https://access.redhat.com/security/cve/cve-2026-39892) – Cryptography: Buffer overflow via non-contiguous buffer in API:
  * `ee-minimal-rhel9` for Ansible Automation Platform 2.6. AAP-75242
  * `ee-supported-rhel9` for Ansible Automation Platform 2.6. AAP-75029

## Gateway

- [CVE-2026-39892](https://access.redhat.com/security/cve/cve-2026-39892) – Cryptography: Buffer overflow via non-contiguous buffer in API:
  * `gateway-rhel9` for Ansible Automation Platform 2.6. AAP-75030

## Hub

- [CVE-2026-40192](https://access.redhat.com/security/cve/cve-2026-40192) – Pillow: Denial of service via decompression bomb in FITS image processing:
  * `hub-rhel9` for Ansible Automation Platform 2.6. AAP-72157
- [CVE-2026-33154](https://access.redhat.com/security/cve/cve-2026-33154) – Dynaconf: Arbitrary code execution via Server-Side Template Injection:
  * `hub-rhel9` for Ansible Automation Platform 2.6. AAP-69467

## Lightspeed

- [CVE-2026-48710](https://access.redhat.com/security/cve/cve-2026-48710) – Starlette: Security restriction bypass via malformed HTTP Host header:
  * `ansible-chatbot-stack` for Ansible Automation Platform 2.6. AAP-76898
  * `aap-rag-content` for Ansible Automation Platform 2.6. AAP-76897
  * `lightspeed-chatbot-rhel9` for Ansible Automation Platform 2.6. AAP-76895
- [CVE-2026-42203](https://access.redhat.com/security/cve/cve-2026-42203)– LiteLLM: Arbitrary code execution via unsandboxed prompt templates:
  * `lightspeed-chatbot-rhel9` for Ansible Automation Platform 2.6. AAP-75260
- [CVE-2026-39892](https://access.redhat.com/security/cve/cve-2026-39892) – Cryptography: Buffer overflow via non-contiguous buffer in API:
  * `ansible-ai-connect-service` for Ansible Automation Platform 2.6. AAP-75140
  * `mcp-tools-rhel9` for Ansible Automation Platform 2.6. AAP-75036
  * `lightspeed-chatbot-rhel9` for Ansible Automation Platform 2.6. AAP-75032
- [CVE-2026-6321](https://access.redhat.com/security/cve/cve-2026-6321) – fast-uri: Path traversal vulnerability allows bypass of security policies:
  * `lightspeed-chatbot-rhel9` for Ansible Automation Platform 2.6. AAP-74329
  * `lightspeed-rhel9` for Ansible Automation Platform 2.6. AAP-74327
- [CVE-2026-41140](https://access.redhat.com/security/cve/cve-2026-41140) – Poetry: Path traversal vulnerability allowing arbitrary file write via malicious package extraction:
  * `lightspeed-chatbot-rhel9` for Ansible Automation Platform 2.6. AAP-73073
- [CVE-2026-41680](https://access.redhat.com/security/cve/cve-2026-41680) – Marked: Denial of service via specific input sequence:
  * `mcp-server-rhel9` for Ansible Automation Platform 2.6. AAP-73067
- [CVE-2026-40217](https://access.redhat.com/security/cve/cve-2026-40217) – LiteLLM: Arbitrary code execution via bytecode rewriting:
  * `lightspeed-chatbot-rhel9` for Ansible Automation Platform 2.6. AAP-71719
- [CVE-2026-40192](https://access.redhat.com/security/cve/cve-2026-40192) – Pillow: Denial of service via decompression bomb in FITS image processing:
  * `lightspeed-chatbot-rhel9` for Ansible Automation Platform 2.6. AAP-72158
- [CVE-2026-39363](https://access.redhat.com/security/cve/cve-2026-39363) – Vite: Information disclosure via WebSocket connection bypasses access control:
  * `mcp-server-rhel9` for Ansible Automation Platform 2.6. AAP-71094
- [CVE-2026-39364](https://access.redhat.com/security/cve/cve-2026-39364) – Vite: Information disclosure via query parameter manipulation on the development server:
  * `mcp-server-rhel9` for Ansible Automation Platform 2.6. AAP-71084
- [CVE-2026-28684](https://access.redhat.com/security/cve/cve-2026-28684) – python-dotenv: Arbitrary file overwrite via symbolic link following:
  * `mcp-tools-rhel9` for Ansible Automation Platform 2.6. AAP-72565
  * `lightspeed-chatbot-rhel9` for Ansible Automation Platform 2.6. AAP-72564
- [CVE-2026-23490](https://access.redhat.com/security/cve/cve-2026-23490) – pyasn1: Denial of service due to memory exhaustion from malformed RELATIVE-OID:
  * `lightspeed-chatbot-rhel9` for Ansible Automation Platform 2.6. AAP-72598
- [CVE-2026-28390](https://access.redhat.com/security/cve/cve-2026-28390) – OpenSSL: Denial of service due to NULL pointer dereference in CMS EnvelopedData processing:
  * `lightspeed-chatbot-rhel9` for Ansible Automation Platform 2.6. AAP-71124
- [CVE-2025-62718](https://access.redhat.com/security/cve/cve-2026-62718) – Axios: Server-Side Request Forgery and proxy bypass due to improper hostname normalization:
  * `lightspeed-rhel9` for Ansible Automation Platform 2.6. AAP-71548

## Metrics service

- [CVE-2026-39892](https://access.redhat.com/security/cve/cve-2026-39892) – Cryptography: Buffer overflow via non-contiguous buffer in API:
  * `metrics-service-rhel9` for Ansible Automation Platform 2.6. AAP-75037

## Packaging

- [CVE-2026-7246](https://access.redhat.com/security/cve/cve-2026-7246) – Click: Arbitrary command execution via command injection in click.edit():
  * `python3.12-click` for Ansible Automation Platform 2.6. AAP-74034
- [CVE-2026-32283](https://access.redhat.com/security/cve/cve-2026-32283) – Go: Denial of service via multiple TLS 1.3 key update messages:
  * `automation-gateway-proxy` for Ansible Automation Platform 2.6. AAP-71649
- [CVE-2026-32280](https://access.redhat.com/security/cve/cve-2026-32280) – Go: Denial of service vulnerability in certificate chain building:
  * `automation-gateway-proxy` for Ansible Automation Platform 2.6. AAP-71613

## Platform UI

- [CVE-2026-40175](https://access.redhat.com/security/cve/cve-2026-40175) – Axios: Remote code execution via prototype pollution escalation:
  * `automation-platform-ui` for Ansible Automation Platform 2.6. AAP-73004
- [CVE-2026-27904](https://access.redhat.com/security/cve/cve-2026-27904) – Minimatch: Denial of service via catastrophic backtracking in glob expressions:
  * `automation-platform-ui` for Ansible Automation Platform 2.6. AAP-73044
- [CVE-2026-39363](https://access.redhat.com/security/cve/cve-2026-39363) – Vite: Information disclosure via WebSocket connection bypasses access control:
  * `gateway-rhel9` for Ansible Automation Platform 2.6. AAP-71092
  * `automation-platform-ui` for Ansible Automation Platform 2.6. AAP-71091
- [CVE-2026-4800](https://access.redhat.com/security/cve/cve-2026-4800) – lodash: Arbitrary code execution vulnerability in _.template imports:
  * `automation-platform-ui` for Ansible Automation Platform 2.6. AAP-70460
- [CVE-2026-33891](https://access.redhat.com/security/cve/cve-2026-33891) – node-forge: Denial of service via infinite loop in BigInteger.modInverse():
  * `automation-platform-ui` for Ansible Automation Platform 2.6. AAP-70124
- CVE-2026-4926 – path-to-regexp: Denial of service via crafted regular expressions:
  * `automation-platform-ui` for Ansible Automation Platform 2.6. AAP-70023
  * `gateway-rhel9` for Ansible Automation Platform 2.6. AAP-70021

## Receptor

- [CVE-2026-32283](https://access.redhat.com/security/cve/cve-2026-32283) – Go: Denial of service via multiple TLS 1.3 key update messages:
  * `receptor` for Ansible Automation Platform 2.6. AAP-71654
- [CVE-2026-32280](https://access.redhat.com/security/cve/cve-2026-32280) – Go: Denial of service vulnerability in certificate chain building:
  * `receptor` for Ansible Automation Platform 2.6. AAP-71618
- [CVE-2026-32282](https://access.redhat.com/security/cve/cve-2026-32282) – Go: Root.Chmod following symlinks out of the root:
  * `receptor` for Ansible Automation Platform 2.6. AAP-71385

## Bug fixes

## Automation controller

- Fixed an issue where PostgreSQL logs were flooded with "could not receive data from client: Connection reset by peer" messages in AAP 2.6 containerized deployment. DB connections are reused for 10 minutes by default. A user can set a new env var to modify that life cycle. (AAP-76997)
- Fixed an issue where the Automation Calculator page was not working when using an HTTP proxy. Fix analytics API requests to respect proxy environment variables. (AAP-75560)
- Fixed an issue where fact storage had degraded performance. (AAP-74522)
- Fixed an issue where awxkit was missing a packaging dependency in setup.py, causing CLI to fail on clean install. Removed unneeded setuptools and replaced with packaging to resolve `ModuleNotFoundError: No module named 'packaging'`. (AAP-74278)
- Fixed an issue where the GET /api/v2/hosts/ endpoint had slow median response time at scale. Changes include deferring the large `ansible_facts` JSON column from host list queries and eliminating an unnecessary database table JOIN from RBAC permission evaluation queries. (AAP-73161)
- Fixed an issue where the Thycotic Secret Server (Delinea) credential plugin failed with an HTTP 500 error when resolving credentials from Delinea Platform URLs. (AAP-73650)
- Fixed an issue where schedules could not parse a valid rrule that contained certain BYHOUR constraints. (AAP-72483)
- Fixed an issue where the collection automatically retried transient HTTP errors. The collection is revised to automatically retry transient HTTP errors with exponential backoff for 502, 503, 500, or 504 errors. (AAP-72705)
- Fixed an issue where workflow node updates failed when a Job Template had labels without "Prompt on Launch". The serializer now validates only the prompt fields included in the request rather than re-validating all persisted prompt state on every update. (AAP-41742)

## Containerized installer

- Fixed an issue where the Strict-Transport-Security header was missing from nginx responses. (AAP-76052)
- Fixed an issue where CA trust import did not always validate. (AAP-72118)
- Fixed an issue where uploading huge images resulted in a 502 Bad Gateway error. (AAP-55134)

## Containerized installer, Metrics service

- Fixed an issue where a permanent restart loop occurred for automation-metrics-web, automation-metrics-tasks, and automation-metrics-scheduler. (AAP-74797)

## Controller, Platform installer

- Fixed an issue where during the upgrade from 2.4 to 2.6, some groups of SAML settings were missing from the mapping. Fixes a bug with the import of team mappers of SAML authenticators. (AAP-76768)

## Django-ansible-base

- Fixed an issue where an authenticator map of map type allow could not recover access once it had been set to False by an earlier deny-all rule. (AAP-75208)
- Fixed an issue where an authenticator map of map type allow could not recover access once it had been set to False by an earlier deny-all rule. (AAP-75206)

## Execution environments

- Fixed an issue where propcache >==0.5.0 was incompatible with setuptools < 82. (AAP-75088)

## Hub

- Fixed an issue where Automation Hub pods experienced sustained high memory usage under idle conditions. Health probes caused progressive memory growth in pulpcore worker processes. This update provides a version of pulpcore that fixes the memory leak. (AAP-68883)

## Metrics service

- Fixed an issue where the max size of a segment message was exceeded. (AAP-72807)

## Platform installer

- Fixed an issue where documentation URLs in containerized installer sample inventory files were outdated. (AAP-75106)
- Fixed an issue where gateway logging configuration caused a permission issue due to log file ownership mismatch. (AAP-65017)
- Fixed an issue where Hub did not respect X-FORWARDED-FOR and used the wrong host for collection download URLs. Changes the X-Forwarded-Proto default behavior and allows preserving the original protocol header. (AAP-64938)
- Fixed an issue where restore could fail trying to obtain service nodes. (AAP-58792)

## Platform operator

- Fixed an issue where a cluster-scoped operator could not resolve Postgres DB connections when components were installed in other namespaces. (AAP-75066)
- Fixed an issue where a permanent reconciliation failure loop occurred when an interrupted deployment left the Hub route uninitiated and the operator was unable to recover on subsequent reconciliation attempts. (AAP-73224)

## Platform UI

- Fixed an issue where padding was missing where users can select domains on several pages. (AAP-72997)
- Fixed an issue where the collection Documentation tab in automation hub would crash when the API response included large unnecessary fields, causing the page to fail to render. (AAP-72875)
- Fixed an issue where the brand logo in the "About" modal did not appear correctly when the About modal was accessed from any page of the platform UI. (AAP-72689)
- Fixed an issue where the UI continued to poll for updates to workflow_approvals even after the user’s session had timed out. (AAP-72071)
- Fixed an issue where a blank page appeared when loading the legacy UI on Controller. The Controller base URL now redirects to Gateway, mirroring Hub and EDA behavior. (AAP-71925)

## Known issues

## Lightspeed

- Internal file IDs visible in the intelligent assistant’s responses. Depending on the LLM you have integrated, the intelligent assistant’s responses may expose internal file IDs (identified by a `file-` prefix). (AAP-72989)
