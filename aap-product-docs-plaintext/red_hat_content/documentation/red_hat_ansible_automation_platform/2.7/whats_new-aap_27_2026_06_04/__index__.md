# Ansible Automation Platform patch release June 4, 2026

The following release notes detail the CVEs and Bug fixes for the Ansible Automation Platform patch released on June 4, 2026

This release includes the following components and versions:

| Release Date     | Component versions                                                                                                                                                                                                                 |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>June 4, 2026 | Automation controller 4.8.0Automation hub 4.12.1Event-Driven Ansible 1.3.1Container-based installer Ansible Automation Platform (bundle) 2.7-1.1Container-based installer Ansible Automation Platform (online) 2.7-1Receptor 1.6.5 |


CSV Versions in this release:

- Namespace-scoped bundle: aap-operator.v2.7.0-0.1780540119
- Cluster-scoped bundle: aap-operator.v2.7.0-0.1780540580

## CVE

## Lightspeed

- [CVE-2026-24486](https://access.redhat.com/security/cve/cve-2026-48710) – Starlette: Security restriction bypass via malformed HTTP Host header

## Bug fixes

## Automation hub

- Fixed an issue where execution environment (EE) container images that existed in automation hub before a 2.6 to 2.7 upgrade failed to sync or pull with errors such as "unexpected end of JSON input" or "manifest unknown." The upgrade did not fully populate some manifest records for pre-existing EE images. New EE images pushed after the upgrade and collections were not affected. (AAP-77470)
