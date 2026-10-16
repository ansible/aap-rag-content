# Ansible Automation Platform 2.7 patch release September 14, 2026 (2.7-8)
## Automation Platform UI

- Fixed an issue where high list refresh frequency caused excessive network load; most lists now refresh every 60 seconds. (AAP-91427)
- Fixed an issue where the Source Control Branch override on a Job Template node in a Workflow Template could not be cleared. (AAP-88997)
- Fixed an issue where the default for the `inventory_source` path field was misleadingly labeled. (AAP-87553)

