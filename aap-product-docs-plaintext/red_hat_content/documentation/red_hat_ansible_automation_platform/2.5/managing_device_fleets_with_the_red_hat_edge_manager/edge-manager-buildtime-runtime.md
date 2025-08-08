# 4. Operating system images for using with the Red Hat Edge Manager
## 4.2. Special considerations for building images
### 4.2.1. Build-time configuration over dynamic runtime configuration




Add the configuration to the operating system image at build time. Adding the configuration at build time ensures that the configurations are tested, distributed, and updated together. In cases when build-time configuration is not feasible or desirable, you can dynamically configure devices at runtime instead with the Red Hat Edge Manager.

Dynamic runtime configuration is preferable in the following cases:

- You have a configuration that is deployment or site-specific, such as a hostname or a site-specific network credential.
- You have secrets that are not secure to distribute with the image.
- You have application workloads that need to be added, updated, or deleted without reboot or they are on a faster cadence than the operating system.


### 4.2.2. Configuration in the `/usr` directory




Place configuration files in the `/usr` directory if the configuration is static and the application or service supports that configuration. By placing the configuration in the `/usr` directory, the configuration remains read-only and fully defined by the image.

Do not place the configuration in the `/usr` directory in the following cases:

- The configuration is deployment or site-specific.
- The application or service only supports reading configuration from the `    /etc` directory.
- The configuration might need to be changed at runtime.


### 4.2.3. Drop-in directories




Use drop-in directories to add, replace, or remove configuration files that the service aggregates. Do not directly edit your configuration files because it can cause deviations from the target configuration.

Note
You can identify drop-in directories by the `.d/` at the end of the directory name. For example, `/etc/containers/certs.d` , `/etc/cron.d` , and `/etc/NetworkManager/conf.d` .



### 4.2.4. Operating system images with scripts




Avoid executing scripts or commands that change the file system. The `bootc` or the Red Hat Edge Manager can overwrite the changed files which can cause a deviation or failed integrity checks..

Instead, run such scripts or commands during image building so changes are part of the image. You can also use the configuration management mechanisms of the Red Hat Edge Manager.

**Additional resources**

