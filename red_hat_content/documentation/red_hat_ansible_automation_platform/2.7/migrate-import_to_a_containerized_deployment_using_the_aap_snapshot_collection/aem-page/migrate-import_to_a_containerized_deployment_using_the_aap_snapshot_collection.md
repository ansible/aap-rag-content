+++
template = "docs/aem-title.html"
title = "Import to a containerized deployment using the aap_snapshot collection - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-import_to_a_containerized_deployment_using_the_aap_snapshot_collection"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/migrate-assembly_target_environment/", "Prepare, configure, and validate the target environment"]]
category = "Migrate"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-import_to_a_containerized_deployment_using_the_aap_snapshot_collection/aem-page/migrate-import_to_a_containerized_deployment_using_the_aap_snapshot_collection.html"
last_crumb = "Import to a containerized deployment using the aap_snapshot collection"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "Import to a containerized deployment using the aap_snapshot collection"
oversized = "false"
page_slug = "migrate-import_to_a_containerized_deployment_using_the_aap_snapshot_collection"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/migrate-import_to_a_containerized_deployment_using_the_aap_snapshot_collection"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/migrate-import_to_a_containerized_deployment_using_the_aap_snapshot_collection/toc/toc.json"
type = "aem-page"
+++

# Import to a containerized deployment using the aap_snapshot collection

Use the `ansible.aap_snapshot` collection to import Ansible Automation Platform data into a containerized target deployment.

## Set up the import inventory for a containerized deployment

Prepare the inventory file that the `ansible.aap_snapshot` collection uses to connect to your containerized target deployment and determine which components to import.

### Before you begin

- All Ansible Automation Platform services on the target hosts are running.
- You have the export artifact file produced by the `ansible.aap_snapshot` export playbook.
- You have the inventory file used to install the target deployment.

### Procedure

1. Create a copy of the inventory file used to install your containerized target deployment.
      The following steps add import-specific variables to this copy.

2. Verify that the inventory copy includes the following host groups for each component you want to import.
  *Table 1. Component inventory groups*

    | Component             | Inventory group        |
    | --------------------- | ---------------------- |
    | Automation controller | `automationcontroller` |
    | Automation hub        | `automationhub`        |
    | Platform gateway      | `automationgateway`    |
    | Event-Driven Ansible  | `automationeda`        |
    To exclude a component from the import, remove its host group from the inventory.

  Note:
      The collection also accepts `automationedacontroller` as the Event-Driven Ansible group name. If you are adapting an existing RPM-based inventory, you do not need to rename this group.

3. Set the following variables in the `[all:vars]` section of the inventory.
  

```ini
[all:vars]
aap_platform=containerized
artifact_file=*/path/to/aap-snapshot-<version>-<date>.tar*
```

    Replace */path/to/aap-snapshot-<version>-<date>.tar* with the full path to the export artifact on the control node.

## Import Ansible Automation Platform data into a containerized deployment

Run the `ansible.aap_snapshot.artifact_import` playbook to restore Ansible Automation Platform data from an export artifact into a containerized target deployment.

### Before you begin

- A containerized Ansible Automation Platform deployment is installed on the target hosts.
- You have completed the import inventory setup.
- The export artifact file is present on the control node at the path specified by `artifact_file` in the inventory.
- The `ansible.aap_snapshot` collection is installed on the control node.
- All target hosts are reachable from the control node through SSH.

### Procedure

1. Run the `artifact_import` playbook with your import inventory.
  

```bash
ansible-playbook -i *<path-to-import-inventory>* ansible.aap_snapshot.artifact_import
```

    Replace *<path-to-import-inventory>* with the path to the inventory file you prepared.

    The collection runs preflight checks, extracts and validates the artifact, transfers the artifact to target hosts, stops Ansible Automation Platform services on the target hosts, restores component databases and updates component secrets, restarts services, and reconciles each component.

2. When the playbook completes, verify that the migration summary confirms all expected components were migrated successfully.
      Output varies based on your source platform and deployment. For example:

```text
=== Migration Complete ===
Source platform: rpm
Target platform: containerized
AAP version: 2.6.0
Components migrated:
  - controller (v2.6.0, database: awx)
  - hub (v2.6.0, database: pulp)
  - gateway (v2.6.0, database: gateway)
  - eda (v2.6.0, database: eda)
```

    If any expected components are missing, verify that their host groups are present in the import inventory and rerun the playbook.

## Rerun the containerized installation program to complete the migration

After the import playbook completes, rerun the containerized installation program to reconcile system-level configuration that the `artifact_import` playbook does not manage.

### Before you begin

- The `artifact_import` playbook has completed successfully.
- You have the containerized installation program directory and the inventory file used to install the target deployment.

### About this task

The `artifact_import` playbook restores component databases and performs basic service reconciliation. The containerized installation program manages system-level configuration outside the databases, including service configuration files, Transport Layer Security (TLS) certificates and trust bundles, and systemd unit files. Rerunning the installation program after the import aligns these with the restored deployment.

### Procedure

1. Navigate to the containerized installation program directory on the control node.
2. Run the containerized installation program using the same inventory file and method used for the original installation of the target deployment.
  

```bash
ansible-playbook -i *<path-to-installer-inventory>* ansible.containerized_installer.install
```

    Replace *<path-to-installer-inventory>* with the path to the inventory file for your target deployment.

## Validate the restored containerized deployment

After rerunning the containerized installation program, verify that the restored Ansible Automation Platform deployment is functioning correctly and complete any required post-import configuration.

### Before you begin

- The `artifact_import` playbook has completed.
- The containerized installation program has run successfully against the target inventory.

### Procedure

1. Sign in to the Ansible Automation Platform user interface using the admin credentials from the target deployment.
2. Verify that the user interface is accessible.
3. Verify that automation controller resources such as inventories, projects, job templates, and credentials are present and correct.
4. Check instance group assignments and reassign any restored resources that reference instance groups from the source deployment that do not exist on the target.
5. From the navigation panel, select Automation Decisions> (and then)Infrastructure> (and then)Credentials.
6. Update any Automation Controller credentials to the new controller URL if the automation controller hostname changed.
7. Register execution nodes for your target environment.
      From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Instances. The collection automatically deprovisions instances from the source environment during the reconcile phase. Add the execution nodes for your target deployment.

8. If the source deployment used custom Transport Layer Security (TLS) certificates, reapply them to the target deployment.
      The collection does not restore certificate material from the artifact.

9. Verify that automation hub content is present.
      The import restores the hub database, including remote registry configurations. Pulp content repair does not run automatically for containerized deployments. You must run it manually after the import completes. Content that was originally uploaded manually without a configured remote source must be re-uploaded manually.
