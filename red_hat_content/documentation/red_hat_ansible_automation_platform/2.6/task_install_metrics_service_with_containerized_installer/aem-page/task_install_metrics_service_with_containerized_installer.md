+++
template = "docs/aem-title.html"
title = "Install metrics service with containerized installer - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/task_install_metrics_service_with_containerized_installer"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/task_install_metrics_service_with_containerized_installer/aem-page/task_install_metrics_service_with_containerized_installer.html"
last_crumb = "Install metrics service with containerized installer"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Install metrics service with containerized installer"
oversized = "false"
page_slug = "task_install_metrics_service_with_containerized_installer"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/task_install_metrics_service_with_containerized_installer"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/task_install_metrics_service_with_containerized_installer/toc/toc.json"
type = "aem-page"
+++

# Install metrics service with containerized installer

Enable and configure metrics service during containerized installation to automatically collect anonymized usage data and transmit it to Red Hat.

## Before you begin

- Red Hat Enterprise Linux 9.2 or later installed and configured
- Active Red Hat Ansible Automation Platform subscription
- Ansible Automation Platform 2.7 containerized installer downloaded and extracted
- Infrastructure meets requirements
- Root or sudo access to installation host


Important:

Metrics service is enabled by default in Ansible Automation Platform 2.7. You do not need to explicitly enable it unless you previously disabled it.

## About this task

This procedure configures metrics service during the initial containerized installation of Ansible Automation Platform 2.7. Metrics service is enabled by default and automatically collects anonymized usage data, stores it in its own PostgreSQL database with read-only access to the controller database, and transmits data to Red Hat without post-installation configuration.

## Procedure

1.  Define metrics service inventory group
      Edit the inventory file and add the `[automationmetrics]` group:

```
[automationcontroller]
aap.example.com

    [automationmetrics]
aap.example.com

    [database]
aap.example.com

    [all:vars]
postgresql_admin_username=postgres
postgresql_admin_password='<secure_password>'

    # Optional: Enable automation dashboard data collection (Tech Preview)
# Default: disabled
FEATURE_DASHBOARD_COLLECTION_ENABLED: false
```
  Note:
      Metrics service is NOT required to be co-located with automation controller. Place it on any node based on your deployment topology.

2.  Run the containerized installer
  

```
cd /path/to/aap-containerized-installer
ansible-playbook -i inventory install.yml
```
    The installer performs the following sequence:

  1. **Database setup:** Creates `metrics_service` database, `metrics_service` user (ALL privileges), and `ms_awx_readonly` user (SELECT-only on controller database)
  2. **Podman secrets:** Creates four secrets:
    - `automationmetrics_pg_password`
    - `automationmetrics_controller_read_pg_password`
    - `automationmetrics_secret_key`
    - `automationmetrics_resource_server`
  3. **Database migrations:** Runs `automation-metrics-init` container (one-shot; runs `migrate`, `init-default-settings`, `init-service-id`, `init-system-tasks`)
  4. **Service deployment:** Creates three containers: `automation-metrics-web`, `automation-metrics-tasks`, `automation-metrics-scheduler`
  5. **Systemd integration:** Generates three user-scope systemd units: `automation-metrics-web.service`, `automation-metrics-tasks.service`, `automation-metrics-scheduler.service`
  6. **Firewall configuration:** Opens ports 8087/tcp (HTTP) and 8450/tcp (HTTPS)

3. **Optional:** Enable automation dashboard
      Automation dashboard provides ROI calculations, cost savings analysis, and executive reporting. It uses metrics service as its backend for data collection and storage.

    To enable automation dashboard data collection during installation, set:

```
FEATURE_DASHBOARD_COLLECTION_ENABLED: true
```
  Note:
      **Dependency:** Dashboard collection requires metrics service to be enabled. The installer fails preflight checks if you enable automation dashboard without metrics service.

4.  Verify installation
  

```
# Container status
podman ps | grep automation-metrics

    # Systemd service status (user scope)
systemctl --user status automation-metrics-web.service
systemctl --user status automation-metrics-tasks.service
systemctl --user status automation-metrics-scheduler.service

    # Init container logs (confirms successful initialization)
podman logs automation-metrics-init
# Expected output:
# Running database migrations...
# Initializing default settings...
# Initializing django-ansible-base ServiceID...
# Initializing system tasks...

    # Health endpoint (via nginx)
curl http://localhost:8087/health/

    # Database connectivity
podman exec automation-metrics-web \
  psql -h localhost -U metrics_service -d metrics_service -c "SELECT version();"
```

## Results

Metrics service is successfully installed when:

- All three containers (`automation-metrics-web`, `automation-metrics-tasks`, `automation-metrics-scheduler`) are running
- All three systemd user-scope services are active and enabled
- Health endpoint returns `{"status": "good", ...}` response
- Database connectivity confirmed


**What happens next:**

After installation, metrics service automatically:

- Begins collecting usage data from automation controller database
- Anonymizes data. Any private object names are marked as Custom.
- Transmits anonymized data to Red Hat Data Ingress via Gateway /api/metrics/ endpoint
- Provides health monitoring at http://localhost:8087/health/ (via nginx)
