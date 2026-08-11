# Back up and restore your containerized deployment
## Skip database restore when using an external database
### About this task

You must set `postgresql_skip_data` to `true` if no database dump file exists in the backup archive, for example if you used `postgresql_skip_data` during backup. If the restore playbook cannot find a database dump file and `postgresql_skip_data` is not set, the playbook fails.

Important:

Restore your external PostgreSQL database before running the restore playbook. The restore playbook starts all Ansible Automation Platform services immediately after restoring configuration files. If the database is not yet restored when services start, the services cannot connect to a valid database.

### Procedure

1.  Restore your PostgreSQL database using your external database provider's tools or a third-party restore solution.
2.  Add the `postgresql_skip_data` variable to your inventory file:


```
postgresql_skip_data=true
```

3.  Run the `restore` playbook:


```
$ ansible-playbook -i <path_to_inventory>
ansible.containerized_installer.restore
```

The restore playbook restores configuration files and data files and skips database restore operations.

