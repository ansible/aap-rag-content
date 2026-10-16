# Understand metrics service architecture
## Metrics service overview

Metrics service is a Django-based application component of Ansible Automation Platform 2.7. It collects anonymized usage and performance data from your automation controller. The service runs as containerized workloads managed by either systemd (containerized installer) or Kubernetes (operator). It maintains its own PostgreSQL database and read-only access to the controller database.

