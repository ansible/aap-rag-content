+++
title = "Define, create, and build execution environments - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-define__create__and_build_execution_environments"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-define__create__and_build_execution_environments/", "Define, create, and build execution environments"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-define__create__and_build_execution_environments/aem-page/administer-define__create__and_build_execution_environments.html"
last_crumb = "Define, create, and build execution environments"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Define, create, and build execution environments"
oversized = "false"
page_slug = "administer-define__create__and_build_execution_environments"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-define__create__and_build_execution_environments"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-define__create__and_build_execution_environments/toc/toc.json"
type = "aem-page"
+++

# Define, create, and build execution environments

Run automation consistently across nodes with execution environments, which are container images that contain everything you need to run your automation.

An execution environment is a containerized runtime that provides the following benefits:

- A consistent environment in which to run automation jobs
- Portability and scalability, as you can run automation jobs on any node, including controller and execution nodes
- Security and governance, as you can control what's inside the runtime environment; and you can have approved, signed, and verified container images
- Improved efficiency, as developers need not spend time troubleshooting environment dependencies

An automation execution environment should contain the following::

- Ansible Core 2.16 or later
- Python 3.12 or later
- Ansible Runner
- System dependencies

Ansible Builder is a command line tool that automates the process of building automation execution environments by using metadata defined in various Ansible Collections or created by the user. You build an execution environment before you can create it using automation controller. After building it, you push it to a repository (such as quay) and then, when creating an execution environment in the UI with automation controller, you must point to that repository to use it in Ansible Automation Platform to use it, for example, in a job template.

With Ansible Builder, you can easily create a customizable automation execution environments definition file that specifies the content you want included in your automation execution environments such as Ansible Core, Python, Collections, third-party Python requirements, and system level packages. This enables you to fulfill all of the necessary requirements and dependencies to get jobs running.

Red Hat provides the following pre-built execution environment images:

**ee-minimal**

Contains ansible-core and Ansible Runner, but does not include collections or other content beyond the minimum required dependencies. Use ee-minimal as the base image when you build custom execution environments. This gives you full control over which collections and dependencies are included. ee-minimal images are available for ansible-core 2.16 and 2.20.

Ansible-core 2.18 is available through version-less images only.

**ee-supported**

Contains ansible-core 2.16 and a curated set of Red Hat Certified Ansible Content Collections and their dependencies. Red Hat recommends that you build your own custom execution environments with only the collections you need. You can use ee-supported when you want a ready-to-use execution environment that covers common automation use cases without building a custom image.

ee-supported is available for ansible-core 2.16 only.

For most custom execution environment builds, use ee-minimal as the base image. This approach keeps the image size small and gives you explicit control over every collection, Python package, and system dependency.

## Choose an ansible-core version for your execution environment

Select the appropriate ansible-core version for your execution environment images to ensure compatibility with your Ansible Automation Platform version, managed nodes, and required automation features.

Ansible Automation Platform supports multiple ansible-core versions concurrently through different execution environment images. You can assign different execution environments to different job templates within the same Ansible Automation Platform installation, allowing you to run multiple ansible-core versions side by side.

The platform itself always installs and operates on the default ansible-core version 2.16, but automation jobs execute inside the execution environment image you select.

**Available ansible-core versions**

**ansible-core 2.16 (default)**

The default ansible-core version used to install and operate Ansible Automation Platform. Supported for the entire lifecycle of Ansible Automation Platform 2.4, 2.5, 2.6, and 2.7.

**ansible-core 2.18**

Provides access to newer ansible-core features while maintaining a stable lifecycle. Supported for the entire lifecycle of Ansible Automation Platform 2.5, 2.6, and 2.7.

Managed node compatibility:

- RHEL 9 as a managed node.
- Python 3.8 through 3.13 on managed nodes.
- PowerShell 5.1 on Microsoft Windows managed nodes.
- Microsoft Windows Server 2025 support (requires ansible-core 2.18 or later).

Available as version-less ee-minimal images only. Ansible-core 2.18 versioned multistream images are not yet available in Ansible Automation Platform 2.7. Use version-less ee-minimal images to access ansible-core 2.18.

**ansible-core 2.20**

The latest ansible-core feature stream with the newest capabilities. Supported for the entire lifecycle of Ansible Automation Platform 2.7. Not available in Ansible Automation Platform 2.5 or 2.6.

Managed node compatibility:

- RHEL 9 as a managed node.
- Python 3.9 through 3.14 on managed nodes.
- PowerShell 5.1 on Microsoft Windows managed nodes.

RHEL 8 is not supported as a control node or managed node with ansible-core 2.20.

Available as ee-minimal images only, on RHEL 9.

**Summary**

| Ansible-core   | Ansible Automation Platform version | ee-minimal | ee-supported | RHEL managed nodes |
| -------------- | ----------------------------------- | ---------- | ------------ | ------------------ |
| 2.16 (default) | 2.4, 2.5, 2.6, 2.7                  | Yes        | Yes          | -                  |
| 2.18           | unversioned                         | No         | No           | 8, 9               |
| 2.20           | 2.7 only                            | Yes        | No           | -                  |

