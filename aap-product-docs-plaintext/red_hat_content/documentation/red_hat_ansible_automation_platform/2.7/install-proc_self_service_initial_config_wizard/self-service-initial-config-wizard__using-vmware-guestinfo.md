# Configure the appliance at first boot
## Using VMware guestinfo properties

Use this method for VMware vSphere deployments.

1. Set the following `guestinfo` properties on the virtual machine in vSphere:

```terminal
guestinfo.portal.ssh_public_key = "<your_ssh_public_key>"
guestinfo.portal.config = "<base64_encoded_config_yaml>"
```
Where `<base64_encoded_config_yaml>` is the Base64-encoded content of your portal configuration YAML.

2. Power on the virtual machine. The appliance detects and applies the `guestinfo` properties on first boot.

