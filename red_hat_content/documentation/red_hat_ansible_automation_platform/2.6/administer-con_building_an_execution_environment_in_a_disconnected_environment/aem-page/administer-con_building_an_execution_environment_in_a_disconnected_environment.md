+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-con_building_an_execution_environment_in_a_disconnected_environment"
title = "Disconnected environment customizations - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-define__create__and_build_execution_environments/", "Define, create, and build execution environments"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-con_building_an_execution_environment_in_a_disconnected_environment/aem-page/administer-con_building_an_execution_environment_in_a_disconnected_environment.html"
last_crumb = "Disconnected environment customizations"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Disconnected environment customizations"
oversized = "false"
page_slug = "administer-con_building_an_execution_environment_in_a_disconnected_environment"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/administer-con_building_an_execution_environment_in_a_disconnected_environment"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/administer-con_building_an_execution_environment_in_a_disconnected_environment/toc/toc.json"
type = "aem-page"
+++

# Disconnected environment customizations

Creating execution environments for Ansible Automation Platform is a common task which works differently in disconnected environments. When building a custom execution environment, the ansible-builder tool defaults to downloading content from the following locations on the internet:

- Red Hat Automation hub (console.redhat.com) or Ansible Galaxy (galaxy.ansible.com) for any Ansible content collections added to the execution environment image.
- PyPI (pypi.org) for any python packages required as collection dependencies.
- RPM repositories such as the RHEL or UBI repositories (cdn.redhat.com) for adding or updating RPMs to the execution environment image, if needed.
- `registry.redhat.io` for access to the base container images.


Building an execution environment image in a disconnected environment requires mirroring content from these locations. For information about importing collections from Ansible Galaxy or automation hub into a private automation hub, see *Importing an automation content collection in automation hub* in the Related Links section.

Mirrored PyPI content once transferred into the disconnected network can be made available by using a web server or an artifact repository such as Nexus. The RHEL and UBI repository content can be exported from an internet-facing Red Hat Satellite Server, copied into the disconnected environment, then imported into a disconnected Satellite so it is available for building custom execution environments. See *ISS Export Sync in an Air-Gapped Scenario* in the Related Links section for details.

The default base container image, `ee-minimal-rhel8`, is used to create custom execution environment images and is included with the bundled installer. This image is added to the private automation hub at install time.

If a different base container image such as `ee-minimal-rhel9` is required, it must be imported to the disconnected network and added to the private automation hub container registry.

Once all of the prerequisites are available on the disconnected network, the ansible-builder command can be used to create custom execution environment images.
