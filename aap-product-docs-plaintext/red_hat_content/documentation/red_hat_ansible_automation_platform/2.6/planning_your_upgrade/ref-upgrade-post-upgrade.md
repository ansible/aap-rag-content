# 5. Identity access management data movement
## 5.3. Post upgrade




It is imperative that administrators verify the assigned permissions for all teams in the platform-wide authentication gateway immediately after the upgrade:

- Ensure the transferred team members have the correct access rights in the Ansible Automation Platform environment based on the filesystem.
- Make sure all members that have been merged are, in fact, the same member. Incorrect permissions could lead to access issues or security vulnerabilities.
- When upgrade to Ansible Automation Platform 2.6 is complete, user accounts that exist in both the automation hub and automation controller systems will be unified, and platform gateway IAM will be the source of truth for users after the data movement.
- Automation hub and Event-Driven Ansible users must either be recreated or the users that moved from automation controller given permission to use those services.


After your upgrade to automation controller 2.6 is complete, verify that you can log in to the upgraded platform with your existing automation controller credentials (username and password).

Note
To do this, you have must have a automation controller account on Ansible Automation Platform 2.4 or 2.5 with administrative privileges.



The following table provides next steps for each type of user after they have upgraded.

| If you are this type of user before upgrading: | Then take these actions after the upgrade: |
| --- | --- |
| An automation controller administrator (no automation hub account) | Log in with your automation controller username and password; you are now a platform gateway administrator. |
| An automation controller normal user (no automation hub account) | Log in with your automation controller username and password; you are now a platform gateway normal user. |
| A automation hub user (no automation controller account) | Request a password reset from your administrator. When you log in with your new password you will be a platform gateway normal user. You will retain your hub-related permissions. |
| An automation controller and automation hub user (with the same username in both services) | Log in with your automation controller username and password; your previous two accounts will be merged and you are now a platform gateway normal user. |
| An automation hub user with SSO (no automation controller account) | Log in with your SSO credentials; you are now a platform gateway normal user. |


