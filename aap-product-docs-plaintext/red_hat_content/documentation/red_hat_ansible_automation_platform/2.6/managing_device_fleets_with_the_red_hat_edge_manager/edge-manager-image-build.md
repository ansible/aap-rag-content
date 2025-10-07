# 4. Operating system images for using with the Red Hat Edge Manager
## 4.1. The image building process




1. Choose a base `    bootc` operating system image, such as a Fedora, CentOS, or RHEL image.
1. Create a container file that layers the following items onto the base `    bootc` image:


- The Red Hat Edge Manager agent and configuration.
- Optional: Any drivers specific to your target deployment environment.
- Optional: Host configuration, for example, certificate authority bundles, and application workloads that are common to all deployments.

1. Build, publish, and sign a `    bootc` operating system image using `    podman` and `    skopeo` .
1. Create an operating system disk image by using `    bootc-image-builder` .
1. Build, publish, and sign an operating system disk image using `    skopeo` .


Note
The operating system disk image has partitions, volumes, the file system, and the initial `bootc` image. You only need to create the operating system disk image once, during provisioning. For later device updates, you only need the `bootc` operating system image, which has the files in the file system.



**Additional resources**

-  [Building a bootc operating system image for the Red Hat Edge Manager](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-build-bootc)
-  [Special considerations for building images](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-images-special-considerations)


