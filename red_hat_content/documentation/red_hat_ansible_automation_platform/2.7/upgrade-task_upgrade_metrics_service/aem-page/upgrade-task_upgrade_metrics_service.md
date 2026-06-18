+++
title = "Upgrade metrics service - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-task_upgrade_metrics_service"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-upgrade_additional_services_for_ansible_automation_platform/", "Upgrade additional services for Ansible Automation Platform"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-task_upgrade_metrics_service/aem-page/upgrade-task_upgrade_metrics_service.html"
last_crumb = "Upgrade metrics service"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Upgrade metrics service"
oversized = "false"
page_slug = "upgrade-task_upgrade_metrics_service"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-task_upgrade_metrics_service"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-task_upgrade_metrics_service/toc/toc.json"
type = "aem-page"
+++

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
