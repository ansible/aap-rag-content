+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-prerequisites_for_migrating_using_the_aap_snapshot_collection"
title = "Prerequisites for migrating using the aap_snapshot collection - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-assembly_migration_prerequisites/", "Migration prerequisites"]]
category = "Migrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-prerequisites_for_migrating_using_the_aap_snapshot_collection/aem-page/migrate-prerequisites_for_migrating_using_the_aap_snapshot_collection.html"
last_crumb = "Prerequisites for migrating using the aap_snapshot collection"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Prerequisites for migrating using the aap_snapshot collection"
oversized = "false"
page_slug = "migrate-prerequisites_for_migrating_using_the_aap_snapshot_collection"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/migrate-prerequisites_for_migrating_using_the_aap_snapshot_collection"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-prerequisites_for_migrating_using_the_aap_snapshot_collection/toc/toc.json"
type = "aem-page"
+++

# Prerequisites for migrating using the aap_snapshot collection

Before using the `ansible.aap_snapshot` collection to migrate your Ansible Automation Platform deployment to OpenShift Container Platform, verify that your environment meets the prerequisites for both phases of the migration.

Prerequisites are divided into two stages that correspond to the export and import phases of the workflow. Meet all export prerequisites before running the `artifact_export` playbook on your source environment. Meet all import prerequisites before running the `artifact_import` playbook on your control node.

## Prerequisites for containerized deployment export

Before running the `artifact_export` playbook, verify that your source containerized deployment, control node, and network connectivity meet all prerequisites.

### Source environment

- Ansible Automation Platform is installed on the source hosts using the containerized installation program.
- All Ansible Automation Platform containerized services are running.
- You have the inventory file from your Ansible Automation Platform containerized installation.

### Control node

- Ansible Core is installed: version 2.14 or later for RHEL 9, version 2.16 or later for RHEL 10.

- The `ansible.aap_snapshot` collection is installed from automation hub. The collection is not included with the Ansible Automation Platform installation program and must be installed separately:

```console
ansible-galaxy collection install ansible.aap_snapshot
```

    For more information, see [anaible.aap_snapshot on automation hub](https://console.redhat.com/ansible/automation-hub/collections/published/ansible/aap_snapshot/details).

- SSH access is available from the control node to all component hosts (automation controller, automation hub, platform gateway, Event-Driven Ansible, and database hosts).

- The control node has sufficient free disk space in the directory from which you run the playbook. The required disk space depends on component database sizes and, if automation hub content export is enabled, the size of the automation hub Pulp media directory on the automation hub host.

## Prerequisites for the OCP deployment import

Before running the `artifact_import` playbook, verify that your control node, OpenShift cluster, and migration artifact are correctly configured. Meeting these requirements before you start prevents mid-run failures that require manual recovery.

### Control node requirements

Ansible Core version
Ansible Core 2.16.0 or later is installed.

Collection installation
The `ansible.aap_snapshot` collection is installed
 from automation hub:

```
ansible-galaxy collection install ansible.aap_snapshot
```

Migration artifact
The `.tar` artifact from the export workflow is present on the control node and readable by the user running the playbook. Pass its full path using `artifact_file`. This variable has no default and the playbook fails at startup if it is not set.

### OCP environment requirements

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

## Prerequisites for containerized deployment import

Before running the `artifact_import` playbook, verify that your target containerized deployment, control node, and migration artifact are correctly configured.

### Target deployment

- Ansible Automation Platform is installed on the target hosts using the containerized installation program.
- All Ansible Automation Platform services on the target hosts are running.
- You have the inventory file used to install the target deployment.

### Control node

- Ansible Core is installed: version 2.14 or later for RHEL 9, version 2.16 or later for RHEL 10.

- The `ansible.aap_snapshot` collection is installed from automation hub. The collection is not included with the Ansible Automation Platform installation program and must be installed separately:

```console
ansible-galaxy collection install ansible.aap_snapshot
```

    For more information, see [anaible.aap_snapshot on automation hub](https://console.redhat.com/ansible/automation-hub/collections/published/ansible/aap_snapshot/details).

- SSH access is available from the control node to all component hosts (automation controller, automation hub, platform gateway, and Event-Driven Ansible hosts).

- The export artifact file (`.tar`) produced by the `artifact_export` playbook is present on the control node and readable by the user running the playbook. Pass its full path using `artifact_file`. This variable has no default and the playbook fails at startup if it is not set.
