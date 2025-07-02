# 10. Patch releases
## 10.2. Ansible Automation Platform patch release June 9, 2025
### 10.2.4. Container-based Ansible Automation Platform




#### 10.2.4.1. Enhancements




- Allow users to skip automation controller demo data creation.(AAP-46482)
- Validating the Automation hub NFS share path format during the preflight role execution.(AAP-46306)


#### 10.2.4.2. Bug Fixes




- Fixed an issue where the custom Certificate Authority (CA) TLS certificate was not passed to the external database validation during the preflight role execution.(AAP-46480)
- Fixed a log redirection error for the Ansible automation hub, Event-Driven Ansible, and Unified UI containers.(AAP-46478)
- Fixed an issue where `    ~/.local/bin` path was not added to the user $ `    PATH` environment variable during PostgreSQL database dump and restore.(AAP-46209)
- Fixed the order of operations for handling service nodes to ensure only valid nodes are configured.(AAP-45551)


