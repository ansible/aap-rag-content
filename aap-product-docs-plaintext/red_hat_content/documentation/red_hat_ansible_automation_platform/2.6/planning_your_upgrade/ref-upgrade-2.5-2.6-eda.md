# 5. Identity access management data movement
## 5.2. Upgrades from Ansible Automation Platform 2.5 to 2.6
### 5.2.3. Event-Driven Ansible




The following apply:

- An Event-Driven Ansible administrator (Automation Decisions Administrator) in 2.5 will be removed in the upgraded version and for this user the permissions must be reassigned manually as part of the movement process.
- For Event-Driven Ansible, you must reset your password to log in to Ansible Automation Platform. You can still use your Event-Driven Ansible username but will require new passwords.
- If an Event-Driven Ansible user with SSO exists, then they will not have to reset password and should have their permissions moved over as part of the SSO migration.


