# Update the operating system

Update a device's operating system by changing the target operating system image name or version in the device specification. The agent detects the requested update upon communicating with the server and automatically begins downloading and verifying the new operating system in the background.

The Red Hat Edge Manager agent schedules the actual system update that is performed according to the update policy. At the scheduled update time, the agent installs the new version without disrupting the currently running operating system. Finally, the device reboots into the new version.

The Red Hat Edge Manager currently supports the following image type and image reference format:

| Image Type | Image Reference                                                                                   |
| ---------- | ------------------------------------------------------------------------------------------------- |
| <br>bootc  | <br>An OCI image reference to a container registry. Example: `quay.io/flightctl-example/rhel:9.5` |


During the process, the agent sends status updates to the service. You can check the update process by viewing the device status.

## Update the operating system on the CLI

You can update the operating system on an individual device by specifying a new target image in the device manifest using the Red Hat Edge Manager CLI. This initiates a secure, transactional update process managed automatically by the device agent.

### About this task

### Procedure

1.  Get the current resource manifest of the device by running the following command:


```bash
flightctl get device/<device_name> -o yaml > my_device.yaml
```

2.  Edit the `Device` resource to specify the new operating system name and version target.

```yaml
apiVersion: flightctl.io/v1alpha1
kind: Device
metadata:
name: <device_name>
spec:
[...]
os:
image: quay.io/flightctl/rhel:9.5
[...]
```

3.  Apply the updated `Device` resource by running the following command:


```bash
flightctl apply -f <device_name>.yaml
```
