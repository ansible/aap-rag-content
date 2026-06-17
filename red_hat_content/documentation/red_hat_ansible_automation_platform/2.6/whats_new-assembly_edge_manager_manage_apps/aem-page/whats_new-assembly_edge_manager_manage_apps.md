+++
title = "Manage applications on an edge device - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_manage_apps"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_manage_apps/aem-page/whats_new-assembly_edge_manager_manage_apps.html"
last_crumb = "Manage applications on an edge device"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Manage applications on an edge device"
oversized = "false"
page_slug = "whats_new-assembly_edge_manager_manage_apps"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_manage_apps"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_manage_apps/toc/toc.json"
type = "aem-page"
+++

# Manage applications on an edge device

Modify the application list in the device specification to deploy, update, or remove applications. The Red Hat Edge Manager agent detects changes upon check-in, downloads new or updated Open Container Initiative (OCI) packages and images, and manages their deployment or removal at runtime.

The Red Hat Edge Manager supports the `podman-compose` tool as the application runtime and format.

## Build an application package image

The Red Hat Edge Manager can download application packages from an Open Container Initiative (OCI) compatible registry. You can build an OCI container image that includes your application package in the `podman-compose` format and push the image to your OCI registry.

### Before you begin

- You must install the Red Hat Edge Manager CLI.
- You must log in to the Red Hat Edge Manager service.
- Your device must run an operating system image with the `podman-compose` tool installed.

### About this task

### Procedure

1.  Define the functionality of the application in a file called `podman-compose.yaml` that follows the Podman Compose specification:

  - Create a file called `Containerfile` with the following content:

```bash
FROM scratch
COPY podman-compose.yaml /podman-compose.yaml
LABEL appType="compose"
```


FROM scratch
Embeds the compose file in a `scratch` container.

LABEL appType="compose"
Adds the `appType=compose` label.

2.  Build and push the container image to your OCI registry:
  1.  Define the image repository that you have permissions to write to by running the following command:
  

```bash
OCI_IMAGE_REPO=quai.io/<your_org>/<your_image>
```

  2.  Define the image tag by running the following command:
  

```bash
OCI_IMAGE_TAG=v1
```

  3.  Build the application container image by running the following command:
  

```bash
podman build -t ${OCI_IMAGE_REPO}:${OCI_IMAGE_TAG} .
```

  4.  Push the container image by running the following command:
  

```bash
podman push ${OCI_IMAGE_REPO}:${OCI_IMAGE_TAG} .
```

## Specify applications inline in the device specification

Application manifests are specified inline in a device’s specification, so you do not need to build an OCI registry application package.

The inline application provider accepts a list of application content with the following parameters:

| Parameter              | Description                                                                                  |
| ---------------------- | -------------------------------------------------------------------------------------------- |
| <br>Path               | <br>The relative path to the file on the device. Note that any existing file is overwritten. |
| <br>Content (Optional) | <br>The plain text (UTF-8) or base64-encoded content of the file.                            |
| <br>ContentEncoding    | <br>How the contents are encoded. Must be either "plain" or "base64". Defaults to "plain".   |


 **Example**

```yaml
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


Note:

Inline compose applications can have two paths at most. You must name the first one `podman-compose.yaml`, and the second (override) `podman-compose.override.yaml`.

## Deploy applications to a device using the CLI

Deploy application packages securely from an OCI registry onto a target device by using the Red Hat Edge Manager CLI. Specifying the container image reference in the device manifest automatically triggers the transactional deployment through the device agent.

### About this task

### Procedure

1.  Specify the application package that you want to deploy in the `spec.applications` field in the `Device` resource:
  

```yaml
apiVersion: flightctl.io/v1alpha1
kind: Device
metadata:
  name: <device_name>
spec:
[...]
  applications:
  - name: wordpress
    image: quay.io/rhem-demos/wordpress-app:latest
    envVars:
      WORDPRESS_DB_HOST: <database_host>
      WORDPRESS_DB_USER: <user_name>
      WORDPRESS_DB_PASSWORD: <password>
[...]
```


name
A user-defined name for the application that is used when the web console and the CLI list applications.

image
A reference to an application package in an OCI registry.

envVars
Optional. A list of key-value pairs that are passed to the deployment tool as environment variables or command line flags.

  Note:
      For each application in the `applications` section of the device specification, you can find the corresponding device status information.

2.  Verify the status of an application deployment on a device by inspecting the device status information by running the following command:
  

```bash
flightctl get device/<your_device_id> -o yaml
```
    See the following example output:

```yaml
[...]
spec:
  applications:
  - name: example-app
    image: quay.io/flightctl-demos/example-app:v1
status:
  applications:
  - name: example-app
    ready: 3/3
    restarts: 0
    status: Running
  applicationsSummary:
    info: All application workloads are healthy.
    status: Healthy
[...]
```
