+++
title = "Import Ansible Automation Platform data into an OCP deployment - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/import_ansible_automation_platform_data_into_an_ocp_deployment"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/import_ansible_automation_platform_data_into_an_ocp_deployment/aem-page/import_ansible_automation_platform_data_into_an_ocp_deployment.html"
last_crumb = "Import Ansible Automation Platform data into an OCP deployment"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Import Ansible Automation Platform data into an OCP deployment"
oversized = "false"
page_slug = "import_ansible_automation_platform_data_into_an_ocp_deployment"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/import_ansible_automation_platform_data_into_an_ocp_deployment"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/import_ansible_automation_platform_data_into_an_ocp_deployment/toc/toc.json"
type = "aem-page"
+++

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

## Procedure

-  Run the import playbook from your working directory, passing required variables as extra vars:
  

```
ansible-playbook -i inventory \
  ansible.aap_snapshot.artifact_import \
  -e aap_platform=operator \
  -e artifact_file=/path/to/aap-snapshot-<version>-<timestamp>.tar \
  -e kubeconfig=/path/to/kubeconfig \
  -e gateway_admin_password=<password> \
  -e gateway_hostname=<hostname>
```

    If your deployment uses a namespace or CR name other than the default `aap`, add:

```
-e ocp_namespace=<namespace> \
-e aap_instance_name=<instance_name>
```

    If your cluster's RWX StorageClass is not auto-detected, specify it:

```
-e hub_file_storage_class=<storage_class_name>
```

  Warning:
  The playbook takes 15 to 45 minutes to complete, depending on artifact size and OCP cluster speed. Do not interrupt the playbook after the Idle AAP phase begins. Interrupting after the deployment is scaled down might leave components unavailable.

-  Monitor terminal output as the playbook progresses through each phase:
    | Phase                                         | What you see                                                                                                        | Notes                                                                                                                                                                                              |
    | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Preflight                                     | Platform and inventory assertions, CR health check, gateway status API check, component service and database checks | Fails early if any check does not pass.                                                                                                                                                            |
    | Validate and extract artifact                 | Checksum verification, extraction progress                                                                          | Fails if artifact is corrupt or version does not match.                                                                                                                                            |
    | Import preflight (OCP)                        | ReadWriteMany StorageClass validation                                                                               | Verifies`hub_file_storage_class` is set and the named class exists. Runs only when artifact includes hub and no CR exists yet.                                                                     |
    | Create Ansible Automation Platform deployment | CR creation, PostgreSQL StatefulSet readiness wait, database secret provisioning                                    | Skipped if a CR already exists.                                                                                                                                                                    |
    | Idle AAP                                      | Operator scale-down, idle status confirmation                                                                       | Do not interrupt after this point.                                                                                                                                                                 |
    | Create temp resources and transfer artifact   | Temporary PVC and pod creation, artifact transfer                                                                   | Pulls`registry.redhat.io/rhel9/postgresql-15:latest`. The OCP cluster must have a pull secret configured for`registry.redhat.io`. Override with`temp_postgres_image` in disconnected environments. |
    | Import databases                              | Per-component database restore                                                                                      | Runs only for components in the artifact.                                                                                                                                                          |
    | Cleanup and resume                            | Temporary resource deletion, operator scale-up, readiness wait                                                      | Deployment returns to running state.                                                                                                                                                               |
    | Reconcile                                     | Gateway, controller, hub, and EDA reconciliation                                                                    | Includes the Pulp repair API call.                                                                                                                                                                 |
    | Post-import report                            | Migration summary and post-import advisory                                                                          | Review both before proceeding.                                                                                                                                                                     |
  Note:
  The OCP cluster's global pull secret provides `registry.redhat.io` access. No additional registry configuration is required. In disconnected environments, override the image using the `temp_postgres_image` variable. See [aap_snapshot collection variable reference: import](/documentation/en-us/red_hat_ansible_automation_platform/2.7/aap_snapshot_collection_variable_reference__import "Use these variables to configure the ansible.aap_snapshot.artifact_import playbook for an OpenShift Container Platform operator-managed deployment. Variables marked as OCP-specific apply only when aap_platform is set to operator.").

-  When the playbook reaches the Post-import validation and report phase, review both messages before taking further action.
      The migration summary confirms what was restored:

```
=== Migration Complete ===
Source platform: rpm
Target platform: operator
AAP version: 2.6.0
Components migrated:
  - controller (v2.6.0, database: awx)
  - hub (v2.6.0, database: pulp)
  - gateway (v2.6.0, database: gateway)
  - eda (v2.6.0, database: eda)
```

    The post-import advisory lists required manual steps:

```
=== Next Steps ===
- Verify admin credentials and login to the gateway UI
- Check instance group assignments - restored resources may need reassignment
- EDA: update automation controller URL in credentials if hostnames changed
- Execution nodes: register equivalent nodes in target controller UI
- Hub content was not migrated - run content sync manually
- Review custom TLS certificates and reapply if needed
```

    The hub content sync item appears only when hub content was excluded from the artifact.

  Note:
      If a CR already exists in the target namespace, the playbook skips CR creation and the RWX StorageClass check, and proceeds directly to idling the deployment. The CR must be healthy with no Failure conditions before the preflight phase will proceed.

    If the playbook fails after the Idle AAP phase begins, the deployment remains scaled down and temporary migration resources may still exist in the namespace. Before re-running, manually resume the deployment by setting `spec.idle: false` on the `AnsibleAutomationPlatform` CR and remove any temporary PVC and pod created by the collection. For a clean retry, starting with a fresh namespace is the safest approach.

## What to do next

After the playbook completes successfully, see [Validate the restored deployment and complete post-import tasks](/documentation/en-us/red_hat_ansible_automation_platform/2.7/validate_the_restored_deployment_and_complete_post_import_tasks "Verify that the restored deployment is healthy and complete any post-import tasks before using it in production. Some steps are conditional on which components were in the artifact and whether hostnames changed.") to verify the restored deployment and complete post-import tasks.
