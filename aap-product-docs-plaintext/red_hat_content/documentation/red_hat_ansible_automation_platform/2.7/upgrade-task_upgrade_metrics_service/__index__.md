# Upgrade metrics service

Safely upgrade metrics service when upgrading Ansible Automation Platform to benefit from new features and bug fixes while maintaining continuous data collection.

## Before you begin

- Current metrics service installation is operational
- Backup of `metrics_service` database completed
- New version of Ansible Automation Platform containerized installer downloaded

## Procedure

1.  Back up current configuration


```
cp /path/to/installer/inventory /path/to/backup/inventory.backup.$(date +%Y%m%d)
pg_dump -h localhost -U metrics_service metrics_service > metrics_service_backup_$(date +%Y%m%d).sql
```

2.  Stop metrics service


```
systemctl --user stop automation-metrics-web.service automation-metrics-tasks.service automation-metrics-scheduler.service
```

3.  Run upgrade installer


```
cd /path/to/new-installer
ansible-playbook -i inventory install.yml
```
Note:
There is no separate upgrade.yml playbook. The install.yml playbook handles upgrades. The role's tasks/update.yml automatically detects image changes, stops services, and recreates containers with the new image.

4.  Verify database schema migration
Database migrations are handled automatically during upgrade via the `automation-metrics-init` container, which executes Django migrations through /app/scripts/init.sh. The process retries up to 5 times if failures occur.

```
# Check init container logs for migration status
podman logs automation-metrics-init

# Verify database schema
psql -h localhost -U metrics_service -d metrics_service -c "\dt"
```
Note:
The update.yml task in the automationmetrics role automatically handles container image updates and sets a recreate flag when newer images are detected.

5.  Start metrics service


```
systemctl --user start automation-metrics-web.service automation-metrics-tasks.service automation-metrics-scheduler.service
```

## Rollback procedure

**Rollback is not supported.** Metrics service does not provide rollback functionality.

**Recovery procedure if upgrade fails:**

1. Uninstall metrics service.
2. Reinstall previous version using previous installer


**Important limitations:**

- Backup & restore is **not guaranteed to work** if the version goes down (version downgrade)
- Django migrations may not be reversible
- Database schema changes may be incompatible with older versions


**Recommendation:** Test upgrades in non-production environments first to validate upgrade path and verify data integrity before upgrading production systems.
