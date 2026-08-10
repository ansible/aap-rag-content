# Install Ansible automation portal on VMware vSphere
## Installing the appliance

1. Upload the VMDK disk image to a datastore using the `govc` CLI:

```terminal
$ govc import.vmdk disk.vmdk *<folder_name>*
```

Note:
The Ansible automation portal VMDK uses stream-optimized format and requires format conversion during upload. Do not upload VMDK disk images by using the vSphere web client or `govc datastore.upload` — these methods copy the file without converting it, producing an unusable 0 MB disk. The `govc import.vmdk` command converts the image automatically. This restriction applies to VMDK disk images only, not to ISO files.

2. Save your `cloud-init` user-data file as `cloud-init-user-data.yaml`. Use the template from Prerequisites for deploying Ansible automation portal on RHEL in the related links below.

3. Create a cloud-init ISO from your user-data file. VMware delivers cloud-init configuration to the VM as a small ISO disk image labeled `cidata`. Cloud-init expects two files on the ISO: `user-data` (your configuration) and `meta-data` (instance identity):

```terminal
$ cp cloud-init-user-data.yaml user-data
$ echo "instance-id: automation-portal" > meta-data
$ genisoimage -output cloud-init.iso -volid cidata -joliet -rock user-data meta-data
```

Note:
Cloud-init runs only once per instance ID. If you need to re-apply cloud-init configuration to an existing VM, change the `instance-id` value in the `meta-data` file to a new unique value (for example, `automation-portal-2`), regenerate the ISO, and reattach it before rebooting.

4. Upload the cloud-init ISO to the same datastore:

```terminal
$ govc datastore.upload cloud-init.iso *<folder_name>*/cloud-init.iso
```

5. Create a virtual machine:
1. Right-click the cluster or host and select **New Virtual Machine** > **Create a new virtual machine**.
2. Set the following example values. Replace the name, CPU, and memory to match your environment:
| Field         | Example value                       |
| ------------- | ----------------------------------- |
| **Name**      | `automation-portal`                 |
| **Guest OS**  | Red Hat Enterprise Linux 9 (64-bit) |
| **CPU**       | 6 cores                             |
| **Memory**    | 24 GB                               |
| **Hard disk** | Remove the default disk             |
| **Network**   | Select your VM network              |

3. Click **Next** and then **Finish**.

6. Attach the VMDK disk and cloud-init ISO to the VM:
1. Edit the VM settings.
2. Click **Add New Device** > **Existing Hard Disk** and browse to the imported VMDK in the *<folder_name>* folder on the datastore.
3. Click **Add New Device** > **CD/DVD Drive**. Select **Datastore ISO File** and browse to the cloud-init ISO.
4. Select **Connect At Power On** for the CD/DVD drive.
5. Save the VM settings.

7. Power on the VM. First-boot configuration takes 2-3 minutes.

**Verification**

- Open the VM console in vSphere or SSH into the VM and confirm that all services are running:

```terminal
$ sudo ansible-portal status
```

- Access the portal URL from your browser.

