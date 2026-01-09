# 2. Hardening Ansible Automation Platform
## 2.2. Installation
### 2.2.5. Compliance profile considerations




In many environments, Ansible Automation Platform might need to be installed on Red Hat Enterprise Linux systems where security controls have been applied to meet the requirements of a compliance profile such as CIS Critical Security Controls, _Payment Card Industry/Data Security Standard_ (PCI/DSS), the DISA STIG, or a similar profile. In these environments, there are a specific set of security controls that might need to be modified for Ansible Automation Platform to run properly. Apply any compliance profile controls to the Red Hat Enterprise Linux servers being used for Ansible Automation Platform before installation, and then modify the following security controls as required.

In environments where these controls are required, discuss waiving the controls with your security auditor.

#### 2.2.5.1. Fapolicyd




A compliance policy might require the `fapolicyd` daemon to be running. However, Ansible Automation Platform is not currently supported when `fapolicyd` is enforcing policy, as this causes failures during both installation and operation of Ansible Automation Platform. Because of this, the installation program runs a pre-flight check that halts installation if it discovers that `fapolicyd` is enforcing policy. This guide recommends setting `fapolicyd` to permissive mode on Ansible Automation Platform using the following steps:

1. Edit the file `    /etc/fapolicyd/fapolicyd.conf` and set "permissive = 1".
1. Restart the service with the command

`    sudo systemctl restart fapolicyd.service`




Note
If this security control is also applied to the installation host, the default `fapolicyd` configuration causes the Ansible Automation Platform installation program to fail. In this case, the recommendation is to set `fapolicyd` to permissive mode on the installation host.



#### 2.2.5.2. File systems mounted with "noexec"




A compliance profile might require that certain file systems are mounted with the `noexec` option to prevent execution of binaries located in these file systems. The Ansible Automation Platform RPM-based installation program runs a preflight check that fails if any of the following file systems are mounted with the `noexec` option:

-  `    /tmp`
-  `    /var`
-  `    /var/tmp`


To install Ansible Automation Platform, you must re-mount these file systems with the `noexec` option removed. When installation is complete, proceed with the following steps:

1. Reapply the `    noexec` option to the `    /tmp` and `    /var/tmp` file systems.
1. Change the automation controller job execution path from `    /tmp` to an alternate directory that does not have the `    noexec` option enabled.
1. To make this change, log in to the automation controller UI as an administrator, navigate to Settings and select **Jobs settings** .
1. Change the "Job execution path" setting to the alternate directory.


During normal operations, the file system which contains the `/var/lib/awx` subdirectory (typically `/var` ) must not be mounted with the `noexec` option, or the automation controller cannot run automation jobs in execution environments.

In environments where STIG controls are routinely audited, discuss waiving the STIG controls related to file system `noexec` with your security auditor.

#### 2.2.5.3. User namespaces




A compliance profile might require that the kernel setting `user.max_user_namespaces` is set to "0", to prevent the launch of Linux containers. The DISA STIG, for example, specifically requires this control but only if Linux containers are not required. Because Ansible Automation Platform can be installed and operated in containers and also uses containers as part of its execution environment capability, Linux containers are required and this control must be disabled.

To check the `user.max_user_namespaces` kernel setting, complete the following steps on each Ansible Automation Platform component in the installation inventory:

1. Log in to your automation controller at the command line.
1. Run the command `    sudo sysctl user.max_user_namespaces` .
1. If the output indicates that the value is zero, look at the contents of the file `    /etc/sysctl.conf` and all files under `    /etc/sysctl.d/` , edit the file containing the `    user.max_user_namespaces` setting, and set the value to "65535".
1. To apply this new value, run the command `    sudo sysctl -p &lt;file&gt;` , where `    &lt;file&gt;` is the file just modified.
1. Re-run the command `    sudo sysctl user.max_user_namespaces` and verify that the value is now set to "65535".


#### 2.2.5.4. Interactive session timeout




A compliance profile might require that an interactive session timeout be enforced. For example, the DISA STIG requires that all users be automatically logged out after 15 minutes of inactivity. The installation process often requires an hour or more to complete, and this control can stop the installation process and log out the user before installation is complete. The same also applies to day two operations such as backup and restore, which in production environments often take longer than the recommended interactive session timeout. During these operations, increase the interactive session timeout to ensure the operation is successful.

There are multiple ways in which this control can be enforced, including shell timeout variables, setting the idle session timeout for `systemd-logind` , or setting SSH connection timeouts, and different compliance profiles can use one or more of these methods. The one that most often interrupts the installation and day two operations is the idle session timeout for `systemd-logind` , which was introduced in the DISA STIG version V2R1 (Red Hat Enterprise Linux 8) and V2R2 (Red Hat Enterprise Linux 9). To increase the idle session timeout for `systemd-logind` , as the root user:

- Edit the file `    /etc/systemd/logind.conf` .
- If the `    StopIdleSessionSec` setting is set to zero, no change is needed.
- If the `    StopIdleSessionSec` setting is non-zero, this indicates that the session will be terminated after that number of seconds.

Change `    StopIdleSessionSec=7200` to increase the timeout, then run `    systemctl restart systemd-logind` to apply the change.


- Log out of the interactive session entirely and log back in to ensure the new setting applies to the current login session.


Note
This change only needs to be made on the installation host, or if an installation host is not used, the host where the Ansible Automation Platform installation program is run.



#### 2.2.5.5. Sudo and NOPASSWD




A compliance profile might require that all users with sudo privileges must provide a password (that is, the `NOPASSWD` directive must not be used in a sudoers file). The Ansible Automation Platform installation program runs many tasks as a privileged user, and by default expects to be able to elevate privileges without a password.

To provide a password to the installation program for elevating privileges, append the following options when launching the RPM installer script:

`./setup.sh &lt;setup options&gt; --ask-become-pass` .

For the container-based installation program:

`ansible-playbook ansible.containerized_installer.install --ask-become-pass`

When the installation program is run, you are prompted for the user’s password to elevate privileges.

Note
Using the `--ask-become-pass` option also applies when running the installation program for day-two operations such as backup and restore.



