# Ensure compliance with host-level security controls
## Fapolicyd

Set the `fapolicyd` daemon to permissive mode before installing Ansible Automation Platform. This prevents the pre-flight checks from stopping your installation and avoids subsequent operational failures caused by enforcing policies.

### Procedure

1.  Edit the file `/etc/fapolicyd/fapolicyd.conf` and set "permissive = 1".
2.  Restart the service with the command
`sudo systemctl restart fapolicyd.service`

Note:
If this security control is also applied to the installation host, the default `fapolicyd` configuration causes the Ansible Automation Platform installation program to fail. In this case, the recommendation is to set `fapolicyd` to permissive mode on the installation host.

