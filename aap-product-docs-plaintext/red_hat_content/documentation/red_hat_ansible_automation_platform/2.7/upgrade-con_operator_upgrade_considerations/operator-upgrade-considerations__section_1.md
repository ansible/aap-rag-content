# Upgrade considerations
## Event streams database user for external databases

If you use an external PostgreSQL database for Event-Driven Ansible and are upgrading your Ansible Automation Platform, verify that a dedicated `eda_event_stream` database user exists on your external database before upgrading. This user is required for event stream operations in Ansible Automation Platform 2.7 and later. See the following related links for more information.
