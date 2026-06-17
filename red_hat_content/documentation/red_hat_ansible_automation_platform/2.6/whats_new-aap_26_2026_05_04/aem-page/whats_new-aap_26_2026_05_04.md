+++
template = "docs/aem-title.html"
title = "Ansible Automation Platform patch release May 4, 2026 - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2026_05_04"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-async_updates/", "Patch releases"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2026_05_04/aem-page/whats_new-aap_26_2026_05_04.html"
last_crumb = "Ansible Automation Platform patch release May 4, 2026"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Ansible Automation Platform patch release May 4, 2026"
oversized = "false"
page_slug = "whats_new-aap_26_2026_05_04"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2026_05_04"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-aap_26_2026_05_04/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform patch release May 4, 2026

The following release notes detail the updates for the Ansible Automation Platform patch released on May 4, 2026

This release includes the following components and versions:

| Release Date | Component versions                                                                                                                                                                                                                                                                                                                                              |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| May 4, 2026  | Automation controller 4.7.11Automation hub 4.11.8Event-Driven Ansible 1.2.8Container-based installer Ansible Automation Platform (bundle) 2.6-8Container-based installer Ansible Automation Platform (online) 2.6-8Receptor 1.6.4RPM-based installer Ansible Automation Platform (bundle) 2.6-6.1RPM-based installer Ansible Automation Platform (online) 2.6-6 |


CSV Versions in this release:

- Namespace-scoped bundle: aap-operator.v2.6.0-0.1777410689
- Cluster-scoped bundle: aap-operator.v2.6.0-0.1777410680

## Overview

This Ansible Automation Platform 2.6 async (20260422) release includes a set of targeted enhancements across installation and platform UX, plus a large batch of security (CVE) remediations and bug fixes across multiple AAP components.

## Enhancements

## Automation hub

- Added verification that Hub supports Execution Environments with PQC signatures.(AAP-71606)

## Container-based installer Ansible Automation Platform

- Fixed the preflight check to allow hop nodes to run on systems with less than 16GB of RAM.(AAP-71341)

## Red Hat Ansible Lightspeed

- Support for llama-stack 0.4.3.(AAP-69996)
- Support for llama-stack 0.4.3.(AAP-65012)

## Ansible Automation Platform Operator

- Allows the ability to disable backup db compression per component using the use_db_compression parameter (default: true). (AAP-69747)

## Ansible Automation Platform ui

- Private flags only appear in UI when enabled - this applies uniformly to both runtime and install-time private flags. Private runtime flags can be toggled off via the UI, which causes them to disappear. This prevents users from easily discovering feature flags that are not meant to be advertised to all customers.(AAP-69669)
- Added a Feature Flags page under Settings that allows platform administrators to view feature flags and toggle runtime flags on or off without restarting services.(AAP-69001)

## Automation controller

- Sets `XDG_CONFIG_HOME=/tmp/.config` in the `Containerfile` so podman-remote can write its config at runtime.
- Fixes `handle_removed_image` task failing with `RuntimeError`: Error running command in containerized installer deployments. (AAP-68260)

## Deprecated

## Ansible Automation Platform Operator

- `old_postgres_configuration_secret` has been deprecated for automation controller and event-driven ansible.
- `postgres_migrant_configuration_secret` has been deprecated for automation hub.(AAP-68604)

## Receptor

