# Understand metrics service architecture
## Network architecture

**Required network connectivity**

| Source                                                                | Destination                        | Protocol/Port     | Purpose                                                          |
| --------------------------------------------------------------------- | ---------------------------------- | ----------------- | ---------------------------------------------------------------- |
| `automation-metrics-tasks` /`automation-metrics-scheduler` containers | Automation controller database     | PostgreSQL (5432) | Read-only data collection via`ms_awx_readonly` user              |
| `automation-metrics-tasks` /`automation-metrics-scheduler` containers | `metrics_service` database         | PostgreSQL (5432) | Read-write metrics storage via`metrics_service` user             |
| `automation-metrics-tasks` container                                  | Red Hat Data Ingress (via Segment) | HTTPS (443)       | Anonymized data transmission authenticated via Segment write key |
| Monitoring systems (optional)                                         | `automation-metrics-web` container | HTTP (8087)       | Health check endpoint at/health/ via nginx                       |

**Firewall requirements**

- **Protocol:** HTTPS (TLS 1.2 or higher); supported TLS versions: TLSv1.2, TLSv1.3
- **Direction:** Outbound from metrics service container to Red Hat Data Ingress
- **Nginx ports:** 8087/tcp (HTTP) and 8450/tcp (HTTPS) opened in firewall (default zone: public)
- **Internal Gunicorn port:** 8006 (localhost only, not opened in firewall)
- **Proxy support:** HTTP/HTTPS proxy configuration supported via standard environment variables (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`)

