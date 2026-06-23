# Upgrade automation dashboard
## Troubleshoot synchronization failures

If new jobs from Ansible Automation Platform do not synchronize to the automation dashboard after an upgrade, an interrupted synchronization job might be blocking the process. This occurs if the automation dashboard service stops or restarts while a synchronization task is active.

### Before you begin

- You have ssh access to the host machine.
- You have access to the PostgreSQL database, including the database user password defined in your inventory file (variable `dashboard_pg_password`).

### About this task

To resolve this issue, you must manually remove the stuck jobs from the database.

### Procedure

1.  Connect to the automation dashboard database. You must replace `<password>` with your configured `dashboard_pg_password`. Replace 127.0.0.1 with database server address if external database is used.

```bash
POSTGRES_PASSWORD=<password> psql -h 127.0.0.1 -p 5432 -U aapdashboard -d aapdashboard
```

2.  Identify jobs that are in a pending or running state:


```sql
SELECT * FROM scheduler_syncjob WHERE status IN ('pending','waiting','running');
```

3.  Wait approximately one minute and run the command again. If the same job IDs appear in the output, these jobs are stuck.
4.  Delete the stuck jobs using their ID. Replace `<id>` with the ID returned in the previous step (for example, `20, 21`):


```sql
DELETE from scheduler_syncjob WHERE id IN (<id>);
```

### Results

- Refresh the automation dashboard to confirm that synchronization has resumed.
