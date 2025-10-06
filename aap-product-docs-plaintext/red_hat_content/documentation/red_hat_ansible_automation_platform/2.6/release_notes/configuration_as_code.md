# 2. New features and enhancements
## 2.4. Configuration as Code




The [ansible.platform](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/platform/) collection now provides unified, platform-wide Role-Based Access Control (RBAC) management across Ansible Automation Platform components. New or enhanced modules include `Organization` , `Team` , `User` , `Role definitions` , `Role Assignments` (team/user). Additionally:

- You can declare the RBAC state as code and apply idempotently across services.
- Ansible collections now use a standard global environment variable prefix across components. Automation controller, Automation hub, and Event-Driven Ansible all use a new standard of “AAP_” instead of "COMPONENT_". For example, `    aap_hostname` . See [the documentation](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/platform/docs/) in Automation hub for more information.


