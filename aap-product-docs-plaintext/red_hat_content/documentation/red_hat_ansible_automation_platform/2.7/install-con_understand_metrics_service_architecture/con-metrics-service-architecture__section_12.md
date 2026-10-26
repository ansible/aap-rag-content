# Understand metrics service architecture
## Containerized installer deployment details

Metrics service is deployed through the `automationmetrics` Ansible role included in the Ansible Automation Platform 2.7 containerized installation program:

- **Container runtime:** Podman with host networking mode (rootless, user namespace)
- **Service management:** Three systemd user-scope units: `automation-metrics-web.service`, `automation-metrics-tasks.service`, `automation-metrics-scheduler.service`
- **Data persistence:** Host volumes mounted from `{{ aap_volumes_dir }}/automationmetrics` into container path /var/lib/ansible-automation-platform/metrics
- **Secrets management:** Four Podman secrets: `automationmetrics_pg_password`, `automationmetrics_controller_read_pg_password`, `automationmetrics_secret_key`, `automationmetrics_resource_server`
- **Firewall integration:** Ports 8087/tcp (HTTP) and 8450/tcp (HTTPS) opened in configured firewall zone (default: public)

**Configuration requirements:**

- Hosts must be added to `[automationmetrics]` inventory group (unless `automationmetrics_skip_install=true` is set)
- Database connection variables must be configured (`automationmetrics_pg_host`, `automationmetrics_pg_password`, etc.)
- Read-only controller database user must be provisioned manually or by installer
- Segment write key must be provided for data transmission

