# Ansible Automation Platform 2.7 patch release September 28, 2026 (portal-2.2.8)
## Ansible automation portal RHEL appliance

- Fixed an issue where the SSH login MOTD listed "View config" as `sudo portal-status`, duplicating the portal status command instead of showing a read-only view of `app-config.production.yaml`. (AAP-92035)

