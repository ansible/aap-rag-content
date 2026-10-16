# Understand metrics service architecture
## Key characteristics

- **Django-based application:** Built on Django framework with database migrations managed through /app/scripts/init.sh
- **Containerized deployment:** Runs as three containers (`automation-metrics-web`, `automation-metrics-tasks`, `automation-metrics-scheduler`) managed by systemd (containerized installer) or Kubernetes (operator)
- **Optional deployment:** Set `automationmetrics_skip_install=true` to opt out of metrics service installation when automation controller is present (containerized installations only)
- **Automatic anonymization:** Customer-defined object names are replaced with "Custom" before transmission. Only built-in object names and publicly available collection names are sent in their original form
- **Auto-configured ingress:** Establishes secure connection to Red Hat Data Ingress without manual setup
- **Read-only access:** Accesses automation controller database in read-only mode to prevent operational impact
- **Isolated database:** Maintains its own `metrics_service` database for metrics processing and storage
- **Health monitoring:** Provides health check endpoint (returns `"status": "good"` when healthy)
- **HTTP proxy support:** Supports HTTP/HTTPS proxy configuration for environments without direct internet access
- **Startup validation:** Validates required production environment variables at startup. Containers exit immediately with validation errors if required variables are missing or invalid
- **Deployment flexibility:** Supports both RHEL-based containerized deployments and OpenShift operator-based deployments with different configuration approaches
- **Date filtering**: Users can only use predefined date range options (Last 7 days, Last 30 days, Last 90 days, etc.)
- **Currency**: All cost values display in USD. Multi-currency support not available.

**Capabilities unavailable without metrics service**

- Automation dashboard has no backend data source and is non-functional
- No anonymized usage data is collected or transmitted
- ROI calculations, automation savings, and executive reporting are unavailable
- Dashboard collection tasks do not run

