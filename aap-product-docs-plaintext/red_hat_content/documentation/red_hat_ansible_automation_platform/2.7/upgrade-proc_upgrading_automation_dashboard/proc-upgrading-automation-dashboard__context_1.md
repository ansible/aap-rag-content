# Upgrade automation dashboard
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

