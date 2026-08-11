# Back up the platform using automation installer

Run the setup script to create a verified archive of your platform database, configurations, and secrets. This ensures your instance is captured in a compatible format for reliable restoration during a system failure or migration.

## Procedure

1.  Navigate to your Ansible Automation Platform installation directory.
2.  Run the `./setup.sh` script as in the following example:


```
$ ./setup.sh -e 'backup_dest=/ansible/mybackup' -e
'use_archive_compression=true' 'use_db_compression=true @credentials.yml -b
```

Where:
- `backup_dest`: Specifies a directory to save your backup to.
- `backup_dir`: Specifies the directory used on the host staging backup files before they are transferred to `backup_dest` locally.
- `use_archive_compression=true` and `use_db_compression=true`: Compresses the backup artifacts before they are sent to the host running the backup operation.
You can use the following variables to customize the compression:
- `use_archive_compression=true`: For global control of compression for filesystem related backup files.
- `<componentName>_use_archive_compression`: For component-level control of compression for filesystem related backup files.
- `use_db_compression=true`: For global control of compression for database related backup files.
- `<componentName>_use_db_compression=true`: For component-level control of compression for database related backup files.

