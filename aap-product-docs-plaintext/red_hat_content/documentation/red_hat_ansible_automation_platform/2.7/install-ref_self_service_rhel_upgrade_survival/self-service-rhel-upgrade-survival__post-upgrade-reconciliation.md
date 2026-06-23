# What survives an upgrade
## Post-upgrade reconciliation

After reboot, the appliance automatically reconciles Ansible plugins and configuration with the new image version:

1. Clears the dynamic plugins directory so that plugins are regenerated from the new image.
2. Clears generated configuration files (regenerated on portal start).
3. Creates any new directories required by the new image version.
4. Fixes file ownership for portal and PostgreSQL directories.
