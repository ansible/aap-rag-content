# Configure an external database for event streams

Event-Driven Ansible event streams require a dedicated PostgreSQL database user for security and access control. By default, the platform uses a separate user (`eda_event_stream`) to isolate event stream operations from other processes.

If you use the Ansible Automation Platform provisioned database, the installer configures this user automatically. For external databases not managed by Ansible Automation Platform, use one of the following scenarios to set up the event streams database user:

1. An external database with PostgreSQL admin credentials: The installer creates the user automatically.
2. An external database without PostgreSQL admin credentials: You must create the user manually.
