# Prepare to migrate to Managed Ansible Automation Platform
## Migrate to Managed Ansible Automation Platform

Submit a support ticket on the Red Hat Customer Portal to request a migration to Managed Ansible Automation Platform.

### Before you begin

- You have a migration artifact from your source environment.

- Your source deployment is on the same major version as the Managed Ansible Automation Platform offering and on the latest async/patch release of that version. For example, if Managed Ansible Automation Platform is running 2.7, your source must be on Ansible Automation Platform 2.7.x (latest patch).

Check the current Managed Ansible Automation Platform version 2.7 [Release notes](/documentation/en-us/red_hat_ansible_automation_platform/2.7/../../2-7/whats-new/2-7-release-notes.ditamap)

### Procedure

1.  Submit a [support ticket](https://access.redhat.com/support/cases/#/case/new/get-support?caseCreate=true) on the Red Hat Customer Portal requesting a migration to Managed Ansible Automation Platform. The support ticket should include:

- Source installation type (RPM, Containerized, OpenShift)
- Managed Ansible Automation Platform URL or deployment name
- Source version (installation program or Operator version)

2.  The Ansible *Site Reliability Engineering* (SRE) team provides instructions in the support ticket on how to upload the resulting migration artifact to secure storage for processing.
3.  The Ansible SRE team imports the migration artifact into the identified target instance and notifies the customer through the support ticket.
4.  The Ansible SRE team notifies customers of successful migration.

