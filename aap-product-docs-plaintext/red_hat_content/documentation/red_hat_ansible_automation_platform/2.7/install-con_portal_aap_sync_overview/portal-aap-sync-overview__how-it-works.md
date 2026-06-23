# Understanding Ansible Automation Platform synchronization
## How it works

1. Ansible automation portal connects to your Ansible Automation Platform instance using configured credentials.
2. Ansible automation portal fetches data based on the configured Ansible Automation Platform Organization and filter criteria.
3. Ansible automation portal converts Ansible Automation Platform entities into portal entities and displays them in the UI.
4. Synchronization runs on a configurable schedule (for example, every 60 minutes).
5. Users access and launch resources based on their existing Ansible Automation Platform permissions.

