# Export playbook variables reference

Use these variables to configure the `artifact_export` playbook. Set them in your inventory file under `[all:vars]` or pass them with `-e` when running the playbook.

| Variable             | Required | Default                   | Description                                                                                                                                                                                              |
| -------------------- | -------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aap_platform`       | Yes      | None                      | Platform type. Set to`rpm` for RPM-based deployments. Accepted values:`rpm`,`containerized`,`operator`.                                                                                                  |
| `artifact_dir`       | No       | Current working directory | Directory on the control node where the artifact is written. Created if it does not exist.                                                                                                               |
| `export_hub_content` | No       | `true`                    | Set to`false` to skip Pulp content export. The automation hub database is still exported when this is set to`false`. After import, automation content must be re-synced from your configured remote registries. |
| `postgresql_db_type` | No       | `managed`                 | Set to`external` if your deployment uses a PostgreSQL instance not managed by the installer.                                                                                                             |
