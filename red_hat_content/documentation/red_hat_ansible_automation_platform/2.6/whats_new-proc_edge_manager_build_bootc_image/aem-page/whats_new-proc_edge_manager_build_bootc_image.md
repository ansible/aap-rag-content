+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-proc_edge_manager_build_bootc_image"
template = "docs/aem-title.html"
title = "Build the operating system image with bootc - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-proc_edge_manager_build_bootc_image/aem-page/whats_new-proc_edge_manager_build_bootc_image.html"
last_crumb = "Build the operating system image with bootc"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Build the operating system image with bootc"
oversized = "false"
page_slug = "whats_new-proc_edge_manager_build_bootc_image"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-proc_edge_manager_build_bootc_image"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-proc_edge_manager_build_bootc_image/toc/toc.json"
type = "aem-page"
+++

# Build the operating system image with *bootc*

Build the operating system image with the `bootc` that contains the Red Hat Edge Manager agent. You can optionally include the following items in your operating system image:

## About this task

- The agent configuration for early binding
- Any drivers
- Host configuration
- Application workloads that you need


Complete the following steps:

## Procedure

1.  Create a `Containerfile` file with the following content to build a RHEL 9-based operating system image that includes the Red Hat Edge Manager agent and configuration:
2.  Build instructions for the bootc image:
  

```bash
FROM registry.redhat.io/rhel9/rhel-bootc:<required_os_version>
RUN dnf --enablerepo ansible-automation-platform-2.5-for-rhel-9-x86_64-rpms -y install flightctl-agent-0.7.2-1.el9fc  && \
    dnf -y clean all && \
    systemctl enable flightctl-agent.service && \
    systemctl mask bootc-fetch-apply-updates.timer
```


<required_os_version>
The base image referenced in `FROM` is a bootable container (`bootc`) image that already has a Linux kernel. You can reuse existing standard container build tools and workflows.

systemctl mask bootc-fetch-apply-updates.timer
This part of the `RUN` command disables the default automatic updates. The updates are managed by the Red Hat Edge Manager.

  Important:
      If your device relies on containers from a private repository, you must place the device pull secret in the `/etc/ostree/auth.json` path. The pull secret must exist on the device before the secret can be consumed.

  - **Optional:** To enable `podman-compose` application support, add the following section to the `Containerfile` file:

```bash
RUN dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm && \
    dnf -y install podman-compose && \
    dnf -y clean all && \
    systemctl enable podman.service
```

  - **Optional:** If you created the `config.yaml` for early binding, add the following section to the `Containerfile`:

