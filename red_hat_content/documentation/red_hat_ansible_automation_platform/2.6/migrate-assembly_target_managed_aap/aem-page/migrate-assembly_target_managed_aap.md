+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/migrate-assembly_target_managed_aap"
template = "docs/aem-title.html"
title = "Prepare to migrate to Managed Ansible Automation Platform - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/migrate-assembly_target_environment/", "Prepare, configure, and validate the target environment"]]
category = "Migrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/migrate-assembly_target_managed_aap/aem-page/migrate-assembly_target_managed_aap.html"
last_crumb = "Prepare to migrate to Managed Ansible Automation Platform"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Prepare to migrate to Managed Ansible Automation Platform"
oversized = "false"
page_slug = "migrate-assembly_target_managed_aap"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/migrate-assembly_target_managed_aap"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/migrate-assembly_target_managed_aap/toc/toc.json"
type = "aem-page"
+++

# Prepare to migrate to Managed Ansible Automation Platform

Prepare and migrate your source environment to a Managed Ansible Automation Platform deployment, and reconcile the target environment post-migration.

## Migrate to Managed Ansible Automation Platform

Submit a support ticket on the Red Hat Customer Portal to request a migration to Managed Ansible Automation Platform.

### Before you begin

- You have a migration artifact from your source environment.

### Procedure

1.  Submit a [support ticket](https://access.redhat.com/support/cases/#/case/new/get-support?caseCreate=true) on the Red Hat Customer Portal requesting a migration to Managed Ansible Automation Platform. The support ticket should include:

  - Source installation type (RPM, Containerized, OpenShift)
  - Managed Ansible Automation Platform URL or deployment name
  - Source version (installer or Operator version)

2.  The Ansible Site Reliability Engineering (SRE) team provides instructions in the support ticket on how to upload the resulting migration artifact to secure storage for processing.
3.  The Ansible SRE team imports the migration artifact into the identified target instance and notifies the customer through the support ticket.
4.  The Ansible SRE team notifies customers of successful migration.

## Reconcile the target environment post-migration

Update necessary configurations after migrating to Managed Ansible Automation Platform.

### Procedure

1.  Log in to the Managed Ansible Automation Platform instance by using the local administrator account to confirm that data was imported.
2.  Perform the following actions based on the configuration of the source deployment:
  1.  Reconfigure Single Sign-On (SSO) authenticators and mappings to reflect the new URLs.
  2.  Update private automation hub content to reflect the new URLs.     1. Run the following command to update the automation hub repositories:

```
curl -d '{\"verify_checksums\": true }' -X POST -k https://<platform url>/api/galaxy/pulp/api/v3/repair/ -u <admin_user>:<admin_password>
```

    2. Perform a sync on any repositories configured in automation hub.
    3. Push any custom execution environments from the source automation hub to the target automation hub.

  3.  Reconfigure automation mesh.
3.  After migration, you can request standard Site Reliability Engineering (SRE) tasks through support tickets, such as configuration of custom certificates, a custom domain, or connectivity through private endpoints.
