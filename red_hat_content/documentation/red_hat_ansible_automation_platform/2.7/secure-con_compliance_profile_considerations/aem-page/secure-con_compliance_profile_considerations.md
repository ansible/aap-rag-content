+++
title = "Ensure compliance with host-level security controls - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_compliance_profile_considerations"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_hardening_aap/", "Harden the platform security posture"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_compliance_profile_considerations/aem-page/secure-con_compliance_profile_considerations.html"
last_crumb = "Ensure compliance with host-level security controls"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Ensure compliance with host-level security controls"
oversized = "false"
page_slug = "secure-con_compliance_profile_considerations"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-con_compliance_profile_considerations"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-con_compliance_profile_considerations/toc/toc.json"
type = "aem-page"
+++

# Ensure compliance with host-level security controls

You can use Ansible Automation Platform to manage systems where security controls have been applied to managed RHEL nodes to meet the requirements of a compliance profile such as CIS, PCI/DSS, the DISA STIG, or similar.

In environments where these controls are required, discuss waiving the controls with your security auditor.

## Fapolicyd

Set the `fapolicyd` daemon to permissive mode before installing Ansible Automation Platform. This prevents the pre-flight checks from stopping your installation and avoids subsequent operational failures caused by enforcing policies.

### Procedure

1.  Edit the file `/etc/fapolicyd/fapolicyd.conf` and set "permissive = 1".
2.  Restart the service with the command
       `sudo systemctl restart fapolicyd.service`

  Note:
      If this security control is also applied to the installation host, the default `fapolicyd` configuration causes the Ansible Automation Platform installation program to fail. In this case, the recommendation is to set `fapolicyd` to permissive mode on the installation host.

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

## Interactive session timeout

Temporarily increase the interactive session timeout during lengthy operations like installations, backups, and restores. This prevents compliance policies from automatically logging you out and helps ensure these critical processes complete successfully.

There are multiple ways in which this control can be enforced, including shell timeout variables, setting the idle session timeout for `systemd-logind`, or setting SSH connection timeouts, and different compliance profiles can use one or more of these methods. The one that most often interrupts the installation and day two operations is the idle session timeout for `systemd-logind`, which was introduced in the DISA STIG version V2R1 (Red Hat Enterprise Linux 8) and V2R2 (Red Hat Enterprise Linux 9). To increase the idle session timeout for `systemd-logind`, as the root user:

- Edit the file `/etc/systemd/logind.conf`.

- If the `StopIdleSessionSec` setting is set to zero, no change is needed.

- If the `StopIdleSessionSec` setting is non-zero, this indicates that the session will be terminated after that number of seconds. Change `StopIdleSessionSec=7200` to increase the timeout, then run `systemctl restart systemd-logind` to apply the change.

- Log out of the interactive session entirely and log back in to ensure the new setting applies to the current login session.

Note:

This change only needs to be made on the installation host, or if an installation host is not used, the host where the Ansible Automation Platform installation program is run.

## Sudo and NOPASSWD

A compliance profile might require that all users with sudo privileges must provide a password (the `NOPASSWD` directive must not be used in a sudoers file). The installation program runs many tasks as a privileged user, and by default expects to be able to elevate privileges without a password.

To provide a password to the installation program for elevating privileges, append the following options when launching the RPM installer script:

`./setup.sh <setup options> --ask-become-pass`.

For the container-based installation program:

 `ansible-playbook ansible.containerized_installer.install --ask-become-pass`

When the installation program is run, you are prompted for the user’s password to elevate privileges.

Note:

Using the `--ask-become-pass` option also applies when running the installation program for day-two operations such as backup and restore.
