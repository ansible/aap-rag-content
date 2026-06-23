# Organize rulebooks for event-driven automation

Projects are a logical collection of rulebooks. They must be a git repository and located in the path defined for Event-Driven Ansible content in Ansible collections: `/extensions/eda/rulebooks` at the root of the project.

Important:

Event-Driven Ansible controller uses PostgreSQL for data storage and background task workers via the `dispatcherd `service. When the workers are unavailable, you will not be able to create or sync projects, or enable rulebook activations.

