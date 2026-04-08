# 5. Advanced containerized deployment
## 5.3. Configuring storage for automation hub
### 5.3.3. Configuring Network File System (NFS) storage for automation hub




NFS is a type of shared storage that is supported in containerized installations. Shared storage is required when installing more than one instance of automation hub with a `file` storage backend. When installing a single instance of the automation hub, shared storage is optional.

**Procedure**

1. To configure shared storage for automation hub, set the `    hub_shared_data_path` variable in your inventory file:


```
hub_shared_data_path=&lt;path_to_nfs_share&gt;
```

The value must match the format `    host:dir` , for example `    nfs-server.example.com:/exports/hub` .


1. (Optional) To change the mount options for your NFS share, use the `    hub_shared_data_mount_opts` variable. The default value is `    rw,sync,hard` .


