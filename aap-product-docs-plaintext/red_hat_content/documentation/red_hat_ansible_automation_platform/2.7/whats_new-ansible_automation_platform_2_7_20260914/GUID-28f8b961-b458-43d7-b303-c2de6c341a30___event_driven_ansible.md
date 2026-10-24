# Ansible Automation Platform 2.7 patch release September 14, 2026 (2.7-8)
## Automation Platform

- Fixed an issue where a performance regression in team role assignment (POST /`role_team_assignments`/) caused latency to increase 2–10x at scale in environments with many organizations and teams. (AAP-88361)

