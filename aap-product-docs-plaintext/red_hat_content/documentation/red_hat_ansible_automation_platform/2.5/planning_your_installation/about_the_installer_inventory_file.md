# Chapter 8. About the installer inventory file




Red Hat Ansible Automation Platform works against a list of managed nodes or hosts in your infrastructure that are logically organized, using an inventory file. You can use the Red Hat Ansible Automation Platform installer inventory file to specify your installation scenario and describe host deployments to Ansible. By using an inventory file, Ansible can manage a large number of hosts with a single command. Inventories also help you use Ansible more efficiently by reducing the number of command line options you have to specify.

The inventory file can be in one of many formats, depending on the inventory plugins that you have. The most common formats are `INI` and `YAML` . Inventory files listed in this document are shown in INI format.

The location of the inventory file depends on the installer you used. The following table shows possible locations:

| Installer | Location |
| --- | --- |
|  **RPM** |  `/opt/ansible-automation-platform/installer` |
|  **RPM bundle tar** |  `/ansible-automation-platform-setup-bundle-&lt;latest-version&gt;` |
|  **RPM non-bundle tar** |  `/ansible-automation-platform-setup-&lt;latest-version&gt;` |
|  **Container bundle tar** |  `/ansible-automation-platform-containerized-setup-bundle-&lt;latest-version&gt;` |
|  **Container non-bundle tar** |  `/ansible-automation-platform-containerized-setup-&lt;latest-version&gt;` |


You can verify the hosts in your inventory using the command:

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

For more information on `registry_username` and `registry_password` , see [Setting registry_username and registry_password](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_installation/index#proc-set-registry-username-password) .

Platform gateway is the service that handles authentication and authorization for the Ansible Automation Platform. It provides a single entry into the Ansible Automation Platform and serves the platform user interface so you can authenticate and access all of the Ansible Automation Platform services from a single location.

