+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-import_migration_content_to_ocp_using_the_aap_snapshot_collection"
template = "docs/aem-title.html"
title = "Import a deployment into OCP using the aap_snapshot collection - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-assembly_target_environment/", "Prepare, configure, and validate the target environment"]]
category = "Migrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-import_migration_content_to_ocp_using_the_aap_snapshot_collection/aem-page/migrate-import_migration_content_to_ocp_using_the_aap_snapshot_collection.html"
last_crumb = "Import a deployment into OCP using the aap_snapshot collection"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Import a deployment into OCP using the aap_snapshot collection"
oversized = "false"
page_slug = "migrate-import_migration_content_to_ocp_using_the_aap_snapshot_collection"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/migrate-import_migration_content_to_ocp_using_the_aap_snapshot_collection"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-import_migration_content_to_ocp_using_the_aap_snapshot_collection/toc/toc.json"
type = "aem-page"
+++

# Import a deployment into OCP using the aap_snapshot collection

Use the `ansible.aap_snapshot` collection to import your Ansible Automation Platform configuration, credentials, and content from an RPM-based deployment into an OpenShift Container Platform operator-managed deployment.

## Set up the import inventory for OCP

Create a minimal inventory file for the `artifact_import` playbook on your control node. The import runs entirely from `localhost` using the `kubernetes.core` collection, so no SSH access to OCP nodes is required.

### Before you begin

- The `ansible.aap_snapshot` collection is installed.
- A valid kubeconfig for the OCP target namespace is available.
- The migration artifact `.tar` file is present on the control node.

### Procedure

Create a file named `inventory` in your working directory with the following content:

```
[localhost]
localhost ansible_connection=local
```

Verify the inventory is valid by running the following command:

```
ansible-inventory -i inventory --list
```

The output lists `localhost`.

### What to do next

For all available variables, see [Import variables reference](/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-aap_snapshot_collection_variable_reference__import "Use these variables to configure the ansible.aap_snapshot.artifact_import playbook. The Platform column indicates which deployment types each variable applies to.").

## Import Ansible Automation Platform data into an OCP deployment

Run the `artifact_import` playbook from the `ansible.aap_snapshot` collection to restore your Ansible Automation Platform configuration, credentials, and content onto an OpenShift Container Platform operator-managed deployment.

### Before you begin

- The `ansible.aap_snapshot` collection is installed on the control node.
- The migration artifact `.tar` file is present and readable on the control node.
- A valid kubeconfig for the OCP target namespace is available.
- The `gateway_admin_password` and `gateway_hostname` for the source deployment are available.
- A ReadWriteMany (RWX) StorageClass is available in the OCP target namespace if the artifact includes automation hub.
- The Ansible Automation Platform version in the artifact matches the Ansible Automation Platform version in the OCP target namespace.

### About this task

The playbook runs automated preflight checks, restores component databases, and produces a post-import advisory listing any required manual steps.

### Procedure

- Run the import playbook from your working directory, passing required variables as extra vars:
  

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

- Monitor terminal output as the playbook progresses through each phase:
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
  The OCP cluster's global pull secret provides `registry.redhat.io` access. No additional registry configuration is required. In disconnected environments, override the image using the `temp_postgres_image` variable. See [Import variables reference](/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-aap_snapshot_collection_variable_reference__import "Use these variables to configure the ansible.aap_snapshot.artifact_import playbook. The Platform column indicates which deployment types each variable applies to.").

- When the playbook reaches the Post-import validation and report phase, review both messages before taking further action.
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

### What to do next

After the playbook completes successfully, see [Validate the restored deployment and complete post-import tasks](/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-import_migration_content_to_ocp_using_the_aap_snapshot_collection#GUID-740c4114-4953-42c1-ba6f-432fc1303063 "Verify that the restored deployment is healthy and complete any post-import tasks before using it in production. Some steps are conditional on which components were in the artifact and whether hostnames changed.") to verify the restored deployment and complete post-import tasks.

## Validate the restored deployment and complete post-import tasks

Verify that the restored deployment is healthy and complete any post-import tasks before using it in production. Some steps are conditional on which components were in the artifact and whether hostnames changed.

### Before you begin

- The `ansible.aap_snapshot.artifact_import` playbook completed without errors.
- The gateway admin password for the restored deployment is available.
- `oc` CLI access to the OCP namespace is available.

### Procedure

1. Log in to the Ansible Automation Platform UI using the `admin` username and the platform gateway admin password.
      Retrieve the Ansible Automation Platform UI URL with the following command:

```
oc get route -n aap -l app.kubernetes.io/component=aap-gateway
```

    If your deployment uses a non-default instance name, replace `aap-gateway` with `<aap_instance_name>-gateway`.

    If login fails, verify that `gateway_admin_password` in your inventory matched the source deployment's password.

2. In the navigation panel, select Automation Execution > Infrastructure > Instance Groups and verify that the expected instance groups are present.
3. If any instance group names differ from the source deployment, reassign resources to the correct instance groups.
4. If Event-Driven Ansible was included and the gateway hostname changed, from the navigation panel select Automation Decisions > Infrastructure > Credentials and update any Automation Controller credentials to the new controller URL.
5. Register execution nodes through the Ansible Automation Platform UI or API.
      From the navigation panel, select Automation Execution > Infrastructure > Instances. The reconcile phase deprovisions instances with no recent heartbeat but does not register new ones.

6. If the post-import advisory includes the message `Hub content was not migrated - run content sync manually`, trigger a content sync.
      From the navigation panel, select Automation Content > Repositories, then sync each repository from its configured remote registry.

7. If the source deployment used custom TLS certificates, reapply them to the OCP namespace.
      The collection does not seed TLS certificate material from the artifact. Only encryption keys (`SECRET_KEY` values) are seeded. For the Ansible Automation Platform Operator CR fields that control TLS injection, see the documentation for renewing and changing SSL/TLS certificates and keys.

8. Verify that all components are healthy:
  

```
oc get ansibleautomationplatform -n aap
oc get automationcontroller,automationhub,automationgateway,automationedacontroller -n aap
```
