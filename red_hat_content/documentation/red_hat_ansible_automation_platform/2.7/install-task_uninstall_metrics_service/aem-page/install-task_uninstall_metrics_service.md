+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-task_uninstall_metrics_service"
title = "Uninstall metrics service - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_understand_metrics_service_architecture/", "Understand metrics service architecture"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-task_uninstall_metrics_service/aem-page/install-task_uninstall_metrics_service.html"
last_crumb = "Uninstall metrics service"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Uninstall metrics service"
oversized = "false"
page_slug = "install-task_uninstall_metrics_service"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-task_uninstall_metrics_service"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-task_uninstall_metrics_service/toc/toc.json"
type = "aem-page"
+++

# Uninstall metrics service

Completely uninstall all metrics service components and optionally preserve or delete data to cleanly remove the service without orphaned resources or configuration conflicts.

## About this task

Warning:

Uninstallation is destructive and irreversible. Back up the `metrics_service` database before proceeding if you need to preserve historical metrics data.

## Procedure

1.  Method 1: Use installer playbook (recommended)
  

```
cd /path/to/aap-containerized-installer
ansible-playbook -i inventory uninstall.yml
```
    The uninstall.yml playbook automatically removes all metrics service components:

  - Stops and disables systemd services
  - Removes containers
  - Deletes systemd unit files
  - Removes Podman secrets
  - Deletes volume directories
  - Removes firewall rules
  Note:
      **Optional:** To also drop the database, add database cleanup tasks to your inventory configuration.

2.  Method 2: Manual uninstall
      Use this method if you need granular control over uninstall steps.

    **Step 1: Stop and disable systemd services**

```
systemctl --user stop automation-metrics-web.service automation-metrics-tasks.service automation-metrics-scheduler.service
systemctl --user disable automation-metrics-web.service automation-metrics-tasks.service automation-metrics-scheduler.service
```
    **Step 2: Remove containers**

```
podman rm -f automation-metrics-web
podman rm -f automation-metrics-tasks
podman rm -f automation-metrics-scheduler
podman rm -f automation-metrics-init
```
    **Step 3: Delete systemd unit files**

```
rm -f ~/.config/systemd/user/automation-metrics-web.service
rm -f ~/.config/systemd/user/automation-metrics-tasks.service
rm -f ~/.config/systemd/user/automation-metrics-scheduler.service
systemctl --user daemon-reload
```
    **Step 4: Delete Podman secrets**

```
podman secret rm automationmetrics_pg_password
podman secret rm automationmetrics_controller_read_pg_password
podman secret rm automationmetrics_secret_key
podman secret rm automationmetrics_resource_server
```
    **Step 5: Remove volumes and data directories**

```
rm -rf {{ aap_volumes_dir }}/automationmetrics
```
    **Step 6: Drop database (optional)**

```
psql -h localhost -U postgres

    DROP DATABASE IF EXISTS metrics_service;
DROP USER IF EXISTS metrics_service;
DROP USER IF EXISTS ms_awx_readonly;
```
    **Step 7: Remove firewall rules**

```
sudo firewall-cmd --remove-port=8087/tcp --permanent
sudo firewall-cmd --remove-port=8450/tcp --permanent
sudo firewall-cmd --reload
```

## Results

**Reinstallation with same database**

Metrics service **can** be reinstalled using the same database:

- Django migrations are idempotent (safe to re-run)
- No code-level block on reinstall
- `init-system-tasks` recreates Task rows


**Limitations:**

- Not officially tested or supported
- Unexpected behavior possible


**Recommendation:** Use a fresh database for reinstallation unless you have specific requirements to preserve existing data.
