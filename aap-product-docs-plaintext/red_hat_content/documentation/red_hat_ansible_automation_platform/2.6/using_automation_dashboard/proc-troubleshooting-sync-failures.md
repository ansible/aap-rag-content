# 1. View key usage metrics with automation dashboard
## 1.4. Upgrading automation dashboard
### 1.4.1. Troubleshooting synchronization failures




If new jobs from Ansible Automation Platform do not synchronize to the automation dashboard after an upgrade, an interrupted synchronization job might be blocking the process. This occurs if the automation dashboard service stops or restarts while a synchronization task is active.

To resolve this issue, you must manually remove the stuck jobs from the database.

**Prerequisites**

- You have ssh access to the host machine.
- You have access to the PostgreSQL database, including the database user password defined in your inventory file (variable `    dashboard_pg_password` ).


**Procedure**

1. Connect to the automation dashboard database. You must replace `    &lt;password&gt;` with your configured `    dashboard_pg_password` . Replace 127.0.0.1 with database server address if external database is used.


```
POSTGRES_PASSWORD=&lt;password&gt; psql -h 127.0.0.1 -p 5432 -U aapdashboard -d aapdashboard
```


1. Identify jobs that are in a pending or running state:


```
SELECT * FROM scheduler_syncjob WHERE status IN ('pending','waiting','running');
```


1. Wait approximately one minute and run the command again. If the same job IDs appear in the output, these jobs are stuck.
1. Delete the stuck jobs using their ID. Replace `    &lt;id&gt;` with the ID returned in the previous step (for example, `    20, 21` ):


```
DELETE from scheduler_syncjob WHERE id IN (&lt;id&gt;);
```




**Verification**

- Refresh the automation dashboard to confirm that synchronization has resumed.