-  [Generic guidance for building images](https://bootc-dev.github.io/bootc/building/guidance.html)


## 4.3. Building a _bootc_ operating system image for the Red Hat Edge Manager




To prepare your device to be managed by the Red Hat Edge Manager, build a `bootc` operating system image that has the Red Hat Edge Manager agent. Then build an operating system disk image for your devices.

For more information, see the following sections:

-  [Installing the Red Hat Edge Manager CLI](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_device_fleets_with_the_red_hat_edge_manager/assembly-edge-manager-images#edge-manager-install-CLI)
-  [Optional: Requesting an enrollment certificate for early binding](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_device_fleets_with_the_red_hat_edge_manager/assembly-edge-manager-images#edge-manager-request-cert)
-  [Optional: Using image pull secrets](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_device_fleets_with_the_red_hat_edge_manager/assembly-edge-manager-images#edge-manager-image-pullsecrets)
-  [Building the operating system image with bootc](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_device_fleets_with_the_red_hat_edge_manager/assembly-edge-manager-images#edge-manager-build-bootc-image)
-  [Signing and publishing the bootc operating system image by using Sigstore](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_device_fleets_with_the_red_hat_edge_manager/assembly-edge-manager-images#edge-manager-build-sign-image)
-  [Building the operating system disk image](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_device_fleets_with_the_red_hat_edge_manager/assembly-edge-manager-images#edge-manager-build-disk-image)
-  [Optional: Signing and publishing the operating system disk image to an Open Container Initiative registry](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_device_fleets_with_the_red_hat_edge_manager/assembly-edge-manager-images#edge-manager-sign-disk-image)


### 4.3.1. Prerequisites




See the following prerequisites for building a `bootc` operating system image:

- Install `    podman` version 5.0 or later and `    skopeo` version 1.14 or later. See [Getting container tools](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/building_running_and_managing_containers/index#proc_getting-container-tools_assembly_starting-with-containers) .
- Install `    bootc-image-builder` . See [Installing bootc-image-builder](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#installing-bootc-image-builder_creating-bootc-compatible-base-disk-images-with-bootc-image-builder) .


### 4.3.2. Installing the Red Hat Edge Manager CLI




To install the Red Hat Edge Manager CLI, complete the following steps:

**Procedure**

1. Enable the subscription manager for the repository appropriate for your system by running the following command:


```
sudo subscription-manager repos --enable ansible-automation-platform-2.5-for-rhel-9-x86_64-rpms
```

For a full list of available repositories for the Red Hat Edge Manager, see the [Additional resources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_device_fleets_with_the_red_hat_edge_manager/assembly-edge-manager-images#edge-manager-additional-resources-images) section.


1. Install the `    flightctl` CLI with your package manager by running the following command:


```
sudo dnf install flightctl
```




If you [set up the OAuth application manually](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_device_fleets_with_the_red_hat_edge_manager/assembly-edge-manager-install#edge-manager-oauth-manually) , you also need to make sure that one utility `xdg-open` , `x-www-browser` , or `www-browser` is available, for example, by installing `xdg-utils` .

### 4.3.3. Logging into the Red Hat Edge Manager through the CLI




How you log in the Red Hat Edge Manager depends on whether you choose the [automatic](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_device_fleets_with_the_red_hat_edge_manager/assembly-edge-manager-install#edge-manager-oauth-auto) or [manual](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/managing_device_fleets_with_the_red_hat_edge_manager/assembly-edge-manager-install#edge-manager-oauth-manually) method when you initially set up the application.

**Procedure**

- If you use the automatic setup you can create a personal access token, even only with Read scope (under the profile icon in the top right corner of your Ansible Automation Platform UI > **User details** > **Tokens** tab) and then use this token to log in directly through the CLI, with the following example syntax:


```
flightctl login https://&lt;your-edge-manager-ip-or-domain&gt;:3443 --token=&lt;your-aap-oauth-token&gt; --insecure-skip-tls-verify
```


- If you use the manual setup, use the **Client ID** to log in through a web-based process, with the following example syntax:


```
flightctl login https://&lt;your-edge-manager-ip-or-domain&gt;:3443 --web --client-id=&lt;your-aap-client-id&gt; --insecure-skip-tls-verify
```


- This opens in a web browser and asks you to approve.

The `        --insecure-skip-tls-verify` parameter is used only if you have not generated your own valid certificates.





**Next steps**

Use the following commands to help you with the CLI:


- To output a list of available commands, use:


```
flightctl
```


- To output both the flightctl CLI version and the back-end Red Hat Edge Manager version, use:


```
flightctl version
```




Important
To ensure supportability and proper functionality, the version of the flightctl CLI must match the version of the Red Hat Edge Manager in use. Mismatched versions are not supported.



### 4.3.4. Optional: Requesting an enrollment certificate for early binding




If you want to include an agent configuration in the image, complete the following steps:

**Procedure**

1. Log in to the flightctl CLI by following the steps in [Logging into the Red Hat Edge Manager through the CLI](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-log-into-CLI) .

Note
The CLI uses the certificate authority pool of the host to verify the identity of the Red Hat Edge Manager service. The verification can lead to a TLS verification error when using self-signed certificates, if you do not add your certificate authority certificate to the pool. You can bypass the server verification by adding the `    --insecure-skip-tls-verify` flag to your command.




1. Get the enrollment credentials in the format of an agent configuration file by running the following command:


```
flightctl certificate request --signer=enrollment --expiration=365d --output=embedded &gt; config.yaml
```

Note

- The `        --expiration=365d` option specifies that the credentials are valid for a year.
- The `        --output=embedded` option specifies that the output is an agent configuration file with the enrollment credentials embedded.


The returned `    config.yaml` contains the URLs of the Red Hat Edge Manager service, the certificate authority bundle, and the enrollment client certificate and key for the agent. See the following example:


```
enrollment-service:      authentication:        client-certificate-data: LS0tLS1CRUdJTiBD...        client-key-data: LS0tLS1CRUdJTiBF...      service:        certificate-authority-data: LS0tLS1CRUdJTiBD...        server: https://agent-api.flightctl.127.0.0.1.nip.io:7443      enrollment-ui-endpoint: https://ui.flightctl.127.0.0.1.nip.io:8081
```




### 4.3.5. Optional: Using image pull secrets




If your device relies on containers from a private repository, you must configure a pull secret for the registry. Complete the following steps:

**Procedure**

1. Depending on the kind of container image you use, place the pull secret in one or both of the following system paths on the device:


- Operating system images use the `        /etc/ostree/auth.json` path.
- Application container images use the `        /root/.config/containers/auth.json` path.

Important
The pull secret must exist on the device before the secret can be consumed.





1. Ensure that the pull secrets use the following format:


```
{      "auths": {        "registry.example.com": {          "auth": "base64-encoded-credentials"        }      }    }
```




For more information, see the [Additional resources](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-additional-resources-images) section.

### 4.3.6. Building the operating system image with _bootc_




Build the operating system image with the `bootc` that contains the Red Hat Edge Manager agent. You can optionally include the following items in your operating system image:

- The agent configuration for early binding
- Any drivers
- Host configuration
- Application workloads that you need


Complete the following steps:

**Procedure**

1. Create a `    Containerfile` file with the following content to build a RHEL 9-based operating system image that includes the Red Hat Edge Manager agent and configuration:


```
FROM registry.redhat.io/rhel9/rhel-bootc:&lt;required_os_version&gt;<span id="CO2-1"><!--Empty--></span><span class="callout">1</span>RUN subscription-manager repos --enable rhacm-2.13-for-rhel-9-$(uname -m)-rpms &amp;&amp; \        dnf -y install flightctl-agent &amp;&amp; \        dnf -y clean all &amp;&amp; \        systemctl enable flightctl-agent.service &amp;&amp; \        systemctl mask bootc-fetch-apply-updates.timer<span id="CO2-2"><!--Empty--></span><span class="callout">2</span>
```

Important
If your device relies on containers from a private repository, you must place the device pull secret in the `    /etc/ostree/auth.json` path. The pull secret must exist on the device before the secret can be consumed.




-  **Optional:** To enable `        podman-compose` application support, add the following section to the `        Containerfile` file:


```
RUN dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm &amp;&amp; \            dnf -y install podman-compose &amp;&amp; \            dnf -y clean all &amp;&amp; \            systemctl enable podman.service
```


-  **Optional:** If you created the `        config.yaml` for early binding, add the following section to the `        Containerfile` :


```
ADD config.yaml /etc/flightctl/
```


For more information, see [Optional: Requesting an enrollment certificate for early binding](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-request-cert) .


1. Define the Open Container Initiative (OCI) registry by running the following command:


```
OCI_REGISTRY=registry.redhat.io
```


1. Define the image repository that you have permissions to write to by running the following command:


```
OCI_IMAGE_REPO=${OCI_REGISTRY}/&lt;your_org&gt;/&lt;your_image&gt;
```


1. Define the image tag by running the following command:


```
OCI_IMAGE_TAG=v1
```


1. Build the operating system image for your target platform:


```
sudo podman build -t ${OCI_IMAGE_REPO}:${OCI_IMAGE_TAG}
```




### 4.3.7. Signing and publishing the _bootc_ operating system image by using Sigstore




To sign the `bootc` operating system image by using Sigstore, complete the following steps:

**Procedure**

1. Generate a Sigstore key pair named `    signingkey.pub` and `    signingkey.private` :


```
skopeo generate-sigstore-key --output-prefix signingkey
```


1. Configure container tools such as Podman and Skopeo to upload Sigstore signatures together with your signed image to your OCI registry:


```
sudo tee "/etc/containers/registries.d/${OCI_REGISTRY}.yaml" &gt; /dev/null &lt;&lt;EOF    docker:        ${OCI_REGISTRY}:            use-sigstore-attachments: true    EOF
```


1. Log in to your OCI registry by running the following command:


```
sudo podman login ${OCI_REGISTRY}
```


1. Sign and publish the operating system image by running the following command:


```
sudo podman push \        --sign-by-sigstore-private-key ./signingkey.private \        ${OCI_IMAGE_REPO}:${OCI_IMAGE_TAG}
```




### 4.3.8. Building the operating system disk image




Build the operating system disk image that contains the file system for your devices.

Complete the following steps:

**Procedure**

1. Create a directory called `    output` by running the following command:


```
mkdir -p output
```


1. Use `    bootc-image-builder` to generate an operating system disk image of type `    iso` from your operating system image by running the following command:


```
sudo podman run --rm -it --privileged --pull=newer \        --security-opt label=type:unconfined_t \        -v "${PWD}/output":/output \        -v /var/lib/containers/storage:/var/lib/containers/storage \        registry.redhat.io/rhel9/bootc-image-builder:latest \        --type iso \        ${OCI_IMAGE_REPO}:${OCI_IMAGE_TAG}
```




When the `bootc-image-builder` completes, you can find the ISO disk image at the `${PWD}/output/bootiso/install.iso` path.

### 4.3.9. Optional: Signing and publishing the operating system disk image to an Open Container Initiative registry




Sign and publish your disk image to your Open Container Initiative (OCI) registry. Optionally, you can compress and publish the disk image as an OCI artifact to the same OCI registry as your `bootc` images, which facilitates a unified hosting and distribution of `bootc` and disk images. To publish your ISO disk image to a repository named after your `bootc` image with `/diskimage-iso` appended.

**Prerequisites**

- You created a private key by using Sigstore. See [Signing and publishing the bootc operating system image by using Sigstore](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-build-sign-image) .


Sign and publish your disk image to your OCI registry by completing the following steps:

**Procedure**

1. Change the owner of the directory where the ISO disk image is located from `    root` to your current user by running the following command:


```
sudo chown -R $(whoami):$(whoami) "${PWD}/output"
```


1. Define the `    OCI_DISK_IMAGE_REPO` environmental variable to be the same repository as your `    bootc` image with `    /diskimage-iso` appended by running the following command:


```
OCI_DISK_IMAGE_REPO=${OCI_IMAGE_REPO}/diskimage-iso
```


1. Create a manifest list by running the following command:


```
sudo podman manifest create \        ${OCI_DISK_IMAGE_REPO}:${OCI_IMAGE_TAG}
```


1. Add the ISO disk image to the manifest list as an OCI artifact by running the following command:


```
sudo podman manifest add \        --artifact --artifact-type application/vnd.diskimage.iso \        --arch=amd64 --os=linux \        ${OCI_DISK_IMAGE_REPO}:${OCI_IMAGE_TAG} \        "${PWD}/output/bootiso/install.iso"
```


1. Sign the manifest list with your private Sigstore key and push the image to the registry by running the following command:


```
sudo podman manifest push --all \         --sign-by-sigstore-private-key ./signingkey.private \        ${OCI_DISK_IMAGE_REPO}:${OCI_IMAGE_TAG} \        docker://${OCI_DISK_IMAGE_REPO}:${OCI_IMAGE_TAG}
```




### 4.3.10. Additional resources




- For more information about building the operating system image on different target platforms, see [Configuring container pull secrets](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#configuring-container-pull-secrets_managing-users-groups-ssh-key-and-secrets-in-image-mode-for-rhel) .


### 4.3.11. Requirements for specific target platforms




See the following platform considerations:

-  [Building images for Red Hat OpenShift Virtualization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-virt)
-  [Building images for VMware vSphere](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-vmware)


#### 4.3.11.1. Building images for Red Hat OpenShift Virtualization




When building operating system images and disk images for Red Hat OpenShift Virtualization, you can follow the generic image building process with the following changes:

- Using late binding by injecting the enrollment certificate or the agent configuration through `    cloud-init` when provisioning the virtual device.
- Adding the `    open-vm-tools` guest tools to the image.
- Building a disk image of type `    qcow2` instead of `    iso` .


Complete the generic steps with changes to the following steps:

**Procedure**

1. Build an operating system image based on RHEL 9 that includes the Red Hat Edge Manager agent and VM guest tools but excludes the agent configuration.
1. Create a file named `    Containerfile` with the following content:


```
FROM registry.redhat.io/rhel9/bootc-image-builder:latest    RUN subscription-manager repos --enable rhacm-2.13-for-rhel-9-$(uname -m)-rpms &amp;&amp; \        dnf -y install flightctl-agent &amp;&amp; \        dnf -y clean all &amp;&amp; \        systemctl enable flightctl-agent.service    RUN dnf -y install cloud-init open-vm-tools &amp;&amp; \        dnf -y clean all &amp;&amp; \        ln -s ../cloud-init.target /usr/lib/systemd/system/default.target.wants &amp;&amp; \        systemctl enable vmtoolsd.service
```


1.  **Optional:** To enable `    podman-compose` application support, add the following section to the `    Containerfile` file:


```
RUN dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm &amp;&amp; \        dnf -y install podman-compose &amp;&amp; \        dnf -y clean all &amp;&amp; \        systemctl enable podman.service
```




#### 4.3.11.2. Building the bootc image




Build, sign, and publish the `bootc` operating system image by following the generic image building process:

**Procedure**

1. Create a directory called `    output` by running the following command:


```
mkdir -p output
```


1. Generate an operating system disk image of type `    vmdk` from your operating system image by running the following command:


```
sudo podman run --rm -it --privileged --pull=newer \        --security-opt label=type:unconfined_t \        -v "${PWD}/output":/output \        -v /var/lib/containers/storage:/var/lib/containers/storage \        registry.redhat.io/rhel9/bootc-image-builder:latest \        --type qcow2 \        ${OCI_IMAGE_REPO}:${OCI_IMAGE_TAG}
```




When the `bootc-image-builder` completes, you can find the disk image under `${PWD}/output/vmdk/disk.vmdk` .

#### 4.3.11.3. Building the QCoW2 disk image




Red Hat OpenShift Virtualization can download disk images from an OCI registry but it expects a container disk image instead of an OCI artifact.

Complete the following steps to build, sign, and upload the QCoW2 disk image:

**Procedure**

1. Create a file called `    Containerfile.qcow2` with the following content:


```
FROM registry.access.redhat.com/ubi9/ubi:latest AS builder    ADD --chown=107:107 output/qcow2/disk.qcow2 /disk/<span id="CO3-1"><!--Empty--></span><span class="callout">1</span>RUN chmod 0440 /disk/*<span id="CO3-2"><!--Empty--></span><span class="callout">2</span>FROM scratch    COPY --from=builder /disk/* /disk/<span id="CO3-3"><!--Empty--></span><span class="callout">3</span>
```


1. Build, sign, and publish your disk image by running the following command:


```
sudo chown -R $(whoami):$(whoami) "${PWD}/output"    OCI_DISK_IMAGE_REPO=${OCI_IMAGE_REPO}/diskimage-qcow2    sudo podman build -t ${OCI_DISK_IMAGE_REPO}:${OCI_IMAGE_TAG} -f Containerfile.qcow2 .    sudo podman push --sign-by-sigstore-private-key ./signingkey.private ${OCI_DISK_IMAGE_REPO}:${OCI_IMAGE_TAG}
```




#### 4.3.11.4. Building images for VMware vSphere




When building operating system images and disk images for VMware vSphere, you can follow the generic image building process with the following changes:

- Using late binding by injecting the enrollment certificate or the agent configuration through `    cloud-init` when provisioning the virtual device.
- Adding the `    open-vm-tools` guest tools to the image.
- Building a disk image of type `    vmdk` instead of `    iso` .


Complete the generic steps with changes to the following steps:

**Procedure**

1. Build an operating system image based on RHEL 9 that includes the Red Hat Edge Manager agent and VM guest tools but excludes the agent configuration.
1. Create a file named `    Containerfile` with the following content:


```
FROM registry.redhat.io/rhel9/bootc-image-builder:latest    RUN subscription-manager repos --enable rhacm-2.13-for-rhel-9-$(uname -m)-rpms &amp;&amp; \        dnf -y install flightctl-agent &amp;&amp; \        dnf -y clean all &amp;&amp; \        systemctl enable flightctl-agent.service &amp;&amp; \    RUN dnf -y install cloud-init open-vm-tools &amp;&amp; \        dnf -y clean all &amp;&amp; \        ln -s ../cloud-init.target /usr/lib/systemd/system/default.target.wants &amp;&amp; \        systemctl enable vmtoolsd.service
```


1. Create a directory called `    output` by running the following command:


```
mkdir -p output
```


1. Generate an operating system disk image of type `    vmdk` from your operating system image by running the following command:


```
sudo podman run --rm -it --privileged --pull=newer \        --security-opt label=type:unconfined_t \        -v "${PWD}/output":/output \        -v /var/lib/containers/storage:/var/lib/containers/storage \        registry.redhat.io/rhel9/bootc-image-builder:latest \        --type vmdk \        ${OCI_IMAGE_REPO}:${OCI_IMAGE_TAG}
```




When the `bootc-image-builder` completes, you can find the disk image under `${PWD}/output/vmdk/disk.vmdk` .

# Chapter 5. Provision devices




You can provision devices with the Red Hat Edge Manager in different environments. Use the operating system image or disk image that you built for use with the Red Hat Edge Manager. Depending on your target environment, provision a physical or virtual device.

See the following sections:

-  [Provision physical devices](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-provisioning-physical)
-  [Provision devices with OpenShift Virtualization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-provisioning-openshift-virt)


## 5.1. Provision physical devices




When you build an International Organization for Standardization (ISO) disk image from an operating system image by using the `bootc-image-builder` tool, the image is similar to the RHEL ISOs available for download. However, your operating system image content is embedded in the ISO disk image.

To install the ISO disk image to a bare metal system without having access to the network, see [Deploying a custom ISO container image](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/deploying-the-rhel-bootc-images_using-image-mode-for-rhel-to-build-deploy-and-manage-operating-systems#deploying-an-custom-iso-container-image_deploying-the-rhel-bootc-images) in the Red Hat Enterprise Linux documentation.

To install the ISO disk image through the network, see [Deploying an ISO bootc image over PXE boot](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/deploying-the-rhel-bootc-images_using-image-mode-for-rhel-to-build-deploy-and-manage-operating-systems#deploying-an-iso-bootc-container-over-pxe-boot_deploying-the-rhel-bootc-images) in the Red Hat Enterprise Linux documentation.

## 5.2. Provision devices with OpenShift Virtualization




You can provision a virtual machine on OpenShift Virtualization by using a QCoW2 container disk image that is hosted on an OCI container registry.

If your operating system image does not already contain the Red Hat Edge Manager agent enrollment configuration, you can inject the configuration through the `cloud-init` user data at provisioning.

**Prerequisites**

- You installed the `    flightctl` CLI and logged in to your Red Hat Edge Manager service instance.
- You installed the `    oc` CLI, used it to log in to your OpenShift cluster instance, and changed to the project in which you want to create your virtual machine.


### 5.2.1. Creating the _cloud-init_ configuration




To create the `cloud-init` configuration, complete the following steps:

**Procedure**

1. Request a new Red Hat Edge Manager agent enrollment configuration and store it in a file called `    config.yaml` by running the following command:


```
flightctl certificate request --signer=enrollment --expiration=365d --output=embedded &gt; config.yaml
```


1. Create a cloud configuration user data file called `    cloud-config.yaml` that places the agent configuration in the correct location on the first boot by running the following command:


```
cat &lt;&lt;EOF &gt; cloud-config.yaml    #cloud-config    write_files:    - path: /etc/flightctl/config.yaml      content: $(cat config.yaml | base64 -w0)      encoding: b64    EOF
```


1. Create a Kubernetes `    Secret` that contains the cloud configuration user data file:


```
oc create secret generic enrollment-secret --from-file=userdata=cloud-config.yaml
```




### 5.2.2. Creating the virtual machine




Create a virtual machine that has its primary disk populated from your QCoW2 container disk image and a `cloud-init` configuration drive that is populated from your enrollment secret.

Complete the following steps:

**Procedure**

1. Create a file that has the `    VirtualMachine` resource manifest by running the following command:


```
cat &lt;&lt;EOF &gt; my-bootc-vm.yaml    apiVersion: kubevirt.io/v1    kind: VirtualMachine    metadata:      name: my-bootc-vm    spec:      runStrategy: RerunOnFailure      template:        spec:          domain:            cpu:              cores: 1            memory:              guest: 1024M            devices:              disks:                - name: containerdisk                  disk:                    bus: virtio                - name: cloudinitdisk                  disk:                    bus: virtio          volumes:            - name: containerdisk              containerDisk:                image: ${OCI_DISK_IMAGE_REPO}:${OCI_IMAGE_TAG}            - name: cloudinitdisk              cloudInitConfigDrive:                secretRef:                  name: enrollment-secret    EOF
```


1. Apply the resource manifest to your cluster by running the following command:


```
oc apply -f my-bootc-vm.yaml
```




**Additional resources**

- For more information about how to inject the configuration through the `    cloud-init` user data, see the [Cloud-init documentation](https://cloudinit.readthedocs.io/en/latest/) .
- See [Building images for Red Hat OpenShift Virtualization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-virt) .


# Chapter 6. Manage devices




The Red Hat Edge Manager manages the device lifecycle from enrollment to decommissioning of a device. The device lifecycle also includes device management, such as organizing, monitoring, and updating your devices with the Red Hat Edge Manager.

You can manage your devices individually or in a fleet. With the Red Hat Edge Manager you can manage a whole fleet of devices as a single object instead of managing many devices individually.

You only need to specify the required configuration once, and then the Red Hat Edge Manager applies the configuration to all devices in the fleet.

Understanding individual device management is the foundation for managing devices in a fleet. You might want to manage your devices individually in the following scenarios:

- If a few devices have different configurations.
- If you use external automation for updating the device.


The following sections focus on managing individual devices:

-  [Enroll devices](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-enroll)
-  [View devices](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-view-devices)
-  [Labels and label selectors](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-labels)
-  [Updating labels on the CLI](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-update-labels)
-  [Update the operating system](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-update-os)
-  [Operating system configuration for edge devices](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-manage-os-config)


## 6.1. Enroll devices




To manage your devices with the Red Hat Edge Manager, you must enroll the devices to the Red Hat Edge Manager service.

The first time the Red Hat Edge Manager agent runs on a device, the agent prepares for the enrollment process by generating a cryptographic key pair. The cryptographic key pair serves as the unique cryptographic identity of the device. The key pair consists of a public and a private key. The private key never leaves the device, so that the device cannot be duplicated or impersonated.

When the device is not yet enrolled, the agent performs service discovery to find its Red Hat Edge Manager service instance. Then, the device establishes a secure, mTLS-protected network connection to the service. The device uses its X.509 enrollment certificate that the device acquired during image building or device provisioning. The device submits an enrollment request to the service that includes the following:

- a description of the device hardware and operating system
- an X.509 Certificate Signing Request which includes the cryptographic identity of the device to obtain the initial management certificate


The device is not considered trusted and remains quarantined in a device lobby until an authorized user approves or denies the request.

For more information, see the following sections:

-  [Device enrollment](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-device-enroll)
-  [Optional: Requesting an enrollment certificate for early binding](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-request-cert)


### 6.1.1. Enrolling devices on the CLI




You must enroll devices into the Red Hat Edge Manager service before you can manage them.

**Prerequisites**

- You must install the Red Hat Edge Manager CLI. See [Installing the Red Hat Edge Manager CLI](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-install-CLI) .
- You must log in to the Red Hat Edge Manager service.


**Procedure**

1. List all devices that are currently waiting for approval by running the following command:


```
flightctl get enrollmentrequests --field-selector="status.approval.approved != true"
```

See the following example:


```
NAME           APPROVAL  APPROVER  APPROVED LABELS    &lt;device_name&gt;  Pending   &lt;none&gt;    &lt;none&gt;
```


Note
The unique device name is generated by the agent and you cannot change it. The agent chooses a base32-encoded hash of its public key as the device name.




1. Approve an enrollment request by specifying the name of the enrollment request. Optionally, you can add labels to the device by using the `    --label` or `    -l` flags. See the following example:


```
flightctl approve -l region=eu-west-1 -l site=factory-berlin enrollmentrequest/54shovu028bvj6stkovjcvovjgo0r48618khdd5huhdjfn6raskg
```

See the following example output:


```
NAME           APPROVAL  APPROVER  APPROVED LABELS    &lt;device_name&gt;  Approved  user      region=eu-west-1,site=factory-berlin
```





After you approve the enrollment request, the service issues the management certificate for the device and registers the device in the device inventory. You can then manage the device.

## 6.2. View devices




To get more information about the devices in your inventory, you can use the Red Hat Edge Manager CLI.

**Prerequisites**

- You must install the Red Hat Edge Manager CLI. See [Installing the Red Hat Edge Manager CLI](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-install-CLI) .
- You must enroll at least one device.


### 6.2.1. Viewing device inventory and device details on the web UI




Complete the following steps:

**Procedure**

1. From the navigation panel, selectApplication Links→Edge Manager. This opens the external Edge Manager instance.
1. From the navigation panel, select **Devices** where you can view your device inventory, details, and decommission devices.


### 6.2.2. Viewing device inventory and device details on the CLI




Complete the following steps:

**Procedure**

1. View the devices in the device inventory by running the following command:


```
flightctl get devices
```

See the following example output:


```
NAME           ALIAS    OWNER   SYSTEM  UPDATED     APPLICATIONS  LAST SEEN    &lt;device_name&gt;  &lt;none&gt;   &lt;none&gt;  Online  Up-to-date  &lt;none&gt;        3 seconds ago
```



1. View the details of this device in YAML format by running the following command:


```
flightctl get device/&lt;device_name&gt; -o yaml
```

See the following example output:


```
apiVersion: flightctl.io/v1alpha1    kind: Device    metadata:      name: &lt;device_name&gt;      labels:<span id="CO4-1"><!--Empty--></span><span class="callout">1</span>region: eu-west-1        site: factory-berlin    spec:      os:        image: quay.io/flightctl/rhel:9.5<span id="CO4-2"><!--Empty--></span><span class="callout">2</span>config:      - name: my-os-configuration<span id="CO4-3"><!--Empty--></span><span class="callout">3</span>configType: GitConfigProviderSpec        gitRef:          path: /configuration          repository: my-configuration-repo          targetRevision: production    status:      os:        image: quay.io/flightctl/rhel:9.5<span id="CO4-4"><!--Empty--></span><span class="callout">4</span>config:        renderedVersion: "1"<span id="CO4-5"><!--Empty--></span><span class="callout">5</span>applications:        data: {}<span id="CO4-6"><!--Empty--></span><span class="callout">6</span>summary:          status: Unknown<span id="CO4-7"><!--Empty--></span><span class="callout">7</span>resources:<span id="CO4-8"><!--Empty--></span><span class="callout">8</span>cpu: Healthy        disk: Healthy        memory: Healthy      systemInfo:<span id="CO4-9"><!--Empty--></span><span class="callout">9</span>architecture: amd64        bootID: 037750f7-f293-4c5b-b06e-481eef4e883f        operatingSystem: linux      summary:        info: ""        status: Online<span id="CO4-10"><!--Empty--></span><span class="callout">10</span>updated:        status: UpToDate<span id="CO4-11"><!--Empty--></span><span class="callout">11</span>lastSeen: "2024-08-28T11:45:34.812851905Z"<span id="CO4-12"><!--Empty--></span><span class="callout">12</span>[...]
```





### 6.2.3. Labels and label selectors




You can organize your resources by assigning them labels, for example, to record their location, hardware type, or purpose. The Red Hat Edge Manager labels follow the same syntax, principles, and operators as Kubernetes labels and label selectors. You can select devices with labels when viewing the device inventory or applying operations to the devices.

Labels follow the `key=value` format. You can use the key to group devices. For example, if your labels follow the `site=&lt;location&gt;` naming convention, you can group your devices by site. You can also use labels that only consist of keys.

Labels must adhere to the following rules to be valid:

- Keys and value must each be 63 characters or less.
- Keys and values can consist of alphanumeric characters ( `    a-z` , `    A-Z` , `    0-9` ).
- Keys and values can also contain dashes ( `    -` ), underscores ( `    _` ), dots ( `    .` ) but not as the first or last character.
- Value can be omitted.


You can apply labels to devices in the following ways:

- Define a set of default labels during image building that are automatically applied to all devices during deployment.
- Assign initial labels during enrollment.
- Assign labels post-enrollment.


When resources are labeled, you can select a subset of devices by creating a label selector. A label selector is a comma-separated list of labels for selecting devices that have the same set of labels.

See the following examples:

| Example label selector | Selected devices |
| --- | --- |
|  `site=factory-berlin` | All devices with a `site` label key and a `factory-berlin` label value. |
|  `site!=factory-berlin` | All devices with a `site` label key but where the label value is not `factory-berlin` . |
|  `site in (factory-berlin,factory-madrid)` | All devices with a `site` label key and where the label value is either `factory-berlin` or `factory-madrid` . |


For more information about labels and selectors, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) in the Kubernetes documentation.

#### 6.2.3.1. Viewing devices and their labels on the web UI




View devices and their associated labels on the web UI. You can use labels to organize your devices and device fleets.

Complete the following steps:

1. From the navigation panel, selectApplication Links→Edge Manager. This opens the external Edge Manager instance.
1. From the navigation panel, select **Devices** .
1. Select the device you want to manage. In the **Details** tab you can view the associated labels under **Labels** .


#### 6.2.3.2. Viewing devices and their labels on the CLI




View devices and their associated labels. You can use labels to organize your devices and device fleets.

Complete the following steps:

**Procedure**

1. View devices in your inventory with their labels by using the `    -o wide` option:


```
flightctl get devices -o wide
```

See the following example output:


```
NAME            ALIAS    OWNER   SYSTEM  UPDATED     APPLICATIONS  LAST SEEN      LABELS    &lt;device1_name&gt;  &lt;none&gt;   &lt;none&gt;  Online  Up-to-date  &lt;none&gt;        3 seconds ago  region=eu-west-1,site=factory-berlin    &lt;device2_name&gt;  &lt;none&gt;   &lt;none&gt;  Online  Up-to-date  &lt;none&gt;        1 minute ago   region=eu-west-1,site=factory-madrid
```


1. View devices in your inventory with a specific label or set of labels by using the `    -l &lt;key=value&gt;` option:


```
flightctl get devices -l site=factory-berlin -o wide
```

See the following example output:


```
NAME            ALIAS    OWNER   SYSTEM  UPDATED     APPLICATIONS  LAST SEEN      LABELS    &lt;device1_name&gt;  &lt;none&gt;   &lt;none&gt;  Online  Up-to-date  &lt;none&gt;        3 seconds ago  region=eu-west-1,site=factory-berlin
```




#### 6.2.3.3. Updating labels on the CLI




Update labels on your devices by using the CLI.

Complete the following steps:

**Procedure**

1. Export the current definition of the device into a file by running the following command:


```
flightctl get device/&lt;device1_name&gt; -o yaml &gt; my_device.yaml
```


1. Use your preferred editor to edit the `    my_device.yaml` file. See the following example:


```
apiVersion: flightctl.io/v1alpha1    kind: Device    metadata:      labels:        some_key: some_value        some_other_key: some_other_value      name: &lt;device1_name&gt;    spec:    [...]
```


1. Save the file and apply the updated device definition by running the following command:


```
flightctl apply -f my_device.yaml
```


1. Verify your changes by running the following example output:


```
NAME            ALIAS    OWNER   SYSTEM  UPDATED     APPLICATIONS  LAST SEEN      LABELS    &lt;device1_name&gt;  &lt;none&gt;   &lt;none&gt;  Online  Up-to-date  &lt;none&gt;        3 minutes ago  some_key=some_value,some_other_key=some_other_value    &lt;device2_name&gt;  &lt;none&gt;   &lt;none&gt;  Online  Up-to-date  &lt;none&gt;        4 minutes ago  region=eu-west-1,site=factory-madrid
```




### 6.2.4. Field selectors




Field selectors filter a list of Red Hat Edge Manager resources based on specific resource field values. They follow the same syntax, principles, and operators as Kubernetes Field and Label selectors, with additional operators available for more advanced search use cases.

#### 6.2.4.1. Supported fields




Red Hat Edge Manager resources give a set of metadata fields that you can select.

Each resource supports the following metadata fields:

-  `    metadata.name`
-  `    metadata.owner`
-  `    metadata.creationTimestamp`


Note
To query labels, use Label Selectors for advanced and flexible label filtering.



For more information, see [Labels and label selectors](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-labels) .

#### 6.2.4.2. List of additional supported fields




In addition to the metadata fields, each resource has its own unique set of fields that you can select, offering further flexibility in filtering and selection based on resource-specific attributes.

The following table lists the fields supported for filtering for each resource kind:

| Kind | Fields |
| --- | --- |
|  **Certificate Signing Request** |  `status.certificate` |
|  **Device** |  `status.summary.status`

`status.applicationsSummary.status`

`status.updated.status`

`status.lastSeen`

`status.lifecycle.status` |
|  **Enrollment Request** |  `status.approval.approved`

`status.certificate` |
|  **Fleet** |  `spec.template.spec.os.image` |
|  **Repository** |  `spec.type`

`spec.url` |
|  **Resource Sync** |  `spec.repository` |


#### 6.2.4.3. Fields discovery




Some Red Hat Edge Manager resources might expose additional supported fields. You can discover the supported fields by using `flightctl` with the `--field-selector` option. If you try to use an unsupported field, the error message lists the available supported fields.

See the following examples:

```
flightctl get device --field-selector='text'
```

```
Error: listing devices: 400, message: unknown or unsupported selector: unable to resolve selector name "text". Supported selectors are: [metadata.alias metadata.creationTimestamp metadata.name metadata.nameoralias metadata.owner status.applicationsSummary.status status.lastSeen status.summary.status status.updated.status]
```

The field `text` is not a valid field for filtering. The error message provides a list of supported fields that you can use with `--field-selector` for the `Device` resource.

You can then use one of the supported fields:

```
flightctl get devices --field-selector 'metadata.alias contains cluster'
```

The `metadata.alias` field is checked with the containment operator `contains` to see if it has the value `cluster` .

**Example 1: Excluding a specific device by name**

The following command filters out a specific device by its name:


```
flightctl get devices --field-selector 'metadata.name!=c3tkb18x9fw32fzx5l556n0p0dracwbl4uiojxu19g2'
```

**Example 2: Filter by owner, labels, and creation timestamp**

This command retrieves devices owned by `Fleet/pos-fleet` , located in the `us` region, and created in 2024:


```
flightctl get devices --field-selector 'metadata.owner=Fleet/pos-fleet, metadata.creationTimestamp &gt;= 2024-01-01T00:00:00Z, metadata.creationTimestamp &lt; //2025-01-01T00:00:00Z' -l 'region=us'
```

**Example 3: Filter by Owner, Labels, and Device Status**

This command retrieves devices owned by `Fleet/pos-fleet` , located in the `us` region, and with a `status.updated.status` of either `Unknown` or `OutOfDate` :


```
flightctl get devices --field-selector 'metadata.owner=Fleet/pos-fleet, status.updated.status in (Unknown, OutOfDate)' -l 'region=us'
```

#### 6.2.4.4. Supported operators




| Operator | Symbol | Description |
| --- | --- | --- |
| Exists |  `exists` | Checks if a field exists |
| DoesNotExist |  `!` | Checks if a field does not exist |
| Equals |  `=` | Checks if a field is equal to a value |
| DoubleEquals |  `==` | Another form of equality check |
| NotEquals |  `!=` | Checks if a field is not equal to a value |
| GreaterThan |  `&gt;` | Checks if a field is greater than a value |
| GreaterThanOrEquals |  `&gt;=` | Checks if a field is greater than or equal to a value |
| LessThan |  `&lt;` | Checks if a field is less than a value |
| LessThanOrEquals |  `⇐` | Checks if a field is less than or equal to a value |
| In |  `in` | Checks if a field is within a list of values |
| NotIn |  `notin` | Checks if a field is not in a list of values |
| Contains |  `contains` | Checks if a field has a value |
| NotContains |  `notcontains` | Checks if a field does not contain a value |


##### 6.2.4.4.1. Operators usage by field type




Each field type supports a specific subset of operators:

| Field Type | Supported Operators | Value |
| --- | --- | --- |
|  **String** |  `Equals` : Matches if the field value is an exact match to the specified string.

`DoubleEquals` : Matches if the field value is an exact match to the specified string (alternative to `Equals` ).

`NotEquals` : Matches if the field value is not an exact match to the specified string.

`In` : Matches if the field value matches at least one string in the list.

`NotIn` : Matches if the field value does not match any of the strings in the list.

`Contains` : Matches if the field value has the specified substring.

`NotContains` : Matches if the field value does not contain the specified substring.

`Exists` : Matches if the field is present.

`DoesNotExist` : Matches if the field is not present. | Text string |
|  **Timestamp** |  `Equals` : Matches if the field value is an exact match to the specified timestamp.

`DoubleEquals` : Matches if the field value is an exact match to the specified timestamp (alternative to `Equals` ).

`NotEquals` : Matches if the field value is not an exact match to the specified timestamp.

`GreaterThan` : Matches if the field value is after the specified timestamp.

`GreaterThanOrEquals` : Matches if the field value is after or equal to the specified timestamp.

`LessThan` : Matches if the field value is before the specified timestamp.

`LessThanOrEquals` : Matches if the field value is before or equal to the specified timestamp.

`In` : Matches if the field value matches at least one timestamp in the list.

`NotIn` : Matches if the field value does not match any of the timestamps in the list.

`Exists` : Matches if the field is present.

`DoesNotExist` : Matches if the field is not present. | RFC 3339 format |
|  **Number** |  `Equals` : Matches if the field value equals the specified number.

`DoubleEquals` : Matches if the field value equals the specified number (alternative to `Equals` ).

`NotEquals` : Matches if the field value does not equal to the specified number.

`GreaterThan` : Matches if the field value is greater than the specified number.

`GreaterThanOrEquals` : Matches if the field value is greater than or equal to the specified number.

`LessThan` : Matches if the field value is less than the specified number.

`LessThanOrEquals` : Matches if the field value is less than or equal to the specified number.

`In` : Matches if the field value equals at least one number in the list.

`NotIn` : Matches if the field value does not equal any numbers in the list.

`Exists` :Matches if the field is present.

`DoesNotExist` : Matches if the field is not present. | Number format |
|  **Boolean** |  `Equals` : Matches if the value is `true` or `false` .

`DoubleEquals` : Matches if the value is `true` or `false` (alternative to `Equals` ).

`NotEquals` : Matches if the value is the opposite of the specified value.

`In` : Matches if the value ( `true` or `false` ) is in the list.

Note
The list can only contain `true` or `false` , so this operator is limited in use.



`NotIn` : Matches if the value is not in the list.

`Exists` : Matches if the field is present.

`DoesNotExist` : Matches if the field is not present. | Boolean format ( `true` , `false` ) |
|  **Array** |  `Contains` : Matches if the array has the specified value.

`NotContains` : Matches if the array does not contain the specified value. `In` : Matches if the array overlaps with the specified values.

`NotIn` : Matches if the array does not overlap with the specified values. `Exists` : Matches if the field is present.

`DoesNotExist` :Matches if the field is not present.

Note
Using `Array[Index]` treats the element as the type defined for the array elements. For example string, timestamp, number, or boolean. | Array element |


## 6.3. Update the operating system




You can update the operating system of a device by updating the target operating system image name or version in the device specification. When the agent communicates with the server, the agent detects the requested update. Then, the agent automatically starts downloading and verifying the new operating system version in the background. The Red Hat Edge Manager agent schedules the actual system update that is performed according to the update policy. At the scheduled update time, the agent installs the new version without disrupting the currently running operating system. Finally, the device reboots into the new version.

The Red Hat Edge Manager currently supports the following image type and image reference format:

| Image Type | Image Reference |
| --- | --- |
| bootc | An OCI image reference to a container registry. Example: `quay.io/flightctl-example/rhel:9.5` |


During the process, the agent sends status updates to the service. You can check the update process by viewing the device status.

For more information, see [View devices](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-view-devices) .

### 6.3.1. Updating the operating system on the CLI




Update a device using the CLI.

Complete the following steps:

**Procedure**

1. Get the current resource manifest of the device by running the following command:


```
flightctl get device/&lt;device_name&gt; -o yaml &gt; my_device.yaml
```


1. Edit the `    Device` resource to specify the new operating system name and version target.


```
apiVersion: flightctl.io/v1alpha1    kind: Device    metadata:      name: &lt;device_name&gt;    spec:    [...]      os:        image: quay.io/flightctl/rhel:9.5    [...]
```


1. Apply the updated `    Device` resource by running the following command:


```
flightctl apply -f &lt;device_name&gt;.yaml
```




## 6.4. Operating system configuration for edge devices




You can include an operating system-level host configuration in the image to give maximum consistency and repeatability. To update the configuration, create a new operating system image and update devices with the new image.

However, updating devices with a new image can be impractical in the following cases:

- The configuration is missing in the image.
- The configuration needs to be specific to a device.
- The configuration needs to be updateable at runtime without updating the operating system image and rebooting.


For these cases, you can declare a set of configuration files that are present on the file system of the device. The Red Hat Edge Manager agent applies updates to the configuration files while ensuring that either all files are successfully updated in the file system, or rolled back to their pre-update state. If the user updates both an operating system and configuration set of a device at the same time, the Red Hat Edge Manager agent updates the operating system first. It then applies the specified set of configuration files.

You can also specify a list of configuration sets that the Red Hat Edge Manager agent applies in sequence. In case of a conflict, the last applied configuration set is valid.

Important
After the Red Hat Edge Manager agent updates the configuration on the disk, the running applications need to reload the new configuration into memory for the configuration to become effective. If the update involves a reboot, `systemd` automatically restarts the applications with the new configuration and in the correct order. If the update does not involve a reboot, many applications can detect changes to their configuration files and automatically reload the files. When an application does not support change detection, you can use device lifecycle hooks to run scripts or commands if certain conditions are met.



### 6.4.1. Configuration providers




You can provide configuration from many sources, called configuration providers, in Red Hat Edge Manager. The Red Hat Edge Manager currently supports the following configuration providers:

Read more about the configuration providers in the following sections:

-  [Configuration from a Git repository](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-config-git-repo)
-  [Secrets from a Kubernetes cluster](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-k8s-cluster)
-  [Configuration from an HTTP server](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-config-http)
-  [Configuration inline in the device specification](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-config-inline)


#### 6.4.1.1. Configuration from a Git repository




You can store device configuration in a Git repository such as GitHub or GitLab. You can then add a Git Config Provider so that the Red Hat Edge Manager synchronizes the configuration from the repository to the file system of the device.

The Git Config Provider takes the following parameters:

| Parameter | Description |
| --- | --- |
|  `Repository` | The name of a `Repository` resource defined in the Red Hat Edge Manager. |
|  `TargetRevision` | The branch, tag, or commit of the repository to checkout. |
|  `Path` | The absolute path to the directory in the repository from which files and subdirectories are synchronized to the file system of the device. The `Path` directory corresponds to the root directory ( `/` ) on the device, unless you specify the `MountPath` parameter. |
|  `MountPath` | Optional. The absolute path to the directory in the file system of the device to write the content of the repository to. By default, the value is the file system root ( `/` ). |


The `Repository` resource defines the Git repository, the protocol, and the access credentials that the Red Hat Edge Manager must use. You only need to set up the repository once. After setting up, you can use the repository to configure individual devices or device fleets.

#### 6.4.1.2. Secrets from a Kubernetes cluster




The Red Hat Edge Manager can query only the Kubernetes cluster that the Red Hat Edge Manager is running on for a Kubernetes secret. You can write the content of that secret to a path on the device file system.

The Kubernetes Secret Provider takes the following parameters:

| Parameter | Description |
| --- | --- |
|  `Name` | The name of the secret. |
|  `NameSpace` | The namespace of the secret. |
|  `MountPath` | The directory in the file system of the device to write the secret contents to. |


Note
The Red Hat Edge Manager needs permission to access secrets in the defined namespace. For example, creating a `ClusterRole` and `ClusterRoleBinding` allows the `flightctl-worker` service account to get and list secrets in that namespace.



#### 6.4.1.3. Configuration from an HTTP server




The Red Hat Edge Manager can query an HTTP server for configuration. The HTTP server can serve static or dynamically generated configuration for a device.

The HTTP Config Provider takes the following parameters:

| Parameter | Description |
| --- | --- |
|  `Repository` | The name of a `Repository` resource defined in the Red Hat Edge Manager. |
|  `Suffix` | The suffix to append to the base URL defined in the `Repository` resource. The suffix can include path and query parameters, for example `/path/to/endpoint?query=param` . |
|  `FilePath` | The absolute path to the file in the file system of the device to write the response of the HTTP server to. |


The `Repository` resource specifies the HTTP server for the Red Hat Edge Manager to connect to, and the protocol and access credentials to use. You must set up the repository needs once, and then you can use the repository to configure many devices or device fleets.

#### 6.4.1.4. Configuration inline in the device specification




You can specify configuration inline in a device specification. When you use the inline device specification, the Red Hat Edge Manager does not need to connect to external systems to fetch the configuration.

The Inline Config Provider takes a list of file specifications, where each file specification takes the following parameters:

| Parameter | Description |
| --- | --- |
|  `Path` | The absolute path to the file in the file system of the device to write the content to. If a file already exists in the specified path, the file is overwritten. |
|  `Content` | The UTF-8 or base64-encoded content of the file. |
|  `ContentEncoding` | Defines how the contents are encoded. Must be either `plain` or `base64` . Default value is set to `plain` . |
|  `Mode` | Optional. The permission mode of the file. You can specify the octal with a leading zero, for example `0644` , or as a decimal without a leading zero, for example `420` . The `setuid` , `setgid` , and `sticky` bits are supported. If not specified, the permission mode for files defaults to `0644` . |
|  `User` | Optional. The owner of the file. Specified either as a name or numeric ID. Default value is set to `root` . |
|  `Group` | Optional. The group of the file. Specified either as a name or numeric ID. |


**Additional resources**

- For more information about device lifecycle hooks and the default rules used by the Red Hat Edge Manager agent, see [Use device lifecycle hooks](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-device-lifecycle) .


### 6.4.2. Managing the device configuration from a Git repository on the CLI




Create and apply a device configuration in a Git repository.

Complete the following steps:

**Procedure**

1. Create a file, for example `    site-settings-repo.yaml` , that contains the following definition for a `    Repository` resource, named `    site-settings` :


```
apiVersion: flightctl.io/v1alpha1    kind: Repository    metadata:      name: site-settings    spec:      type: git      url: https://github.com/&lt;your_org&gt;/&lt;your_repo&gt;.git
```


1. Create the `    Repository` resource by running the following command:


```
flightctl apply -f site-settings-repo.yaml
```


1. Verify that the resource has been correctly created and is accessible by Red Hat Edge Manager running the following command:


```
flightctl get repository/site-settings
```

See the following example output:


```
NAME           TYPE  REPOSITORY URL                                 ACCESSIBLE    site-settings  git   https://github.com/&lt;your_org&gt;/&lt;your_repo&gt;.git  True
```


1. Apply the `    example-site` configuration to a device by updating the device specification:


```
apiVersion: flightctl.io/v1alpha1    kind: Device    metadata:      name: &lt;device_name&gt;    spec:    [...]      config:<span id="CO5-1"><!--Empty--></span><span class="callout">1</span>- name: example-site        configType: GitConfigProviderSpec        gitRef:          repository: site-settings          targetRevision: production          path: /etc/example-site<span id="CO5-2"><!--Empty--></span><span class="callout">2</span>[...]
```




## 6.5. Use device lifecycle hooks




The Red Hat Edge Manager agent can run user-defined commands at specific points in the device lifecycle by using device lifecycle hooks. For example, you can add a shell script to your operating system images that backs up your application data. You can then specify that the script must run and complete successfully before the agent can start updating the operating system.

As another example, certain applications or system services do not automatically reload their configuration file when the file changes on the disk. You can manually reload the configuration file by specifying a command as another hook, which is called after the agent completes the update process.

The following device lifecycle hooks are supported:

| Lifecycle Hook | Description |
| --- | --- |
|  `beforeUpdating` | This hook is called after the agent completed preparing for the update and before actually making changes to the system. If an action in this hook returns with failure, the agent cancels the update. |
|  `afterUpdating` | This hook is called after the agent has written the update to disk. If an action in this hook returns with failure,the agent cancels and rolls back the update. |
|  `beforeRebooting` | This hook is called before the system reboots. The agent blocks the reboot until running the action has completed or timed out. If any action in this hook returns with failure, the agent cancels and rolls back the update. |
|  `afterRebooting` | This hook is called when the agent first starts after a reboot. If any action in this hook returns with failure, the agent reports this but continues starting up. |


### 6.5.1. Rule files




You can define device lifecycle hooks by adding rule files to one of the following locations in the device file system:

- Rules in the `    /usr/lib/flightctl/hooks.d/&lt;lifecycle_hook_name&gt;/` drop-in directory are read-only. To add rules to the `    /usr` directory, you must add them to the operating system image during image building.
- Rules in the `    /etc/flightctl/hooks.d/&lt;lifecycle_hook_name&gt;/` drop-in directory are read-writable. You can update the rules at runtime by using several methods.


When creating and placing the files, you must consider the following practices:

- The name of the rule must be all lower case.
- If you define rules in both locations, the rules are merged.
- If you add more than one rule files to a lifecycle hook directory, the files are processed in lexical order of the file names.
- If you define files with identical file names in both locations, the file in the `    /etc` folder takes precedence over the file of the same name in the `    /usr` folder.


A rule file is written in YAML format and has a list of one or more actions. An action can be an instruction to run an external command.

When you specify many actions for a hook, the actions are performed in sequence, finishing one action before starting the next.

If an action returns with a failure, the following actions are skipped.

A `run` action takes the following parameters:

| Parameter | Description |
| --- | --- |
|  `Run` | The absolute path to the command to run, followed by any flags or arguments, for example `/usr/bin/nmcli connection reload` . The command is not executed in a shell, so you cannot use shell variables, such as `$PATH` or `$HOME` , or chain commands, such as `|` or `;` . If necessary, you can start a shell by specifying the shell as command to run, for example `/usr/bin/bash -c 'echo $SHELL $HOME $USER'` . |
|  `EnvVars` | Optional. A list of key-value pairs to set as environment variables for the command. |
|  `WorkDir` | Optional. The directory the command is run from. |
|  `Timeout` | Optional. The maximum duration that is allowed for the action to complete. Specify the duration as a single positive integer followed by a time unit. The `s` , `m` , and `h` units are supported for seconds, minutes, and hours. |
|  `If` | Optional. A list of conditions that must be true for the action to be run. If not provided, actions run unconditionally. |


By default, the system performs actions every time the hook is triggered. However, for the `afterUpdating` hook, you can use the `If` parameter to add conditions that must be true for an action to be performed. Otherwise, the action is skipped.

For example, to run an action only if a given file or directory changes during the update, you can define a path condition that takes the following parameters:

| Parameter | Description |
| --- | --- |
|  `Job type` | An absolute path to a file or directory that must change during the update as a condition for the action to be performed. Specify paths by using forward slashes (/):

- If the path is to a directory, it must end with a forward slash ( `    /` ).
- If you specify a path to a file, the file must have changed to satisfy the condition
- If you specify a path to a directory, a file in that directory or any of its subdirectories must have changed to satisfy the condition |
|  `Op` | A list of file operations, such as `created` , `updated` , and `removed` , to limit the type of changes to the specified path as a condition for the action to be performed. |


If you specify a path condition for an action in the `afterUpdating` hook, you have the following variables that you can include in arguments to your command and are replaced with the absolute paths to the changed files:

| Variable | Description |
| --- | --- |
|  `${ Path }` | The absolute path to the file or directory specified in the path condition. |
|  `${ Files }` | A space-separated list of absolute paths of the files that changed during the update and are covered by the path condition. |
|  `${ CreatedFiles }` | A space-separated list of absolute paths of the files that were created during the update and are covered by the path condition. |
|  `${ UpdatedFiles }` | A space-separated list of absolute paths of the files that were updated during the update and are covered by the path condition. |
|  `${ RemovedFiles }` | A space-separated list of absolute paths of the files that were removed during the update and are covered by the path condition. |


The Red Hat Edge Manager agent includes a built-in set of rules defined in `/usr/lib/flightctl/hooks.d/afterupdating/00-default.yaml` . The following commands are executed if certain files are changed:

| File | Command | Description |
| --- | --- | --- |
|  `/etc/systemd/system/` |  `systemctl daemon-reload` | Changes to `systemd` units are activated by signaling the `systemd` daemon to reload the `systemd` manager configuration. This reruns all generators, reloads all unit files, and re-creates the entire dependency tree. |
|  `/etc/NetworkManager/system-connections/` |  `nmcli conn reload` | Changes to `NetworkManager` system connections are activated by signaling the `NetworkManager` daemon to reload all connections. For more information, see the _Additional resources_ section. |
|  `/etc/firewalld/` |  `firewall-cmd --reload` | Changes to the permanent configuration of `firewalld` are activated by signaling `firewalld` to reload firewall rules as new runtime configuration. |


**Additional resources**

- For more information, see [Configuring and managing networking](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/index) .


## 6.6. Monitor device resources




You can set up monitors for device resources and define alerts when the use of these resources crosses a defined threshold. When the agent alerts the Red Hat Edge Manager service, the service sets the device status to "degraded" or "error" (depending on the severity level).

Resource monitors take the following parameters:

| Parameter | Description |
| --- | --- |
| MonitorType | The resource to monitor. Currently supported resources are "CPU", "Memory", and "Disk". |
| SamplingInterval | The interval in which the monitor samples use, specified as positive integer followed by a time unit ("s" for seconds, "m" for minutes, "h" for hours). |
| AlertRules | A list of alert rules. |
| Path | (Disk monitor only) The absolute path to the directory to monitor. Utilization reflects the filesystem containing the path, similar to df, even if it’s not a mount point. |


Alert rules take the following parameters:

| Parameter | Description |
| --- | --- |
| Severity | The alert rule’s severity level out of "Info", "Warning", or "Critical". Only one alert rule is allowed per severity level and monitor. |
| Duration | The duration that resource use is measured and averaged over when sampling, specified as positive integer followed by a time unit ("s" for seconds, "m" for minutes, "h" for hours). It must be smaller than the sampling interval. |
| Percentage | The use threshold that triggers the alert, as percentage value (range 0 to 100 without the "%" sign). |
| Description | A human-readable description of the alert. This is useful for adding details about the alert that might help with debugging. By default it populates the alert as : load is above >% for more than. |


### 6.6.1. Monitoring device resources on the CLI




Monitor the resources of your device through the CLI, providing you with the tools and commands to track performance and troubleshoot issues.

**Procedure**

- Add resource monitors in the `    resources:` section of the device’s specification.


For example, add the following monitor for your disk:

```
apiVersion: flightctl.io/v1alpha1
kind: Device
metadata:
name: &lt;device_name&gt;
spec:
[...]
resources:
- monitorType: Disk
samplingInterval: 5s<span id="CO6-1"><!--Empty--></span><span class="callout">1</span>path: /application_data<span id="CO6-2"><!--Empty--></span><span class="callout">2</span>alertRules:
- severity: Warning<span id="CO6-3"><!--Empty--></span><span class="callout">3</span>duration: 30m
percentage: 75
description: Disk space for application data is &gt;75% full for over 30m.
- severity: Critical<span id="CO6-4"><!--Empty--></span><span class="callout">4</span>duration: 10m
percentage: 90
description: Disk space for application data is &gt;90% full over 10m.
[...]
```

# Chapter 7. Managing applications on an edge device




You can deploy, update, or remove applications on a device by updating the list of applications in the device specification. When the Red Hat Edge Manager agent checks in and detects the change in the specification, the agent downloads any new or updated application packages and images from an Open Container Initiative (OCI)-compatible registry. Then, the agent deploys the packages to the appropriate application runtime or removes them from that runtime.

The Red Hat Edge Manager supports the `podman-compose` tool as the application runtime and format.

**Prerequisites**

- You must install the Red Hat Edge Manager CLI.
- You must log in to the Red Hat Edge Manager service.
- Your device must run an operating system image with the `    podman-compose` tool installed.


For more information, see [Building a bootc operating system image for use with the Red Hat Edge Manager](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-build-bootc) .

## 7.1. Building an application package image




The Red Hat Edge Manager can download application packages from an Open Container Initiative (OCI) compatible registry. You can build an OCI container image that includes your application package in the `podman-compose` format and push the image to your OCI registry.

Complete the following steps:

**Procedure**

1. Define the functionality of the application in a file called `    podman-compose.yaml` that follows the Podman Compose specification:


- Create a file called `        Containerfile` with the following content:


```
FROM scratch<span id="CO7-1"><!--Empty--></span><span class="callout">1</span>COPY podman-compose.yaml /podman-compose.yaml        LABEL appType="compose"<span id="CO7-2"><!--Empty--></span><span class="callout">2</span>
```



1. Build and push the container image to your OCI registry:


1. Define the image repository that you have permissions to write to by running the following command:


```
OCI_IMAGE_REPO=quai.io/&lt;your_org&gt;/&lt;your_image&gt;
```


1. Define the image tag by running the following command:


```
OCI_IMAGE_TAG=v1
```


1. Build the application container image by running the following command:


```
podman build -t ${OCI_IMAGE_REPO}:${OCI_IMAGE_TAG} .
```


1. Push the container image by running the following command:


```
podman push ${OCI_IMAGE_REPO}:${OCI_IMAGE_TAG} .
```





## 7.2. Specify applications inline in the device specification




Application manifests are specified inline in a device’s specification, so you do not need to build an OCI registry application package.

The inline application provider accepts a list of application content with the following parameters:

| Parameter | Description |
| --- | --- |
| Path | The relative path to the file on the device. Note that any existing file is overwritten. |
| Content (Optional) | The plain text (UTF-8) or base64-encoded content of the file. |
| ContentEncoding | How the contents are encoded. Must be either "plain" or "base64". Defaults to "plain". |


**Example**

```
apiVersion: flightctl.io/v1alpha1
kind: Device
metadata:
name: some_device_name
spec:
[...]
applications:
- name: my-app
appType: compose
inline:
- content: |
version: "3.8"
services:
service1:
image:  quay.io/flightctl-tests/alpine:v1
command: ["sleep", "infinity"]
path: podman-compose.yaml
[...]
```


Note
Inline compose applications can have two paths at most. You must name the first one `podman-compose.yaml` , and the second (override) `podman-compose.override.yaml` .



## 7.3. Deploying applications to a device using the CLI




Deploy an application package to a device from an OCI registry by using the CLI.

Complete the following steps:

**Procedure**

1. Specify the application package that you want to deploy in the `    spec.applications` field in the `    Device` resource:


```
apiVersion: flightctl.io/v1alpha1    kind: Device    metadata:      name: &lt;device_name&gt;    spec:    [...]      applications:      - name: wordpress<span id="CO8-1"><!--Empty--></span><span class="callout">1</span>image: quay.io/rhem-demos/wordpress-app:latest<span id="CO8-2"><!--Empty--></span><span class="callout">2</span>envVars:<span id="CO8-3"><!--Empty--></span><span class="callout">3</span>WORDPRESS_DB_HOST: &lt;database_host&gt;          WORDPRESS_DB_USER: &lt;user_name&gt;          WORDPRESS_DB_PASSWORD: &lt;password&gt;    [...]
```

Note
For each application in the `    applications` section of the device specification, you can find the corresponding device status information.




1. Verify the status of an application deployment on a device by inspecting the device status information by running the following command:


```
flightctl get device/&lt;your_device_id&gt; -o yaml
```

See the following example output:


```
[...]    spec:      applications:      - name: example-app        image: quay.io/flightctl-demos/example-app:v1    status:      applications:      - name: example-app        ready: 3/3        restarts: 0        status: Running      applicationsSummary:        info: All application workloads are healthy.        status: Healthy    [...]
```




# Chapter 8. Device fleets




The Red Hat Edge Manager simplifies the management of a large number of devices and workloads through _device fleets_ . A fleet is a resource that defines a group of devices governed by a common device template and management policies.

When you make a change to the device template, all devices in the fleet receive the changes when the Red Hat Edge Manager agent detects the new target specification.

Device monitoring in a fleet is also simplified because you can check the status summary of the whole fleet.

Fleet-level management offers the following advantages:

- Scales your operations because you perform operations only once for each fleet instead of once for each device.
- Minimizes the risk of configuration mistakes and configuration drift.
- Automatically applies the target configuration when you add devices to the fleet or replace devices in the fleet. The fleet specification consists of the following features:




You can have both individually managed and fleet-managed devices at the same time.

When you select a device into a fleet, the Red Hat Edge Manager creates the device specification for the new device based on the device template. If you update the device template for a fleet or a new device joins the fleet, the Red Hat Edge Manager enforces the new specification in the fleet.

If a device is not selected into any fleets, the device is considered user-managed or unmanaged. For user-managed devices, you must update the device specification either manually or through an external automation.

Important
A device cannot be a member of more than one fleet at the same time.



For more information, see [Labels and label selectors](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-labels) .

## 8.1. Device selection into a fleet




By default, devices are not assigned to a fleet. Instead, each fleet uses a selector that defines which labels a device must have to be added to the fleet.

To understand how to use labels in a fleet, see the following example.

The following list shows point-of-sales terminal devices and their labels:

| Device | Labels |
| --- | --- |
| A |  `type: pos-terminal` , `region: east` , `stage: production` |
| B |  `type: pos-terminal` , `region: east` , `stage: development` |
| C |  `type: pos-terminal` , `region: west` , `stage: production` |
| D |  `type: pos-terminal` , `region: west` , `stage: development` |


If all point-of-sale terminals use the same configuration and are managed by the same operations team, you can define a single fleet called `pos-terminals` with the `type=pos-terminal` label selector. Then, the fleet contains devices A, B, C, and D.

However, you might want to create separate fleets for the different organizations for development or production. You can define a fleet for development with the `type=pos-terminal, stage=development` label selector, which selects devices C and D. Then, you can define another fleet for production with the `type=pos-terminal, stage=production` label selector. By using the correct label selectors, you can manage both fleets independently.

Important
You must define selectors in a way that two fleets do not select the same device. For example, if one fleet selects `region=east` , and another fleet selects `stage=production` , both fleets try to select device A. If two fleets try to select the same device, the Red Hat Edge Manager keeps the device in the currently assigned fleet, if any, and sets the `OverlappingSelectors` condition on the affected fleets to `true` .



## 8.2. Device templates




A device template of a fleet contains a device specification that is applied to all devices in the fleet when the template is updated.

For example, you can specify in the device template of a fleet that all devices in the fleet must run the `quay.io/flightctl/rhel:9.5` operating system image.

The Red Hat Edge Manager service then rolls out the target specification to all devices in the fleet, and the Red Hat Edge Manager agents update each device.

You can change other specification items in the device template and the Red Hat Edge Manager applies the changes in the same way.

However, sometimes not all of the devices in the fleet need to have the exact same specification. The Red Hat Edge Manager allows templates to contain placeholders that are populated based on the device name or label values.

The syntax of the placeholders matches that of [Go templates](https://pkg.go.dev/text/template) . However, you can only use simple text and actions.

The use of conditionals or loops in the placeholders is not supported.

You can reference anything from the metadata of a device, such as `{{ .metadata.labels.key }}` or `{{ .metadata.name }}` .

You can also use the following functions in your placeholders:

- The `    upper` function changes the value to uppercase. For example, the function is `    {{ upper .metadata.name }}` .
- The `    lower` function changes the value to lowercase. For example, the function is `    {{ lower .metadata.labels.key }}` .
- The `    replace` function replaces all occurrences of a substring with another string. For example, the function is `    {{ replace "old" "new" .metadata.labels.key }}` .
- The `    getOrDefault` function returns a default value if accessing a missing label. For example, the function is `    {{ getOrDefault .metadata.labels "key" "default" }}` . You can combine the functions in pipelines, for example, a combined function is `    {{ getOrDefault .metadata.labels "key" "default" | upper | replace " " "-" }}` .


Note
Ensure you are using proper Go template syntax. For example, `{{ .metadata.labels.target-revision }}` is not valid because of the hyphen. Instead, you must refer to the field as `{{ index .metadata.labels "target-revision" }}` .



You can use the placeholders in device templates in the following ways:

- You can label devices by deployment stage, for example, stage labels are `    stage: testing` and `    stage: production` . Then, you can use the label with the `    stage` key as placeholder when referencing the operating system image to use, for example, use `    quay.io/myorg/myimage:latest-{{ .metadata.labels.stage }}` or when referencing a configuration folder in a Git repository.
- You can label devices by deployment site, for example, deployment sites are `    site: factory-berlin` and `    site: factory-madrid` .
- Then, you can use the label with the `    site` key as parameter when referencing the secret with network access credentials in Kubernetes. The following fields in device templates support placeholders:

| Field | Placeholders supported in |
| --- | --- |
| Operating System Image | repository name, image name, image tag |
| Git Config Provider | target revision, path |
| HTTP Config Provider | URL suffix, path |
| Inline Config Provider | content, path |





## 8.3. Adding devices to a fleet on the web UI




Define the label selector to add devices into a fleet on the web UI.

Complete the following tasks:

**Procedure**

1. From the navigation panel, selectApplication Links→Edge Manager. This opens the external Edge Manager instance.
1. From the navigation panel, select **Fleets** . Select the fleet that you want to add devices to.
1. ClickActionsand select **Edit fleet** .
1. In the **General info** tab, click **Add label** under the **Device selector** option.
1. Add the label to select devices for your fleet. Any devices with that label are added to the fleet.


## 8.4. Adding devices to a fleet on the CLI




Define the label selector to add devices into a fleet.

Complete the following tasks:

**Procedure**

1. Run the following command to verify that the label selector returns the devices that you want to add to the fleet:


```
flightctl get devices -l type=pos-terminal -l stage=development
```


1. If running the command returns the expected list of devices, you can define a fleet that selects the devices by using the following YAML file:


```
apiVersion: flightctl.io/v1alpha1    kind: Fleet    metadata:      name: my_fleet    spec:      selector:        matchLabels:          type: pos-terminal          stage: development    [...]
```


1. Apply the change by running the following command:


```
flightctl apply -f my_fleet.yaml
```


1. Check for any overlaps with the selector of other fleets by running the following command:


```
flightctl get fleets/my_fleet -o json | jq -r '.status.conditions[] | select(.type=="OverlappingSelectors").status'
```

See the following example output:


```
False
```




## 8.5. Rollout device selection




When performing a rollout by using `flightctl` , you must manage which devices participate in the rollout and how much disruption is acceptable. The device selection process and the rollout disruption budget concept ensure controlled and predictable rollouts.

The process and configuration for selecting devices during a rollout includes targeting strategies, batch sequencing, and success criteria for controlled software deployment.

### 8.5.1. Device targeting




A rollout applies only to devices that belong to a fleet. Each device can belong to only a single fleet. Since rollout definitions are done at the fleet level, the selection process determines which devices within a fleet that participate in a batch rollout based on label criteria. After processing all batches, all fleet devices are rolled out.

-  **Labels** : Devices with specific metadata labels can be targeted for rollouts.
-  **Fleet membership** : Rollouts apply only to devices within the specified fleet.


### 8.5.2. Device selection strategy




The Red Hat Edge Manager supports only the `BatchSequence` strategy for device selection. This strategy defines a stepwise rollout process where devices are added in batches based on specific criteria. Batches are executed sequentially. After each batch completes, execution proceeds to the next batch only if the success rate of the previous batch meets or exceeds the configured success threshold.

The success rate is determined as:

```
# of successful rollouts in the batch / # of devices in the batch &gt;= success threshold
```

In a batch sequence, the final batch is an implicit batch and it is not specified in the batch sequence. It selects all devices in a fleet that have not been selected by the explicit batches in the sequence.

### 8.5.3. Limit in device selection




Each batch in the `BatchSequence` strategy might use an optional `limit` parameter to define how many devices should be included in the batch. You can specify the limit can in two ways:

-  **Absolute number** : A fixed number of devices to be selected.
-  **Percentage** : The percentage of the total matching device population to be selected.


- If you provide a `        selector` with labels, the percentage is calculated based on the number of devices that match the label criteria within the fleet.
- If you do not provide a `        selector` , the percentage is applied to all devices in the fleet.



### 8.5.4. Success threshold




The `successThreshold` defines the percentage of successfully updated devices required to continue the rollout. If the success rate falls below this threshold, the rollout might be paused to prevent further failures.

**Example**

The following shows an example YAML configuration for a fleet specification:


```
apiVersion: v1alpha1
kind: Fleet
metadata:
name: default
spec:
selector:
matchLabels:
fleet: default
rolloutPolicy:
deviceSelection:
strategy: 'BatchSequence'
sequence:
- selector:
matchLabels:
site: madrid
limit: 1  # Absolute number
- selector:
matchLabels:
site: madrid
limit: 80%  # Percentage of devices matching the label criteria within the fleet
- limit: 50%  # Percentage of all devices in the fleet
- selector:
matchLabels:
site: paris
- limit: 80%
- limit: 100%
successThreshold: 95%
```

In this example, there are 6 explicit batches and 1 implicit batch:

- The first batch selects 1 device having a label **site:madrid** .
- With the second batch 80% of all devices having the label **site:madrid** are either selected for rollout in the current batch or were previously selected for rollout.
- With the third batch 50% of all devices are either selected for rollout in the current batch or were previously selected for rollout.
- With the fourth batch all devices that were not previously selected and have the label **site:paris** are selected.
- With the fifth batch 80% of all devices are either selected for rollout in the current batch or were previously selected for rollout.
- With the sixth batch 100% of all devices are either selected for rollout in the current batch or were previously selected for rollout.
- The last implicit batch selects all devices that have not been selected in any previous batch (might be none).


## 8.6. Rollout disruption budget




A rollout disruption budget defines the acceptable level of service impact during a rollout. This ensures that a deployment does not take down too many devices at once, maintaining overall system stability.

### 8.6.1. Disruption budget parameters




-  `    groupBy` : Defines how devices are grouped when applying the disruption budget. The grouping is done by label keys.
-  `    minAvailable` : Specifies the minimum number of devices that must remain available during a rollout.
-  `    maxUnavailable` : Limits the number of devices that can be unavailable at the same time.


**Example**

The following shows an example YAML configuration for a fleet specification:


```
apiVersion: v1alpha1
kind: Fleet
metadata:
name: default
spec:
selector:
matchLabels:
fleet: default
rolloutPolicy:
disruptionBudget:
groupBy: ['site', 'function']
minAvailable: 1
maxUnavailable: 10
```

In this example, the grouping is performed on 2 label keys: **site** and **function** . A group for disruption budget consists of all devices in a fleet having the same label values for the preceding label keys. For every such group the conditions defined in this specification are continuously enforced.

# Chapter 9. Troubleshooting Red Hat Edge Manager




When working with devices in Red Hat Edge Manager, you might see issues related to configuration, connectivity, or deployment. Troubleshooting these issues requires understanding how device configurations are applied, how to check logs, and how to verify communication between the device and the service.

## 9.1. Viewing a device’s effective target configuration




The device manifest returned by the `flightctl get device` command still only has references to external configuration and secret objects. Only when the device agent queries the service, the service replaces the references with the actual configuration and secret data. While this better protects potentially sensitive data, it also makes troubleshooting faulty configurations hard. This is why a user can be authorized to query the effective configuration as rendered by the service to the agent.

**Procedure**

- To query the effective configuration, use the following command:


```
flightctl get device/${device_name} --rendered | jq
```




## 9.2. Generating a device log bundle




The device includes a script that generates a bundle of logs necessary to debug the agent.

**Procedure**

- Run the following command on the device and include the .tar file in the bug report.

Note
This depends on an SSH connection to extract the .tar file.




```
sudo flightctl-must-gather
```





<span id="idm140539236684896"></span>
# Legal Notice

Copyright© 2025 Red Hat, Inc.
The text of and illustrations in this document are licensed by Red Hat under a Creative Commons Attribution–Share Alike 3.0 Unported license ("CC-BY-SA"). An explanation of CC-BY-SA is available at [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/) . In accordance with CC-BY-SA, if you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, Red Hat Enterprise Linux, the Shadowman logo, the Red Hat logo, JBoss, OpenShift, Fedora, the Infinity logo, and RHCE are trademarks of Red Hat, Inc., registered in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
Java® is a registered trademark of Oracle and/or its affiliates.
XFS® is a trademark of Silicon Graphics International Corp. or its subsidiaries in the United States and/or other countries.
MySQL® is a registered trademark of MySQL AB in the United States, the European Union and other countries.
Node.js® is an official trademark of Joyent. Red Hat is not formally related to or endorsed by the official Joyent Node.js open source or commercial project.
TheOpenStack® Word Mark and OpenStack logo are either registered trademarks/service marks or trademarks/service marks of the OpenStack Foundation, in the United States and other countries and are used with the OpenStack Foundation's permission. We are not affiliated with, endorsed or sponsored by the OpenStack Foundation, or the OpenStack community.
All other trademarks are the property of their respective owners.





