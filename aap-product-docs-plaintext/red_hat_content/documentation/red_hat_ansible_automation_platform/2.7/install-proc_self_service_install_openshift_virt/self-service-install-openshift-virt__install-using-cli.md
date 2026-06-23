# Install Ansible automation portal on Red Hat OpenShift Virtualization
## Install using the CLI

1. Create a project for the deployment:

```terminal
$ oc new-project <project-name>
```

2. Upload the QCOW2 disk image using `virtctl`:

```terminal
$ virtctl image-upload dv <disk-datavolume-name> \
--size=50Gi \
--image-path=/path/to/disk.qcow2 \
--uploadproxy-url=https://cdi-uploadproxy-openshift-cnv.apps.<cluster-domain> \
--wait-secs=600 \
-n <project-name>
```
| Option         | Description                                                                                                                                           |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--size`       | Set to at least 50 Gi. The QCOW2 expands during conversion to raw format and requires additional space.                                               |
| `--insecure`   | Add this flag if the Containerized Data Importer (CDI) upload proxy uses a self-signed certificate. Omit it when the proxy has a trusted certificate. |
| `--force-bind` | Add this flag if the storage class uses `WaitForFirstConsumer` volume binding mode.                                                                   |
Wait for both upload and processing to complete. The "Processing completed successfully" message confirms that CDI converted the image. For more information about CDI, see the Managing data volumes section of the Red Hat OpenShift Virtualization documentation.

3. Create a Secret from the cloud-init file:

```terminal
$ oc create secret generic <cloudinit-secret-name> \
--from-file=userdata=cloud-init-user-data.yaml \
-n <project-name>
```

4. Create a VirtualMachine manifest and save it as a YAML file (for example, `portal-vm.yaml`). The following example shows a minimal configuration. Replace the resource names and namespace to match your environment:



```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
name: <vm-name>
namespace: <project-name>
spec:
runStrategy: Always
template:
spec:
domain:
devices:
disks:
- disk:
bus: virtio
name: rootdisk
- disk:
bus: virtio
name: cloudinitdisk
interfaces:
- masquerade: {}
name: default
resources:
requests:
memory: 16Gi
networks:
- name: default
pod: {}
volumes:
- name: rootdisk
dataVolume:
name: <disk-datavolume-name>
- name: cloudinitdisk
cloudInitNoCloud:
secretRef:
name: <cloudinit-secret-name>
```
The `dataVolume` name must match the DataVolume created by `virtctl image-upload` in step 2. The `secretRef` name must match the Secret created in step 3.

5. Apply the manifest:

```terminal
$ oc apply -f <vm-manifest>.yaml
```

6. Wait for the VM to reach `Running` status:

```terminal
$ oc get vmi -n <project-name> -w
```
The VM is ready when PHASE shows `Running` and READY shows `True`.

7. Create a Service and Route to expose Ansible automation portal:

```terminal
$ virtctl expose vm <vm-name> --port=443 --name=<service-name> -n <project-name>
$ oc create route passthrough <route-name> --service=<service-name> --port=443 -n <project-name>
$ ROUTE_HOST=$(oc get route <route-name> -o jsonpath='{.spec.host}' -n <project-name>)
$ echo "Automation portal URL: https://$ROUTE_HOST"
```

8. Update the Ansible automation portal user-accessible URL to match the route. SSH into the VM:



```terminal
$ virtctl ssh <username>@vmi/<vm-name> -n <project-name>
```
Edit the configuration file:



```terminal
$ sudo vi /etc/portal/configs/app-config/app-config.production.yaml
```
Set the following three values, replacing `<route-host>` with the route hostname from step 7:



```yaml
app:
baseUrl: "https://<route-host>"
backend:
baseUrl: "https://<route-host>"
cors:
origin: "https://<route-host>"
```
Save the file and restart the Ansible automation portal service. Restarting the `portal` service also restarts `postgres` and `devtools` due to service dependencies:



```terminal
$ sudo systemctl restart portal
```

**Verification**

- Verify that the virtual machine is running:

```terminal
$ oc get vmi -n <project-name>
```
The output shows the virtual machine in `Running` phase with `READY` status set to `True`.

- SSH into the appliance and verify that all services are running:

```terminal
$ sudo ansible-portal status
```

- Access the portal URL from your browser.

