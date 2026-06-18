# Red Hat Virtualization credential type

Select this credential to enable automation controller to access Ansible’s `oVirt4.py` dynamic inventory plugin, which is managed by *Red Hat Virtualization*.

Automation controller uses the following environment variables for Red Hat Virtualization credentials. These are fields in the user interface:

```
OVIRT_URL
OVIRT_USERNAME
OVIRT_PASSWORD
```
Provide the following information for Red Hat Virtualization credentials:

- **Host (Authentication URL)**: The host URL or IP address to connect to. To sync with the inventory, the credential URL needs to include the `ovirt-engine/api` path.
- **Username**: The username to use to connect to oVirt4. This must include the domain profile to succeed, for example `username@ovirt.host.com`.
- **Password**: The password to use to connect to it.
- Optional: **CA File**: Provide an absolute path to the oVirt certificate file (it might end in `.pem`, `.cer` and `.crt` extensions, but preferably `.pem` for consistency)
