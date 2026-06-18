+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansible_automation_platform_custom_resources"
template = "docs/aem-title.html"
title = "Ansible Automation Platform custom resources - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/reference-ansible_automation_platform_custom_resources/", "Ansible Automation Platform custom resources"]]
category = "Reference"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/reference-ansible_automation_platform_custom_resources/aem-page/reference-ansible_automation_platform_custom_resources.html"
last_crumb = "Ansible Automation Platform custom resources"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Ansible Automation Platform custom resources"
oversized = "false"
page_slug = "reference-ansible_automation_platform_custom_resources"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/reference-ansible_automation_platform_custom_resources"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/reference-ansible_automation_platform_custom_resources/toc/toc.json"
type = "aem-page"
+++

# Ansible Automation Platform custom resources

The Ansible Automation Platform operator provides custom resources for deploying, backing up, and restoring a complete Ansible Automation Platform instance on OpenShift Container Platform.

The `AnsibleAutomationPlatform` custom resource is the top-level resource for deploying the platform. It manages all components, including automation controller, automation hub, Event-Driven Ansible, Ansible Lightspeed, and the platform gateway. Use this custom resource when you want the operator to manage the full platform deployment as a single unit.

The `AnsibleAutomationPlatformBackup` and `AnsibleAutomationPlatformRestore` custom resources manage data protection for the platform. A backup captures the state of all platform components and their databases. A restore recreates the platform from a previously created backup. You can configure backup settings globally or override them for individual components such as automation controller, automation hub, and Event-Driven Ansible.
