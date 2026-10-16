# Ansible Automation Platform 2.7 patch release August 24, 2026 (2.7-6)
## Metrics Service

- Fixed an issue where prefer metrics.ms_awx_readonly_user_secret (the value explicitly set on the platform cr) over metrics_read_token_secret_name (AAP-83681)
- Fixed an issue where fixing minor issue where turning off anonymized did not stop a send to segment task if the timing was wrong (AAP-87824)
- Fixed an issue where auto-remove invalid Content Types potentially created from migrate_service_data command. (AAP-88482)

