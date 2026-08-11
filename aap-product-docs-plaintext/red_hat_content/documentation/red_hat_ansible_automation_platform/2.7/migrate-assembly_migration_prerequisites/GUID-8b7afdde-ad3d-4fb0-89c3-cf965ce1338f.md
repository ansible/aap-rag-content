# Migration prerequisites
## Prerequisites for migrating using the aap_snapshot collection
### Prerequisites for the OCP deployment import

Before running the `artifact_import` playbook, verify that your control node, OpenShift cluster, and migration artifact are correctly configured. Meeting these requirements before you start prevents mid-run failures that require manual recovery.

#### Control node requirements

Ansible Core version
Ansible Core 2.16.0 or later is installed.

Collection installation
The `ansible.aap_snapshot` collection is installed from automation hub:

```
ansible-galaxy collection install ansible.aap_snapshot
```

Migration artifact
The `.tar` artifact from the export workflow is present on the control node and readable by the user running the playbook. Pass its full path using `artifact_file`. This variable has no default and the playbook fails at startup if it is not set.

#### OCP environment requirements

OpenShift cluster readiness
An OpenShift Container Platform cluster is provisioned and the Ansible Automation Platform Operator is installed in the target namespace. If the team responsible for your OpenShift environment is separate from the team managing Ansible Automation Platform, coordinate cluster access and namespace provisioning before beginning the import.

Kubeconfig access
A valid `kubeconfig` file with cluster-admin or namespace-admin access to the OpenShift Container Platform target namespace is available. The playbook resolves kubeconfig in this order:

1. The `kubeconfig` extra variable (`-e kubeconfig=/path/to/kubeconfig`)
2. The `K8S_AUTH_KUBECONFIG` environment variable
3. The `KUBECONFIG` environment variable
4. The default location (`~/.kube/config`)

The Ansible Automation Platform Operator uses the `aap.ansible.com/v1alpha1` API version for all custom resources (`AnsibleAutomationPlatform`, `AnsibleAutomationPlatformBackup`, `AnsibleAutomationPlatformRestore`).

ReadWriteMany StorageClass for automation hub
A ReadWriteMany (RWX) StorageClass is available in the OpenShift Container Platform cluster, and `hub_file_storage_class` is set to its name. This is required when the artifact includes automation hub. Storage class auto-detection is not supported. If `hub_file_storage_class` is not set and the artifact includes automation hub, the import fails at preflight.

Platform gateway admin password and hostname
`gateway_admin_password` and `gateway_hostname` are set in your inventory. Both are required for the Pulp repair API call during hub reconciliation. The reconcile hub role runs for all OpenShift Container Platform imports regardless of whether the artifact includes automation hub, so these variables are required even if hub was not exported.

Version match
The Ansible Automation Platform version in the artifact matches the version installed in the OpenShift Container Platform target namespace, and the operator deployment is healthy.

Network access
The control node has network access to the OpenShift Container Platform API endpoint on port 6443.

