# Event streams database user for external databases

If you use an external PostgreSQL database for Event-Driven Ansible, you must create a dedicated database user for event stream operations before installing or upgrading Ansible Automation Platform.

Event-Driven Ansible event streams require a dedicated PostgreSQL database user (`eda_event_stream`) for event stream operations. If you use a database managed by the Ansible Automation Platform installer or Operator, this user is created automatically. If you use an external database, you must create this user before installing or upgrading.

The `eda_event_stream` user requires only `CONNECT` privileges. Event streams use the database connection for pub-sub messaging only, with no read or write operations performed on the database. For more information, see the following related concepts and tasks.
