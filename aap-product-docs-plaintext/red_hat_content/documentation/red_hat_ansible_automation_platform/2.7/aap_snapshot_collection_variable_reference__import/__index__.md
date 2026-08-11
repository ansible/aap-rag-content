# aap_snapshot collection variable reference: import

Use these variables to configure the `ansible.aap_snapshot.artifact_import` playbook for an OpenShift Container Platform operator-managed deployment. Variables marked as OCP-specific apply only when `aap_platform` is set to `operator`.

Important:

The Ansible Automation Platform version recorded in the artifact must match the Ansible Automation Platform version running in the OCP target namespace exactly. The preflight phase enforces this and fails if the versions differ.

## Common import variables

| Variable         | Required | Default | OCP-specific | Description                                                                                                                                                                                              |
| ---------------- | -------- | ------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aap_platform`   | Yes      | None    | No           | Target deployment type. Set to `operator` for OCP operator-managed deployments. Accepted values: `rpm`, `containerized`, `operator`.                                                                     |
| `artifact_file`  | No       | None    | No           | Absolute path to the `.tar` artifact on the control node. The playbook fails at startup if neither `artifact_file` nor the `artifact_dir` + `artifact` pair is set. Use this or the `artifact_dir` + `artifact` pair. |
| `artifact_dir`   | No       | `$PWD`  | No           | Directory containing the artifact. Use with `artifact` to construct the full path.                                                                                                                       |
| `artifact`       | No       | None    | No           | Artifact filename. Combine with `artifact_dir` to construct the full artifact path. Set to the full timestamped filename, for example `aap-snapshot-2.6-20260601-143022.tar`. Prefer `artifact_file` for a simpler single-variable approach. |
| `disable_no_log` | No       | `false` | No           | Set to `true` to show sensitive values in output. Use for debugging only.                                                                                                                                |

## OCP connection variables

| Variable            | Required | Default         | OCP-specific | Description                                                                                                             |
| ------------------- | -------- | --------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `kubeconfig`        | No       | See description | Yes          | Path to a kubeconfig file. Resolution order: `-e kubeconfig` > `K8S_AUTH_KUBECONFIG` > `KUBECONFIG` > `~/.kube/config`. |
| `ocp_namespace`     | No       | `aap`           | Yes          | OCP namespace containing the Ansible Automation Platform deployment.                                                    |
| `aap_instance_name` | No       | `aap`           | Yes          | Name of the `AnsibleAutomationPlatform` custom resource (CR).                                                           |

## Hub storage variable

| Variable                 | Required                      | Default | OCP-specific | Description                                                                                                                                                                                       |
| ------------------------ | ----------------------------- | ------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hub_file_storage_class` | Yes (when hub is in artifact) | None    | Yes          | Name of the RWX StorageClass for automation hub file storage. Must be set explicitly. Auto-detection is not supported. Preflight fails if this variable is not set and the artifact includes hub. |

## Hub reconciliation variables

| Variable                 | Required | Default | OCP-specific | Description                                                                                      |
| ------------------------ | -------- | ------- | ------------ | ------------------------------------------------------------------------------------------------ |
| `gateway_admin_password` | Yes      | None    | No           | Gateway admin password. Required for the Pulp repair API call during hub reconciliation.         |
| `gateway_hostname`       | Yes      | None    | No           | Fully qualified hostname of the gateway service. Used to construct the Pulp repair API endpoint. |
| `gateway_admin_user`     | No       | `admin` | No           | Admin username for the Pulp repair API call.                                                     |
| `validate_certs`         | No       | `false` | No           | Whether to validate TLS certificates for API calls during reconciliation.                        |

## Content and database variables

| Variable                        | Required | Default    | OCP-specific | Description                                                                                                                                   |
| ------------------------------- | -------- | ---------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `export_hub_content`            | No       | `true`     | No           | Controls whether Pulp content was included at export time. This value is read from the artifact manifest at import. Do not set during import. |
| `postgresql_db_type`            | No       | `managed`  | No           | Database topology. `managed` for co-located PostgreSQL, `external` for an external database.                                                  |
| `postgresql_restore_admin_user` | No       | `postgres` | No           | PostgreSQL superuser for database restore operations.                                                                                         |
| `postgresql_restore_timeout`    | No       | `3600`     | No           | Async timeout in seconds for `pg_restore`. Increase this value for large databases.                                                           |

## Temporary migration resource variables (OCP)

These variables control the temporary PVC and PostgreSQL pod created during the database transfer phase. Both resources are removed automatically after import.

| Variable              | Required | Default                                         | OCP-specific | Description                                                                                              |
| --------------------- | -------- | ----------------------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------- |
| `temp_pvc_size`       | No       | `200Gi`                                         | Yes          | Size of the temporary PVC for staging the artifact. Increase this value if the artifact exceeds 200 GiB. |
| `temp_postgres_image` | No       | `registry.redhat.io/rhel9/postgresql-15:latest` | Yes          | Container image for the temporary PostgreSQL pod. Override this value in disconnected environments.      |
