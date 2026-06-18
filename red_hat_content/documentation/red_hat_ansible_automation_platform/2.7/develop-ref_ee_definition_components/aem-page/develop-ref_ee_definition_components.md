+++
template = "docs/aem-title.html"
title = "Execution environment definition components - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-ref_ee_definition_components"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-con_ee_builder_overview/", "Understand execution environment builder"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_ee_definition_components/aem-page/develop-ref_ee_definition_components.html"
last_crumb = "Execution environment definition components"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Execution environment definition components"
oversized = "false"
page_slug = "develop-ref_ee_definition_components"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-ref_ee_definition_components"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/develop-ref_ee_definition_components/toc/toc.json"
type = "aem-page"
+++

# Execution environment definition components

When you create a custom execution environment definition, you configure the core components that determine the environment's capabilities, security, and dependencies.

| Component                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                  | Key considerations and examples                                                                                                                                                                                                                                                   |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Base images**            | <br>The foundation layer of your execution environment, pre-configured with a specific operating system and toolset.<br>The following base images are available in all predefined templates:<br>Red Hat Ansible Minimal EE - Ansible Core 2.18 (RHEL 9)Red Hat Ansible Minimal EE - Ansible Core 2.18 (RHEL 8)Red Hat Ansible Minimal EE - Ansible Core 2.16 (RHEL 9)Red Hat Ansible Minimal EE - Ansible Core 2.16 (RHEL 8) | <br>If you provide a custom image, it must include **ansible-core** and **ansible-runner**.                                                                                                                                                                                       |
| **Collections**            | Specifies the Ansible collections and Python libraries required by your automation content. You can add collections manually or upload a `requirements.yml` file.                                                                                                                                                                                                                                                            | <br>When collections overlap, the system merges the contents. If duplicates occur:<br>If a version is not specified, the system prioritizes the most recent version available.If versions are explicitly specified for both collections, the system uses the most recent version. |
| **Python requirements**    | Defines the minimum Python version and any extra Python packages required for this execution environment.                                                                                                                                                                                                                                                                                                                    | <br>Must reflect the version compatibility used across your organization for running automation reliably.<br>Avoid repeating Python requirements already specified as a dependency by the selected collections (for example, in their respective `requirements.txt` files).       |
| **System packages**        | Operating system libraries and packages required by the Python packages or collections in the execution environment.                                                                                                                                                                                                                                                                                                         | <br>Examples: **git**, **gcc**, **python3-devel**. These are necessary for compiling Python packages during the build process.<br>This list supplements, and must not repeat, any base OS dependencies already managed by your environment's build system.                        |
| **Additional build steps** | Custom shell commands injected directly into the container runtime instruction file at specific build phases (prepend or append to base, galaxy, builder, or final stages).                                                                                                                                                                                                                                                  | Use additional build steps for actions like installing private certificates or configuring environment variables not covered by standard package installation.                                                                                                                    |

## Predefined execution environment templates

Predefined templates accelerate environment setup for common use cases. AAP administrators manage which templates are available and can control access with RBAC.

| Template                  | Description                                                                                                                                                | Use cases                                                                                                                                                 |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Start from scratch**    | A blank-slate template for creating custom execution environments (loaded by default).                                                                     | Use this template when you require complete control over the base image and dependencies to build a highly customized or minimized execution environment. |
| **Networking Automation** | A template optimized for network device interaction with pre-selected networking collections (included in Helm chart but commented out by default).        | Use this template when your automation primarily interacts with switches, routers, firewalls, and other network infrastructure.                           |
| **Cloud Automation**      | A template optimized for deploying and managing cloud resources with pre-selected cloud collections (included in Helm chart but commented out by default). | Use this template when your automation targets provisioning, configuration, and management of cloud services.                                             |


Note:

Networking Automation and Cloud Automation templates require their referenced collections to be discoverable from a configured content source.
