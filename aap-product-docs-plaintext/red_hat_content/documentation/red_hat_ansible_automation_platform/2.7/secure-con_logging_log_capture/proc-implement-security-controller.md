# Best practices for setting up secure logging
## Implement security control for each host

Restrict access to automation controller log files using explicitly defined privileges. Protecting log confidentiality prevents attackers from gathering sensitive system details and helps ensure your environment is safe from privilege escalation or lateral movement.

### About this task

To implement the security control, use the following procedure:

### Procedure

1.  As a system administrator for each automation controller host, set the permissions and owner of the automation controller NGINX log directory:

-  `chmod 770 /var/log/nginx`
-  `chown nginx:root /var/log/nginx`

2.  Set the permissions and owner of the automation controller log directory:

-  `chmod 770 /var/log/tower`
-  `chown awx:awx /var/log/tower`

3.  Set the permissions and owner of the automation controller supervisor log directory:

-  `chmod 770 /var/log/supervisor/`
-  `chown root:root /var/log/supervisor/`
- If automation controller is not in an HA configuration, the administrator must reinstall automation controller.

