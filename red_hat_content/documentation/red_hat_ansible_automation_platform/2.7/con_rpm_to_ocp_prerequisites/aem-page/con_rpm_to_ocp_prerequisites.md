+++
template = "docs/aem-title.html"
title = "RPM to OpenShift Container Platform migration prerequisites - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/con_rpm_to_ocp_prerequisites"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/con_rpm_to_ocp_prerequisites/aem-page/con_rpm_to_ocp_prerequisites.html"
last_crumb = "RPM to OpenShift Container Platform migration prerequisites"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "RPM to OpenShift Container Platform migration prerequisites"
oversized = "false"
page_slug = "con_rpm_to_ocp_prerequisites"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/con_rpm_to_ocp_prerequisites"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/con_rpm_to_ocp_prerequisites/toc/toc.json"
type = "aem-page"
+++

# RPM to OpenShift Container Platform migration prerequisites

Before migrating from an RPM-based deployment to an OpenShift Container Platform deployment, ensure you meet the following prerequisites:

Note:

Completing this migration is a required step if you plan to upgrade to Ansible Automation Platform 2.7. RPM-based deployments are not supported as an upgrade path to 2.7.

- You have a source RPM-based deployment of Ansible Automation Platform.
- The source RPM-based deployment is on the latest async release of the version you are on.
- You have a target OpenShift Container Platform environment ready.
- You have Ansible Automation Platform Operator available for the latest release of the Ansible Automation Platform version you are on.
- You have made a decision on internal or external database configuration.
- You have made a decision on internal or external Redis configuration.
- There is network connectivity between the source and target environments.
