# What survives an upgrade

The following table describes what happens to each type of content during a bootc upgrade of the Ansible automation portal RHEL appliance.

| Content                    | Location                                    | Survives upgrade | Notes                                        |
| -------------------------- | ------------------------------------------- | ---------------- | -------------------------------------------- |
| Portal configuration       | /etc/portal/configs/                        | Yes              | Three-way merge preserves your modifications |
| SSL certificates           | /etc/portal/ssl/                            | Yes              | Three-way merge                              |
| Quadlet drop-ins           | /etc/containers/systemd/portal.container.d/ | Yes              | Three-way merge                              |
| Quadlet port customization | /etc/containers/systemd/                    | Yes              | Three-way merge                              |
| PostgreSQL data            | /var/lib/portal/postgres-data/              | Yes              | Never touched by bootc                       |
| Backups                    | /var/lib/portal/backups/                    | Yes              | Never touched by bootc                       |
| Podman secrets             | /var/lib/containers/                        | Yes              | Never touched by bootc                       |
| Ansible plugins            | /usr/share/portal/plugins/                  | Updated          | New plugins from the new image               |
| Portal scripts             | /usr/share/portal/scripts/                  | Updated          | New scripts from the new image               |
| Dynamic plugin configs     | /var/lib/portal/dynamic-plugins-root/       | Cleared          | Regenerated from new plugins on first start  |

## Post-upgrade reconciliation

After reboot, the appliance automatically reconciles Ansible plugins and configuration with the new image version:

1. Clears the dynamic plugins directory so that plugins are regenerated from the new image.
2. Clears generated configuration files (regenerated on portal start).
3. Creates any new directories required by the new image version.
4. Fixes file ownership for portal and PostgreSQL directories.
