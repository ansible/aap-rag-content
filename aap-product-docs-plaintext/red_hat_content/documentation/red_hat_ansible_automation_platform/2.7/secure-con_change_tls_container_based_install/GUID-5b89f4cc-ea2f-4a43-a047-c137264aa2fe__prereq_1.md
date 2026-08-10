# Container-based installations
## Renew self-signed TLS certificates using the installation program
### Before you begin

- You have root access or equal privileges on the host where the containerized installer is running.
- You have access to the inventory file used during the initial installation.

### Procedure

1.  Add `aap_service_regen_cert=true` to the inventory file in the `[all:vars]` section:


```
[all:vars]
aap_service_regen_cert=true
```

To also regenerate the internal CA certificate, add the following variable:

```
[all:vars]
aap_service_regen_cert=true
aap_ca_regenerate=true
```

2.  Run the install playbook from your installation directory:


```
ansible-playbook -i <inventory_file_name>
ansible.containerized_installer.install
```

