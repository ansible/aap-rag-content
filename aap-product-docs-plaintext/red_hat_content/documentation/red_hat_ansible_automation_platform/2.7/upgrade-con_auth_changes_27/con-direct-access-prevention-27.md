# Authentication changes in Ansible Automation Platform 2.7
## How direct access is prevented in Ansible Automation Platform 2.7

In Ansible Automation Platform 2.7, platform components are configured to accept only platform gateway JWT authentication, ensuring that all external access goes through platform gateway.

When deployed as part of Ansible Automation Platform, this enforcement is immutable and cannot be changed through configuration files or environment variables, ensuring no bypass is possible.
