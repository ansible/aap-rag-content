# 14. Inventories
## 14.3. Inventory Plugins




Automation controller uses inventory plugins to dynamically generate inventory data from external sources. These plugins enable automation controller to integrate with cloud providers, virtualization platforms, and other external systems to retrieve up-to-date information about managed nodes.

Inventory updates use dynamically-generated YAML files which are parsed by their inventory plugin. In automation controller v4.4, you can provide the inventory plugin configuration directly to automation controller using the inventory source `source_vars` for the following inventory sources:

-  [Amazon Web Services EC2](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-controller-amazon-ec2)
-  [Google Compute Engine](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-controller-inv-source-gce)
-  [Microsoft Azure Resource Manager](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-controller-azure-resource-manager)
-  [VMware vCenter](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-controller-inv-source-vm-vcenter)
-  [VMWare ESXI](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-controller-inv-source-vm-esxi)
-  [Red Hat Satellite 6](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-controller-inv-source-satellite)
-  [Red Hat Lightspeed](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-controller-inv-source-insights)
-  [OpenStack](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-controller-inv-source-openstack)
-  [Red Hat Virtualization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-controller-inv-source-rh-virt)
-  [Red Hat Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-controller-inv-source-aap)
-  [Terraform State](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-controller-inv-source-terraform)
-  [OpenShift Virtualization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#proc-controller-inv-source-open-shift-virt)


Newly created configurations for inventory sources contain the default plugin configuration values. If you want your newly created inventory sources to match the output of a legacy source, you must apply a specific set of configuration values for that source. To ensure backward compatibility, automation controller uses "templates" for each of these sources to force the output of inventory plugins into the legacy format.

For more information about sources and their templates, see [Supported inventory plugin templates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-inventory-templates) .

`source_vars` that contain `plugin: foo.bar.baz` as a top-level key are replaced with the fully-qualified inventory plugin name at runtime based on the `InventorySource` source. For example, if you select ec2 for the `InventorySource` then, at run time, plugin is set to `amazon.aws.aws_ec2` .

