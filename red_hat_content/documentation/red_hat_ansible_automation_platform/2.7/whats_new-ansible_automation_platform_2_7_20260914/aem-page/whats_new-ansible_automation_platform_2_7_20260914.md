+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-ansible_automation_platform_2_7_20260914"
title = "Ansible Automation Platform 2.7 patch release September 14, 2026 (2.7-8) - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-overview_of_redhat_ansible_intro/", "Ansible Automation Platform release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-ansible_automation_platform_2_7_20260914/aem-page/whats_new-ansible_automation_platform_2_7_20260914.html"
last_crumb = "Ansible Automation Platform 2.7 patch release September 14, 2026 (2.7-8)"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Ansible Automation Platform 2.7 patch release September 14, 2026 (2.7-8)"
oversized = "false"
page_slug = "whats_new-ansible_automation_platform_2_7_20260914"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-ansible_automation_platform_2_7_20260914"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-ansible_automation_platform_2_7_20260914/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform 2.7 patch release September 14, 2026 (2.7-8)

The following enhancements and bug fixes have been implemented in this release of Ansible Automation Platform.

This release includes the following components and versions:

| Release Date       | Component versions                                                                                                                                                                                       |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| September 14, 2026 | Automation controller 4.8.8Automation hub 4.12.6Event-Driven Ansible 1.3.10Container-based installer Ansible Automation Platform (bundle) 2.7-8Container-based installer Ansible Automation Platform (online) 2.7-8Receptor 1.6.8 |

CSV Versions in this release:

- namespace scoped: aap-operator.v2.7.0-0.1788930800
- cluster scoped: aap-operator.v2.7.0-0.1788929740

## Overview

Red Hat Ansible Automation Platform 2.7.20260914 is a security and bug fix update. This release delivers critical security patches addressing vulnerabilities in third-party dependencies—including GitPython, sqlparse, Django, AIOHTTP, lxml, brace-expansion, and protobufjs—across multiple platform components. It also introduces NetworkPolicy enforcement for all AAP operator pods on OpenShift, improves secret key rotation and startup failure diagnostics in the gateway, resolves SSO/Social Auth failures with large identity-provider callbacks, and updates bundled Ansible collections in the supported execution environments.

## Features

No new features are included in this release.

## Highlights

