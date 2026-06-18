# Migration process overview

Understand the complete migration workflow including preparation, export, artifact creation, import, reconciliation, and validation steps for moving between Ansible Automation Platform installation types.

Important:

You can only migrate to a different installation type of the same Ansible Automation Platform version. For example, you can migrate from containerized 2.7 to OpenShift Container Platform 2.7, but not from containerized 2.6 to OpenShift Container Platform 2.7.

Warning:

If you are running an RPM-based deployment, complete your migration to a containerized or OpenShift Container Platform deployment before upgrading to Ansible Automation Platform 2.7. RPM-based deployments are not supported as an upgrade path to 2.7.

The migration between Ansible Automation Platform installation types follows this general workflow:

1. Prepare and assess the source environment
2. Export the source environment
3. Create and verify the migration artifact
4. Prepare and assess the target environment
5. Import the migration content to the target environment
6. Reconcile the target environment post-import
7. Validate the target environment
