# Ansible Automation Platform 2.7 patch release August 24, 2026 (2.7-6)
## Platform Operator

- Fixed an issue where reconciling while idled could leave the AutomationController CR with an empty spec, breaking controller API routing after un-idling (AAP-83609)