- **Security:** GitPython has been updated to 3.1.59 (Automation Controller) and 3.1.57+ (Automation Hub) to address 11 CVEs, including critical remote code execution and arbitrary command injection flaws.
- **Security:** A critical Kubernetes service account token exfiltration vulnerability (CVE[-2026-12564](https://access.redhat.com/security/cve/CVE-2026-12564?__atl_rovo=disable_public_resolution)) in the HashiCorp Vault credential plugin has been resolved; tokens are now audience-scoped and short-lived via the Kubernetes TokenRequest API.
- **Enhancement:** All AAP operator components on OpenShift now enforce NetworkPolicy rules at runtime, restricting pod-to-pod communication to only required paths per OCPSTRAT-819.
- **Bug fix:** Gateway SSO/Social Auth failures with large identity-provider callbacks (Entra ID and similar) have been resolved by increasing the uWSGI request buffer size to 32 KB.

## Enhancements

## Containerized installer

- Gateway uWSGI request buffer size is increased to 32 KB so Entra ID and other SSO logins no longer fail when the callback request exceeds 10 KB. (AAP-89129)

## Execution environments

- The ansible.controller collection version has been updated to 4.8.8. (AAP-91356)

Collection updates:

| Collection        | Version change  |
| ----------------- | --------------- |
| ansible.netcommon | 8.5.3 → 8.6.2   |
| ansible.posix     | 2.2.0 → 2.2.2   |
| ansible.utils     | 6.0.3 → 6.1.0   |
| ansible.windows   | 3.6.1 → 3.8.0   |
| cisco.intersight  | 2.20.0 → 2.21.0 |
| hashicorp.vault   | 1.2.0 → 1.3.0   |
| microsoft.iis     | 1.2.0 → 1.3.0   |
| microsoft.mecm    | 1.0.0 → 2.0.0   |
| redhat.data\_grid | 1.3.3 → 1.3.4   |
| redhat.openshift  | 5.0.0 → 6.0.0   |
| servicenow.itsm   | 2.15.1 → 2.16.0 |

(AAP-89887)

## Platform operator

- The AAP operator now creates NetworkPolicy resources at runtime for Automation Controller pods on AAP 2.7, restricting pod-to-pod communication to only the required paths per OCPSTRAT-819. (AAP-87540)
- The AAP operator now creates NetworkPolicy resources at runtime for Automation Hub pods on AAP 2.7, restricting pod-to-pod communication to only the required paths per OCPSTRAT-819. (AAP-87541)
- The AAP operator now creates NetworkPolicy resources at runtime for Event-Driven Ansible pods on AAP 2.7, restricting pod-to-pod communication to only the required paths per OCPSTRAT-819. (AAP-87542)
- The AAP operator now creates NetworkPolicy resources at runtime for Ansible Lightspeed pods on AAP 2.7, restricting pod-to-pod communication to only the required paths per OCPSTRAT-819. (AAP-87543)
- The AAP operator now creates NetworkPolicy resources at runtime for Automation Platform Gateway pods on AAP 2.7, restricting pod-to-pod communication to only the required paths per OCPSTRAT-819. (AAP-87544)
- The AAP operator now creates NetworkPolicy resources at runtime for Platform Resource Operator pods on AAP 2.7, restricting pod-to-pod communication to only the required paths per OCPSTRAT-819. (AAP-87545)
- The AAP operator now creates NetworkPolicy resources at runtime for Automation Metrics Service pods on AAP 2.7, restricting pod-to-pod communication to only the required paths per OCPSTRAT-819. (AAP-87547)
- Gateway uWSGI request buffer size is increased to 32 KB so Entra ID and other SSO logins no longer fail when the callback request exceeds 10 KB. (AAP-89129)

## CVE

## Automation Platform Gateway

- [CVE-2026-54284](https://access.redhat.com/security/cve/CVE-2026-54284?__atl_rovo=disable_public_resolution) – Denial of service via quadratic CPU consumption in SQL parsing (sqlparse) in:
  * `gateway-rhel9`. AAP-89937
- [CVE-2026-59893](https://access.redhat.com/security/cve/CVE-2026-59893?__atl_rovo=disable_public_resolution) – Denial of service via inefficient SQL parsing (sqlparse) in:
  * `gateway-rhel9`. AAP-89899
- [CVE-2026-71491](https://access.redhat.com/security/cve/CVE-2026-71491?__atl_rovo=disable_public_resolution) – Denial of service via quadratic CPU consumption in comment grouping (sqlparse) in:
  * `gateway-rhel9`. AAP-89815

## Automation platform UI

- [CVE-2026-14257](https://access.redhat.com/security/cve/CVE-2026-14257?__atl_rovo=disable_public_resolution) – Denial of service via memory exhaustion in expand() (brace-expansion) in:
  * `gateway-rhel9`. AAP-85638
- [CVE-2026-69152](https://access.redhat.com/security/cve/CVE-2026-69152?__atl_rovo=disable_public_resolution) – Denial of service via unbounded intermediate arrays (brace-expansion) in:
  * `gateway-rhel9`. AAP-85492
- [CVE-2026-69153](https://access.redhat.com/security/cve/CVE-2026-69153?__atl_rovo=disable_public_resolution) – Information disclosure via crafted sourceMappingURL (PostCSS) in:
  * `gateway-rhel9`. AAP-85476
- [CVE-2026-59877](https://access.redhat.com/security/cve/CVE-2026-59877?__atl_rovo=disable_public_resolution) – Denial of service via crafted .proto schema (protobufjs) in:
  * `gateway-rhel9`. AAP-83853

## Automation Controller

- [CVE-2026-12564](https://access.redhat.com/security/cve/CVE-2026-12564?__atl_rovo=disable_public_resolution) – Kubernetes service account token exfiltration via HashiCorp Vault credential SSRF in:
  * `controller-rhel9`. AAP-79772
- [CVE-2026-15307](https://access.redhat.com/security/cve/CVE-2026-15307?__atl_rovo=disable_public_resolution) – Remote code execution via GeoDjango spatial lookups (Django) in:
  * `controller-rhel9`. AAP-85810
- [CVE-2026-42215](https://access.redhat.com/security/cve/CVE-2026-42215?__atl_rovo=disable_public_resolution) – Rollup: Arbitrary command execution via bypass of dangerous Git option checks (GitPython) in:
  * `controller-rhel9`. AAP-88225
- [CVE-2026-42284](https://access.redhat.com/security/cve/CVE-2026-42284?__atl_rovo=disable_public_resolution) – Arbitrary code execution via improper validation of clone options (GitPython) in:
  * `controller-rhel9`. AAP-88201
- [CVE-2026-67322](https://access.redhat.com/security/cve/CVE-2026-67322?__atl_rovo=disable_public_resolution) – Environment variable exfiltration via attacker-controlled clone URL (GitPython) in:
  * `controller-rhel9`. AAP-86806
- [CVE-2026-67323](https://access.redhat.com/security/cve/CVE-2026-67323?__atl_rovo=disable_public_resolution) – Arbitrary code execution via command injection due to unguarded Git options (GitPython) in:
  * `controller-rhel9`. AAP-86840
- [CVE-2026-67325](https://access.redhat.com/security/cve/CVE-2026-67325?__atl_rovo=disable_public_resolution) – Command injection via Git option prefix abbreviation (GitPython) in:
  * `controller-rhel9`. AAP-86824
- [CVE-2026-69244](https://access.redhat.com/security/cve/CVE-2026-69244?__atl_rovo=disable_public_resolution) – Denial of service via malformed HTTP responses (AIOHTTP) in:
  * `controller-rhel9`. AAP-85562
- [CVE-2026-73620](https://access.redhat.com/security/cve/CVE-2026-73620?__atl_rovo=disable_public_resolution) – Arbitrary file overwrite and read via unsafe Git option forwarding (GitPython) in:
  * `controller-rhel9`. AAP-88164
- [CVE-2026-73622](https://access.redhat.com/security/cve/CVE-2026-73622?__atl_rovo=disable_public_resolution) – Information disclosure via environment variable expansion in URL handling (GitPython) in:
  * `controller-rhel9`. AAP-88050
- [CVE-2026-73623](https://access.redhat.com/security/cve/CVE-2026-73623?__atl_rovo=disable_public_resolution) – Rollup: Remote code execution via malicious Git template (GitPython) in:
  * `controller-rhel9`. AAP-88147
- [CVE-2026-73624](https://access.redhat.com/security/cve/CVE-2026-73624?__atl_rovo=disable_public_resolution) – Arbitrary file overwrite via improper Git option validation (GitPython) in:
  * `controller-rhel9`. AAP-87987
- [CVE-2026-73625](https://access.redhat.com/security/cve/CVE-2026-73625?__atl_rovo=disable_public_resolution) – Remote code execution via kwarg value smuggling (GitPython) in:
  * `controller-rhel9`. AAP-88042

## Event-Driven Ansible

- [CVE-2026-54284](https://access.redhat.com/security/cve/CVE-2026-54284?__atl_rovo=disable_public_resolution) – Denial of service via quadratic CPU consumption in SQL parsing (sqlparse) in:
  * `eda-controller-rhel9`. AAP-89936
- [CVE-2026-59893](https://access.redhat.com/security/cve/CVE-2026-59893?__atl_rovo=disable_public_resolution) – Denial of service via inefficient SQL parsing (sqlparse) in:
  * `eda-controller-rhel9`. AAP-89898
- [CVE-2026-71491](https://access.redhat.com/security/cve/CVE-2026-71491?__atl_rovo=disable_public_resolution) – Denial of service via quadratic CPU consumption in comment grouping (sqlparse) in:
  * `eda-controller-rhel9`. AAP-89814

## Automation Execution Environments

- [CVE-2025-57847](https://access.redhat.com/security/cve/CVE-2025-57847?__atl_rovo=disable_public_resolution) – Privilege escalation via excessive group-writable /etc/passwd permissions in:
  * `ee-minimal-rhel9`. AAP-86652
- [CVE-2026-49825](https://access.redhat.com/security/cve/CVE-2026-49825?__atl_rovo=disable_public_resolution) – Rollup: URL bypass vulnerability in the Cleaner class via missing xlink:href (lxml) in:
  * `ee-minimal-rhel9`. AAP-90328
  * `ee-supported-rhel9`. AAP-90305

## Automation Hub

- [CVE-2026-15307](https://access.redhat.com/security/cve/CVE-2026-15307?__atl_rovo=disable_public_resolution) – Rollup: Remote code execution via GeoDjango spatial lookups (Django) in:
  * `hub-rhel9`. AAP-85794
- [CVE-2026-42215](https://access.redhat.com/security/cve/CVE-2026-42215?__atl_rovo=disable_public_resolution) – Rollup: Arbitrary command execution via bypass of dangerous Git option checks (GitPython) in:
  * `hub-rhel9`. AAP-88226
- [CVE-2026-42284](https://access.redhat.com/security/cve/CVE-2026-42284?__atl_rovo=disable_public_resolution) – Arbitrary code execution via improper validation of clone options (GitPython) in:
  * `hub-rhel9`. AAP-88202
- [CVE-2026-44244](https://access.redhat.com/security/cve/CVE-2026-44244?__atl_rovo=disable_public_resolution) – Arbitrary code execution via injected newlines in Git configuration (GitPython) in:
  * `hub-rhel9`. AAP-88241
- [CVE-2026-67322](https://access.redhat.com/security/cve/CVE-2026-67322?__atl_rovo=disable_public_resolution) – Environment variable exfiltration via attacker-controlled clone URL (GitPython) in:
  * `hub-rhel9`. AAP-86807
- [CVE-2026-67323](https://access.redhat.com/security/cve/CVE-2026-67323?__atl_rovo=disable_public_resolution) – Arbitrary code execution via command injection due to unguarded Git options (GitPython) in:
  * `hub-rhel9`. AAP-86837
- [CVE-2026-67325](https://access.redhat.com/security/cve/CVE-2026-67325?__atl_rovo=disable_public_resolution) – Command injection via Git option prefix abbreviation (GitPython) in:
  * `hub-rhel9`. AAP-86822
- [CVE-2026-69243](https://access.redhat.com/security/cve/CVE-2026-69243?__atl_rovo=disable_public_resolution) – HTTP request smuggling via WebSocket upgrade (AIOHTTP) in:
  * `hub-rhel9`. AAP-85606
- [CVE-2026-69244](https://access.redhat.com/security/cve/CVE-2026-69244?__atl_rovo=disable_public_resolution) – Denial of service via malformed HTTP responses (AIOHTTP) in:
  * `hub-rhel9`. AAP-85535
- [CVE-2026-73620](https://access.redhat.com/security/cve/CVE-2026-73620?__atl_rovo=disable_public_resolution) – Arbitrary file overwrite and read via unsafe Git option forwarding (GitPython) in:
  * `hub-rhel9`. AAP-88165
- [CVE-2026-73622](https://access.redhat.com/security/cve/CVE-2026-73622?__atl_rovo=disable_public_resolution) – Information disclosure via environment variable expansion in URL handling (GitPython) in:
  * `hub-rhel9`. AAP-88051
- [CVE-2026-73623](https://access.redhat.com/security/cve/CVE-2026-73623?__atl_rovo=disable_public_resolution) – Remote code execution via malicious Git template (GitPython) in:
  * `hub-rhel9`. AAP-88148
- [CVE-2026-73624](https://access.redhat.com/security/cve/CVE-2026-73624?__atl_rovo=disable_public_resolution) – Arbitrary file overwrite via improper Git option validation (GitPython) in:
  * `hub-rhel9`. AAP-87988
- [CVE-2026-73625](https://access.redhat.com/security/cve/CVE-2026-73625?__atl_rovo=disable_public_resolution) – Remote code execution via kwarg value smuggling (GitPython) in:
  * `hub-rhel9`. AAP-88043

## Ansible Lightspeed

- [CVE-2026-54284](https://access.redhat.com/security/cve/CVE-2026-54284?__atl_rovo=disable_public_resolution) – Denial of service via quadratic CPU consumption in SQL parsing (sqlparse) in:
  * `lightspeed-rhel9`. AAP-89938
- [CVE-2026-59877](https://access.redhat.com/security/cve/CVE-2026-59877?__atl_rovo=disable_public_resolution) – Denial of service via crafted .proto schema (protobufjs) in:
  * `gateway-rhel9`. AAP-83853
- [CVE-2026-59893](https://access.redhat.com/security/cve/CVE-2026-59893?__atl_rovo=disable_public_resolution) – Denial of service via inefficient SQL parsing (sqlparse) in:
  * `lightspeed-rhel9`. AAP-89900
- [CVE-2026-71491](https://access.redhat.com/security/cve/CVE-2026-71491?__atl_rovo=disable_public_resolution) – Denial of service via quadratic CPU consumption in comment grouping (sqlparse) in:
  * `lightspeed-rhel9`. AAP-89816

## Automation Metrics Service

- [CVE-2026-15307](https://access.redhat.com/security/cve/CVE-2026-15307?__atl_rovo=disable_public_resolution) – Remote code execution via GeoDjango spatial lookups (Django) in:
  * `metrics-service-rhel9`. AAP-85808
- [CVE-2026-54284](https://access.redhat.com/security/cve/CVE-2026-54284?__atl_rovo=disable_public_resolution) – Denial of service via quadratic CPU consumption in SQL parsing (sqlparse) in:
  * `metrics-service-rhel9`. AAP-89954
- [CVE-2026-59893](https://access.redhat.com/security/cve/CVE-2026-59893?__atl_rovo=disable_public_resolution) – Denial of service via inefficient SQL parsing (sqlparse) in:
  * `metrics-service-rhel9`. AAP-89915
- [CVE-2026-71491](https://access.redhat.com/security/cve/CVE-2026-71491?__atl_rovo=disable_public_resolution) – Denial of service via quadratic CPU consumption in comment grouping (sqlparse) in:
  * `metrics-service-rhel9`:. AAP-89832

## MCP Server

- [CVE-2026-84375](https://access.redhat.com/security/cve/CVE-2026-84375?__atl_rovo=disable_public_resolution) – Denial of service vulnerability in YAML parsing (js-yaml) in:
  * `mcp-server-rhel9`. AAP-91029
- [CVE-2026-76172](https://access.redhat.com/security/cve/CVE-2026-76172?__atl_rovo=disable_public_resolution) – URI parsing flaw enables server-side request forgery and redirects (fast-uri) in:
  * `mcp-server-rhel9`. AAP-90021
- [CVE-2026-75975](https://access.redhat.com/security/cve/CVE-2026-75975?__atl_rovo=disable_public_resolution) – Server-side request forgery via malformed IPv6 normalization (fast-uri) in:
  * `mcp-server-rhel9`. AAP-89994
- [CVE-2026-75931](https://access.redhat.com/security/cve/CVE-2026-75931?__atl_rovo=disable_public_resolution) – Host confusion via skipped IDN canonicalization (fast-uri) in:
  * `mcp-server-rhel9`. AAP-89890
- [CVE-2026-75899](https://access.redhat.com/security/cve/CVE-2026-75899?__atl_rovo=disable_public_resolution) – Server-Side Request Forgery via repeated hostname percent-decoding (fast-uri) in:
  * `mcp-server-rhel9`. AAP-89850

## Receptor

- [CVE-2026-42504](https://access.redhat.com/security/cve/CVE-2026-42504?__atl_rovo=disable_public_resolution) – Denial of service via maliciously crafted MIME header (Golang MIME library) in:
  * `receptor-rhel9`. AAP-90277

## Bug fixes

## Automation Platform Gateway

- Fixed an issue where encrypted preferences could not be decrypted after a `SECRET_KEY` change, causing the gateway to crash with an unactionable traceback; the gateway now exits with a clear message identifying which preferences are affected and their failure type. (AAP-90126)
- Fixed an issue where the `rotate_secret_key` management command failed to re-encrypt fields stored in PostgreSQL `jsonb` columns, leaving `AuthenticatorUser.extra_data` records encrypted with the old key and causing user authentication failures after the deployment secret was updated. (AAP-88914)

## Automation Platform UI

- Fixed an issue where high list refresh frequency caused excessive network load; most lists now refresh every 60 seconds. (AAP-91427)
- Fixed an issue where the Source Control Branch override on a Job Template node in a Workflow Template could not be cleared. (AAP-88997)
- Fixed an issue where the default for the `inventory_source` path field was misleadingly labeled. (AAP-87553)

## Containerized installer

- Fixed an issue where the containerized installer failed to create the Automation Metrics Service PostgreSQL database on external Aurora/RDS due to incorrect task ordering. (AAP-91639)

## Automation Controller

- Fixed an issue where Automation Controller 4.8.1 resource synchronization created duplicate global `RoleUserAssignment` records, causing JWT authentication to fail with `MultipleObjectsReturned`; global role assignments are now deduplicated and uniqueness is enforced via a database constraint. (AAP-90593)

## Automation Platform

- Fixed an issue where a performance regression in team role assignment (POST /`role_team_assignments`/) caused latency to increase 2–10x at scale in environments with many organizations and teams. (AAP-88361)

## Automation Metrics Service

- Fixed an issue where the containerized installer failed to create the Automation Metrics Service PostgreSQL database on external Aurora/RDS due to incorrect task ordering. (AAP-91639)

## Platform operator

- Fixed an issue where the `clean_backup_on_delete`: true option did not remove the correct backup directory for Event-Driven Ansible backups, leaving stale backup data behind. (AAP-90115)

## Known issues

No known issues are documented in this release.
