+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_09_21"
template = "docs/aem-title.html"
title = "Ansible Automation Platform 2.7 patch release September 21, 2026 (2.7-9) - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-overview_of_redhat_ansible_intro/", "Ansible Automation Platform release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_09_21/aem-page/whats_new-aap_27_2026_09_21.html"
last_crumb = "Ansible Automation Platform 2.7 patch release September 21, 2026 (2.7-9)"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Ansible Automation Platform 2.7 patch release September 21, 2026 (2.7-9)"
oversized = "false"
page_slug = "whats_new-aap_27_2026_09_21"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_09_21"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-aap_27_2026_09_21/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform 2.7 patch release September 21, 2026 (2.7-9)

The following release notes detail the CVEs and Bug fixes for the Ansible Automation Platform patch released on September 21, 2026

This release includes the following components and versions:

| Release Date       | Component versions                                                                                                                                                                                       |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| September 21, 2026 | Automation controller 4.8.9Automation hub 4.12.7Event-Driven Ansible 1.3.11Container-based installer Ansible Automation Platform (bundle) 2.7-9Container-based installer Ansible Automation Platform (online) 2.7-9Receptor 1.6.8 |

CSV Versions in this release:

- Namespace: aap-operator.v2.7.0-0.1789585373
- Cluster: aap-operator.v2.7.0-0.1789585368

## Overview

This release of Ansible Automation Platform 2.7 includes 57 security updates addressing critical vulnerabilities, 2 performance enhancements, and 19 bug fixes. The updates affect multiple components including Automation controller, AAP UI, Event-Driven Ansible, Automation Hub, and platform infrastructure. Security fixes address authentication bypass, privilege escalation, cross-tenant data exposure, command injection, and other critical vulnerabilities in the controller component.

## Enhancements

## Aap UI

- Added Deprecations Dashboard to surface Ansible deprecation warnings (AAP-91491)

## Controller

- Updated project_update.yml for ansible-core 2.20. (AAP-90699)

## Execution Environments

- ansible.controller collection updated to 4.8.9 (AAP-92575)

## CVE

## Automation controller

