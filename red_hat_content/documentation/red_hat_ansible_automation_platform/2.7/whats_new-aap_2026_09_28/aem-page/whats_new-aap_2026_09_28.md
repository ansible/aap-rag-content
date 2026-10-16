+++
template = "docs/aem-title.html"
title = "Ansible Automation Platform 2.7 patch release September 28, 2026 (portal-2.2.8) - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-aap_2026_09_28"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/whats_new-overview_of_redhat_ansible_intro/", "Ansible Automation Platform release notes"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-aap_2026_09_28/aem-page/whats_new-aap_2026_09_28.html"
last_crumb = "Ansible Automation Platform 2.7 patch release September 28, 2026 (portal-2.2.8)"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Ansible Automation Platform 2.7 patch release September 28, 2026 (portal-2.2.8)"
oversized = "false"
page_slug = "whats_new-aap_2026_09_28"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/whats_new-aap_2026_09_28"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/whats_new-aap_2026_09_28/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform 2.7 patch release September 28, 2026 (portal-2.2.8)

The following enhancements and bug fixes have been implemented in this release of Ansible automation portal.

This release includes the following components and versions:

| Release Date       |  |
| ------------------ | --- |
| September 23, 2026 |  |

## Overview

Red Hat Ansible Automation Platform portal 2.2.8 is a security and bug fix update. This release delivers third-party dependency security patches across automation portal plugins, fixes the SSH login MOTD "View config" command on the RHEL bootc appliance, and updates the automation portal operator for OpenShift deployments.

## Features

This release includes no new features.

## Highlights

- **Security:** Third-party dependency updates address vulnerabilities in automation portal plugins, including urllib credential leakage, js-yaml denial of service, qs and undici hardening, isomorphic-git prototype pollution, compression memory leaks, adm-zip archive handling, multer upload handling, and vm2 sandbox issues. The automation portal operator image includes a Go/stdlib fix for XML decoding recursion depth denial of service (CVE-2026-56859).
- **Bug fix:** The SSH login MOTD "View config" command now opens the production app configuration file with `sudo less` instead of incorrectly duplicating the `portal-status` command. (AAP-92035)
- **Enhancement:** Configurable customer support URL via `spec.branding.customerSupportURL`. (AAP-93824)
- **Bug fix:** Configurable AAP organizations for catalog plugin discovery via `spec.plugins.catalog.orgs`. (AAP-93823)
- **Bug fix:** OperatorHub catalog icon updated to match other AAP platform operators. (AAP-92252)
- **Changed:** Operator configuration UI uses Ansible automation portal language instead of Backstage terminology. (AAP-92046)

## Enhancements

## Ansible automation portal operator Technology Preview

- Added `spec.branding.customerSupportURL` (default `https://access.redhat.com/support`); the value is written to the portal environment secret and resolves the global header support link. (AAP-93824)

## Bug fixes

## Ansible automation portal RHEL appliance

- Fixed an issue where the SSH login MOTD listed "View config" as `sudo portal-status`, duplicating the portal status command instead of showing a read-only view of `app-config.production.yaml`. (AAP-92035)

## Ansible automation portal operator Technology Preview

- OperatorHub catalog icon updated to the Ansible product icon. (AAP-92252)
- Fixed an issue where the operator pod entered CrashLoopBackOff after successful reconciliation due to health probe failures on port 8081. (AAP-92908)
- Added `spec.plugins.catalog.orgs` to scope catalog plugin discovery to specified AAP organizations; when omitted, existing single-org behavior is unchanged. (AAP-93823)
- Fixed an issue where the DevTools sidecar defaulted to the community `ghcr.io/ansible/community-ansible-dev-tools:devel` image when `spec.devtools.image` was omitted, instead of the documented production Red Hat stream. Override via `spec.devtools.image` for air-gapped installs. (AAP-92057)
- Fixed an issue where `app.baseUrl`, `backend.baseUrl`, and `backend.cors.origin` were not set in the generated portal-app-config when `spec.deployment.route.enabled` was false and a custom `spec.deployment.route.host` was used, causing the GitHub sign-in page instead of Sign in using Ansible Automation Platform. (AAP-94213)

## Changed features

## Ansible automation portal operator Technology Preview

- Operator configuration UI and API labels updated from Backstage terminology to Ansible automation portal language. (AAP-92046)
- Managed Backstage custom resource naming corrected so RHDH resources use `backstage-<cr-name>` instead of `backstage-<cr-name>-backstage`. (AAP-93825)
  * Existing installs must manually delete the old Backstage CR after upgrade: `oc delete backstage <name>-backstage -n <namespace>`
- `spec.plugins.selfService`, `spec.plugins.rbac`, and `spec.plugins.scaffolder` removed from the CRD; these plugins are always on. To disable a plugin, use `spec.plugins.overrides`. (AAP-93825)
- `spec.devtools` and `spec.plugins.ghcrRegistry` hidden from the operator form; both remain settable via YAML. (AAP-93825)
- Lightspeed plugin option removed from the AutomationPortal operator form; `spec.plugins.lightspeed.enabled` remains valid in YAML for advanced use. (AAP-92058)

## CVE

## Ansible automation portal

