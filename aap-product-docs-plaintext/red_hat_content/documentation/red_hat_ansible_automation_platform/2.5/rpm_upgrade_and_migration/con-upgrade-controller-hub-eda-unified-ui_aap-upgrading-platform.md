# 2. Upgrading to Red Hat Ansible Automation Platform 2.5
## 2.8. Automation controller and automation hub 2.4 and Event-Driven Ansible 2.5 with unified UI upgrades




Ansible Automation Platform 2.5 supports upgrades from Ansible Automation Platform 2.4 environments for all components, with the exception of Event-Driven Ansible. You can also configure a mixed environment with Event-Driven Ansible from 2.5 connected to a legacy 2.4 cluster. Combining install methods (OCP, RPM, Containerized) within such a topology is not supported by Ansible Automation Platform.

Note
If you are running the 2.4 version of Event-Driven Ansible in production, before you upgrade, contact Red Hat support or your account representative for more information on how to move to Ansible Automation Platform 2.5.



Supported topologies described in this document assume that:

- 2.4 services will only include automation controller and automation hub.
- 2.5 parts will always include Event-Driven Ansible and the unified UI (platform gateway).
- Combining installation methods for these topologies is not supported.


