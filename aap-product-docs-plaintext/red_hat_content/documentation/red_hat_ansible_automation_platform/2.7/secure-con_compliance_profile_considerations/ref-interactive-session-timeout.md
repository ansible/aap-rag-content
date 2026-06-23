# Ensure compliance with host-level security controls
## Interactive session timeout

Temporarily increase the interactive session timeout during lengthy operations like installations, backups, and restores. This prevents compliance policies from automatically logging you out and helps ensure these critical processes complete successfully.

There are multiple ways in which this control can be enforced, including shell timeout variables, setting the idle session timeout for `systemd-logind`, or setting SSH connection timeouts, and different compliance profiles can use one or more of these methods. The one that most often interrupts the installation and day two operations is the idle session timeout for `systemd-logind`, which was introduced in the DISA STIG version V2R1 (Red Hat Enterprise Linux 8) and V2R2 (Red Hat Enterprise Linux 9). To increase the idle session timeout for `systemd-logind`, as the root user:

- Edit the file `/etc/systemd/logind.conf`.

- If the `StopIdleSessionSec` setting is set to zero, no change is needed.

- If the `StopIdleSessionSec` setting is non-zero, this indicates that the session will be terminated after that number of seconds. Change `StopIdleSessionSec=7200` to increase the timeout, then run `systemctl restart systemd-logind` to apply the change.

- Log out of the interactive session entirely and log back in to ensure the new setting applies to the current login session.

Note:

This change only needs to be made on the installation host, or if an installation host is not used, the host where the Ansible Automation Platform installation program is run.

