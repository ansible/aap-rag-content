# 2. Hardening Ansible Automation Platform
## 2.3. Initial configuration
### 2.3.3. Implement security control for system administrators




Ansible Automation Platform must generate the appropriate log records related to user sessions in support of troubleshooting, debugging, and forensic analysis. Without a data logging feature, the organization loses an important auditing and analysis tool for event investigations.

Use the following procedure to implement the security control as a System Administrator for each automation controller host:

**Procedure**

1. From the navigation panel, selectSettings→Automation Execution→System. The System Settings page is displayed.
1. ClickEdit.
1. Set the following:


-  **Enable Activity Stream** = On
-  **Enable Activity Stream for Inventory Sync** = On

1. ClickSave.


