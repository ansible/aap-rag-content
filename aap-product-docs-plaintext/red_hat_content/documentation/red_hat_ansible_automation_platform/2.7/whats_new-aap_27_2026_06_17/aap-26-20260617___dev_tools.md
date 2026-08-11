# Ansible Automation Platform patch release June 17, 2026
## Dev-tools

- Fixed an issue where the devspaces container was missing tzdata, causing ansible-navigator to crash with a ZoneInfoNotFoundError on startup. (AAP-78087)

