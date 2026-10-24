# Ansible Automation Platform 2.7 patch release August 24, 2026 (2.7-6)
## Dispatcherd

- Fixed an issue where now queue names longer than 63 characters will be transformed with UUID5 to work with pg_notify. (AAP-78938)

