# 14. Inventories
## 14.3. Inventory Plugins

Automation controller uses inventory plugins to dynamically generate inventory data from external sources. These plugins enable automation controller to integrate with cloud providers, virtualization platforms, and other external systems to retrieve up-to-date information about managed nodes.

Inventory updates use dynamically-generated YAML files which are parsed by their inventory plugin. In automation controller v4.4, you can provide the inventory plugin configuration directly to automation controller using the inventory source `source_vars` for the following inventory sources:

- [Amazon Web Services EC2](#proc-controller-amazon-ec2 "14.4.7.2.&nbsp;Amazon Web Services EC2")
- [Google Compute Engine](#proc-controller-inv-source-gce "14.4.7.3.&nbsp;Google Compute Engine")
- [Microsoft Azure Resource Manager](#proc-controller-azure-resource-manager "14.4.7.4.&nbsp;Microsoft Azure resource manager")
- [VMware vCenter](#proc-controller-inv-source-vm-vcenter "14.4.7.5.&nbsp;VMware vCenter")
- [VMWare ESXI](#proc-controller-inv-source-vm-esxi "14.4.7.6.&nbsp;VMware ESXi")
- [Red Hat Satellite 6](#proc-controller-inv-source-satellite "14.4.7.7.&nbsp;Red Hat Satellite 6")
- [Red Hat Lightspeed](#proc-controller-inv-source-insights "14.4.7.8.&nbsp;Red Hat Lightspeed")
- [OpenStack](#proc-controller-inv-source-openstack "14.4.7.9.&nbsp;OpenStack")
- [Red Hat Virtualization](#proc-controller-inv-source-rh-virt "14.4.7.10.&nbsp;Red Hat Virtualization")
- [Red Hat Ansible Automation Platform](#proc-controller-inv-source-aap "14.4.7.11.&nbsp;Red Hat Ansible Automation Platform")
- [Terraform State](#proc-controller-inv-source-terraform "14.4.7.12.&nbsp;Terraform State")
- [OpenShift Virtualization](#proc-controller-inv-source-open-shift-virt "14.4.7.13.&nbsp;OpenShift Virtualization")

Newly created configurations for inventory sources contain the default plugin configuration values. If you want your newly created inventory sources to match the output of a legacy source, you must apply a specific set of configuration values for that source. To ensure backward compatibility, automation controller uses "templates" for each of these sources to force the output of inventory plugins into the legacy format.

For more information about sources and their templates, see [Supported inventory plugin templates](#controller-inventory-templates "Chapter&nbsp;15.&nbsp;Supported Inventory plugin templates").

`source_vars` that contain `plugin: foo.bar.baz` as a top-level key are replaced with the fully-qualified inventory plugin name at runtime based on the `InventorySource` source. For example, if you select ec2 for the `InventorySource` then, at run time, plugin is set to `amazon.aws.aws_ec2`.

