# Event persistence in rulebook activations

By default, events processed by rulebook activations are not persisted. When you enable event persistence, Event-Driven Ansible stores matched events in a dedicated database so you can review and audit the events that triggered your automation rules.

Because the event persistence database is deployed during installation, you must decide whether to use this feature before you begin the installation process. If you enable event persistence after installation, additional configuration steps are required.

Event persistence requires a dedicated PostgreSQL database using one of the following options:

- **Built-in event persistence database** - Deployed automatically during Ansible Automation Platform installation. With this option, event persistence works out of the box with a default Event-Driven Ansible Rule Engine credential.
- **External database** - A PostgreSQL database instance you manage separately. This option requires creating a custom Rule Engine credential pointing to your external database. For more information on creating a custom Rule Engine, see the following **Related tasks**. For specific information on **persistence database requirements** (sizing, IOPs, and similar), refer to the deployment topology content in the following related concepts and tasks.

When event persistence is enabled for a rulebook activation:

1. Event-Driven Ansible receives events from the configured event source.
2. Each matched event is saved to the event persistence database.
3. Matched events are retained in the database until all conditions are met and an action is fired.
4. Processed events are then removed from the database.

Important:

The default Event-Driven Ansible Rule Engine credential does not support encryption of event data. If your events contain sensitive information, you must create a custom Rule Engine credential with encryption keys to protect your event data. To create your own custom Event-Driven Ansible Rule engine credential, see the following related concept and tasks.
