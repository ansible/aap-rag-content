+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-aap_snapshot_collection_variable_reference__import"
template = "docs/aem-title.html"
title = "Import variables reference - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-assembly_target_environment/", "Prepare, configure, and validate the target environment"]]
category = "Migrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-aap_snapshot_collection_variable_reference__import/aem-page/migrate-aap_snapshot_collection_variable_reference__import.html"
last_crumb = "Import variables reference"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Import variables reference"
oversized = "false"
page_slug = "migrate-aap_snapshot_collection_variable_reference__import"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/migrate-aap_snapshot_collection_variable_reference__import"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-aap_snapshot_collection_variable_reference__import/toc/toc.json"
type = "aem-page"
+++

# Import variables reference

Use these variables to configure the `ansible.aap_snapshot.artifact_import` playbook. The Platform column indicates which deployment types each variable applies to.

Important:

The Ansible Automation Platform version recorded in the artifact must match the version running on the target deployment exactly. The preflight phase enforces this and fails if the versions differ.

## Common import variables

| Variable         | Required | Default | Platform | Description                                                                                                                                             |
| ---------------- | -------- | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aap_platform`   | Yes      | None    | All      | Target deployment type. Accepted values:`rpm`,`containerized`,`operator`.                                                                               |
| `artifact_file`  | Yes      | None    | All      | Path to the`.tar` artifact file on the control node. Accepts an absolute or relative path. The playbook fails at preflight if this variable is not set. |
| `disable_no_log` | No       | `false` | All      | Set to`true` to show sensitive values in output. Use for debugging only.                                                                                |

## OCP connection variables

| Variable            | Required | Default         | Platform | Description                                                                                                         |
| ------------------- | -------- | --------------- | -------- | ------------------------------------------------------------------------------------------------------------------- |
| `kubeconfig`        | No       | See description | OCP only | Path to a kubeconfig file. Resolution order:`-e kubeconfig` >`K8S_AUTH_KUBECONFIG` >`KUBECONFIG` >`~/.kube/config`. |
| `ocp_namespace`     | No       | `aap`           | OCP only | OCP namespace containing the Ansible Automation Platform deployment.                                                |
| `aap_instance_name` | No       | `aap`           | OCP only | Name of the`AnsibleAutomationPlatform` custom resource (CR).                                                        |

## Hub storage variable

| Variable                 | Required                      | Default | Platform | Description                                                                                                                                                                                       |
| ------------------------ | ----------------------------- | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hub_file_storage_class` | Yes (when hub is in artifact) | None    | OCP only | Name of the RWX StorageClass for automation hub file storage. Must be set explicitly. Auto-detection is not supported. Preflight fails if this variable is not set and the artifact includes hub. |

## Hub reconciliation variables

| Variable                            | Required | Default | Platform | Description                                                                                                                                                                                              |
| ----------------------------------- | -------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `gateway_admin_password`            | No       | None    | OCP only | Gateway admin password for the Pulp repair API call during hub reconciliation. For OCP imports, the collection discovers this value automatically from OCP secrets.                                      |
| `gateway_hostname`                  | No       | None    | OCP only | Fully qualified hostname of the gateway service. Used to construct the Pulp repair API endpoint. For OCP imports, the collection discovers this value automatically from the gateway route.              |
| `gateway_admin_user`                | No       | `admin` | OCP only | Admin username for the Pulp repair API call.                                                                                                                                                             |
| `automationhub_pulp_repair_retries` | No       | `120`   | OCP only | Number of polling attempts when waiting for Pulp content repair to complete. Combined with`automationhub_pulp_repair_delay`, the default allows up to 60 minutes. Increase for large hub deployments with many collections. |
| `automationhub_pulp_repair_delay`   | No       | `30`    | OCP only | Seconds between Pulp repair polling attempts.                                                                                                                                                            |
| `validate_certs`                    | No       | `false` | OCP only | Whether to validate TLS certificates for API calls during reconciliation.                                                                                                                                |

## Content and database variables

| Variable                           | Required | Default    | Platform | Description                                                                                                                                   |
| ---------------------------------- | -------- | ---------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `automationhub_export_hub_content` | No       | `true`     | All      | Controls whether Pulp content was included at export time. This value is read from the artifact manifest at import. Do not set during import. |
| `postgresql_restore_admin_user`    | No       | `postgres` | All      | PostgreSQL superuser for database restore operations.                                                                                         |
| `postgresql_restore_timeout`       | No       | `3600`     | All      | Async timeout in seconds for`pg_restore`. Increase this value for large databases.                                                            |

## Temporary migration resource variables (OCP)

These variables control the temporary PVC and PostgreSQL pod created during the database transfer phase. Both resources are removed automatically after import.

| Variable                        | Required | Default                                         | Platform | Description                                                                                             |
| ------------------------------- | -------- | ----------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------- |
| `temp_pvc_size`                 | No       | `60Gi`                                          | OCP only | Size of the temporary PVC for staging the artifact. Increase this value if the artifact exceeds 60 GiB. |
| `ocp_utils_temp_postgres_image` | No       | `registry.redhat.io/rhel9/postgresql-15:latest` | OCP only | Container image for the temporary PostgreSQL pod. Override this value in disconnected environments.     |
