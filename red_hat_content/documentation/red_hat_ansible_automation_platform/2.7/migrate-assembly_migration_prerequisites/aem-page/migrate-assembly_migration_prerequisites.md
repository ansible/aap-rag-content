+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-assembly_migration_prerequisites"
title = "Migration prerequisites - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-assembly_migration_prerequisites/", "Migration prerequisites"]]
category = "Migrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-assembly_migration_prerequisites/aem-page/migrate-assembly_migration_prerequisites.html"
last_crumb = "Migration prerequisites"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Migration prerequisites"
oversized = "false"
page_slug = "migrate-assembly_migration_prerequisites"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/migrate-assembly_migration_prerequisites"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-assembly_migration_prerequisites/toc/toc.json"
type = "aem-page"
+++

# Migration prerequisites

Prerequisites for migrating your Ansible Automation Platform deployment. For your specific migration path, ensure that you meet all necessary conditions before proceeding.

Warning:

To upgrade to Ansible Automation Platform 2.7, you must first migrate from your RPM-based deployment to a containerized or OpenShift Container Platform deployment. RPM-based deployments are not supported as an upgrade path to 2.7.

## Prerequisites for migrating using the aap_snapshot collection

Before using the `ansible.aap_snapshot` collection to migrate your Ansible Automation Platform deployment to OpenShift Container Platform, verify that your environment meets the prerequisites for both phases of the migration.

Prerequisites are divided into two stages that correspond to the export and import phases of the workflow. Meet all export prerequisites before running the `artifact_export` playbook on your source environment. Meet all import prerequisites before running the `artifact_import` playbook on your control node.

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
