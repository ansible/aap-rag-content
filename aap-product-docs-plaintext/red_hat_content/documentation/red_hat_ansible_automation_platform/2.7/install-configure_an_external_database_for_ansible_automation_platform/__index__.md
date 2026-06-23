# Configure an external database for Ansible Automation Platform

Configure an external database for Ansible Automation Platform Operator to use your own database infrastructure.

Using an external database lets you share and reuse resources and manually manage backups, upgrades, and performance optimizations.

To configure an external database, create Kubernetes secrets with credentials for connecting to the database. The same external database (PostgreSQL instance) can be used for platform gateway, automation controller, automation hub, Event-Driven Ansible controller, and metrics service as long as the database names are different.

Note:

The automation hub database requires the `hstore` PostgreSQL extension.

