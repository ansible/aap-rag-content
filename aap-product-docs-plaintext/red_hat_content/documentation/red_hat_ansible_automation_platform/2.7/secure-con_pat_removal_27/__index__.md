# Personal Access Token removal in Ansible Automation Platform 2.7

In Ansible Automation Platform 2.7, component-level Personal Access Tokens (PATs) have been removed. Tokens created directly in automation controller, automation hub, or Event-Driven Ansible controller in Ansible Automation Platform 2.6 or earlier no longer work in Ansible Automation Platform 2.7.

All tokens must now be created and managed through platform gateway.

## Token migration timeline

- **Ansible Automation Platform 2.5:** Platform gateway introduced; component-level PATs deprecated.
- **Ansible Automation Platform 2.6:** PAT migration from components to platform gateway supported; component-level PATs still functional.
- **Ansible Automation Platform 2.7:** Component-level PATs removed; only platform gateway tokens supported.

## Create new tokens after upgrade

Component-level tokens from automation controller, automation hub, or Event-Driven Ansible are not migrated to platform gateway during upgrade. After upgrading to Ansible Automation Platform 2.7, you must create new tokens through platform gateway.

### Procedure

1.  Log in to the platform gateway UI.
2.  Navigate to Access Management> (and then)Users> (and then)[your user]> (and then)Tokens.
3.  Create new tokens as needed.
4.  Update any scripts or integrations to use the new platform gateway tokens.
