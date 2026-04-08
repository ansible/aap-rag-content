# Chapter 8. About the installation program inventory file




Configure your Ansible Automation Platform installation by defining hosts, groups, and deployment scenarios in the inventory file.

By using an inventory file, Ansible can manage a large number of hosts with a single command and reduce the number of command line options you have to specify.

The inventory file can be in one of many formats, depending on the inventory plugins that you have. The most common formats are `ini` and `yaml` . Inventory files listed in this document are shown in `ini` format.

The location of the inventory file depends on the installation program you used. The following table shows possible locations:

Note
The Ansible Automation Platform RPM installer was deprecated in 2.5 and will be removed in Ansible Automation Platform 2.7. The RPM installer will be supported for RHEL 9 during the lifecycle of Ansible Automation Platform 2.6 to support migrations to existing supported topologies. For more information on upgrade and migration paths, see the [Support matrix for upgrade scenarios](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/planning_your_upgrade/index#upgrade-support-matrix) .



| Installer | Location |
| --- | --- |
|  **RPM** |  `/opt/ansible-automation-platform/installer` |
|  **RPM bundle tar** |  `/ansible-automation-platform-setup-bundle-&lt;latest-version&gt;` |
|  **RPM non-bundle tar** |  `/ansible-automation-platform-setup-&lt;latest-version&gt;` |
|  **Container bundle tar** |  `/ansible-automation-platform-containerized-setup-bundle-&lt;latest-version&gt;` |
|  **Container non-bundle tar** |  `/ansible-automation-platform-containerized-setup-&lt;latest-version&gt;` |


You can verify the hosts in your inventory by using the command:

```
ansible all -i &lt;path-to-inventory-file. --list-hosts
```

**Example inventory file**

```
[automationcontroller]
controller.example.com


[automationhub]
automationhub.example.com

[automationedacontroller]
automationedacontroller.example.com

[automationgateway]
gateway.example.com

[database]
data.example.com

[all:vars]
admin_password='&lt;password&gt;'

pg_host=''
pg_port=''

pg_database='awx'
pg_username='awx'
pg_password='&lt;password&gt;'

registry_url='registry.redhat.io'
registry_username='&lt;registry username&gt;'
registry_password='&lt;registry password&gt;'

automationgateway_admin_password=""
automationgateway_pg_host=""
automationgateway_pg_database=""
automationgateway_pg_username=""
automationgateway_pg_password=""
```

The first part of the inventory file specifies the hosts or groups that Ansible can work with.

For more information on `registry_username` and `registry_password` , see [Setting registry_username and registry_password](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/preparing-containerized-installation#proc-set-registry-username-password) .

Platform gateway is the service that handles authentication and authorization for the Ansible Automation Platform. It provides a single entry into the Ansible Automation Platform and serves the platform user interface so you can authenticate and access all of the Ansible Automation Platform services from a single location.

