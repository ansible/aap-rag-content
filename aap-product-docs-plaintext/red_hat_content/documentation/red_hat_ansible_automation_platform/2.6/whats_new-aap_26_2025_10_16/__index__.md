# Ansible Automation Platform patch release October 16, 2025

The following release notes detail the updates for the Ansible Automation Platform patch released on October 16, 2025.

This release includes the following components and versions:

| Release Date         | Component versions                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>October 16, 2025 | Automation controller 4.7.2Automation hub 4.11.1Event-Driven Ansible 1.2.0Container-based installer Ansible Automation Platform (bundle) 2.6-1.1Container-based installer Ansible Automation Platform (online) 2.6-1Receptor 1.5.7RPM-based installer Ansible Automation Platform (bundle) 2.6-1.1RPM-based installer Ansible Automation Platform (online) 2.6-1 |


CSV Versions in this release:

- Namespace-scoped Bundle: aap-operator.v2.6.0-0.1760139263
- Cluster-scoped Bundle: aap-operator.v2.6.0-0.1760139657

## Ansible Automation Platform

Bug Fixes
- Fixed an issue where the claims processing failed to migrate services during the post-migrate upgrade process.(AAP-55631)

## Automation controller

Bug Fixes
- Fixed an issue where the Ansible Automation Platform upgrade would be marked as failed if a single authenticator failed to migrate.(AAP-55629)

## Automation hub

Bug Fixes
- Fixed a global galaxy team role migration issue that could occur during the post-migrate upgrade process.(AAP-55304)
- Fixed an issue caused by a constraint violation during migrations.(AAP-55309)
- Fixed an issue from `aap-gateway-manage,``migrate_service_data`, that states **Role definition content type must be null to assign globally**, which was due to permissions in hub that failed validation.(AAP-55639)
