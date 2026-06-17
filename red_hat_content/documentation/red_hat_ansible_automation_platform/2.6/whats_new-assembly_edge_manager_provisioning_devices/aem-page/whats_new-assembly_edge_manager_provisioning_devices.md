+++
title = "Provision edge devices - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_provisioning_devices"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_provisioning_devices/aem-page/whats_new-assembly_edge_manager_provisioning_devices.html"
last_crumb = "Provision edge devices"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Provision edge devices"
oversized = "false"
page_slug = "whats_new-assembly_edge_manager_provisioning_devices"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_provisioning_devices"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_provisioning_devices/toc/toc.json"
type = "aem-page"
+++

# Provision edge devices

You can provision devices with the Red Hat Edge Manager in different environments. Use the operating system image or disk image that you built for use with the Red Hat Edge Manager. Depending on your target environment, provision a physical or virtual device.

## Provision physical devices

When you build an International Organization for Standardization (ISO) disk image from an operating system image by using the `bootc-image-builder` tool, the image is similar to the RHEL ISOs available for download. However, your operating system image content is embedded in the ISO disk image.

## Provision devices with OpenShift Virtualization

You can provision a virtual machine on OpenShift Virtualization by using a QCoW2 container disk image that is hosted on an OCI container registry.

If your operating system image does not already contain the Red Hat Edge Manager agent enrollment configuration, you can inject the configuration through the `cloud-init` user data at provisioning.

### Create the `cloud-init` configuration

The `cloud-init` configuration customizes a virtual machine instance on its first boot, allowing you to automatically enroll it as a new agent in your Red Hat Edge Manager service.

#### Before you begin

- You installed the `flightctl` CLI and logged in to your Red Hat Edge Manager service instance.
- You installed the `oc` CLI, used it to log in to your OpenShift cluster instance, and changed to the project in which you want to create your virtual machine.

#### About this task

#### Procedure

1.  Request a new Red Hat Edge Manager agent enrollment configuration and store it in a file called `config.yaml` by running the following command:
  

```bash
flightctl certificate request --signer=enrollment --expiration=365d --output=embedded > config.yaml
```

2.  Create a cloud configuration user data file called `cloud-config.yaml` that places the agent configuration in the correct location on the first boot by running the following command:
  

```bash
cat <<EOF > cloud-config.yaml
#cloud-config
write_files:
- path: /etc/flightctl/config.yaml
  content: $(cat config.yaml | base64 -w0)
  encoding: b64
EOF
```

3.  Create a Kubernetes `Secret` that contains the cloud configuration user data file:
  

```bash
oc create secret generic enrollment-secret --from-file=userdata=cloud-config.yaml
```

### Create the virtual machine

Create a virtual machine that has its primary disk populated from your QCoW2 container disk image and a `cloud-init` configuration drive that is populated from your enrollment secret.

#### About this task

Complete the following steps:

#### Procedure

1.  Create a file that has the `VirtualMachine` resource manifest by running the following command:
  

```bash
cat <<EOF > my-bootc-vm.yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: my-bootc-vm
spec:
  runStrategy: RerunOnFailure
  template:
    spec:
      domain:
        cpu:
          cores: 1
        memory:
          guest: 1024M
        devices:
          disks:
            - name: containerdisk
              disk:
                bus: virtio
            - name: cloudinitdisk
              disk:
                bus: virtio
      volumes:
        - name: containerdisk
          containerDisk:
            image: ${OCI_DISK_IMAGE_REPO}:${OCI_IMAGE_TAG}
        - name: cloudinitdisk
          cloudInitConfigDrive:
            secretRef:
              name: enrollment-secret
EOF
```

2.  Apply the resource manifest to your cluster by running the following command:
  

```bash
oc apply -f my-bootc-vm.yaml
```
