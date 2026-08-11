# Import Ansible Automation Platform data into an OCP deployment

Run the `artifact_import` playbook from the `ansible.aap_snapshot` collection to restore your Ansible Automation Platform configuration, credentials, and content onto an OpenShift Container Platform operator-managed deployment.

## Before you begin

- The `ansible.aap_snapshot` collection is installed on the control node.
- The migration artifact `.tar` file is present and readable on the control node.
- A valid kubeconfig for the OCP target namespace is available.
- The `gateway_admin_password` and `gateway_hostname` for the source deployment are available.
- A ReadWriteMany (RWX) StorageClass is available in the OCP target namespace if the artifact includes automation hub.
- The Ansible Automation Platform version in the artifact matches the Ansible Automation Platform version in the OCP target namespace.

## About this task

The playbook runs automated preflight checks, restores component databases, and produces a post-import advisory listing any required manual steps.

