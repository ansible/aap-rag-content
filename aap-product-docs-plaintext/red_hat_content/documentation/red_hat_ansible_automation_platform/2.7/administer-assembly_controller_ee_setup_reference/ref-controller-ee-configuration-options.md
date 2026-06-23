# Execution environment setup reference
## Configuration options

When defining a custom execution environment for use with automation controller, you can specify various configuration options in the definition file used by Ansible Builder to build the EE image.

Use the following configuration YAML keys in your definition file.

The Ansible Builder 3.x execution environment definition file accepts seven top-level sections:

- [Additional_build_files](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_ee_setup_reference#ref-controller-additional-build-files "Various build steps can require additional files to be present in the build context directory. These files can be specified using the additional_build_files configuration item in the controller_settings section of the controller_configuration.yml file.")
- [Additional_build_steps](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_ee_setup_reference#ref-controller-additional-build-steps "The build steps specify custom build commands for any build phase. These commands are inserted directly into the build instruction file for the container runtime, for example, Containerfile or Dockerfile. The commands must conform to any rules required by the containerization tool.")
- [build_arg_defaults](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_ee_setup_reference#ref-controller-build-arg-defaults "This specifies the default values for build arguments as a dictionary.")
- [Dependencies](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_ee_setup_reference#ref-controller-dependencies "Specifies dependencies to install into the final image, including ansible-core, ansible-runner, Python packages, system packages, and collections.")
- [Images](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_ee_setup_reference#ref-controller-images "Use the images dictionary to define container images for your execution environment. Each key represents a unique image name, while the corresponding value is a dictionary defining that image's properties.")
* [Image verification](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_ee_setup_reference#ref-controller-image-verification "You can verify signed container images if you are using the podman container runtime.")
- [Options](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_ee_setup_reference#ref-controller-config-options "A dictionary of keywords or options that can affect the runtime functionality Ansible Builder.")
- [Version](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_controller_ee_setup_reference#ref-controller-config-version "An integer value that sets the schema version of the execution environment definition file.")




