# 3. Installing Red Hat Ansible Automation Platform
## 3.6. Backing up your Ansible Automation Platform instance




Back up an existing Ansible Automation Platform instance by running the `.setup.sh` script with the `backup_dest` flag, which saves the content and configuration of your current environment. Use the compression flags `use_archive_compression` and `use_db_compression` to compress the backup artifacts before they are sent to the host running the backup operation.

**Procedure**

1. Navigate to your Ansible Automation Platform installation directory.
1. Run the `    ./setup.sh` script following the example below:


```
$ ./setup.sh -e 'backup_dest=/ansible/mybackup' -e    'use_archive_compression=true' 'use_db_compression=true' @credentials.yml -b
```

Where:


-  `        backup_dest` : Specifies a directory to save your backup to.
-  `        use_archive_compression=true` and `        use_db_compression=true` : Compresses the backup artifacts before they are sent to the host running the backup operation.

You can use the following variables to customize the compression:


- For global control of compression for filesystem related backup files: `            use_archive_compression=true`
- For component-level control of compression for filesystem related backup files: `            &lt;componentName&gt;_use_archive_compression`

For example:


-  `                automationgateway_use_archive_compression=true`
-  `                automationcontroller_use_archive_compression=true`
-  `                automationhub_use_archive_compression=true`
-  `                automationedacontroller_use_archive_compression=true`

- For global control of compression for database related backup files: `            use_db_compression=true`
- For component-level control of compression for database related backup files: `            &lt;componentName&gt;_use_db_compression=true`

For example:


-  `                automationgateway_use_db_compression=true`
-  `                automationcontroller_use_db_compression=true`
-  `                automationhub_use_db_compression=true`
-  `                automationedacontroller_use_db_compression=true`

After a successful backup, a backup file is created at `                /ansible/mybackup/automation-platform-backup-&lt;date/time&gt;.tar.gz` .







