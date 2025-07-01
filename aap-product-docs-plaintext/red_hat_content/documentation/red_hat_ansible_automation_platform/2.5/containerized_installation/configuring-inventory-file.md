# 2. Ansible Automation Platform containerized installation
## 2.6. Configuring the inventory file




You can control the installation of Ansible Automation Platform with inventory files. Inventory files define the information needed to customize the installation. For example, host details, certificate details, and various component-specific settings.

Example inventory files are available in this document that you can copy and change to quickly get started.

Additionally, growth topology and enterprise topology inventory files are available in the following locations:

- In the downloaded installation program package:


- The default inventory file, named `        inventory` , is for the enterprise topology pattern.
- To deploy the growth topology (all-in-one) pattern, you need to copy over or use the `        inventory-growth` file instead.

- In [Container topologies](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models/container-topologies) in _Tested deployment models_ .


To use the example inventory files, replace the `&lt; &gt;` placeholders with your specific variables, and update the host names.

Refer to the `README.md` file in the installation directory or [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars) for more information about optional and required variables.

