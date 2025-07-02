# 8. About the installer inventory file
## 8.1. Guidelines for hosts and groups




**Databases**

- When using an external database, ensure the `    [database]` sections of your inventory file are properly set up.
- To improve performance, do not colocate the database and the automation controller on the same server.


Important
When using an external database with Ansible Automation Platform, you must create and maintain that database. Ensure that you clear your external database when uninstalling the Ansible Automation Platform.



**Automation hub**

- If there is an `    [automationhub]` group, you must include the variables `    automationhub_pg_host` and `    automationhub_pg_port` .
- Add Ansible automation hub information in the `    [automationhub]` group.
- Do not install Ansible automation hub and automation controller on the same node.
- Provide a reachable IP address or fully qualified domain name (FQDN) for the `    [automationhub]` and `    [automationcontroller]` hosts to ensure that users can synchronize and install content from Ansible automation hub and automation controller from a different node.

The FQDN must not contain the `    _` symbol, as it will not be processed correctly in Skopeo. You may use the `    -` symbol, as long as it is not at the start or the end of the host name.

Do not use `    localhost` .




**Private automation hub**

- Do not install private automation hub and automation controller on the same node.
- You can use the same PostgreSQL (database) instance, but they must use a different (database) name.
- If you install private automation hub from an internal address, and have a certificate which only encompasses the external address, it can result in an installation you cannot use as a container registry without certificate issues.


Important
You must separate the installation of automation controller and Ansible automation hub because the `[database]` group does not distinguish between the two if both are installed at the same time.

If you use one value in `[database]` and both automation controller and Ansible automation hub define it, they would use the same database.



**Automation controller**

- Automation controller does not configure replication or failover for the database that it uses.
- Automation controller works with any replication that you have.


**Event-Driven Ansible controller**

- Event-Driven Ansible controller must be installed on a separate server and cannot be installed on the same host as automation hub and automation controller.


**Platform gateway**

- The platform gateway is the service that handles authentication and authorization for Ansible Automation Platform. It provides a single entry into the platform and serves the platform’s user interface.


**Clustered installations**

- When upgrading an existing cluster, you can also reconfigure your cluster to omit existing instances or instance groups. Omitting the instance or the instance group from the inventory file is not enough to remove them from the cluster. In addition to omitting instances or instance groups from the inventory file, you must also deprovision instances or instance groups before starting the upgrade. For more information, see [Deprovisioning nodes or groups](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/planning_your_installation/index#ref-deprovisioning) . Otherwise, omitted instances or instance groups continue to communicate with the cluster, which can cause issues with automation controller services during the upgrade.
- If you are creating a clustered installation setup, you must replace `    [localhost]` with the hostname or IP address of all instances. Installers for automation controller and automation hub do not accept `    [localhost]` All nodes and instances must be able to reach any others by using this hostname or address. You cannot use the localhost `    ansible_connection=local` on one of the nodes. Use the same format for the host names of all the nodes.

Therefore, this does not work:


```
[automationhub]    localhost ansible_connection=local    hostA    hostB.example.com    172.27.0.4
```

Instead, use these formats:


```
[automationhub]    hostA    hostB    hostC
```

or


```
[automationhub]    hostA.example.com    hostB.example.com    hostC.example.com
```




