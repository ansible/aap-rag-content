# About the aap_snapshot import workflow

Use the `ansible.aap_snapshot` collection to import your Ansible Automation Platform configuration, credentials, and content from an RPM-based deployment into an OpenShift Container Platform operator-managed deployment.

The `artifact_import.yaml` playbook automates the full import sequence, from preflight validation through database restore and post-import reconciliation.

The Ansible Automation Platform version in the artifact must exactly match the version running in the OCP target namespace. The preflight phase enforces this requirement and fails early if the versions do not match.

After import, instance groups and host groups require manual reconciliation. Virtual machine nodes do not map one-to-one to pods, so group assignments must be reviewed and updated in the Ansible Automation Platform UI before the restored deployment is used in production.