- Address [CVE-2025-68121](https://access.redhat.com/security/cve/cve-2025-68121).(AAP-65759)

## CVE

## General

- CVE-2026-6266: Account hijacking and unauthorized access via unverified email linking. This affects the following components:
  * `automation-controller` for Ansible Automation Platform 2.5 and 2.6.
  * `automation-gateway` for {PlatformNameShort} 2.5 and 2.6.
  * `python3.12-django-ansible-base` for Ansible Automation Platform 2.5 and 2.6.
  * `ansible-automation-platform-26/controller-rhel9` for Ansible Automation Platform 2.6 only.
  * `ansible-automation-platform-26/gateway-rhel9` for Ansible Automation Platform 2.6 only.

## Execution Environment

- [CVE-2026-23490](https://access.redhat.com/security/cve/cve-2026-23490)- pyasn1: Denial of Service due to memory exhaustion from malformed RELATIVE-OID in:
  * `ansible-automation-platform-26/ee-supported-rhel9` for Ansible Automation Platform 2.6. AAP-72593
- [CVE-2026-27459](https://access.redhat.com/security/cve/cve-2026-27459) - pyOpenSSL: DTLS cookie callback buffer overflow in:
  * ansible-automation-platform-26/ee-supported-rhel9 for Ansible Automation Platform 2.6. AAP-68956
- [CVE-2026-32274](https://access.redhat.com/security/cve/cve-2026-32274) - Black: Arbitrary file writes from unsanitized user input in cache file name in:
  * `ansible-automation-platform-26/ee-minimal-rhel9` for Ansible Automation Platform 2.6. AAP-68419
- [CVE-2026-32597](https://access.redhat.com/security/cve/cve-2026-32597) - PyJWT accepts unknown crit header extensions (RFC 7515 §4.1.11 MUST violation) in:
  * ansible-automation-platform-26/ee-supported-rhel9 for Ansible Automation Platform 2.6. AAP-68399

## Automation controller

- [CVE-2025-14550](https://access.redhat.com/security/cve/cve-2026-14550) - Django: Denial of Service via crafted request with duplicate headers in:
  * automation-controller for Ansible Automation Platform 2.6. AAP-64818
- [CVE-2025-69534](https://access.redhat.com/security/cve/cve-2026-69534) - markdown: Denial of Service via malformed HTML-like sequences in:
  * automation-controller for Ansible Automation Platform 2.6. AAP-67446
- [CVE-2026-26007](https://access.redhat.com/security/cve/cve-2026-26007) - cryptography: Subgroup Attack due to missing subgroup validation for SECT curves in:
  * automation-controller for Ansible Automation Platform 2.6. AAP-65413
- [CVE-2026-27459](https://access.redhat.com/security/cve/cve-2026-27459) - pyOpenSSL: DTLS cookie callback buffer overflow in:
  * automation-controller for Ansible Automation Platform 2.6. AAP-68960
- [CVE-2026-32597](https://access.redhat.com/security/cve/cve-2026-32597) - PyJWT accepts unknown crit header extensions (RFC 7515 §4.1.11 MUST violation) in:
  * automation-controller for Ansible Automation Platform 2.6. AAP-68405

## Automation hub

- [CVE-2026-27459](https://access.redhat.com/security/cve/cve-2026-27459) - pyOpenSSL: DTLS cookie callback buffer overflow in:
  * ansible-automation-platform-26/hub-rhel9 for Ansible Automation Platform 2.6. AAP-68957
- [CVE-2026-32274](https://access.redhat.com/security/cve/cve-2026-32274) - Black: Arbitrary file writes from unsanitized user input in cache file name in:
  * ansible-automation-platform-26/hub-rhel9 for Ansible Automation Platform 2.6. AAP-68421
- [CVE-2026-32597](https://access.redhat.com/security/cve/cve-2026-32597) - PyJWT accepts unknown crit header extensions (RFC 7515 §4.1.11 MUST violation) in:
  * ansible-automation-platform-26/hub-rhel9 for Ansible Automation Platform 2.6. AAP-68401

## Platform Gateway

- [CVE-2026-27459](https://access.redhat.com/security/cve/cve-2026-27459) - pyasn1: Denial of Service via unbounded recursion in ASN.1 decoding in:
  * ansible-automation-platform-26/gateway-rhel9 for Ansible Automation Platform 2.6. AAP-69035
- [CVE-2026-27606](https://access.redhat.com/security/cve/cve-2026-27606) - Rollup: Remote Code Execution via Path Traversal Vulnerability in:
  * ansible-automation-platform-26/gateway-rhel9 for Ansible Automation Platform 2.6. AAP-66536
- [CVE-2026-29074](https://access.redhat.com/security/cve/cve-2026-29074) - SVGO: Denial of Service via XML entity expansion in:
  * automation-gateway for Ansible Automation Platform 2.6. AAP-68531
- [CVE-2026-32597](https://access.redhat.com/security/cve/cve-2026-32597) - PyJWT accepts unknown crit header extensions (RFC 7515 §4.1.11 MUST violation) in:
  * ansible-automation-platform-26/gateway-rhel9 for Ansible Automation Platform 2.6. AAP-68400
- [CVE-2026-33154](https://access.redhat.com/security/cve/cve-2026-33154) - Dynaconf: Arbitrary code execution via Server-Side Template Injection in:
  * ansible-automation-platform-26/gateway-rhel9 for Ansible Automation Platform 2.6. AAP-69466

## Ansible Automation Platform UI

- [CVE-2026-26996](https://access.redhat.com/security/cve/cve-2026-26996) - minimatch: Denial of Service via specially crafted glob patterns in:
  * automation-platform-ui for Ansible Automation Platform 2.6. AAP-66292
- [CVE-2026-27606](https://access.redhat.com/security/cve/cve-2026-27606) - Rollup: Remote Code Execution via Path Traversal Vulnerability in:
  * automation-platform-ui for Ansible Automation Platform 2.6. AAP-66535

## Event-Driven Ansible

- [CVE-2026-24049](https://access.redhat.com/security/cve/cve-2026-24049) - wheel: Privilege escalation or arbitrary code execution via malicious wheel file unpacking in:
  * ansible-automation-platform-26/eda-controller-rhel9-operator for Ansible Automation Platform 2.6. AAP-63863
- [CVE-2026-26007](https://access.redhat.com/security/cve/cve-2026-26007) - cryptography: Subgroup Attack due to missing subgroup validation for SECT curves in:
  * ansible-automation-platform-26/eda-controller-rhel9 for Ansible Automation Platform 2.6. AAP-65406
- [CVE-2026-27459](https://access.redhat.com/security/cve/cve-2026-27459) - pyOpenSSL: DTLS cookie callback buffer overflow in:
  * ansible-automation-platform-26/eda-controller-rhel9 for Ansible Automation Platform 2.6. AAP-68954
- [CVE-2026-30922](https://access.redhat.com/security/cve/cve-2026-30922) - pyasn1: Denial of Service via unbounded recursion in:
  * ansible-automation-platform-26/eda-controller-rhel9 for Ansible Automation Platform 2.6. AAP-69032
- [CVE-2026-32597](https://access.redhat.com/security/cve/cve-2026-32597) - PyJWT accepts unknown crit header extensions (RFC 7515 §4.1.11 MUST violation) in:
  * ansible-automation-platform-26/eda-controller-rhel9 for Ansible Automation Platform 2.6. AAP-68398
- [CVE-2026-33154](https://access.redhat.com/security/cve/cve-2026-33154) - Dynaconf: Arbitrary code execution via Server-Side Template Injection in:
  * ansible-automation-platform-26/eda-controller-rhel9 for Ansible Automation Platform 2.6. AAP-69465

## Red Hat Ansible Lightspeed

- [CVE-2025-69227](https://access.redhat.com/security/cve/cve-2025-69227) - aiohttp: Denial of Service via specially crafted POST request in:
  * ansible-automation-platform/ansible-lightspeed-service-container(2.6) for Ansible Automation Platform 2.6. AAP-65586
  * ansible-automation-platform/ansible-lightspeed-chatbot-container(2.6) for Ansible Automation Platform 2.6. AAP-65585
- [CVE-2025-69228](https://access.redhat.com/security/cve/cve-2025-69228) - aiohttp: Denial of Service via memory exhaustion from crafted POST request in:
  * ansible-automation-platform-26/ansible-lightspeed-service-container(2.6) for Ansible Automation Platform 2.6. AAP-65629
  * ansible-automation-platform/ansible-lightspeed-chatbot-container(2.6) for Ansible Automation Platform 2.6. AAP-65627
- [CVE-2026-0598](https://access.redhat.com/security/cve/cve-2026-0598) - Broken Object Level Authorization leading to cross-user AI conversation context injection in:
  * ansible-automation-platform/ansible-wisdom-service for Ansible Automation Platform 2.6. AAP-64145
- [CVE-2026-26007](https://access.redhat.com/security/cve/cve-2026-26007) - cryptography: Subgroup Attack due to missing subgroup validation for SECT curves in:
  * ansible-automation-platform-26/mcp-tools-rhel9 for Ansible Automation Platform 2.6. AAP-71204
  * ansible-automation-platform-26/lightspeed-rhel9 for Ansible Automation Platform 2.6. AAP-71203
  * ansible-automation-platform-26/lightspeed-chatbot-rhel9 for Ansible Automation Platform 2.6. AAP-71202
- [CVE-2026-27459](https://access.redhat.com/security/cve/cve-2026-27459) - pyOpenSSL: DTLS cookie callback buffer overflow in:
  * ansible-automation-platform-26/lightspeed-rhel9 for Ansible Automation Platform 2.6. AAP-68958
- [CVE-2026-29074](https://access.redhat.com/security/cve/cve-2026-29074) - SVGO: Denial of Service via XML entity expansion in:
  * ansible-automation-platform-26/lightspeed-rhel9 for Ansible Automation Platform 2.6. AAP-68528
- [CVE-2026-30922](https://access.redhat.com/security/cve/cve-2026-30922) - pyasn1: Denial of Service via unbounded recursion in:
  * ansible-automation-platform-26/lightspeed-rhel9 for Ansible Automation Platform 2.6. AAP-69041
- [CVE-2026-31812](https://access.redhat.com/security/cve/cve-2026-31812) - quinn-proto: Denial of Service via crafted QUIC Initial packet in:
  * ansible-automation-platform-26/lightspeed-chatbot-rhel9 for Ansible Automation Platform 2.6. AAP-68140
- [CVE-2026-32597](https://access.redhat.com/security/cve/cve-2026-32597) - PyJWT accepts unknown crit header extensions (RFC 7515 §4.1.11 MUST violation) in:
  * ansible-automation-platform-26/mcp-tools-rhel9 for Ansible Automation Platform 2.6. AAP-68404
  * ansible-automation-platform-26/lightspeed-rhel9 for Ansible Automation Platform 2.6. AAP-68403
  * ansible-automation-platform-26/lightspeed-chatbot-rhel9 for Ansible Automation Platform 2.6. AAP-68402
- [CVE-2026-33154](https://access.redhat.com/security/cve/cve-2026-33154) - Dynaconf: Arbitrary code execution via Server-Side Template Injection in:
  * ansible-automation-platform-26/lightspeed-rhel9 for Ansible Automation Platform 2.6. AAP-69468
- [CVE-2026-39373](https://access.redhat.com/security/cve/cve-2026-39373) - JWCrypto: Memory exhaustion via crafted compressed JWE tokens in:
  * ansible-automation-platform-26/lightspeed-rhel9 for Ansible Automation Platform 2.6. AAP-71150
- [CVE-2026-4800](https://access.redhat.com/security/cve/cve-2026-4800) - lodash: Arbitrary code execution via untrusted input in template imports in:
  * ansible-automation-platform-26/lightspeed-rhel9 for Ansible Automation Platform 2.6. AAP-70458

## Ansible Automation Platform security

- [CVE-2026-35029](https://access.redhat.com/security/cve/cve-2026-35029) - LiteLLM: Remote code execution and privilege escalation via unrestricted proxy configuration endpoint in:
  * redhat-user-workloads/lightspeed-chatbot-rhel9 for Ansible Automation Platform 2.6. AAP-70909
- [CVE-2026-35030](https://access.redhat.com/security/cve/cve-2026-35030) - LiteLLM: Authentication bypass and privilege escalation via OIDC userinfo cache key collision in:
  * redhat-user-workloads/lightspeed-chatbot-rhel9 for Ansible Automation Platform 2.6. AAP-70913
- [CVE-2026-4926](https://access.redhat.com/security/cve/cve-2026-4926) - path-to-regexp: Denial of Service via crafted regular expressions in:
  * ansible-automation-platform-tech-preview/mcp-server-rhel9 for Ansible Automation Platform 2.6. AAP-70022

## Receptor

- [CVE-2026-25679](https://access.redhat.com/security/cve/cve-2026-25679) - Incorrect parsing of IPv6 host literals in net/url in:
  * ansible-automation-platform-26/receptor-rhel9 for Ansible Automation Platform 2.6. AAP-68747
  * receptor for Ansible Automation Platform 2.6. AAP-68731
- [CVE-2026-27137](https://access.redhat.com/security/cve/cve-2026-27137) - Incorrect enforcement of email constraints in crypto/x509 in:
  * ansible-automation-platform-26/receptor-rhel9 for Ansible Automation Platform 2.6. AAP-68737

## Bug fixes

## Platform gateway

- Fixed an issue where organization administrators could not view, modify, or remove permissions on teams outside of their organization.(AAP-72502)

## Automation Hub

- Fixed an issue where the Automation Hub OpenAPI specification was missing service_index endpoints.(AAP-72227)
- Fixed an issue where artifact download view counting could return an error instead of correctly using name/namespace.(AAP-71346)

## Red Hat Lightspeed

- Fixed an issue where the containerized Red Hat Lightspeed install did not correctly configure the Azure OpenAI provider base URL for Llama Stack 0.4.3.(AAP-72046)
- Fixed an issue where the containerized Red Hat Lightspeed install did not correctly configure the Azure OpenAI provider base URL for Llama Stack 0.4.3.(AAP-71979)
- Fixed an issue where the /api/lightspeed/v1/ai/chat endpoint response schema could deviate from the documented API specification.(AAP-70666)
- Fixed an issue where MCP-enabled prompts could fail due to max_tokens handling and provider defaults in lightspeed-stack-providers.(AAP-70396)
- Fixed an issue where the wisdom-manage shell command output was impacted by the Django 5.2 verbosity level change.(AAP-69164)
- Fixed an issue where ALIA/Lightspeed backups were abnormally large due to unnecessary files being included.(AAP-68774)
- Fixed an issue where ALIA/Lightspeed backups were abnormally large due to unnecessary files being included.(AAP-67911)

## Container-based installer Ansible Automation Platform

- Fixed an issue where component TLS certificates were not regenerated on certain CA certificate changes.(AAP-71956)
- Fixed an issue where the Redis hostname could fail to be set in disconnected containerized installer environments.(AAP-71493)
- Fixed an issue where the 2.6 bundle installer could fail when PCP was enabled with a metrics service host in inventory, by ensuring the PCP image is loaded on Automation Metrics nodes.(AAP-71026)

## Django ansible base

- Fixed an issue where a fresh installation could immediately show a “RoleDefinition matching query does not exist” error during resource sync.(AAP-71868)
- Fixed an issue where periodic resource sync between Controller and Gateway could delete valid role assignments when pagination failed mid-fetch.(AAP-71775)

## Content

- Fixed an issue where the ansible.controller collection job_template module did not support Bitbucket webhooks.(AAP-71827)

## Event-Drive Ansible

- Fixed an issue where projects could be deleted while a project sync was running.(AAP-71406)
- Fixed an issue where the EDA event-stream node tag in gateway config could be incorrect, causing routing issues to EDA event-stream.(AAP-69827)

## Automation controller

- Fixed an issue where nested workflows could apply incorrect variable precedence when set_stats artifacts were passed via extra_vars.(AAP-70756)
- Fixed an issue where object creation could be significantly slower in organizations with large numbers of resources, by reducing RoleEvaluation object creation overhead.(AAP-70752)
- Fixed an issue where inventory imports with large numbers of changes could take an excessive amount of time.(AAP-70377)
- Fixed an issue where concurrent jobs could incorrectly clear host facts due to a race condition.(AAP-69262)
- Fixed an issue where job cancellation did not reliably propagate to dependent jobs in workflows.(AAP-68975)
- Fixed an issue where project_update.yml could fail with a jinja2 error when using custom execution environment images with newer ansible-core versions.(AAP-68783)

## Ansible Automation Platform Operator

- Fixed an issue where the Gateway Operator stored database passwords unencrypted, by removing postgresql-init ConfigMap and switching to runtime-executed postgresql modules.(AAP-70404)
- Fixed an issue where Automation Hub backup ignored postgres_image and postgres_image_version, causing it to always use the default PostgreSQL image.(AAP-69856)
- Fixed an issue where operator event creation could fail with a time-parsing error that masked the underlying error message.(AAP-69634)
- Fixed an issue where CRD validation for _image and _image_version fields was missing for installer operators.(AAP-68765)
- Fixed an issue where users could not override nested restore parameters (including `no_log`) in `AnsibleAutomationPlatformRestore.(`AAP-68242)

## Ansible Automation Platform ui

- Fixed an issue where unthrottled WebSocket refresh events caused excessive Jobs list API requests, leading to queued requests and an unresponsive UI under high concurrency.(AAP-70349)
- Fixed an issue where the Assign Roles wizard did not correctly show “System” as a resource type when assigning custom roles.(AAP-67506)
- Fixed an issue where OAuth authorization could fail to redirect correctly after Keycloak SSO because the next parameter was not preserved.(AAP-59343)

## Receptor

- Fixed an issue where the work results command could emit misleading warnings during connection shutdown.(AAP-43847)
