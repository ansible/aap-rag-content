# Ansible Automation Platform 2.7 patch release September 21, 2026 (2.7-9)
## Aap Gateway

- Fixed an issue where authentication mappings that assign an object-scoped role (for example, JobTemplate Execute) are now rejected when the mapping is saved, instead of being accepted and failing silently at login. (AAP-92571)

