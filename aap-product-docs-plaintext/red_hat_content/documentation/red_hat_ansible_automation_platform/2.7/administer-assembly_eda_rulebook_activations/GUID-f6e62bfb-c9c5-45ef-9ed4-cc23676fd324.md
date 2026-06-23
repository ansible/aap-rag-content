# Define rules that trigger automation from events
## Rulebook activation list view
### Event persistence in rulebook activations

Event persistence stores incoming data from event sources in a dedicated database. After event persistence is enabled for an activation, the system retains matched events until the rule triggers, ensuring no data is lost before an action occurs.

Event persistence ensures continuity by retaining events during rulebook activation restarts. This feature requires a dedicated PostgreSQL database using one of the following options:

- **Built-in event persistence database** - Deployed automatically during Ansible Automation Platform installation, if selected. With this option, event persistence works out of the box with a default Event-Driven Ansible Rule Engine credential.
- **External database** - A PostgreSQL database instance you manage separately. This option requires creating a custom Rule Engine credential pointing to your external database. For more information on creating a custom Rule Engine, see the following **Related tasks**. For specific information on **persistence database requirements** (sizing, IOPs, and similar), refer to the deployment topology content in the following **Related concepts** and **Related reference**.


When event persistence is enabled for a rulebook activation:

1. Event-Driven Ansible receives events from the configured event source.
2. Each matched event is saved to the event persistence database.
3. Matched events are retained in the database until all conditions are met and an action is fired.
4. Processed events are then removed from the database.


Here are key factors to consider when choosing to enable event persistence:

- If your events contain sensitive information, you must create a custom Rule Engine credential with encryption keys to protect your event data. To create your own custom Event-Driven Ansible Rule engine credential, see the following related concept and tasks.
- The default Event-Driven Ansible Rule Engine credential does not support encryption of event data.