- ansible-automation-platform-27/controller-rhel9
- [CVE-2026-71461](https://access.redhat.com/security/cve/cve-2026-71461) – Internal exception detail disclosure via HostList error handler. AAP-86996
- [CVE-2026-71460](https://access.redhat.com/security/cve/cve-2026-71460) – Unrestricted subscription and license information disclosure. AAP-87001
- [CVE-2026-71458](https://access.redhat.com/security/cve/cve-2026-71458) – Cross-tenant resource enumeration via Named-URL 404 response oracle. AAP-87051
- [CVE-2026-71459](https://access.redhat.com/security/cve/cve-2026-71459) – Cross-tenant job event data exposure via missing RBAC check. AAP-87056
- [CVE-2026-71462](https://access.redhat.com/security/cve/cve-2026-71462) – Filesystem path-existence oracle via CUSTOM\_VENV\_PATHS validation. AAP-87061
- [CVE-2026-71463](https://access.redhat.com/security/cve/cve-2026-71463) – Stack trace disclosure via notification-template Jinja whitelist bypass. AAP-87066
- [CVE-2026-71464](https://access.redhat.com/security/cve/cve-2026-71464) – Git argument-injection guard bypass via Schedule scm\_branch prompt. AAP-87071
- [CVE-2026-71465](https://access.redhat.com/security/cve/cve-2026-71465) – Command-line argument injection via ad hoc command limit field. AAP-87077
- [CVE-2026-75884](https://access.redhat.com/security/cve/cve-2026-75884) – awx: Privilege escalation to OpenShift namespace via pod\_spec\_override injection in container groups. AAP-88500
- [CVE-2026-76648](https://access.redhat.com/security/cve/cve-2026-76648) – Job template secret recovery via missing read-permission check on copy. AAP-88768
- [CVE-2026-76222](https://access.redhat.com/security/cve/cve-2026-76222) – GitPython: Arbitrary file creation via path traversal in .gitmodules submodule names. AAP-90016
- [CVE-2026-76218](https://access.redhat.com/security/cve/cve-2026-76218) – GitPython: Remote Code Execution via malicious Git hooks. AAP-90046
- [CVE-2026-76220](https://access.redhat.com/security/cve/cve-2026-76220) – GitPython: Arbitrary command execution via crafted kwargs. AAP-90060
- [CVE-2026-76219](https://access.redhat.com/security/cve/cve-2026-76219) – GitPython: Arbitrary File Overwrite via `git read-tree` option injection. AAP-90072
- [CVE-2026-76221](https://access.redhat.com/security/cve/cve-2026-76221) – GitPython: Arbitrary code execution via config-name injection. AAP-90084
- [CVE-2026-84470](https://access.redhat.com/security/cve/cve-2026-84470) – Instance-group privilege escalation via Bulk Job Launch permission check. AAP-90925
- [CVE-2026-84474](https://access.redhat.com/security/cve/cve-2026-84474) – Privilege escalation via provisioning-callback host-match bypass. AAP-90928
- [CVE-2026-84475](https://access.redhat.com/security/cve/cve-2026-84475) – Cross-tenant cloud credential disclosure via inventory source search. AAP-90934
- [CVE-2026-84486](https://access.redhat.com/security/cve/cve-2026-84486) – Unauthenticated scheduler-trigger endpoint exposure (regression). AAP-90936
- [CVE-2026-84499](https://access.redhat.com/security/cve/cve-2026-84499) – Survey password disclosure via validation error message. AAP-90946
- [CVE-2026-84502](https://access.redhat.com/security/cve/cve-2026-84502) – Remote code execution via Project scm\_url git argument injection. AAP-90957
- [CVE-2026-84638](https://access.redhat.com/security/cve/cve-2026-84638) – Instance-group privilege escalation via Schedule and workflow node attachment. AAP-90996
- [CVE-2026-84643](https://access.redhat.com/security/cve/cve-2026-84643) – Cross-organization credential exposure via Project signature-validation binding. AAP-91003
- [CVE-2026-84644](https://access.redhat.com/security/cve/cve-2026-84644) – Server-side request forgery via Thycotic Secret Server credential test. AAP-91011
- [CVE-2026-84678](https://access.redhat.com/security/cve/cve-2026-84678) – Code execution via GALAXY\_TASK\_ENV environment variable injection. AAP-91022
- [CVE-2026-84680](https://access.redhat.com/security/cve/cve-2026-84680) – Credential-use privilege escalation via organization Galaxy credential attachment. AAP-91073
- [CVE-2026-84683](https://access.redhat.com/security/cve/cve-2026-84683) – Stored cross-site scripting via ANSI hyperlink sequence in job output. AAP-91074
- [CVE-2026-84684](https://access.redhat.com/security/cve/cve-2026-84684) – Privilege escalation via constructed inventory attachment. AAP-91083
- [CVE-2026-84686](https://access.redhat.com/security/cve/cve-2026-84686) – Credential token disclosure via notification template type-switch replay. AAP-91085
- [CVE-2026-84689](https://access.redhat.com/security/cve/cve-2026-84689) – Cross-tenant job hijack via Bulk Job Launch node reference. AAP-91095
- [CVE-2026-84691](https://access.redhat.com/security/cve/cve-2026-84691) – Secret key and database credential disclosure via format-string injection. AAP-91102
- [CVE-2026-84692](https://access.redhat.com/security/cve/cve-2026-84692) – Cross-tenant execution privilege bypass via workflow job template node patch. AAP-91104
- [CVE-2026-84703](https://access.redhat.com/security/cve/cve-2026-84703) – Cross-tenant credential exposure via execution environment binding. AAP-91113
- [CVE-2026-84706](https://access.redhat.com/security/cve/cve-2026-84706) – Code execution via credential type environment-injector blocklist bypass. AAP-91128
- [CVE-2026-84707](https://access.redhat.com/security/cve/cve-2026-84707) – Unauthorized job output disclosure via host filter query traversal. AAP-91137
- [CVE-2026-84708](https://access.redhat.com/security/cve/cve-2026-84708) – Control-plane secret exposure via container group pod spec override. AAP-91139
- [CVE-2026-84709](https://access.redhat.com/security/cve/cve-2026-84709) – Denial of service via credential type injector Jinja rendering. AAP-91147
- [CVE-2026-84712](https://access.redhat.com/security/cve/cve-2026-84712) – Automation mesh topology disclosure via unauthenticated ping endpoint. AAP-91159
- [CVE-2026-84713](https://access.redhat.com/security/cve/cve-2026-84713) – Cross-tenant notification credential disclosure via recipient field search. AAP-91166
- [CVE-2026-84714](https://access.redhat.com/security/cve/cve-2026-84714) – Template injection via sanitize\_jinja regex bypass. AAP-91169
- [CVE-2026-84716](https://access.redhat.com/security/cve/cve-2026-84716) – Mesh certificate issuance for arbitrary hostnames via install bundle. AAP-91177
- [CVE-2026-84718](https://access.redhat.com/security/cve/cve-2026-84718) – Audit log falsification via unrestricted X-Forwarded-For trust. AAP-91182
- [CVE-2026-84719](https://access.redhat.com/security/cve/cve-2026-84719) – Instance-group privilege escalation via workflow job template copy. AAP-91183
- [CVE-2026-84720](https://access.redhat.com/security/cve/cve-2026-84720) – Masked credential data disclosure via workflow job node artifact search. AAP-91191
- [CVE-2026-84721](https://access.redhat.com/security/cve/cve-2026-84721) – Server-side request forgery via email notification template host validation bypass. AAP-91193
- [CVE-2026-84724](https://access.redhat.com/security/cve/cve-2026-84724) – Command argument injection via SystemJob extra\_vars. AAP-91204
- [CVE-2026-85475](https://access.redhat.com/security/cve/cve-2026-85475) – Remote code execution via rsyslog configuration injection. AAP-91691
- [CVE-2026-84717](https://access.redhat.com/security/cve/cve-2026-84717) – Job template enumeration via unauthenticated Bitbucket webhook oracle. AAP-92198
- [CVE-2026-87817](https://access.redhat.com/security/cve/cve-2026-87817) – GitPython: Remote Code Execution via Git directory impersonation. AAP-92296
- [CVE-2026-84711](https://access.redhat.com/security/cve/cve-2026-84711) – Arbitrary file read via Project scm\_branch git argument injection. AAP-92383

## Automation hub

- ansible-automation-platform-27/hub-rhel9
- [CVE-2026-71491](https://access.redhat.com/security/cve/cve-2026-71491) – sqlparse: Denial of Service via quadratic CPU consumption in comment grouping. AAP-89831
- [CVE-2026-59893](https://access.redhat.com/security/cve/cve-2026-59893) – sqlparse: Denial of Service via inefficient SQL parsing. AAP-89914
- [CVE-2026-54284](https://access.redhat.com/security/cve/cve-2026-54284) – sqlparse: Denial of Service via quadratic CPU consumption in SQL parsing. AAP-89953
- [CVE-2026-49825](https://access.redhat.com/security/cve/cve-2026-49825) – lxml: URL bypass vulnerability in Cleaner via missing xlink:href. AAP-90306
- [CVE-2026-78679](https://access.redhat.com/security/cve/cve-2026-78679) – GitPython: Arbitrary file read via TagReference.create(). AAP-92237

## Event-Driven Ansible

- ansible-automation-platform-27/de-minimal-rhel9
- [CVE-2025-57847](https://access.redhat.com/security/cve/cve-2025-57847) – privilege escalation via excessive group writable /etc/passwd permissions. AAP-86650
- ansible-automation-platform-27/de-supported-rhel9
- [CVE-2025-57847](https://access.redhat.com/security/cve/cve-2025-57847) – privilege escalation via excessive group writable /etc/passwd permissions. AAP-86651

## Execution Environments

- ansible-automation-platform-27/ee-supported-rhel9
- [CVE-2025-66418](https://access.redhat.com/security/cve/cve-2025-66418) – urllib3: Unbounded decompression chain leads to resource exhaustion. AAP-92494

## MCP Server

- ansible-automation-platform-27/mcp-server-rhel9
- [CVE-2026-84292](https://access.redhat.com/security/cve/cve-2026-84292) – fast-uri: Authority Injection via Unvalidated Port Serialization. AAP-91501
- [CVE-2026-84394](https://access.redhat.com/security/cve/cve-2026-84394) – fast-uri: Host confusion via unbalanced URI brackets can bypass security policies. AAP-91519

## Platform Operator

- ansible-automation-platform-27/aap-must-gather-rhel9
- [CVE-2026-53488](https://access.redhat.com/security/cve/cve-2026-53488) – containerd: Host-root command execution via unvalidated image config labels in CRI plugin. AAP-81260
- [CVE-2026-53492](https://access.redhat.com/security/cve/cve-2026-53492) – containerd: Security bypass via Container Device Interface (CDI) annotation smuggling during checkpoint restoration. AAP-81559

## Receptor

- [CVE-2026-56853](https://access.redhat.com/security/cve/cve-2026-56853) – Go net/http: Unencrypted HTTP/2 connections vulnerable to Denial of Service. AAP-87997
- [CVE-2026-56862](https://access.redhat.com/security/cve/cve-2026-56862) – Golang crypto/tls: Denial of Service via indefinite KeyUpdate messages. AAP-88027
- [CVE-2026-33818](https://access.redhat.com/security/cve/cve-2026-33818) – Go encoding/asn1: Denial of Service via excessive recursion in Unmarshal. AAP-88075
- [CVE-2026-56860](https://access.redhat.com/security/cve/cve-2026-56860) – golang net/url: Denial of Service from quadratic complexity in path resolution. AAP-88098
- [CVE-2026-56859](https://access.redhat.com/security/cve/cve-2026-56859) – Go: Denial of Service via XML decoding recursion depth issue. AAP-88110
- [CVE-2026-56858](https://access.redhat.com/security/cve/cve-2026-56858) – Go html/template: Cross-Site Scripting via pathological input. AAP-88154

## Other packages

- python-sqlparse
- [CVE-2026-71491](https://access.redhat.com/security/cve/cve-2026-71491) – Denial of Service via quadratic CPU consumption in comment grouping. AAP-89825
- [CVE-2026-59893](https://access.redhat.com/security/cve/cve-2026-59893) – Denial of Service via inefficient SQL parsing. AAP-89908
- [CVE-2026-54284](https://access.redhat.com/security/cve/cve-2026-54284) – Denial of Service via quadratic CPU consumption in SQL parsing. AAP-89947
- python3.12-sqlparse
- [CVE-2026-71491](https://access.redhat.com/security/cve/cve-2026-71491) – Denial of Service via quadratic CPU consumption in comment grouping. AAP-89826
- [CVE-2026-59893](https://access.redhat.com/security/cve/cve-2026-59893) – Denial of Service via inefficient SQL parsing. AAP-89909
- [CVE-2026-54284](https://access.redhat.com/security/cve/cve-2026-54284) – Denial of Service via quadratic CPU consumption in SQL parsing. AAP-89948

## Bug fixes

## Aap Gateway

- Fixed an issue where authentication mappings that assign an object-scoped role (for example, JobTemplate Execute) are now rejected when the mapping is saved, instead of being accepted and failing silently at login. (AAP-92571)

## Aap UI

- Fixed an issue where table displaying subscriptions and time remaining is visible. (AAP-50487)
- Fixed an issue where description entered on the approval node (and returned by the API) is visible in the Workflow Approvals UI (list and/or details), as it was in AAP 2.4.

Approvers can complete approvals using UI context alone, without consulting the API. (AAP-87838)

- Fixed an issue where show authenticator options on details page (AAP-90343)
- Fixed an issue where optimized network call when loading jobs list (AAP-91986)
- Fixed an issue where fixed markdown formatting in Hub Execution Environment readme (AAP-92092)

## Controller

- Fixed an issue where fixes a locking issue when updating the last_seen timestamp of control and execution nodes (AAP-89560)

## Django Ansible Base

- Fixed an issue where authentication mappings that assign a global role to an organization or team are now rejected at save time instead of failing silently at login. (AAP-92091)
- Fixed an issue where an issue where OIDC RP-initiated logout incorrectly revoked all OAuth tokens for a user. Logout now removes only tokens belonging to the OAuth application that initiated logout and that were used only for authentication. (AAP-92790)
- Fixed an issue where namespace-scoped role assignments from Gateway not being applied in Hub. (AAP-93576)

## Event Driven Ansible

- Fixed an issue where an issue where the de-minimal decision environment image was not surfaced in Automation Hub or Automation Decisions, preventing users from using it as a base for custom decision environments. (AAP-91934)

## Platform Operator

- Fixed an issue where EDA would get a 401 when running Controller job templates, due to a misconfigured automation_server_url value.Fixed an issue where EDA would get a 401 when running Controller job templates, due to a misconfigured automation_server_url value. (AAP-91353)
- Fixed an issue where the Gateway would incorrectly report healthy components (Controller, Hub, EDA) as failed when an HTTP/HTTPS proxy was configured, by ensuring generated Service names are included in the Gateway’s NO_PROXY whitelist. (AAP-91490)
