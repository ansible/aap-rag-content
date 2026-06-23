# Configure the inventory file

You can control the installation of Ansible Automation Platform with inventory files. Inventory files define the host details, certificate details, and component-specific settings needed to customize the installation.

Example inventory files are available in this document that you can copy and change to get started.

Important:

The inventory file requirements differ based on your installation type:

- **Online installation**: Requires the `registry_username` and `registry_password` variables to authenticate and pull container images from Red Hat registries during installation.
- **Disconnected (bundled) installation**: Does not require `registry_username` or `registry_password` because all container images are pre-packaged in the bundle. Instead, requires the `bundle_install=true` and `bundle_dir` variables.


The following inventory file examples are for online installations. For disconnected installation inventory requirements, see [Perform a disconnected installation](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_aap_containerized_disconnected_installation#perform-disconnected-installation "A disconnected installation installs containerized Ansible Automation Platform without requiring network access to external registries.").

Important:

The `[automationmetrics]` inventory group is required in Ansible Automation Platform 2.7 when `[automationcontroller]` is present. The installer will fail preflight checks if this group is missing.

Metrics service must be deployed on a dedicated host in containerized deployments.

Additionally, growth topology and enterprise topology inventory files are available in the following locations:

- In the downloaded installation program package:
* The default inventory file, named `inventory`, is for the enterprise topology pattern.
* To deploy the growth topology (all-in-one) pattern, use the `inventory-growth` file instead.
- In [Container growth topology](/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-ref_cont_a_env_a "The container-based growth topology provides a smaller footprint deployment without redundancy for organizations getting started with Ansible Automation Platform.") and [Container enterprise topology](/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-ref_cont_b_env_a "The container-based enterprise topology provides redundancy and higher compute for large volumes of automation.") in *Tested deployment models*.


To use the example inventory files, replace the `< >` placeholders with your specific variables, and update the host names.

Refer to the `README.md` file in the installation directory or [Inventory file variables](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_inventory_file_vars "The following tables contain information about the variables used in Ansible Automation Platform’s installation inventory files.") for more information about optional and required variables.

Important:

Metrics service is a required component in Ansible Automation Platform 2.7. When you include the `[automationcontroller]` inventory group, you must also include the `[automationmetrics]` inventory group. The installer will fail if `[automationcontroller]` is present without `[automationmetrics]`.

In containerized deployments, metrics service must be deployed on a dedicated host. Do not co-locate metrics service with other Ansible Automation Platform components.

