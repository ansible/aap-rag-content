# 4. Migration prerequisites
## 4.3. RPM to Managed Ansible Automation Platform migration prerequisites




Before migrating from an RPM-based deployment to a Managed Ansible Automation Platform deployment, ensure you meet the following prerequisites:

- You have a source RPM-based deployment of Ansible Automation Platform.
- The source deployment is on the latest release of the Ansible Automation Platform version you are on.
- You have a target Managed Ansible Automation Platform deployment.
- You have enabled local authentication on the source deployment before the migration.
- A local administrator account must be functional on the source deployment before migration. Verify this by performing a successful login to the source deployment.
- You have a plan to retain a backup throughout the migration process and to ensure that your existing Ansible Automation Platform deployment remains active until your migration has completed successfully.
- You have a plan for any environment changes based on the migration from a self-hosted Ansible Automation Platform deployment to a Managed Ansible Automation Platform deployment:


- Job log retention changes from a customer-configured option to 30 days.
- Network changes occur when moving the control plane to the managed service.
- Automation mesh requires reconfiguration.

- You must reconfigure or re-create Single Sign-On (SSO) identity providers post-migration to account for URL changes.


