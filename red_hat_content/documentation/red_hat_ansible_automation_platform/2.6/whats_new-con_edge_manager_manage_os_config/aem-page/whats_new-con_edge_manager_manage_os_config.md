+++
template = "docs/aem-title.html"
title = "Operating system configuration for edge devices - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_manage_os_config"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_manage_os_config/aem-page/whats_new-con_edge_manager_manage_os_config.html"
last_crumb = "Operating system configuration for edge devices"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Operating system configuration for edge devices"
oversized = "false"
page_slug = "whats_new-con_edge_manager_manage_os_config"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_manage_os_config"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-con_edge_manager_manage_os_config/toc/toc.json"
type = "aem-page"
+++

# Operating system configuration for edge devices

You can include an operating system-level host configuration in the image to give maximum consistency and repeatability. To update the configuration, create a new operating system image and update devices with the new image.

However, updating devices with a new image can be impractical in the following cases:

- The configuration is missing in the image.
- The configuration needs to be specific to a device.
- The configuration needs to be updateable at runtime without updating the operating system image and rebooting.


For these cases, you can declare a set of configuration files that are present on the file system of the device. The Red Hat Edge Manager agent applies updates to the configuration files while ensuring that either all files are successfully updated in the file system, or rolled back to their pre-update state. If the user updates both an operating system and configuration set of a device at the same time, the Red Hat Edge Manager agent updates the operating system first. It then applies the specified set of configuration files.

You can also specify a list of configuration sets that the Red Hat Edge Manager agent applies in sequence. In case of a conflict, the last applied configuration set is valid.

Important:

After the Red Hat Edge Manager agent updates the configuration on the disk, the running applications need to reload the new configuration into memory for the configuration to become effective. If the update involves a reboot, `systemd` automatically restarts the applications with the new configuration and in the correct order. If the update does not involve a reboot, many applications can detect changes to their configuration files and automatically reload the files. When an application does not support change detection, you can use device lifecycle hooks to run scripts or commands if certain conditions are met.

## Configuration providers

You can provide configuration from many sources, called configuration providers, in Red Hat Edge Manager. The Red Hat Edge Manager currently supports the following configuration providers:

Git Config Provider
Fetches device configuration files from a Git repository.

Kubernetes Secret Provider
Fetches a secret from a Kubernetes cluster and writes the content to the file system of the device.

HTTP Config Provider
Fetches device configuration files from an HTTP(S) endpoint.

Inline Config Provider
Allows specifying device configuration files inline in the device manifest without querying external systems.

## Configuration from a Git repository

You can store device configuration in a Git repository such as GitHub or GitLab. You can then add a Git Config Provider so that the Red Hat Edge Manager synchronizes the configuration from the repository to the file system of the device.

The Git Config Provider takes the following parameters:

| Parameter             | Description                                                                                                                                                                                                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `Repository`     | <br>The name of a `Repository` resource defined in the Red Hat Edge Manager.                                                                                                                                                                                              |
| <br> `TargetRevision` | <br>The branch, tag, or commit of the repository to checkout.                                                                                                                                                                                                             |
| <br> `Path`           | <br>The absolute path to the directory in the repository from which files and subdirectories are synchronized to the file system of the device. The `Path` directory corresponds to the root directory (`/`) on the device, unless you specify the `MountPath` parameter. |
| <br> `MountPath`      | <br>Optional. The absolute path to the directory in the file system of the device to write the content of the repository to. By default, the value is the file system root (`/`).                                                                                         |


The `Repository` resource defines the Git repository, the protocol, and the access credentials that the Red Hat Edge Manager must use. You only need to set up the repository once. After setting up, you can use the repository to configure individual devices or device fleets.

## Secrets from a Kubernetes cluster

The Red Hat Edge Manager can query only the Kubernetes cluster that the Red Hat Edge Manager is running on for a Kubernetes secret. You can write the content of that secret to a path on the device file system.

The Kubernetes Secret Provider takes the following parameters:

| Parameter        | Description                                                                         |
| ---------------- | ----------------------------------------------------------------------------------- |
| <br> `Name`      | <br>The name of the secret.                                                         |
| <br> `NameSpace` | <br>The namespace of the secret.                                                    |
| <br> `MountPath` | <br>The directory in the file system of the device to write the secret contents to. |


