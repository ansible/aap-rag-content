# Back up and restore an RPM deployment from RHEL 8 to new RHEL 9 hosts
## Before you begin

Note:

If you need to back up or restore your deployment outside of a migration context, see [Back up and restore your RPM deployment](/documentation/en-us/red_hat_ansible_automation_platform/2.7/ref_controller_backup_restore_considerations "Consider the following points when you back up and restore your system:").

- Your source deployment is the latest release of Ansible Automation Platform RPM 2.4 on RHEL 8.
- You have access to the RPM 2.4 installation program directory on the RHEL 8 source host.
- Sufficient disk space is available on the RHEL 8 source host to hold the backup archive. Archive size depends on the size of your component databases and, if automation hub is installed, the size of the Pulp data directory (`/var/lib/pulp/`).
- RHEL 9 hosts are provisioned and meet RPM 2.4 system requirements.
- The RPM 2.4 installation program tar file is downloaded and available on the RHEL 9 host.
- Network connectivity or a file transfer path is available between the RHEL 8 source host and the RHEL 9 target host.

## Procedure

1.  Navigate to the RPM 2.4 installation program directory on the RHEL 8 source host.
2.  Run the backup command:


```
$ ./setup.sh -b
```

When the backup completes, the archive `automation-platform-backup-latest.tar.gz` appears in the installation program directory. If the command exits with an error, resolve the reported error before transferring any files to the RHEL 9 host.

3.  Extract the RPM 2.4 installation program tar file on the RHEL 9 host.
4.  Configure the inventory file for your RHEL 9 hosts and install Ansible Automation Platform 2.4:


```
$ ./setup.sh
```

The restore requires Ansible Automation Platform to be installed on the target hosts before it can run.

5.  Copy the backup archive to the RPM 2.4 installation program directory on the RHEL 9 host:


```
$ scp automation-platform-backup-latest.tar.gz <rhel9-host>:<path-to-rpm-installer>/
```

6.  From the RPM 2.4 installation program directory on the RHEL 9 host, run the restore command:


```
$ ./setup.sh -r
```

If errors occur, resolve them before proceeding.

