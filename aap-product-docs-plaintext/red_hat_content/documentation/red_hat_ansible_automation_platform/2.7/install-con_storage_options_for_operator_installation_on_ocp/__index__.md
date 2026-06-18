# Storage options for automation hub

Automation hub requires `ReadWriteMany` file-based storage, Azure Blob storage, or Amazon S3 storage for operation so that multiple pods can access shared content, such as collections.

The process for configuring object storage on the `AutomationHub` CR is similar for Amazon S3 and Azure Blob Storage.

If you are using file-based storage and your installation scenario includes automation hub, ensure that the storage option for Ansible Automation Platform Operator is set to `ReadWriteMany`. `ReadWriteMany` is the default storage option.

In addition, OpenShift Data Foundation provides a `ReadWriteMany` or S3 implementation. Also, you can set up NFS storage configuration to support `ReadWriteMany`. This, however, introduces the NFS server as a potential, single point of failure.
