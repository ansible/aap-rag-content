# Back up and restore your containerized deployment
## What the restore playbook restores
### Data restored from backup

The restore playbook restores the following from the backup archive:

- PostgreSQL database content for all Ansible Automation Platform components
- Application encryption keys used to protect credential and configuration data at rest
- Configuration files for each Ansible Automation Platform component
- Data files for each Ansible Automation Platform component

The restore playbook selectively restores application encryption keys so that each component can decrypt its database content after the restore. If encryption keys are not restored from the same backup, components cannot read their stored credentials.

