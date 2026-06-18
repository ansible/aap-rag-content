# Trigger automation from events with Event-Driven Ansible

Event-Driven Ansible is a highly scalable, flexible automation capability. It works with external event sources (like software vendors' monitoring tools) to identify IT events and automatically implement the defined changes or responses within a rulebook.

Learn how to configure and manage the end-to-end lifecycle of event-driven automation within the Red Hat Ansible Automation Platform. Event-Driven Ansible provides you the ability to perform the following actions:

- Manage projects for rulebook storage
- Build and restore decision environments for execution
- Define credentials for secure authentication
- Create event streams for centralized routing
- Manage rulebook activations to main persistent, scalable listeners that monitor infrastructure and trigger automated workflows in real time


Note:

- API documentation for Event-Driven Ansible controller is available through the platform gateway (for example, `https://<gateway-host>/api/eda/v1/docs`)
- Event-Driven Ansible controller uses PostgreSQL for data storage and background task workers via the `dispatcherd` service. When the workers are unavailable, you will not be able to create or sync projects, or enable rulebook activations.

Important:

In new installations of Ansible Automation Platform, using Event-Driven Ansible controller’s API to manage organizations, teams, or users requires an automated sync of up to 15 minutes to propagate changes to the rest of the Ansible Automation Platform components. To avoid potential errors and ensure immediate access, use the platform gateway API instead, or the unified UI.