**Guidance for choosing a version**

Choose ansible-core 2.16 when:

- You want newer ansible-core features on a stable lifecycle stream.
- All your managed nodes run RHEL 8 or 9.
- You need Microsoft Windows Server 2025 support.

Choose ansible-core 2.20 when:

- You want the latest ansible-core features.
- You are running Ansible Automation Platform 2.7.
- All your managed nodes run RHEL 9.
- You do not require RHEL 8 on any control or managed node.

## Execution environment image index

Locate the registry paths for Ansible Automation Platform 2.7 execution environment images and select the appropriate versioned or version-less tag based on your environment's requirements

The following table lists the execution environment images available for each ansible-core version in Ansible Automation Platform 2.7.

| ansible-core | Base OS | Registry path                                                               |
| ------------ | ------- | --------------------------------------------------------------------------- |
| 2.16         | RHEL 8  | registry.redhat.io/ansible-automation-platform-27/ee-minimal-rhel8:2.16     |
| 2.16         | RHEL 9  | registry.redhat.io/ansible-automation-platform-27/ee-minimal-rhel9:2.16     |
| 2.16         | RHEL 8  | registry.redhat.io/ansible-automation-platform-27/ee-supported-rhel8:latest |
| 2.16         | RHEL 9  | registry.redhat.io/ansible-automation-platform-27/ee-supported-rhel9:latest |
| 2.20         | RHEL 9  | registry.redhat.io/ansible-automation-platform-27/ee-minimal-rhel9:2.20     |

Note:

Ansible-core 2.18 versioned multistream images are not yet available. To use ansible-core 2.18, use the version-less ee-minimal images. See "Versioned and version-less image tags".

**Versioned and version-less image tags**

Versioned multistream images are tagged with a specific Ansible Automation Platform version (for example, `ansible-automation-platform-27/ee-minimal-rhel9:<tag>`) and have fixed, predictable contents tied to that platform release. Use a tag to select the ansible-core version (for example, :2.16 or :2.20).

Version-less images also use an ansible-core tag (for example, ansible-automation-platform/ee-minimal-rhel9:2.18). The contents behind this tag may change when new fixes or ansible-core updates are released.

Use versioned images for production environments where exact reproducibility is required. Use version-less images only when you need an ansible-core version not included in the versioned images.

## Using certified collections with ansible-core 2.18 and 2.20

Incorporate Red Hat Certified Ansible Content Collections into custom execution environments running ansible-core 2.18 or 2.20, and verify their compatibility before deploying them to production.

The ee-supported execution environment image, which includes Red Hat Certified Ansible Content Collections, is available only for ansible-core 2.16. If you build a custom execution environment using an ee-minimal image with ansible-core 2.18 or 2.20, you must add any required collections yourself.

Red Hat Certified Ansible Content Collections are formally certified against ansible-core 2.16. Collections certified for ansible-core 2.16 may work with ansible-core 2.18 and 2.20 but have not been formally certified against those versions.

Before deploying certified collections with ansible-core 2.18 or 2.20 in production, take the following steps:

1. Check the release notes of each collection for ansible-core version compatibility information.
2. Test your custom execution environment in a staging or non-production environment to verify that all collections function correctly with your chosen ansible-core version.
3. Monitor the Red Hat Ansible Certified Content page for updates to collection certification status

## Disconnected environment customizations

Creating execution environments for Ansible Automation Platform is a common task which works differently in disconnected environments. When building a custom execution environment, the ansible-builder tool defaults to downloading content from the following locations on the internet:

- Red Hat Automation hub (console.redhat.com) or Ansible Galaxy (galaxy.ansible.com) for any Ansible content collections added to the execution environment image.
- PyPI (pypi.org) for any python packages required as collection dependencies.
- RPM repositories such as the RHEL or UBI repositories (cdn.redhat.com) for adding or updating RPMs to the execution environment image, if needed.
- `registry.redhat.io` for access to the base container images.

Building an execution environment image in a disconnected environment requires mirroring content from these locations. For information about importing collections from Ansible Galaxy or automation hub into a private automation hub, see *Importing an automation content collection in automation hub* in the Related Links section.

Mirrored PyPI content once transferred into the disconnected network can be made available by using a web server or an artifact repository such as Nexus. The RHEL and UBI repository content can be exported from an internet-facing Red Hat Satellite Server, copied into the disconnected environment, then imported into a disconnected Satellite so it is available for building custom execution environments. See *ISS Export Sync in an Air-Gapped Scenario* in the Related Links section for details.

The `ee-minimal` base container image is included with the bundled installer and added to the private automation hub at install time. If a base container image that is not included with the bundled installer is required, you must import it to the disconnected network and add it to the private automation hub container registry.

Once all of the prerequisites are available on the disconnected network, the ansible-builder command can be used to create custom execution environment images.