Note:

The Red Hat Edge Manager needs permission to access secrets in the defined namespace. For example, creating a `ClusterRole` and `ClusterRoleBinding` allows the `flightctl-worker` service account to get and list secrets in that namespace.

## Configuration from an HTTP server

The Red Hat Edge Manager can query an HTTP server for configuration. The HTTP server can serve static or dynamically generated configuration for a device.

The HTTP Config Provider takes the following parameters:

| Parameter         | Description                                                                                                                                                                   |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `Repository` | <br>The name of a `Repository` resource defined in the Red Hat Edge Manager.                                                                                                  |
| <br> `Suffix`     | <br>The suffix to append to the base URL defined in the `Repository` resource. The suffix can include path and query parameters, for example `/path/to/endpoint?query=param`. |
| <br> `FilePath`   | <br>The absolute path to the file in the file system of the device to write the response of the HTTP server to.                                                               |


The `Repository` resource specifies the HTTP server for the Red Hat Edge Manager to connect to, and the protocol and access credentials to use. You must set up the repository needs once, and then you can use the repository to configure many devices or device fleets.

## Configuration inline in the device specification

You can specify configuration inline in a device specification. When you use the inline device specification, the Red Hat Edge Manager does not need to connect to external systems to fetch the configuration.

The Inline Config Provider takes a list of file specifications, where each file specification takes the following parameters:

| Parameter              | Description                                                                                                                                                                                                                                                                                               |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `Path`            | <br>The absolute path to the file in the file system of the device to write the content to. If a file already exists in the specified path, the file is overwritten.                                                                                                                                      |
| <br> `Content`         | <br>The UTF-8 or base64-encoded content of the file.                                                                                                                                                                                                                                                      |
| <br> `ContentEncoding` | <br>Defines how the contents are encoded. Must be either `plain` or `base64`. Default value is set to `plain`.                                                                                                                                                                                            |
| <br> `Mode`            | <br>Optional. The permission mode of the file. You can specify the octal with a leading zero, for example `0644`, or as a decimal without a leading zero, for example `420`. The `setuid`, `setgid`, and `sticky` bits are supported. If not specified, the permission mode for files defaults to `0644`. |
| <br> `User`            | <br>Optional. The owner of the file. Specified either as a name or numeric ID. Default value is set to `root`.                                                                                                                                                                                            |
| <br> `Group`           | <br>Optional. The group of the file. Specified either as a name or numeric ID.                                                                                                                                                                                                                            |

## Manage the device configuration from a Git repository on the CLI

Integrate your device configuration files with standard Git workflows by defining a Repository resource by using the CLI. This enables the Red Hat Edge Manager to automatically synchronize configuration file updates from the repository onto the device’s file system.

### About this task

### Procedure

1.  Create a file, for example `site-settings-repo.yaml`, that has the following definition for a `Repository` resource, named `site-settings`:
  

```yaml
apiVersion: flightctl.io/v1alpha1
kind: Repository
metadata:
  name: site-settings
spec:
  type: git
  url: https://github.com/<your_org>/<your_repo>.git
```

2.  Create the `Repository` resource by running the following command:
  

```bash
flightctl apply -f site-settings-repo.yaml
```

3.  Verify that the resource has been correctly created and is accessible by Red Hat Edge Manager running the following command:
  

```bash
flightctl get repository/site-settings
```
    See the following example output:

```bash
NAME           TYPE  REPOSITORY URL                                 ACCESSIBLE
site-settings  git   https://github.com/<your_org>/<your_repo>.git  True
```

4.  Apply the `example-site` configuration to a device by updating the device specification:
  

```yaml
apiVersion: flightctl.io/v1alpha1
kind: Device
metadata:
  name: <device_name>
spec:
[...]
  config:
  - name: example-site
    configType: GitConfigProviderSpec
    gitRef:
      repository: site-settings
      targetRevision: production
      path: /etc/example-site
[...]
```


config
The example configuration takes all the files from the `example-site` directory from the `production` branch of the `site-settings` repository and places the files in the root directory (`/`).

gitRef:path
Ensure that the target path is writeable by creating your directory structure. The root directory (`/`) is not writeable in `bootc` systems.
