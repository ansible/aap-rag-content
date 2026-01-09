# 4. Preparing the containerized Ansible Automation Platform installation
## 4.6. Configuring the inventory file




You can control the installation of Ansible Automation Platform with inventory files. Inventory files define the host details, certificate details, and component-specific settings needed to customize the installation.

Example inventory files are available in this document that you can copy and change to get started.

Important
The inventory file requirements differ based on your installation type:

-  **Online installation** : Requires the `    registry_username` and `    registry_password` variables to authenticate and pull container images from Red Hat registries during installation.
-  **Disconnected (bundled) installation** : Does not require `    registry_username` or `    registry_password` because all container images are pre-packaged in the bundle. Instead, requires the `    bundle_install=true` and `    bundle_dir` variables.


The following inventory file examples are for online installations. For disconnected installation inventory requirements, see [Performing a disconnected installation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/aap-containerized-disconnected-installation#perform-disconnected-installation) .



Additionally, growth topology and enterprise topology inventory files are available in the following locations:

- In the downloaded installation program package:


- The default inventory file, named `        inventory` , is for the enterprise topology pattern.
- To deploy the growth topology (all-in-one) pattern, use the `        inventory-growth` file instead.

- In [Container topologies](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/tested_deployment_models/container-topologies) in _Tested deployment models_ .


To use the example inventory files, replace the `&lt; &gt;` placeholders with your specific variables, and update the host names.

Refer to the `README.md` file in the installation directory or [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/appendix-inventory-files-vars) for more information about optional and required variables.

