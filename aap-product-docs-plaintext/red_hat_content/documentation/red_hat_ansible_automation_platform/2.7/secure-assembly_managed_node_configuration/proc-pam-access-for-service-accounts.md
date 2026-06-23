# Improve the security of nodes managed by Ansible Automation Platform
## Enable and configure pam_access controls for service accounts

To restrict remote login access to connections originating from the Ansible Automation Platform automation controller and execution nodes and ensure the service account is exclusively used by Ansible Automation Platform, use the following procedure:

### Procedure

1.  Use the FQDNs of your automation controller and execution nodes to add the following content to the `/etc/security/access.conf` file, using the FQDNs of your controller nodes and execution nodes:


```
# allow the ansible service account to log in from local sources and
# the hybrid controller or execution nodes, and deny all other sources
+:ansible:LOCAL controller1.example.com controller2.example.com en1.example.com
-:ansible:ALL
```

2.  Enable the `with-pamaccess` feature in the current authselect profile. All authselect profiles included by default with RHEL have this feature.  `sudo authselect enable-feature with-pamaccess`
