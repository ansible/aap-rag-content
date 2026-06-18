# Ansible Automation Platform 2.7 patch release June 17, 2026

The following release notes detail the CVEs and Bug fixes for the Ansible Automation Platform patch released on June 17, 2026

This release includes the following components and versions:

| Release Date      | Component versions                                                                                                                                                                                                                 |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>June 17, 2026 | Automation controller 4.8.1Automation hub 4.12.2Event-Driven Ansible 1.3.2Container-based installer Ansible Automation Platform (bundle) 2.7-1.2Container-based installer Ansible Automation Platform (online) 2.7-1Receptor 1.6.5 |


CSV Versions in this release: * namespace scoped: aap-operator.v2.7.0-0.1781122804 * cluster scoped: aap-operator.v2.7.0-0.1781122780

## Overview

Ansible Automation Platform 2.7.20260617 delivers a focused set of improvements across the platform, including new backup and restore capabilities for the Metrics Service, enhanced security through multiple CVE remediations, and a broad collection of bug fixes spanning the controller, gateway, operator, and hub components. This release also introduces always-on case-insensitive authentication map matching, FIPS-compliant Receptor builds, and proxy support for operator deployments.

## Highlights

- **Metrics Service Backup & Restore** — Full backup and restore support is now available for the Metrics Service and its operator, ensuring data resilience across reinstall and disaster recovery scenarios.
- **Security Hardening** — Eighteen CVE fixes address vulnerabilities in cryptography, urllib3, PyJWT, and SQL injection vectors across multiple components.
- **Case-Insensitive Auth Maps** — Case-insensitive matching for authenticator maps is now always enabled; the feature flag has been removed.
- **FIPS-Compliant Receptor** — The Receptor binary is now built FIPS-compliant.

## Features

## Metrics service

- Enabling Backup & Restore in Metrics Operator. (AAP-77549)
- Enabling Backup & Restore for Metrics Operator. (AAP-75055)
- Enabling Backup & Restore for Metrics Service. (AAP-77225)
- This will be handled in product docs that metrics service is a required component. (AAP-74059)

## Enhancements

## Aap-gateway

- Removed the `FEATURE_CASE_INSENSITIVE_AUTH_MAPS_ENABLED` feature flag, making case-insensitive matching for authenticator maps always enabled. (AAP-75521)
- Case-insensitive authentication map matching is now always enabled. The `FEATURE_CASE_INSENSITIVE_AUTH_MAPS_ENABLED` feature flag has been removed. (AAP-61226)

## Controller

- Installed collections and Ansible version are now recorded for every job run, regardless of whether the Indirect Node Counting feature flag is enabled. Previously, this metadata was only collected when `FEATURE_INDIRECT_NODE_COUNTING_ENABLED` was on. (AAP-76810)

## Hub

Move healthz and prometheus metrics under /api/galaxy/status/ to avoid root-level path conflicts. New endpoints can be accessed on /api/galaxy/status/healthz and /api/galaxy/status/metrics. (AAP-78324)

## Metrics service

- Increased task retry window with logarithmic backoff. (AAP-75409)

## Platform-operator

- Added proxy variables for hub operator deployments. (AAP-73663)
- Added proxy variables for lightspeed operator deployments. (AAP-73660)
- Added proxy variables for lightspeed operator deployments. (AAP-73659)

## Receptor

- Receptor binary is built FIPS compliant. (AAP-76100)

## CVE

## Automation hub

