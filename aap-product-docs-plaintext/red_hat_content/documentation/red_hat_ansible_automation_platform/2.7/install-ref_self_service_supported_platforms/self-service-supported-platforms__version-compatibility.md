# Supported platforms for Ansible automation portal
## Ansible Automation Platform version compatibility

Ansible automation portal operates on an independent, asynchronous release schedule from the core platform. A given release of Ansible automation portal remains compatible with multiple Ansible Automation Platform releases.

*Table 1. Ansible automation portal compatibility matrix*

| Component                          | Supported versions                                                                                          |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Ansible Automation Platform        | Versions 2.5, 2.6, and 2.7                                                                                  |
| OpenShift Container Platform       | Version 4.14 and later (Helm chart; Operator available in version 2.7)                                      |
| Red Hat Enterprise Linux appliance | Red Hat Enterprise Linux 9.4 and later deployed on KVM, Red Hat OpenShift Virtualization, or VMware vSphere |

Note:

Ansible automation portal connects to Ansible Automation Platform 2.5, 2.6, and 2.7 instances. For OpenShift Helm deployments connecting to an Ansible Automation Platform 2.5 instance, see the self-service automation portal documentation published on the Red Hat Customer Portal. For RHEL appliance deployments, use the version-agnostic deployment instructions in this guide.

