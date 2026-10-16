# Configure storage for automation hub
## Configure Network File System (NFS) storage for automation hub
### About this task

Note:

The containerized installer automatically handles NFS mounting when you configure the `hub_shared_data_path` and `hub_shared_data_mount_opts` variables in your inventory file. Manual NFS configuration on automation hub nodes is not required.

Unlike Ansible Automation Platform RPM-based installations, you do not need to:

- Create /var/lib/pulp directories on automation hub nodes
- Add NFS mount entries to /etc/fstab
- Manually mount the NFS share before running the installer
- Configure SELinux contexts for pulp storage paths

The installer manages all NFS mount operations automatically based on your inventory file settings.

### Procedure

1. To configure shared storage for automation hub, set the `hub_shared_data_path` variable in your inventory file:


```yaml
hub_shared_data_path=<path_to_nfs_share>
```

The value must match the format `host:dir`, for example `nfs-server.example.com:/exports/hub`.

2. (Optional) To change the mount options for your NFS share, use the `hub_shared_data_mount_opts` variable. The default value is `rw,sync,hard`.
