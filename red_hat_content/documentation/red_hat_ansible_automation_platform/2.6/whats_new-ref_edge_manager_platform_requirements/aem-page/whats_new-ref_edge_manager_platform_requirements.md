+++
title = "Requirements for specific target platforms - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_platform_requirements"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_platform_requirements/aem-page/whats_new-ref_edge_manager_platform_requirements.html"
last_crumb = "Requirements for specific target platforms"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Requirements for specific target platforms"
oversized = "false"
page_slug = "whats_new-ref_edge_manager_platform_requirements"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_platform_requirements"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_platform_requirements/toc/toc.json"
type = "aem-page"
+++

# Requirements for specific target platforms

Review the specific requirements and procedures necessary to prepare operating system images for deployment onto target platforms such as Red Hat OpenShift Virtualization and VMware vSphere.

-  [Building images for Red Hat OpenShift Virtualization](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_platform_requirements#edge-manager-virt "When building operating system images and disk images for Red Hat OpenShift Virtualization, you can follow the generic image building process with the following changes:")
-  [Building images for VMware vSphere](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_platform_requirements#edge-manager-vmware "When building operating system images and disk images for VMware vSphere, you can follow the generic image building process with the following changes:")

## Build images for Red Hat OpenShift Virtualization

When building operating system images and disk images for Red Hat OpenShift Virtualization, you can follow the generic image building process with the following changes:

### About this task

- Using late binding by injecting the enrollment certificate or the agent configuration through `cloud-init` when provisioning the virtual device.
- Adding the `open-vm-tools` guest tools to the image.
- Building a disk image of type `qcow2` instead of `iso`.


Complete the generic steps with changes to the following steps:

### Procedure

1.  Build an operating system image based on RHEL 9 that includes the Red Hat Edge Manager agent and VM guest tools but excludes the agent configuration.
2.  Create a file named `Containerfile` with the following content:
  

```bash
FROM registry.redhat.io/rhel9/bootc-image-builder:latest
RUN subscription-manager repos --enable ansible-automation-platform-2.5-for-rhel-9-x86_64-rpms
    dnf -y install flightctl-agent && \
    dnf -y clean all && \
    systemctl enable flightctl-agent.service
RUN dnf -y install cloud-init open-vm-tools && \
    dnf -y clean all && \
    ln -s ../cloud-init.target /usr/lib/systemd/system/default.target.wants && \
    systemctl enable vmtoolsd.service
```

3.  **Optional:** To enable `podman-compose` application support, add the following section to the `Containerfile` file:
  

```bash
RUN dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm && \
    dnf -y install podman-compose && \
    dnf -y clean all && \
    systemctl enable podman.service
```

### Build the bootc image

Build, sign, and publish the `bootc` operating system image by following the generic image building process:

#### About this task

#### Procedure

1.  Create a directory called `output` by running the following command:
  

```bash
mkdir -p output
```

2.  Generate an operating system disk image of type `vmdk` from your operating system image by running the following command:
  

```bash
sudo podman run --rm -it --privileged --pull=newer \
    --security-opt label=type:unconfined_t \
    -v "${PWD}/output":/output \
    -v /var/lib/containers/storage:/var/lib/containers/storage \
    registry.redhat.io/rhel9/bootc-image-builder:latest \
    --type qcow2 \
    ${OCI_IMAGE_REPO}:${OCI_IMAGE_TAG}
```

#### What to do next

When the `bootc-image-builder` completes, you can find the disk image under `${PWD}/output/vmdk/disk.vmdk`.

### Build the QCoW2 disk image

Red Hat OpenShift Virtualization can download disk images from an OCI registry but it expects a container disk image instead of an OCI artifact.

#### About this task

Complete the following steps to build, sign, and upload the QCoW2 disk image:

#### Procedure

1.  Create a file called `Containerfile.qcow2` with the following content:
  

```bash
FROM registry.access.redhat.com/ubi9/ubi:latest AS builder
ADD --chown=107:107 output/qcow2/disk.qcow2 /disk/
RUN chmod 0440 /disk/*
FROM scratch
COPY --from=builder /disk/* /disk/
```


ADD --chown=107:107 output/qcow2/disk.qcow2 /disk/
Adds the QCoW2 disk image to a builder container to set the required `107` file ownership, which is the QEMU user.

RUN chmod 0440 /disk/*
Sets the required `0440` file permissions.

COPY --from=builder /disk/* /disk/
Copies the file to a scratch image.

2.  Build, sign, and publish your disk image by running the following command:
  

```bash
sudo chown -R $(whoami):$(whoami) "${PWD}/output"
OCI_DISK_IMAGE_REPO=${OCI_IMAGE_REPO}/diskimage-qcow2
sudo podman build -t ${OCI_DISK_IMAGE_REPO}:${OCI_IMAGE_TAG} -f Containerfile.qcow2 .
sudo podman push --sign-by-sigstore-private-key ./signingkey.private ${OCI_DISK_IMAGE_REPO}:${OCI_IMAGE_TAG}
```

## Build images for VMware vSphere

When building operating system images and disk images for VMware vSphere, you can follow the generic image building process with the following changes:

### About this task

- Using late binding by injecting the enrollment certificate or the agent configuration through `cloud-init` when provisioning the virtual device.
- Adding the `open-vm-tools` guest tools to the image.
- Building a disk image of type `vmdk` instead of `iso`.


Complete the generic steps with changes to the following steps:

### Procedure

1.  Build an operating system image based on RHEL 9 that includes the Red Hat Edge Manager agent and VM guest tools but excludes the agent configuration.
2.  Create a file named `Containerfile` with the following content:
  

```bash
FROM registry.redhat.io/rhel9/bootc-image-builder:latest
RUN subscription-manager repos --enable ansible-automation-platform-2.5-for-rhel-9-x86_64-rpms
    dnf -y install flightctl-agent && \
    dnf -y clean all && \
    systemctl enable flightctl-agent.service && \
RUN dnf -y install cloud-init open-vm-tools && \
    dnf -y clean all && \
    ln -s ../cloud-init.target /usr/lib/systemd/system/default.target.wants && \
    systemctl enable vmtoolsd.service
```

3.  Create a directory called `output` by running the following command:
  

```bash
mkdir -p output
```

4.  Generate an operating system disk image of type `vmdk` from your operating system image by running the following command:
  

```bash
sudo podman run --rm -it --privileged --pull=newer \
    --security-opt label=type:unconfined_t \
    -v "${PWD}/output":/output \
    -v /var/lib/containers/storage:/var/lib/containers/storage \
    registry.redhat.io/rhel9/bootc-image-builder:latest \
    --type vmdk \
    ${OCI_IMAGE_REPO}:${OCI_IMAGE_TAG}
```

### What to do next

When the `bootc-image-builder` completes, you can find the disk image under `${PWD}/output/vmdk/disk.vmdk`.
