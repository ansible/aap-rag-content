# Understand bootable container images

Image-based operating systems allow the operating system and its configuration and applications to be versioned, deployed, and updated as a single unit. Using an image-based operating system reduces operational risks by doing the following:

- Minimizing potential drift between what is tested and what is deployed to a large number of devices.
- Minimizing the risk of failed updates that require expensive maintenance or replacement through transactional updates and rollbacks.


The Red Hat Edge Manager focuses on image-based Linux operating systems that run bootable container images (`bootc`).

Important:

The `bootc` tool does not update package-based operating systems.

## The image building process

Create the bootable container (bootc) images you need to provision Edge Manager devices.

### Before you begin

- Podman
- Skopeo
- bootc-image-builder

### About this task

### Procedure

1.  Choose a base `bootc` operating system image, such as a Fedora, CentOS, or RHEL image.
2.  Create a container file that layers the following items onto the base `bootc` image:

- The Red Hat Edge Manager agent and configuration.
- Optional: Any drivers specific to your target deployment environment.
- Optional: Host configuration, for example, certificate authority bundles, and application workloads that are common to all deployments.

3.  Build, publish, and sign a `bootc` operating system image using `podman` and `skopeo`.
4.  Create an operating system disk image by using `bootc-image-builder`.
5.  Build, publish, and sign an operating system disk image using `skopeo`. Note:
The operating system disk image has partitions, volumes, the file system, and the initial `bootc` image. You only need to create the operating system disk image once, during provisioning. For later device updates, you only need the `bootc` operating system image, which has the files in the file system.

## Special considerations for building images

Follow these key considerations when building Red Hat Edge Manager operating system images to keep consistency and stability across your device fleet. These guidelines specify how and where to implement configuration details during the image creation process.

-  [Build-time configuration over dynamic runtime configuration](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_images#edge-manager-buildtime-runtime "Apply configuration directly to the operating system image at build time to ensure your configurations are tested, distributed, and updated together. If build-time configuration is not feasible, you can use Red Hat Edge Manager to dynamically configure devices at runtime instead.")
-  [Configuration in the `/usr` directory](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_images#edge-manager-usr-dir "Place configuration files in the /usr directory if the configuration is static and the application or service supports that configuration. By placing the configuration in the /usr directory, the configuration remains read-only and fully defined by the image.")
-  [Drop-in directories](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_images#edge-manager-drop-dir "Use drop-in directories to add, replace, or remove configuration files that the service aggregates. Do not directly edit your configuration files because it can cause deviations from the target configuration.")
-  [Operating system images with scripts](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_images#edge-manager-os-img-script "Avoid executing scripts or commands that change the file system. The bootc or the Red Hat Edge Manager can overwrite the changed files that can cause a deviation or failed integrity checks.")

## Build-time configuration over dynamic runtime configuration

Apply configuration directly to the operating system image at build time to ensure your configurations are tested, distributed, and updated together. If build-time configuration is not feasible, you can use Red Hat Edge Manager to dynamically configure devices at runtime instead.

Dynamic runtime configuration is preferable in the following cases:

- You have a configuration that is deployment or site-specific, such as a hostname or a site-specific network credential.
- You have secrets that are not secure to distribute with the image.
- You have application workloads that need to be added, updated, or deleted without reboot or they are on a faster cadence than the operating system.

## Configuration in the `/usr` directory

Place configuration files in the `/usr` directory if the configuration is static and the application or service supports that configuration. By placing the configuration in the `/usr` directory, the configuration remains read-only and fully defined by the image.

Do not place the configuration in the `/usr` directory in the following cases:

- The configuration is deployment or site-specific.
- The application or service only supports reading configuration from the `/etc` directory.
- The configuration might need to be changed at runtime.

## Drop-in directories

Use drop-in directories to add, replace, or remove configuration files that the service aggregates. Do not directly edit your configuration files because it can cause deviations from the target configuration.

Note:

You can identify drop-in directories by the `.d/` at the end of the directory name. For example, `/etc/containers/certs.d`, `/etc/cron.d`, and `/etc/NetworkManager/conf.d`.

## Operating system images with scripts

Avoid executing scripts or commands that change the file system. The `bootc` or the Red Hat Edge Manager can overwrite the changed files that can cause a deviation or failed integrity checks.

Instead, run such scripts or commands during image building so changes are part of the image. You can also use the configuration management mechanisms of the Red Hat Edge Manager.
