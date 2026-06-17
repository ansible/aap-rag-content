# Ansible Automation Platform patch release October 6, 2025

The following release notes detail the updates for the Ansible Automation Platform patch released on October 6, 2025.

This release includes the following components and versions:

| Release Date        | Component versions                                                                                                                                                                                                                                                                                                                                           |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <br>October 6, 2025 | Automation controller 4.7.1Automation hub 4.11.0Event-Driven Ansible 1.2.0Container-based installer Ansible Automation Platform (bundle) 2.6-1Container-based installer Ansible Automation Platform (online) 2.6-1Receptor 1.5.7RPM-based installer Ansible Automation Platform (bundle) 2.6-1RPM-based installer Ansible Automation Platform (online) 2.6-1 |


CSV Versions in this release:

- Namespace-scoped Bundle: aap-operator.v2.6.0-0.1759764484
- Cluster-scoped Bundle: aap-operator.v2.6.0-0.1759764962

## Automation hub

- Fixed an issue where the automation hub collections in 2.6 could not be pulled with Ansible Galaxy due to incorrect dynamic http logic. This issue only affects the Red Hat Ansible Automation Platform Operator installation.(AAP-55099)
