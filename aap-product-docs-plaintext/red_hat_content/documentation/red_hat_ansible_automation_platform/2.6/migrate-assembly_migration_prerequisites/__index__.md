# Migration prerequisites

Prerequisites for migrating your Ansible Automation Platform deployment. For your specific migration path, ensure that you meet all necessary conditions before proceeding.

Warning:

To upgrade to Ansible Automation Platform 2.7, you must first migrate from your RPM-based deployment to a containerized or OpenShift Container Platform deployment. RPM-based deployments are not supported as an upgrade path to 2.7.

## RPM to containerized migration prerequisites

Before migrating from an RPM-based deployment to a container-based deployment, ensure you meet the following prerequisites:

Note:

Completing this migration is a required step if you plan to upgrade to Ansible Automation Platform 2.7. RPM-based deployments are not supported as an upgrade path to 2.7.

- You have a source RPM-based deployment of Ansible Automation Platform.
- The source RPM-based deployment is on the latest async release of the version you are on.
- You have a target environment prepared for a container-based deployment of Ansible Automation Platform.
- You have downloaded the containerized installation program for the latest release of the Ansible Automation Platform version you are on.
- You have enough storage for database dumps and backups.
- There is network connectivity between the source and target environments.

## RPM to OpenShift Container Platform migration prerequisites

Before migrating from an RPM-based deployment to an OpenShift Container Platform deployment, ensure you meet the following prerequisites:

Note:

Completing this migration is a required step if you plan to upgrade to Ansible Automation Platform 2.7. RPM-based deployments are not supported as an upgrade path to 2.7.

- You have a source RPM-based deployment of Ansible Automation Platform.
- The source RPM-based deployment is on the latest async release of the version you are on.
- You have a target OpenShift Container Platform environment ready.
- You have Ansible Automation Platform Operator available for the latest release of the Ansible Automation Platform version you are on.
- You have made a decision on internal or external database configuration.
- You have made a decision on internal or external Redis configuration.
- There is network connectivity between the source and target environments.

## RPM to Managed Ansible Automation Platform migration prerequisites

Before migrating from an RPM-based deployment to a Managed Ansible Automation Platform deployment, ensure you meet the following prerequisites:

Note:

Completing this migration is a required step if you plan to upgrade to Ansible Automation Platform 2.7. RPM-based deployments are not supported as an upgrade path to 2.7.

- You have a source RPM-based deployment of Ansible Automation Platform.
- The source deployment is on the latest release of the Ansible Automation Platform version you are on.
- You have a target Managed Ansible Automation Platform deployment.
- You have enabled local authentication on the source deployment before the migration.
- A local administrator account must be functional on the source deployment before migration. Verify this by performing a successful login to the source deployment.
- You have a plan to retain a backup throughout the migration process and to ensure that your existing Ansible Automation Platform deployment remains active until your migration has completed successfully.
- You have a plan for any environment changes based on the migration from a self-hosted Ansible Automation Platform deployment to a Managed Ansible Automation Platform deployment:
* Job log retention changes from a customer-configured option to 30 days.
* Network changes occur when moving the control plane to the managed service.
* Automation mesh requires reconfiguration.
- You must reconfigure or re-create Single Sign-On (SSO) identity providers post-migration to account for URL changes.

## Containerized to OpenShift Container Platform migration prerequisites

Before migrating from a container-based deployment to an OpenShift Container Platform deployment, ensure that you meet the following prerequisites:

- You have a source container-based deployment of Ansible Automation Platform.
- The source deployment is on the latest async release of the version you are on.
- You have a target OpenShift Container Platform environment ready.
- You have an Ansible Automation Platform Operator available for the latest release of the Ansible Automation Platform version you are on.
- You have decided between internal or external database configuration.
- You have decided between internal or external Redis configuration.
- There is network connectivity between the source and target environments.

## Containerized to Managed Ansible Automation Platform migration prerequisites

Before migrating from a container-based deployment to a Managed Ansible Automation Platform deployment, ensure that you meet the following prerequisites:

- You have a source container-based deployment of Ansible Automation Platform.
- The source deployment is on the latest release of the Ansible Automation Platform version you are on.
- You have a target Managed Ansible Automation Platform deployment.
- You have enabled local authentication on the source deployment before the migration.
- A local administrator account must be functional on the source deployment before migration. Verify this by performing a successful login to the source deployment.
- You have a plan to retain a backup throughout the migration process and to ensure that your existing Ansible Automation Platform deployment remains active until your migration has completed successfully.
- You have a plan for any environment changes based on the migration from a self-hosted Ansible Automation Platform deployment to a Managed Ansible Automation Platform deployment:
* Job log retention changes from a customer-configured option to 30 days.
* Network changes occur when moving the control plane to the managed service.
* Automation mesh requires reconfiguration.
- You must reconfigure or re-create Single Sign-On (SSO) identity providers post-migration to account for URL changes.
