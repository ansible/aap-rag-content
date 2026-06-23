# Generate dynamic data from external sources with inventory plugins

Automation controller uses inventory plugins to dynamically generate inventory data from external sources. These plugins enable automation controller to integrate with cloud providers, virtualization platforms, and other external systems to retrieve up-to-date information about managed nodes.

Inventory updates use dynamically-generated YAML files which are parsed by their inventory plugin. In automation controller, you can provide the inventory plugin configuration directly to automation controller using the inventory source `source_vars` for the following inventory sources:

-  [Amazon Web Services EC2](/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-assembly_ag_controller_troubleshooting#controller-ec2-vpc-instances "By default, automation controller only shows instances in a VPC that have an Elastic IP (EIP) associated with them.")
-  [Google Compute Engine](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-gce "Learn how to configure a Google-sourced inventory:")
-  [Microsoft Azure Resource Manager](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-azure-resource-manager "Use the following procedure to configure an Microsoft Azure Resource Manager-sourced inventory.")
-  [VMware vCenter](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-vm-vcenter "You can configure automation controller to synchronize inventory from a VMware vCenter server. You can manage virtual machines as part of your automation workflows.")
-  [VMWare ESXI](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-vm-esxi "Learn how to configure a VMWare ESXi sourced inventory.")
-  [Red Hat Satellite 6](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-satellite "automation controller can integrate with Red Hat Satellite 6 as a dynamic inventory source.")
-  Red Hat Lightspeed
-  [OpenStack](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-openstack "You can create an inventory source that uses the OpenStack inventory plugin to dynamically generate inventory from your OpenStack cloud.")
-  [Red Hat Virtualization](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-rh-virt "Learn how to configure a Red Hat virtualization-sourced inventory.")
-  [Red Hat Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-aap "An inventory that is sourced from Red Hat Ansible Automation Platform uses the Red Hat Ansible Automation Platform inventory plugin to gather inventory data from the Red Hat Ansible Automation Platform platform.")
-  [Terraform State](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-terraform "Use the following procedure to create a Terraform State inventory source.")
-  [OpenShift Virtualization](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-open-shift-virt "Learn how to add an OpenShift Virtualization inventory source to an existing inventory.")


Newly created configurations for inventory sources contain the default plugin configuration values. If you want your newly created inventory sources to match the output of a legacy source, you must apply a specific set of configuration values for that source. To ensure backward compatibility, automation controller uses "templates" for each of these sources to force the output of inventory plugins into the legacy format.

For more information about sources and their templates, see [Supported inventory plugin templates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-controller_inventory_templates#controller-inventory-templates "After upgrade to 4.x, existing configurations are migrated to the new format that produces an inventory output compatible with earlier versions. Use the following templates to aid in migrating your inventories to the new style inventory plugin output.").

`source_vars` that contain `plugin: xxx.yyy.zzz` as a top-level key are replaced with the fully-qualified inventory plugin name at runtime based on the `InventorySource` source.

For example, if you select `ec2` for the `InventorySource` then, at run time, the plugin is set to `amazon.aws.aws_ec2`.

