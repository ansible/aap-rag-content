+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-about_the_aap_snapshot_import_workflow"
title = "About the aap_snapshot import workflow - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-assembly_target_environment/", "Prepare, configure, and validate the target environment"]]
category = "Migrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-about_the_aap_snapshot_import_workflow/aem-page/migrate-about_the_aap_snapshot_import_workflow.html"
last_crumb = "About the aap_snapshot import workflow"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "About the aap_snapshot import workflow"
oversized = "false"
page_slug = "migrate-about_the_aap_snapshot_import_workflow"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/migrate-about_the_aap_snapshot_import_workflow"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-about_the_aap_snapshot_import_workflow/toc/toc.json"
type = "aem-page"
+++

# About the aap_snapshot import workflow

Use the `ansible.aap_snapshot` collection to import your Ansible Automation Platform configuration, credentials, and content from an RPM-based deployment into an OpenShift Container Platform operator-managed deployment.

The `artifact_import.yaml` playbook automates the full import sequence, from preflight validation through database restore and post-import reconciliation.

The Ansible Automation Platform version in the artifact must exactly match the version running in the OCP target namespace. The preflight phase enforces this requirement and fails early if the versions do not match.

After import, instance groups and host groups require manual reconciliation. Virtual machine nodes do not map one-to-one to pods, so group assignments must be reviewed and updated in the Ansible Automation Platform UI before the restored deployment is used in production.
