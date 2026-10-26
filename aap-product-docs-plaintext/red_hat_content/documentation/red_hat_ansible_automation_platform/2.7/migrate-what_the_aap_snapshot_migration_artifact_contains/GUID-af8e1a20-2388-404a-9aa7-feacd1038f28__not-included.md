# What the aap_snapshot migration artifact contains
## What the artifact does not include

The artifact does not include infrastructure-level state or post-deployment configuration that exists outside the platform databases:

- Live network connections or active session state
- Running job output or execution environment logs
- System-level configuration outside the Ansible Automation Platform component scope (OS configuration, firewall rules, custom certificates)
- Content not present in the platform database at export time (for example, collections on an external automation hub that were never synced)

The following application-level items require manual reconfiguration after import and are not automatically restored by the collection:

- Execution node re-registration (execution node records migrate in the database dump, but the reconcile phase deprovisions nodes with no recent heartbeat; nodes must be re-registered through the Ansible Automation Platform UI)
- System settings not stored in the platform database
- Custom TLS certificates
- Custom automation controller configuration files from `/etc/tower/conf.d/` (exported into the artifact but not applied during OpenShift Container Platform import, as OCP deployments use operator-managed configuration instead of file-based settings)
- Host metrics and facts (regenerated after the first inventory sync)

Authentication settings configured through the automation controller or gateway UI (LDAP, SAML, social authentication) are stored in the component databases and migrate automatically with the database dump. No manual reconfiguration is required for these settings unless hostname or redirect URI changes are needed in the external identity provider.
