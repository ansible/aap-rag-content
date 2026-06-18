# RPM to OpenShift Container Platform migration prerequisites

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
