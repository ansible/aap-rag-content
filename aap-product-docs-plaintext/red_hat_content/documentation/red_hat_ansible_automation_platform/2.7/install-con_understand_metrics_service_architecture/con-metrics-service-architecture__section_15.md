# Understand metrics service architecture
## Naming conventions

| Element                  | Value                                        |
| ------------------------ | -------------------------------------------- |
| Role name                | `automationmetrics`                          |
| Inventory group          | `[automationmetrics]`                        |
| Web container            | `automation-metrics-web`                     |
| Tasks container          | `automation-metrics-tasks`                   |
| Scheduler container      | `automation-metrics-scheduler`               |
| Init container           | `automation-metrics-init`                    |
| Variable prefix          | `automationmetrics_`                         |
| Gunicorn port (internal) | `8006` (localhost only)                      |
| Nginx HTTP port          | `8087`                                       |
| Nginx HTTPS port         | `8450`                                       |
| Health endpoint          | http://localhost:8087/health/                |
| Host volume path         | `{{ aap_volumes_dir }}/automationmetrics`    |
| Container data path      | /var/lib/ansible-automation-platform/metrics |
