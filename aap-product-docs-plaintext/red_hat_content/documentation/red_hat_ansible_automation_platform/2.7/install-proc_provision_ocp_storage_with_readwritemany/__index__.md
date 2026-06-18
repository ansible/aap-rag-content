# Provision OpenShift Container Platform storage with `ReadWriteMany` access mode

To ensure successful installation of Ansible Automation Platform Operator, you must provision your storage type for automation hub initially to `ReadWriteMany` access mode.

## About this task

## Procedure

1.  Go to Storage> (and then)PersistentVolume.
2.  Click Create PersistentVolume.
3.  In the first step, update the `accessModes` from the default `ReadWriteOnce` to `ReadWriteMany`.   1.  See [Provisioning](https://docs.redhat.com/en/documentation/openshift_container_platform/4.10/html-single/storage/index#persistent-storage-nfs-provisioning_persistent-storage-nfs) to update the access mode. for a detailed overview.
4.  Complete the additional steps in this section to create the persistent volume claim (PVC).