- [CVE-2026-48526](https://access.redhat.com/security/cve/cve-2026-48526) - PyJWT: Authentication bypass due to forged JSON Web Tokens in:
* hub-rhel9 for Ansible Automation Platform 2.7. AAP-78042
- [CVE-2026-44432](https://access.redhat.com/security/cve/cve-2026-44432) - urllib3: Denial of Service due to excessive HTTP response decompression in:
* hub-rhel9 for Ansible Automation Platform 2.7. AAP-77363
- [CVE-2026-44431](https://access.redhat.com/security/cve/cve-2026-44431) - urllib3: Information disclosure via cross-origin redirects forwarding sensitive headers in:
* hub-rhel9 for Ansible Automation Platform 2.7. AAP-77359
- [CVE-2026-39892](https://access.redhat.com/security/cve/cve-2026-39892) - Cryptography: Buffer overflow via non-contiguous buffer in API in:
* hub-rhel9 for Ansible Automation Platform 2.7. AAP-75149

## Execution environments

- [CVE-2026-48526](https://access.redhat.com/security/cve/cve-2026-48526) - PyJWT: Authentication bypass due to forged JSON Web Tokens in:
* ee-supported-rhel9 for Ansible Automation Platform 2.7. AAP-78039

## Ansible Lightspeed

- [CVE-2026-48526](https://access.redhat.com/security/cve/cve-2026-48526) - PyJWT: Authentication bypass due to forged JSON Web Tokens in:
* lightspeed-rhel9 for Ansible Automation Platform 2.7. AAP-78038
* mcp-tools-rhel9 for Ansible Automation Platform 2.7. AAP-78037
* lightspeed-chatbot-rhel9 for Ansible Automation Platform 2.7. AAP-78034

## Event-Driven Ansible

- [CVE-2026-44432](https://access.redhat.com/security/cve/cve-2026-44432) - urllib3: Denial of Service due to excessive HTTP response decompression in:
* eda-controller-rhel9 for Ansible Automation Platform 2.7. AAP-77887
* de-minimal-rhel9 for Ansible Automation Platform 2.7. AAP-77254
* SQL injection vulnerability - EDA PGNotify SQL Injection via Dollar-Quote Escape in:
* eda-controller-rhel9 for Ansible Automation Platform 2.7. AAP-76113

## Bug fixes

## General

- Fixed an issue where an authenticator map of map type "allow" could not recover access once it had been set to False by an earlier deny-all rule. (AAP-75209)
- Fixed an issue where an authenticator map of map type "allow" could not recover access once it had been set to False by an earlier deny-all rule. (AAP-75207)

## Aap-ui

- Fixed an issue where editing Platform roles with the "System" resource type prevented saving permissions due to an error. (AAP-78150)
- Fixed an issue where health checks could not run on managed instances even when the user had permissions. (AAP-75398)
- Fixed an issue where the Credential plugins test modal did not include a job template dropdown when a job template was required for the test operation. (AAP-75176)
- Fixed an issue where a Job Template update in a Workflow template was not getting saved intermittently. (AAP-74443)
- Fixed an issue where the collection Documentation tab in Automation Hub would crash when the API response included large unnecessary fields, causing the page to fail to render. (AAP-72872)

## Controller

- Fixed an issue where Execution Nodes were incorrectly included in the Control Plane. (AAP-78341)
- Fixed an issue where jobs would remain in Waiting indefinitely if the assigned controller node instance was deprovisioned. (AAP-78097)
- Fixed an issue where the Azure Key Vault credential plugin failed with a TypeError because the cloud_name field was not accepted by the backend function, a regression introduced when explicit typed parameters replaced **kwargs. (AAP-77748)
- Fixed an issue where setting an rrule interval to 0 caused the dispatcher to hang. (AAP-77568)
- Fixed an issue where the request_timeout field on the Ansible Automation Platform credential was not working correctly. (AAP-77341)
- Fixed an issue where populate_workload_identity_tokens() did not accept an additional list of credentials, causing workload identity token injection to fail for inventory update cloud credentials. (AAP-75205)
- Fixed an issue where workflow node updates failed when the Job Template had labels without "Prompt on Launch" enabled, because the serializer re-validated all persisted prompt state on every update instead of only the fields included in the request. (AAP-75202)
- Fixed an issue where as_user() failed to switch the authenticated user when requests went through the AAP gateway because the gateway_sessionid cookie was not checked as a fallback. (AAP-75199)
- Fixed an issue where the Thycotic Secret Server (Delinea) credential plugin failed with an HTTP 500 error when resolving credentials from Delinea Platform URLs. (AAP-75198)
- Fixed an issue where fact cache queries were expensive, degrading performance. (AAP-74523)
- Fixed an issue where awxkit failed with ModuleNotFoundError for the packaging module because install_requires listed setuptools instead of packaging after the Python 3.12 upgrade. (AAP-74277)
- Fixed an issue where analytics API requests did not respect proxy environment variables, causing DNS resolution failures in proxy environments. (AAP-73163)
- Fixed an issue where the GET /api/v2/hosts/ endpoint had slow response times at scale due to loading the large ansible_facts JSON column and an unnecessary database table JOIN in RBAC permission evaluation queries. (AAP-73161)
- Fixed an issue where schedules could not parse a valid RRULE with certain BYHOUR constraints. (AAP-72482)

## Dev-tools

- Fixed an issue where the devspaces container was missing tzdata, causing ansible-navigator to crash with a ZoneInfoNotFoundError on startup. (AAP-78087)

## Event-driven Ansible

- Fixed an issue where a bug affected event-driven Ansible functionality. (AAP-77441)

## Execution environments

- Fixed an issue where the ansible.platform collection was outdated; updated to v2.7.20260604. (AAP-78099)

## Hub

- Fixed an issue where creating and syncing roles from DAB to Hub (pulp) resulted in incorrect locked (managed) values. (AAP-78275)
- Fixed an issue where Automation Hub pods experienced high memory usage under idle conditions because health probes caused progressive memory growth in pulpcore worker processes, triggering unnecessary HPA scaling events. (AAP-68883)

## Lightspeed

- Fixed an issue where the containerized installer Ansible Lightspeed chatbot did not show the image used for BYOK. (AAP-73534)
- Fixed an issue where the containerized installer Ansible Lightspeed chatbot did not show the image used for BYOK. (AAP-72986)

## Metrics service

- Fixed an issue where the Gateway Operator failed to recreate the read user for the metrics service after a database rebuild. (AAP-78410)
- Fixed an issue where the Metrics Operator reinstall/restore process failed. (AAP-77551)

## Platform-operator

- Fixed an issue where Hub nginx and gunicorn timeout values were not derived from the gateway client_request_timeout annotation, causing 502 errors during long-running operations such as content uploads and Collections as Code workflows. (AAP-78055)
- Fixed an issue where the gateway operator failed to reconcile after HA/DR failback due to a stale OAuth2 token that was not properly validated or regenerated. (AAP-77512)
- Fixed an issue where the Lightspeed status URL was not reported when using ingress or none as the ingress type, which could cause the gateway operator to wait indefinitely for Lightspeed readiness. (AAP-76781)
