# Ensure compliance with host-level security controls
## User namespaces

To support Ansible Automation Platform execution environments, you must allow Linux containers. If a compliance profile (like DISA STIG) has set `user.max_user_namespaces` to "0," you must disable this control.

### About this task

To check the `user.max_user_namespaces` kernel setting, complete the following steps on each Ansible Automation Platform component in the installation inventory.

### Procedure

1.  Log in to your automation controller at the command line.
2.  Run the command `sudo sysctl user.max_user_namespaces`.
3.  If the output indicates that the value is zero, look at the contents of the file `/etc/sysctl.conf` and all files under `/etc/sysctl.d/`, edit the file containing the `user.max_user_namespaces` setting, and set the value to "65535".
4.  To apply this new value, run the command `sudo sysctl -p <file>`, where `<file>` is the file just modified.
5.  Re-run the command `sudo sysctl user.max_user_namespaces` and verify that the value is now set to "65535".

