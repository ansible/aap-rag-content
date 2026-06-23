# Ensure compliance with host-level security controls
## File systems mounted with "noexec"

Remove the `noexec` mount option from the` /tmp`, `/var`, and `/var/tmp` file systems so the Ansible Automation Platform RPM installer can execute binaries. This prevents preflight check failures and helps ensure a successful installation.

### About this task

To install Ansible Automation Platform, you must re-mount these file systems with the `noexec` option removed. When installation is complete, proceed with the following steps:

### Procedure

1.  Reapply the `noexec` option to the `/tmp` and `/var/tmp` file systems.
2.  Change the automation controller job execution path from `/tmp` to an alternate directory that does not have the `noexec` option enabled.
3.  To make this change, log in to the automation controller UI as an administrator, navigate to Settings and select **Jobs settings**.
4.  Change the "Job execution path" setting to the alternate directory. During normal operations, the file system which contains the `/var/lib/awx` subdirectory (typically `/var`) must not be mounted with the `noexec` option, or the automation controller cannot run automation jobs in execution environments.

5.  In environments where STIG controls are routinely audited, discuss waiving the STIG controls related to file system `noexec` with your security auditor.

