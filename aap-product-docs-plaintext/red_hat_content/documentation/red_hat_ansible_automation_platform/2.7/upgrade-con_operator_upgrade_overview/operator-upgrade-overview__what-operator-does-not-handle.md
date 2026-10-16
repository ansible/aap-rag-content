# Overview
## What the operator does not handle

The operator automates the core platform upgrade, but several tasks require manual action before or after the upgrade:

- **Execution node updates.** For operator-based deployments, execution node updates at the OS level are not managed by the operator. You must update execution nodes manually after the control plane upgrade completes.
- **API endpoint and integration changes.** If the new release includes API changes, such as the migration to platform gateway in Ansible Automation Platform 2.7, you must update scripts, playbooks, and external integrations separately.
- **Authentication provider migration.** Changes to authentication configuration, such as moving third-party providers from component-level to platform gateway, require manual reconfiguration.
- **Backup and restore.** The operator does not create backups before an upgrade. You must create `AutomationControllerBackup`, `AutomationHubBackup`, and `EDABackup` resources before starting the upgrade.
- **OpenShift Container Platform version compatibility.** The operator does not verify whether your OpenShift cluster version is supported by the target Ansible Automation Platform release. You must confirm compatibility before upgrading.

