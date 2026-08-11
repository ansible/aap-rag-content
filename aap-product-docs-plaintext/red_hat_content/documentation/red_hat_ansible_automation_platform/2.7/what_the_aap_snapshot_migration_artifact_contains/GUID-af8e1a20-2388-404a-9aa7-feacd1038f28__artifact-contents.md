# What the aap_snapshot migration artifact contains
## Artifact contents

The artifact has a flat directory structure at its root, with per-component subdirectories for database dumps. Only components defined in your inventory are included.

| File or directory                       | Description                                                                                                                         |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `manifest.yml`                          | Schema version, Ansible Automation Platform version, source topology, list of exported components, and per-component checksums.     |
| `secrets.yml`                           | All`SECRET_KEY` values, database credentials, and encryption keys extracted from each component. File permissions are set to`0600`. |
| `sha256sum.txt`                         | SHA-256 checksums for each component database dump file.                                                                            |
| `controller/controller.pgc`             | PostgreSQL custom-format database dump for automation controller.                                                                   |
| `controller/custom_configs/<hostname>/` | Custom configuration files per controller node. Present only for RPM-based source deployments.                                      |
| `gateway/gateway.pgc`                   | PostgreSQL custom-format database dump for platform gateway.                                                                        |
| `hub/hub.pgc`                           | PostgreSQL custom-format database dump for automation hub.                                                                          |
| `hub/hub_content.tar`                   | Pulp data directory content. Included only when`export_hub_content` is`true` (the default).                                         |
| `eda/eda.pgc`                           | PostgreSQL custom-format database dump for Event-Driven Ansible.                                                                    |

