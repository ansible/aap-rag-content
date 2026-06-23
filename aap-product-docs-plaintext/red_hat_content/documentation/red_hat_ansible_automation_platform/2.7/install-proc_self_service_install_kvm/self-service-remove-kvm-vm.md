# Install Ansible automation portal on RHEL with KVM
## Remove the VM

Delete the VM and its storage after an evaluation.

### About this task

To delete the VM and its storage after an evaluation, run the following commands.

### Procedure

Destroy the VM, remove its definition and storage, and clean up the working directory.

```terminal
$ sudo virsh destroy "$VM_NAME"
$ sudo virsh undefine "$VM_NAME" --remove-all-storage
$ rm -rf "$WORK_DIR"
```
