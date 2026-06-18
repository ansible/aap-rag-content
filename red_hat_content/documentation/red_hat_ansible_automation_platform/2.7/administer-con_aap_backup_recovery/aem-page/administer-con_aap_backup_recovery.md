+++
title = "About backup and recovery - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-con_aap_backup_recovery"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_aap_backup_recovery/", "Back up and restore in an OpenShift environment"]]
category = "Administer"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-con_aap_backup_recovery/aem-page/administer-con_aap_backup_recovery.html"
last_crumb = "About backup and recovery"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "About backup and recovery"
oversized = "false"
page_slug = "administer-con_aap_backup_recovery"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/administer-con_aap_backup_recovery"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/administer-con_aap_backup_recovery/toc/toc.json"
type = "aem-page"
+++

# About backup and recovery

Red Hat recommends backing up deployments of Red Hat Ansible Automation Platform in your Red Hat OpenShift Container Platform environment to prevent data loss.

A backup resource of your Red Hat Ansible Automation Platform deployment includes the following:

- Custom deployment of specific values in the `spec` section of the Ansible Automation Platform custom resource object.
- Back up of the `postgresql` database.
- `secret_key`, `admin_password`, and `broadcast_websocket` secrets.
- Database configuration.


Note:

Be sure to secure your backup resources because they can include sensitive information.

## Backup recommendations

Recovering from data loss requires that you plan for and create backup resources of your Red Hat Ansible Automation Platform deployments on a regular basis. At a minimum, Red Hat recommends backing up deployments of Red Hat Ansible Automation Platform under the following circumstances:

- Before upgrading your Red Hat Ansible Automation Platform deployments.
- Before upgrading your OpenShift cluster.
- Once per week. This is particularly important if your environment is configured for automatic upgrades.

## Backup database compression for operator-based deployments

Ansible Automation Platform 2.6 supports database compression for operator-based backup operations. You can enable or disable compression globally or per component to optimize backup size and performance.

When you enable database compression, the operator compresses the PostgreSQL database dump for each component. This reduces the overall backup size but increases CPU usage during the backup process.

## Backup compression configuration parameters

Use these compression parameters to configure the `AnsibleAutomationPlatformBackup` custom resource:

| Parameter                            | Description                                                                | Default                           |
| ------------------------------------ | -------------------------------------------------------------------------- | --------------------------------- |
| `spec.use_db_compression`            | Enables or disables database dump compression for all components globally. | `True`                            |
| `spec.gateway.use_db_compression`    | Overrides the global compression setting for the platform gateway.         | Value of`spec.use_db_compression` |
| `spec.controller.use_db_compression` | Overrides the global compression setting for automation controller.        | Value of`spec.use_db_compression` |
| `spec.hub.use_db_compression`        | Overrides the global compression setting for automation hub.               | Value of`spec.use_db_compression` |
| `spec.eda.use_db_compression`        | Overrides the global compression setting for Event-Driven Ansible.         | Value of`spec.use_db_compression` |

When you set a per-component parameter, it overrides the global `spec.use_db_compression` value for that component only.

## Configure backup compression

Configure database compression for your Ansible Automation Platform backup by setting compression parameters in the `AnsibleAutomationPlatformBackup` custom resource.

### Before you begin

- You have installed Ansible Automation Platform 2.6 by using the operator.
- You have administrator access to the Red Hat OpenShift Container Platform cluster.

### Procedure

1.  Create or edit an `AnsibleAutomationPlatformBackup` custom resource file. The following example enables compression globally but disables it for automation controller:
  

```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatformBackup
metadata:
  name: aap-backup
  namespace: aap
spec:
  deployment_name: aap

    # Global — applies to gateway and all child components by default
  use_db_compression: true

    # Per-component override (optional)
  controller:
    use_db_compression: false   # disable compression for controller only
```

2.  Apply the custom resource to your cluster:
  

```
$ oc apply -f <backup_cr_file>.yml
```

3.  Monitor the backup progress:
  

```
$ oc get ansibleautomationplatformbackup -n aap -w
```

### Results

Verify that the backup completed successfully:

```
$ oc get ansibleautomationplatformbackup <backup_name> -n aap -o jsonpath='{.status.conditions}'
```

The output shows a `Successful` condition when the backup completes.