```bash
ADD config.yaml /etc/flightctl/
```

    For more information, see [Optional: Requesting an enrollment certificate for early binding](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_build_bootc#edge-manager-request-cert "If you want to include an agent configuration in the image, complete the following steps:").

3.  Define the Open Container Initiative (OCI) registry by running the following command:
  

```bash
OCI_REGISTRY=registry.redhat.io
```

4.  Define the image repository that you have permissions to write to by running the following command:
  

```bash
OCI_IMAGE_REPO=${OCI_REGISTRY}/<your_org>/<your_image>
```

5.  Define the image tag by running the following command:
  

```bash
OCI_IMAGE_TAG=v1
```

6.  Build the operating system image for your target platform:
  

```bash
sudo podman build -t ${OCI_IMAGE_REPO}:${OCI_IMAGE_TAG} .
```

## Sign and publish the bootc operating system image by using Sigstore

To sign the `bootc` operating system image by using Sigstore, complete the following steps:

### About this task

### Procedure

1.  Generate a Sigstore key pair named `signingkey.pub` and `signingkey.private`:
  

```bash
skopeo generate-sigstore-key --output-prefix signingkey
```

2.  Configure container tools such as Podman and Skopeo to upload Sigstore signatures together with your signed image to your OCI registry:
  

```bash
sudo tee "/etc/containers/registries.d/${OCI_REGISTRY}.yaml" > /dev/null <<EOF
docker:
    ${OCI_REGISTRY}:
        use-sigstore-attachments: true
EOF
```

3.  Log in to your OCI registry by running the following command:
  

```bash
sudo podman login ${OCI_REGISTRY}
```

4.  Sign and publish the operating system image by running the following command:
  

```bash
sudo podman push \
    --sign-by-sigstore-private-key ./signingkey.private \
    ${OCI_IMAGE_REPO}:${OCI_IMAGE_TAG}
```

## Build the operating system disk image

Build the operating system disk image that has the file system for your devices.

### About this task

### Procedure

1.  Create a directory called `output` by running the following command:
  

```bash
mkdir -p output
```

2.  Use `bootc-image-builder` to generate an operating system disk image of type `iso` from your operating system image by running the following command:
  

```bash
sudo podman run --rm -it --privileged --pull=newer \
    --security-opt label=type:unconfined_t \
    -v "${PWD}/output":/output \
    -v /var/lib/containers/storage:/var/lib/containers/storage \
    registry.redhat.io/rhel9/bootc-image-builder:latest \
    --type iso \
    ${OCI_IMAGE_REPO}:${OCI_IMAGE_TAG}
```

### Results

When the `bootc-image-builder` completes, you can find the ISO disk image at the `${PWD}/output/bootiso/install.iso` path.

## Optional: Sign and publish the operating system disk image to an Open Container Initiative registry

Sign and publish disk images to your Open Container Initiative (OCI) registry. Optionally compress them as OCI artifacts for unified distribution with bootc images. To publish an ISO, use a repository named after your `bootc` image with `/diskimage-iso` appended.

### Before you begin

- You created a private key by using Sigstore. See [Signing and publishing the *bootc* operating system image by using Sigstore](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-proc_edge_manager_build_bootc_image#edge-manager-build-sign-image "To sign the bootc operating system image by using Sigstore, complete the following steps:").


Sign and publish your disk image to your OCI registry by completing the following steps:

### About this task

### Procedure

1.  Change the owner of the directory where the ISO disk image is located from `root` to your current user by running the following command:
  

```bash
sudo chown -R $(whoami):$(whoami) "${PWD}/output"
```

2.  Define the `OCI_DISK_IMAGE_REPO` environmental variable to be the same repository as your `bootc` image with `/diskimage-iso` appended by running the following command:
  

```bash
OCI_DISK_IMAGE_REPO=${OCI_IMAGE_REPO}/diskimage-iso
```

3.  Create a manifest list by running the following command:
  

```bash
sudo podman manifest create \
    ${OCI_DISK_IMAGE_REPO}:${OCI_IMAGE_TAG}
```

4.  Add the ISO disk image to the manifest list as an OCI artifact by running the following command:
  

```bash
sudo podman manifest add \
    --artifact --artifact-type application/vnd.diskimage.iso \
    --arch=amd64 --os=linux \
    ${OCI_DISK_IMAGE_REPO}:${OCI_IMAGE_TAG} \
    "${PWD}/output/bootiso/install.iso"
```

5.  Sign the manifest list with your private Sigstore key and push the image to the registry by running the following command:
  

```bash
sudo podman manifest push --all \
     --sign-by-sigstore-private-key ./signingkey.private \
    ${OCI_DISK_IMAGE_REPO}:${OCI_IMAGE_TAG} \
    docker://${OCI_DISK_IMAGE_REPO}:${OCI_IMAGE_TAG}
```

## Additional resources

Access supplementary documentation for detailed guidance on building Red Hat Edge Manager operating system images for different target platforms, including how to configure container pull secrets.

- For more information about building the operating system image on different target platforms, see [Configuring container pull secrets](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#configuring-container-pull-secrets_managing-users-groups-ssh-key-and-secrets-in-image-mode-for-rhel).
