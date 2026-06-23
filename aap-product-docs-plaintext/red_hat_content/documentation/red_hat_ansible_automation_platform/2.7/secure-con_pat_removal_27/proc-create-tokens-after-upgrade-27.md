# Personal Access Token removal in Ansible Automation Platform 2.7
## Create new tokens after upgrade

Component-level tokens from automation controller, automation hub, or Event-Driven Ansible are not migrated to platform gateway during upgrade. After upgrading to Ansible Automation Platform 2.7, you must create new tokens through platform gateway.

### Procedure

1.  Log in to the platform gateway UI.
2.  Navigate to Access Management> (and then)Users> (and then)[your user]> (and then)Tokens.
3.  Create new tokens as needed.
4.  Update any scripts or integrations to use the new platform gateway tokens.
