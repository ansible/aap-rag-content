+++
template = "docs/aem-title.html"
title = "RPM to containerized migration prerequisites - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/con_rpm_to_containerized_prerequisites"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/con_rpm_to_containerized_prerequisites/aem-page/con_rpm_to_containerized_prerequisites.html"
last_crumb = "RPM to containerized migration prerequisites"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "RPM to containerized migration prerequisites"
oversized = "false"
page_slug = "con_rpm_to_containerized_prerequisites"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/con_rpm_to_containerized_prerequisites"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/con_rpm_to_containerized_prerequisites/toc/toc.json"
type = "aem-page"
+++

# RPM to containerized migration prerequisites

Before migrating from an RPM-based deployment to a container-based deployment, ensure you meet the following prerequisites:

Note:

Completing this migration is a required step if you plan to upgrade to Ansible Automation Platform 2.7. RPM-based deployments are not supported as an upgrade path to 2.7.

- You have a source RPM-based deployment of Ansible Automation Platform.
- The source RPM-based deployment is on the latest async release of the version you are on.
- You have a target environment prepared for a container-based deployment of Ansible Automation Platform.
- You have downloaded the containerized installation program for the latest release of the Ansible Automation Platform version you are on.
- You have enough storage for database dumps and backups.
- There is network connectivity between the source and target environments.
