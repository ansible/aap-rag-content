# Configure role-based access control for Ansible automation portal
## Adjust synchronization frequency

Ansible automation portal synchronizes users, teams, organization, and job template information from Ansible Automation Platform at regular intervals. By default, synchronization occurs hourly.

To change the synchronization frequency:

- **RHEL appliance:** Edit /etc/portal/configs/app-config/app-config.production.yaml and update the `schedule.frequency` value under the `catalog.providers.rhaap` section. Restart the portal service after saving.
- **OpenShift Container Platform:** Update the `schedule.frequency` value in the Helm chart values file and upgrade the Helm release.
