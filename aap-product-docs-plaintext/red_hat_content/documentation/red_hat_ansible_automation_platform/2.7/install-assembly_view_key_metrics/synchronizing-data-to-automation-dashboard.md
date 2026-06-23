# Install automation dashboard to calculate savings (RHEL only)
## Install automation dashboard
### Synchronize data to automation dashboard

Synchronize data from your connected Ansible Automation Platform clusters to the automation dashboard to view the latest automation metrics.

#### Before you begin

- You have installed automation dashboard.
- You have configured the `clusters.yaml` file with your platform details.

#### Procedure

1.  Identify the running automation dashboard container:


```terminal
$ podman ps | grep automation-dashboard-web
```

2.  Run the synchronization command using one of the following methods:


- **Interactive mode:** Run `syncdata` without arguments. You must confirm the synchronization request when prompted.

```terminal
$ podman exec -it automation-dashboard-web /venv/bin/python manage.py syncdata
```

- **Noninteractive mode:** Use the `--since` and `--until` flags to define the date range. This method bypasses the user prompt and is required for automated scripts or `cron` jobs.

```terminal
$ podman exec -it automation-dashboard-web /venv/bin/python manage.py syncdata --since=2024-01-01 --until=2024-06-30
```

#### Results

1. Verify that the terminal displays the success message: `Successfully created Sync task for Cluster <cluster_url>`.
2. Refresh automation dashboard in your browser to view the updated metrics.

