# Automate nodes that comply with security profiles
## Option 1: Set the fapolicyd service to permissive mode

The fapolicyd service can be set to "permissive" mode, meaning that it only logs fapolicyd rule violations, rather than enforcing them.

### About this task

To configure permissive mode for fapolicyd, use the following procedure:

### Procedure

1.  Edit the file `/etc/fapolicyd/fapolicyd.conf`, and set "permissive = 1".
2.  Restart the `fapolicy` service by running `systemctl restart fapolicyd.service`.
3.  In environments where this configuration might not meet a required compliance profile or local policy, discuss waiving the relevant security control with your security auditor.