- [CVE-2026-55553](https://access.redhat.com/security/cve/cve-2026-55553) – Credential leakage via cross-origin redirects (urllib). (AAP-89885)
- [CVE-2026-59869](https://access.redhat.com/security/cve/cve-2026-59869) – Denial of Service via crafted YAML documents (js-yaml). (AAP-90387)
- [CVE-2026-84375](https://access.redhat.com/security/cve/cve-2026-84375) – Denial of Service vulnerability in YAML parsing (js-yaml). (AAP-91035)
- [CVE-2026-82417](https://access.redhat.com/security/cve/cve-2026-82417) – Denial of Service via improper validation in stringify function (qs). (AAP-91548)
- [CVE-2026-19534](https://access.redhat.com/security/cve/cve-2026-19534) – Denial of Service via unrequested WebSocket subprotocol (undici). (AAP-91751)
- [CVE-2026-89011](https://access.redhat.com/security/cve/cve-2026-89011) – Information disclosure via prototype pollution in getRemoteInfo function (isomorphic-git). (AAP-92394)
- [CVE-2026-87776](https://access.redhat.com/security/cve/cve-2026-87776) – Denial of Service via memory leak on premature response close (compression). (AAP-92537)
- [CVE-2026-88932](https://access.redhat.com/security/cve/cve-2026-88932) – Denial of Service via orphaned disk writes on aborted uploads (multer). (AAP-92729)
- [CVE-2026-92000](https://access.redhat.com/security/cve/cve-2026-92000) – Denial of Service via crafted ZIP archives with zero declared uncompressed size (adm-zip). (AAP-92995)
- [CVE-2026-92959](https://access.redhat.com/security/cve/cve-2026-92959) – Asynchronous code execution bypass via Promise thenable assimilation (vm2). (AAP-93383)
- [CVE-2026-92961](https://access.redhat.com/security/cve/cve-2026-92961) – Denial of Service via memory exhaustion (vm2). (AAP-93386)
- [CVE-2026-92958](https://access.redhat.com/security/cve/cve-2026-92958) – Sandbox escape via denylist bypass in NodeVM (vm2). (AAP-93389)
- [CVE-2026-92942](https://access.redhat.com/security/cve/cve-2026-92942) – Denial of Service via timeout bypass in sandboxed code (vm2). (AAP-93391)
- [CVE-2026-47683](https://access.redhat.com/security/cve/cve-2026-47683) – Denial of Service due to memory allocation limit bypass (vm2). (AAP-93421)

## Ansible automation portal RHEL appliance

- [CVE-2026-6471](https://access.redhat.com/security/cve/cve-2026-6471) – Arbitrary code execution via logical decoding plugin (PostgreSQL). (AAP-89750)
- [CVE-2026-6464](https://access.redhat.com/security/cve/cve-2026-6464) – Arbitrary command execution via untrusted data in COPY FROM STDIN (PostgreSQL psql). (AAP-90283)
- [CVE-2026-5038](https://access.redhat.com/security/cve/cve-2026-5038) – Denial of Service via aborted or malformed multipart uploads (Multer). (AAP-90371)
- [CVE-2026-14662](https://access.redhat.com/security/cve/cve-2026-14662) – Arbitrary code execution via integer wraparound in tsvector and tsquery functions (PostgreSQL). (AAP-89549)
- [CVE-2026-14664](https://access.redhat.com/security/cve/cve-2026-14664) – Arbitrary code execution via heap buffer overflow in regexp (PostgreSQL). (AAP-89609)
- [CVE-2026-14668](https://access.redhat.com/security/cve/cve-2026-14668) – Information disclosure via type confusion in ctid selectivity estimator (PostgreSQL). (AAP-90230)
- [CVE-2026-14669](https://access.redhat.com/security/cve/cve-2026-14669) – Arbitrary code execution via long POSIX timezone abbreviation (PostgreSQL). (AAP-89304)
- [CVE-2026-14670](https://access.redhat.com/security/cve/cve-2026-14670) – Arbitrary code execution via plperl tied hash heap buffer overflow (PostgreSQL). (AAP-90231)
- [CVE-2026-14671](https://access.redhat.com/security/cve/cve-2026-14671) – Arbitrary code execution via type confusion in 'refint' module (PostgreSQL). (AAP-90175)
- [CVE-2026-14677](https://access.redhat.com/security/cve/cve-2026-14677) – Arbitrary code execution in 32-bit pltcl and plperl (PostgreSQL). (AAP-89894)
- [CVE-2026-14679](https://access.redhat.com/security/cve/cve-2026-14679) – Stack buffer overflow via OUT parameter count manipulation (PostgreSQL). (AAP-90263)
- [CVE-2026-14680](https://access.redhat.com/security/cve/cve-2026-14680) – Arbitrary code execution via type confusion with "internal" arguments (PostgreSQL). (AAP-89597)
- [CVE-2026-15741](https://access.redhat.com/security/cve/cve-2026-15741) – Privilege escalation via SQL injection in EXTRACT() deparse (PostgreSQL). (AAP-90280)
- [CVE-2026-15742](https://access.redhat.com/security/cve/cve-2026-15742) – Arbitrary code execution via integer wraparound (PostgreSQL fuzzystrmatch). (AAP-89635)
- [CVE-2026-16239](https://access.redhat.com/security/cve/cve-2026-16239) – Arbitrary code execution via type confusion in cursor lifecycle (PostgreSQL). (AAP-89778)
- [CVE-2026-18408](https://access.redhat.com/security/cve/cve-2026-18408) – Arbitrary code execution via untrusted data inclusion in pg_dump (PostgreSQL). (AAP-90286)
- [CVE-2026-19385](https://access.redhat.com/security/cve/cve-2026-19385) – Arbitrary code execution via crafted transform lists (PostgreSQL pg_dump). (AAP-89594)

## Ansible automation portal operator Technology Preview

- [CVE-2026-56859](https://access.redhat.com/security/cve/cve-2026-56859) – Denial of Service via XML decoding recursion depth issue (Go) (AAP-92216)
