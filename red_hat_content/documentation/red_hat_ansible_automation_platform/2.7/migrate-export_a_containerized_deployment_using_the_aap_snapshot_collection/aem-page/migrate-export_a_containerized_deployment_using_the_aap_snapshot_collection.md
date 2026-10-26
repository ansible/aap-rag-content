+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-export_a_containerized_deployment_using_the_aap_snapshot_collection"
title = "Export a containerized deployment using the aap_snapshot collection - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-assembly_source_environment/", "Prepare and export data from the source environment"]]
category = "Migrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-export_a_containerized_deployment_using_the_aap_snapshot_collection/aem-page/migrate-export_a_containerized_deployment_using_the_aap_snapshot_collection.html"
last_crumb = "Export a containerized deployment using the aap_snapshot collection"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Export a containerized deployment using the aap_snapshot collection"
oversized = "false"
page_slug = "migrate-export_a_containerized_deployment_using_the_aap_snapshot_collection"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/migrate-export_a_containerized_deployment_using_the_aap_snapshot_collection"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-export_a_containerized_deployment_using_the_aap_snapshot_collection/toc/toc.json"
type = "aem-page"
+++

# Export a containerized deployment using the aap_snapshot collection

Use the `ansible.aap_snapshot` collection to export your Ansible Automation Platform containerized deployment into a portable artifact that can be imported into an OpenShift Container Platform.

## Export data from a containerized Ansible Automation Platform deployment

Run the `artifact_export` playbook from the `ansible.aap_snapshot` collection to export credentials, database content, and automation hub Pulp data from your containerized deployment into a portable migration artifact.

### Before you begin

Verify that your environment meets all prerequisites before running the export. For more information, see [Prerequisites for containerized deployment export](/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-prerequisites_for_migrating_using_the_aap_snapshot_collection#GUID-32fd208d-506a-487c-b6ab-f8b9a569b51a "Before running the artifact_export playbook, verify that your source containerized deployment, control node, and network connectivity meet all prerequisites.").

### Procedure

1. Locate the inventory file from your containerized installation program.
      This is the same file you used to install Ansible Automation Platform.

2. Change to the directory where you want to create the migration artifact.
      Alternatively, `pass -e artifact_dest_dir=<path<` to write the artifact to a specific directory without changing your working directory.

3. Run the export playbook.
  

```console
$ ansible-playbook -i <inventory-file> ansible.aap_snapshot.artifact_export -e aap_platform=containerized
```

    Replace `<inventory-file>` with the path to your installation inventory file.

    If preflight fails, the error message identifies the failing check.

4. Verify that the artifact exists.
  

```console
$ ls -lh
```

      Expected output:

```text
aap-snapshot-2.6-20260601-143022.tar
aap-snapshot-2.6-20260601-143022.tar.sha256
```

    Record the full timestamped filename. You need it when you run the import playbook.

### What to do next

Import your Ansible Automation Platform data into your target deployment. For more information, see:

- [Import Ansible Automation Platform data into an OpenShift Container Platform deployment](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/migrate-import_ansible_automation_platform_data_into_an_ocp_deployment)
