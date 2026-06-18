+++
template = "docs/aem-title.html"
title = "Upgrade automation dashboard - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-proc_upgrading_automation_dashboard"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-upgrade_additional_services_for_ansible_automation_platform/", "Upgrade additional services for Ansible Automation Platform"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-proc_upgrading_automation_dashboard/aem-page/upgrade-proc_upgrading_automation_dashboard.html"
last_crumb = "Upgrade automation dashboard"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Upgrade automation dashboard"
oversized = "false"
page_slug = "upgrade-proc_upgrading_automation_dashboard"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-proc_upgrading_automation_dashboard"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-proc_upgrading_automation_dashboard/toc/toc.json"
type = "aem-page"
+++

# Upgrade automation dashboard

This procedure applies when upgrading from automation dashboard versions before 0.1 (which did not include Redis) to the current version. This process involves running the installation program and updating your cluster configuration with new authentication requirements.

## About this task

Note:

For more information about recent updates to automation dashboard, see [What’s new: Updates for automation dashboard](https://access.redhat.com/articles/7136888).

## Procedure

1.  Download the latest installation bundle from access.redhat.com. Navigate to Downloads > Red Hat Ansible Automation Platform Product Software.
2.  Extract the bundle to a new directory.
3.  Copy the `inventory` file from your previous installation directory to the new directory.
4.  Edit the `inventory` file to include the mandatory Redis configuration. You must add a `[redis]` group and define the `redis_mode` variable:
  
  Note:
      The inventory file lines prefixed with + must be added when upgrading your automation dashboard.

```ini
[database]
host.example.com ansible_connection=local

    +[redis]
+host.example.com ansible_connection=local
+
 [all:vars]
+redis_mode=standalone
+
 postgresql_admin_username=postgres
 postgresql_admin_password=TODO
 # registry_username=
```

5.  Run the installation playbook from the new directory:
  

```bash
ansible-galaxy collection install -r requirements.yml
ansible-playbook -i inventory ansible.containerized_installer.dashboard_install --ask-become-pass
```

6.  Update your `clusters.yaml` file. You must add the `refresh_token`, `client_id`, and `client_secret` variables to your existing cluster configurations. Note:
      For instructions on obtaining these values, see [Integrating automation dashboard with your Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_view_key_metrics#proc-integrating-automation-dashboard "Integrate your Ansible Automation Platform instances into the automation dashboard configuration to collect and visualise data and gain insights into your automation.").

7.  Apply the updated configuration to the dashboard. You must copy the configuration file to the container's `/tmp/` directory:
  

```bash
podman cp clusters.yaml automation-dashboard-web:/tmp/
podman exec -it automation-dashboard-web /venv/bin/python manage.py setclusters /tmp/clusters.yaml
```

## Results

1. Retrieve the current cluster configuration:

```bash
podman exec -it automation-dashboard-web /venv/bin/python ./manage.py getclusters --decrypt
```

2. Verify that the output displays the content from your `clusters.yaml` file, including the `access_token`, `refresh_token`, `client_id`, and `client_secret` fields.

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
