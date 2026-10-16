# Ansible Automation Platform 2.7 patch release August 4, 2026 (2.7.4)
## Highlights

- Bulk migration processing, UNION ALL RBAC queries, elimination of N+1 serialization patterns, and database-backed cursor pagination significantly reduce DB load and API latency for large deployments.
- New Protected Resource Metadata (RFC 9728) support and configurable `MCP_SERVER_URL` environment variable for both operator and containerized deployments.
- New `rotate_secret_key` command for SECRET_KEY rotation, configurable concurrent session limits, and progress reporting during merge organization operations.
- Over 30 CVE remediations across Gateway, Controller, Event-Driven Ansible, Automation Hub, Lightspeed, and Receptor addressing authentication bypass, code execution, and denial-of-service vulnerabilities.
- Fixed database backup failures on EFS-backed storage, automatic NO_PROXY augmentation for proxy-configured clusters, and new Envoy proxy resource tuning.

