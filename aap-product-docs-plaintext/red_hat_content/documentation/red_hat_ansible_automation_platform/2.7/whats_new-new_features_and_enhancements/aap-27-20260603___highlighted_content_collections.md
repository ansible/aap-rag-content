# New features and enhancements
## Highlighted Content Collections

- hashicorp.vault
* Supports Vault KV secret lookups and is compatible with AAP’s existing Vault credential plugin workflows.
* The collection includes content for managing Vault policies, authentication methods, dynamic secrets (e.g., database, cloud), and PKI workflows.
* Enterprise Vault features such as namespaces and multi-tenant configurations are supported and documented.
* Event-Driven Ansible can trigger rulebook workflows based on Vault events via webhook or polling mechanisms.
* Migration documentation is available to help users transition from `community.hashi_vault` to `hashicorp.vault` with minimal disruption.
* Solution guides and examples are published for common Vault use cases, including dynamic credentials, short-lived SSH keys, and secure application integration.
- microsoft.mecm
* Brand New Certified Collection: Officially launched as a Red Hat Certified Collection (v1.0.0) with 26 new modules acting as a bridge between Ansible and Microsoft Endpoint Configuration Manager.
* Patch Management & Zero-Downtime: Features granular modules like software_update_group, software_update_deployment, and install_updates to orchestrate zero-downtime Windows Server patching.
* Client Management: Added a client_action module to trigger immediate actions on client devices (e.g., forcing machine policy retrievals) without waiting for standard polling cycles.
* Health Status Retrieval: Features several info modules (dp_status_info, wsus_sync_status_info) to verify MECM infrastructure health before kicking off deployments.
- microsoft.scom
* New Certified Release: Reached v1.0.1 as a newly certified collection.
* SCOM Infrastructure Management: Provides a suite of modules for automating Microsoft System Center Operations Manager infrastructure.
* Event-Driven Hooks: Designed to route SCOM alerts (via webhooks or event streams) into Event-Driven Ansible for automated remediations to Windows Server alerts.

