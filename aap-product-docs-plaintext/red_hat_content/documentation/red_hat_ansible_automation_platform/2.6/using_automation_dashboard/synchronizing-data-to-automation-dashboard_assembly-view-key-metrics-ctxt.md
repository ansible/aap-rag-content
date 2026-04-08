# 1. View key usage metrics with automation dashboard
## 1.3. Integrating automation dashboard with your Ansible Automation Platform
### 1.3.1. Synchronizing data to automation dashboard




Synchronize data from your connected Ansible Automation Platform clusters to the automation dashboard to view the latest automation metrics.

**Prerequisites**

- You have installed automation dashboard.
- You have configured the `    clusters.yaml` file with your platform details.


**Procedure**

1. Identify the running automation dashboard container:


```
$ podman ps | grep automation-dashboard-web
```


1. Run the synchronization command using one of the following methods:


-  **Interactive mode:** Run `        syncdata` without arguments. You must confirm the synchronization request when prompted.


```
$ podman exec -it automation-dashboard-web /venv/bin/python manage.py syncdata
```


-  **Noninteractive mode:** Use the `        --since` and `        --until` flags to define the date range. This method bypasses the user prompt and is required for automated scripts or `        cron` jobs.


```
$ podman exec -it automation-dashboard-web /venv/bin/python manage.py syncdata --since=2024-01-01 --until=2024-06-30
```






**Verification**

1. Verify that the terminal displays the success message: `    Successfully created Sync task for Cluster &lt;cluster_url&gt;` .
1. Refresh automation dashboard in your browser to view the updated metrics.


