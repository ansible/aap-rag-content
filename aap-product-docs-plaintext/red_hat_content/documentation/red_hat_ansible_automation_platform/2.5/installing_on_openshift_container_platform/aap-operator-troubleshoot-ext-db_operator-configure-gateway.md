# 3. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 3.1. Configuring platform gateway on Red Hat OpenShift Container Platform web console
### 3.1.2. Troubleshooting an external database with an unexpected DataStyle set




When upgrading the Ansible Automation Platform Operator you may encounter an error like the following:

```
NotImplementedError: can't parse timestamptz with DateStyle 'Redwood, SHOW_TIME': '18-MAY-23 20:33:55.765755 +00:00'
```

Errors like this occur when you have an external database with an unexpected DateStyle set. You can refer to the following steps to resolve this issue.

**Procedure**

1. Edit the `    /var/lib/pgsql/data/postgres.conf` file on the database server:


```
# vi /var/lib/pgsql/data/postgres.conf
```


1. Find and comment out the line:


```
#datestyle = 'Redwood, SHOW_TIME'
```


1. Add the following setting immediately below the newly-commented line:


```
datestyle = 'iso, mdy'
```


1. Save and close the `    postgres.conf` file.
1. Reload the database configuration:


```
# systemctl reload postgresql
```

Note
Running this command does not disrupt database operations.






