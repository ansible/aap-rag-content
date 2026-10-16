# Ensure compliance with host-level security controls

You can use Ansible Automation Platform to manage systems where security controls have been applied to managed RHEL nodes to meet the requirements of a compliance profile such as CIS, PCI/DSS, the DISA STIG, or similar.

In environments where these controls are required, discuss waiving the controls with your security auditor.

Warning:

For a containerized installation of Ansible Automation Platform 2.7 on Red Hat Enterprise Linux 9, set the host `umask` to `022` or `002` for the installation. With `umask 077`, the installation program can report success even though the `automation-controller-task` container fails to start with a `Permission denied` error. If the installation already completed with `umask 077`, set the host `umask` to `022` or `002` and run the installation program again. If your security policy requires `umask 077`, consult your security auditor before changing it.

