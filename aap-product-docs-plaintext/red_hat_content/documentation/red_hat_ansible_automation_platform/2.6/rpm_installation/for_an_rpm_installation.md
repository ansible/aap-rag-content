# 4. Installing Red Hat Ansible Automation Platform
## 4.2. Editing the Red Hat Ansible Automation Platform installer inventory file
### 4.2.1. For an RPM installation




_Procedure_

**RPM installed package**

```
$ cd /opt/ansible-automation-platform/installer/
```

**Bundled installer**

```
$ cd ansible-automation-platform-setup-bundle-&lt;latest-version&gt;
```

**Online installer**

```
$ cd ansible-automation-platform-setup-&lt;latest-version&gt;
```

1. Open the `    inventory` file with a text editor.
1. Edit the `    inventory` file parameters to specify your installation scenario.

For containerized installation, see [Configuring the inventory file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/preparing-containerized-installation#configuring-inventory-file) You can use one of the supported [Installation scenario examples](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/rpm_installation/index#con-install-scenario-examples) as the basis for your `    inventory` file.




**Additional resources**

-  [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars)


