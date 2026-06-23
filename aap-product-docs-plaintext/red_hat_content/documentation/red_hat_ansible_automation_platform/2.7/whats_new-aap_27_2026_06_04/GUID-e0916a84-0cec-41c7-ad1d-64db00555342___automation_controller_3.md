# Ansible Automation Platform patch release June 4, 2026
## Automation hub

- Fixed an issue where execution environment (EE) container images that existed in automation hub before a 2.6 to 2.7 upgrade failed to sync or pull with errors such as "unexpected end of JSON input" or "manifest unknown." The upgrade did not fully populate some manifest records for pre-existing EE images. New EE images pushed after the upgrade and collections were not affected. (AAP-77470)
