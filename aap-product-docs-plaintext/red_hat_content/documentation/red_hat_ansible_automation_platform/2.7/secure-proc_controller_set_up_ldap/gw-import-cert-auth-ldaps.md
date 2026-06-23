# Configure LDAP authentication
## Import a certificate authority in automation controller for LDAPS integration

You can authenticate to the automation controller server by using LDAP. However, if you change to using LDAPS (LDAP over SSL/TLS) to authenticate and the TLS certificate is not trusted by platform gateway, it fails with an error such as:

### About this task

```
2025-08-26 16:40:56,141 WARNING   django_auth_ldap Caught LDAPError while authenticating: SERVER_DOWN({'result': -1, 'desc': "Can't contact LDAP server", 'ctrls': [], 'info': 'error:0A000086:SSL routines::certificate verify failed (self-signed certificate)'})
```
To get Ansible Automation Platform to trust the certificate coming from LDAP, perform the following procedure on all platform gateway instances.

### Procedure

1.  Place a copy of the LDAP servers certificate in the directory, `/etc/pki/ca-trust/source/anchors/`.
2.  Run the command:


```
update-ca-trust
```
