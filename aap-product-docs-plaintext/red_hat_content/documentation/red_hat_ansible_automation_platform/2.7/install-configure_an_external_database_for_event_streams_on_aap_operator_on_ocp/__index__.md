# Configure an external database for event streams in Operator on OpenShift Container Platform

The Ansible Automation Platform Operator automatically creates a dedicated PostgreSQL user (`eda_event_stream`) for Event-Driven Ansible event stream operations. This user has minimal privileges (`CONNECT` only) to reduce the security impact if credentials are exposed in decision environments.

