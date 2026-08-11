# Install Ansible automation portal on VMware vSphere
## Using VMware guestinfo properties

Use this method for VMware vSphere deployments as an alternative to the ISO method.

1. Base64-encode your cloud-init user-data file:

```terminal
$ base64 -w 0 user-data > user-data.b64
```

2. Create a metadata file with an instance ID and Base64-encode it:

```terminal
$ echo '{"instance-id": "automation-portal"}' > meta-data
$ base64 -w 0 meta-data > meta-data.b64
```

3. Set the following guestinfo properties on the virtual machine in vSphere:

```none
guestinfo.userdata = "*<contents-of-user-data.b64>*"
guestinfo.userdata.encoding = "base64"
guestinfo.metadata = "*<contents-of-meta-data.b64>*"
guestinfo.metadata.encoding = "base64"
```

Set these properties using the vSphere web client (**Edit Settings** > **VM Options** > **Advanced** > **Configuration Parameters**).

4. Power on the virtual machine. Cloud-init reads the guestinfo properties and applies the configuration on first boot.

Note:

Cloud-init runs only once per instance ID. If you need to re-apply cloud-init configuration to an existing VM, change the `instance-id` value in the metadata, re-encode it, and update the `guestinfo.metadata` property before rebooting.

For additional native cloud-init configuration options, such as network configuration, see the cloud-init VMware datasource documentation in the related links below.
