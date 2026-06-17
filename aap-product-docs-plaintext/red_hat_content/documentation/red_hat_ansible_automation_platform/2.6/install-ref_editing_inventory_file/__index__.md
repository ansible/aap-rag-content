# Edit the inventory file

You can use the Ansible Automation Platform installer inventory file to specify your installation scenario.

## For an RPM installation

*Procedure*

**RPM installed package**

```
$ cd /opt/ansible-automation-platform/installer/
```
**Bundled installer**

```
$ cd ansible-automation-platform-setup-bundle-<latest-version>
```
**Online installer**

```
$ cd ansible-automation-platform-setup-<latest-version>
```

## For online installations

1. Open the `inventory` file with a text editor.

2. Edit the `inventory` file parameters to specify your installation scenario. For containerized installation, see [Configuring the inventory file](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-ref_configuring_inventory_file#configuring-inventory-file "You can control the installation of Ansible Automation Platform with inventory files. Inventory files define the host details, certificate details, and component-specific settings needed to customize the installation.")

You can use one of the supported Installation scenario examples as the basis for your `inventory` file.
