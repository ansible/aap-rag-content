# 10. Patch releases
## 10.1. Ansible Automation Platform patch release September 23, 2025
### 10.1.10. RPM-based Ansible Automation Platform




#### 10.1.10.1. Bug Fixes




- Fixed an issue where backup was failing when the deployment had more than one Event-Driven Ansible node without `    eda_node_type` defined. (AAP-52892)
- Fixed a typographical error in the automation controller group name that led to restore failures. (AAP-52078) Fixed an issue where platform gateway `    uwsgi` processes were not configurable in the Ansible Automation Platform 2.5 RPM installer. (AAP-50390)
- Fixed an issue where `    redis_mode=standalone` and the Redis group were defined at the same time. (AAP-53560)
- Fixed an issue where the Redis node list could not be created on Event-Driven Ansible or platform gateway nodes which were not part of the Redis group. (AAP-53528)
- Removed the `    pulpcore-manager` sudo requirement. (AAP-52288)


