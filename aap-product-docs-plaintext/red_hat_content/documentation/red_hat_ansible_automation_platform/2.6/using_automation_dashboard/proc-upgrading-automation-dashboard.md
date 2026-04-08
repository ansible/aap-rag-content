# 1. View key usage metrics with automation dashboard
## 1.4. Upgrading automation dashboard




Upgrade your automation dashboard installation to the latest version. This process involves running the installation program and updating your cluster configuration with new authentication requirements.

Note
For more information about recent updates to automation dashboard, see [What’s new: Upgrades for automation dashboard](https://access.redhat.com/articles/7136888) .



**Procedure**

1. Download the latest installation bundle from access.redhat.com. Navigate to Downloads > Red Hat Ansible Automation Platform Product Software.
1. Extract the bundle to a new directory.
1. Copy the `    inventory` file from your previous installation directory to the new directory.
1. Edit the `    inventory` file to include the mandatory Redis configuration. You must add a `    [redis]` group and define the `    redis_mode` variable:

Note
The inventory file lines prefixed with + must be added when upgrading your automation dashboard.




```
[database]    host.example.com ansible_connection=local        +[redis]    +host.example.com ansible_connection=local    +     [all:vars]    +redis_mode=standalone    +     postgresql_admin_username=postgres     postgresql_admin_password=TODO     # registry_username=
```


1. Run the installation playbook from the new directory:


```
ansible-galaxy collection install -r requirements.yml    ansible-playbook -i inventory ansible.containerized_installer.dashboard_install --ask-become-pass
```


1. Update your `    clusters.yaml` file. You must add the `    refresh_token` , `    client_id` , and `    client_secret` variables to your existing cluster configurations.

Note
For instructions on obtaining these values, see [Integrating automation dashboard with your Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_dashboard/index#proc-integrating-automation-dashboard) .




1. Apply the updated configuration to the dashboard. You must copy the configuration file to the container’s `    /tmp/` directory:


```
podman cp clusters.yaml automation-dashboard-web:/tmp/    podman exec -it automation-dashboard-web /venv/bin/python manage.py setclusters /tmp/clusters.yaml
```




**Verification**

1. Retrieve the current cluster configuration:


```
podman exec -it automation-dashboard-web /venv/bin/python ./manage.py getclusters --decrypt
```


1. Verify that the output displays the content from your `    clusters.yaml` file, including the `    access_token` , `    refresh_token` , `    client_id` , and `    client_secret` fields.


