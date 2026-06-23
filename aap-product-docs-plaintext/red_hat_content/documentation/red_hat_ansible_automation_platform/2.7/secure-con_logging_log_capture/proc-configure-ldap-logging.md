# Best practices for setting up secure logging
## Configure LDAP logging

Enable debug logging for LDAP in the platform gateway settings to capture detailed authentication messages. Reviewing these logs ensures that you can effectively troubleshoot and resolve LDAP connection issues.

### Procedure

1.  Edit the gateway settings file:
1.  On Ansible Automation Platform 2.6 Containerized, the file is `~/aap/gateway/etc/settings.py` (as the user running the platform gateway container).
2.  On Ansible Automation Platform 2.6 RPM-based, the file is `/etc/ansible-automation-platform/gateway/settings.py`.

```
(...)
CACHES['fallback']['LOCATION'] = '/var/cache/ansible-automation-platform/gateway'

LOGGING['loggers']['aap']['level'] = 'INFO'
LOGGING['loggers']['ansible_base']['level'] = 'INFO'
LOGGING['loggers']['django_auth_ldap']['level'] = 'DEBUG'      ######      add this line

(...)
```

2.  Restart the platform gateway service or container:
1.  On Ansible Automation Platform 2.6 Containerized, restart the platform gateway service so that it restarts the platform gateway container:

Note:
Ensure that you run `` systemctl with the `--user` `` flag as follows:

+ `$ systemctl --user restart automation-gateway`

2.  On Ansible Automation Platform 2.6 RPM-based, use the `automation-gateway-service` command:
`# automation-gateway-service restart`

