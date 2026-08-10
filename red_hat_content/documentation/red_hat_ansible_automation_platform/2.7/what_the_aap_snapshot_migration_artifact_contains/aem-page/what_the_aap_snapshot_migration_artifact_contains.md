+++
template = "docs/aem-title.html"
title = "What the aap_snapshot migration artifact contains - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/what_the_aap_snapshot_migration_artifact_contains"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/what_the_aap_snapshot_migration_artifact_contains/aem-page/what_the_aap_snapshot_migration_artifact_contains.html"
last_crumb = "What the aap_snapshot migration artifact contains"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "What the aap_snapshot migration artifact contains"
oversized = "false"
page_slug = "what_the_aap_snapshot_migration_artifact_contains"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/what_the_aap_snapshot_migration_artifact_contains"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/what_the_aap_snapshot_migration_artifact_contains/toc/toc.json"
type = "aem-page"
+++

# What the aap_snapshot migration artifact contains

The `artifact_export` playbook creates a portable snapshot of your Ansible Automation Platform deployment that the import playbook uses to restore your configuration, data, and content on a new platform.

## Artifact contents

The artifact has a flat directory structure at its root, with per-component subdirectories for database dumps. Only components defined in your inventory are included.

| File or directory                       | Description                                                                                                                         |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `manifest.yml`                          | Schema version, Ansible Automation Platform version, source topology, list of exported components, and per-component checksums.     |
| `secrets.yml`                           | All`SECRET_KEY` values, database credentials, and encryption keys extracted from each component. File permissions are set to`0600`. |
| `sha256sum.txt`                         | SHA-256 checksums for each component database dump file.                                                                            |
| `controller/controller.pgc`             | PostgreSQL custom-format database dump for automation controller.                                                                   |
| `controller/custom_configs/<hostname>/` | Custom configuration files per controller node. Present only for RPM-based source deployments.                                      |
| `gateway/gateway.pgc`                   | PostgreSQL custom-format database dump for platform gateway.                                                                        |
| `hub/hub.pgc`                           | PostgreSQL custom-format database dump for automation hub.                                                                          |
| `hub/hub_content.tar`                   | Pulp data directory content. Included only when`export_hub_content` is`true` (the default).                                         |
| `eda/eda.pgc`                           | PostgreSQL custom-format database dump for Event-Driven Ansible.                                                                    |

## Artifact naming

The playbook creates one file in `artifact_dir`:

- `aap-snapshot-<aap-version>-<timestamp>.tar` — timestamped artifact, where the timestamp uses the format `YYYYMMDD-HHMMSS` (UTC).

A `.sha256` checksum file is created alongside it. Pass the full timestamped filename to the import playbook.

## Security considerations

Important:

The artifact contains database credentials, encryption keys, and `SECRET_KEY` values for all exported components. Treat the artifact as sensitive material. Restrict access to the `artifact_dir` directory on the control node, and use secure transfer methods when moving the artifact to the import host.

## What the artifact does not include

The artifact does not include infrastructure-level state or post-deployment configuration that exists outside the platform databases:

- Live network connections or active session state
- Running job output or execution environment logs
- System-level configuration outside the Ansible Automation Platform component scope (OS configuration, firewall rules, custom certificates)
- Content not present in the platform database at export time (for example, collections on an external automation hub that were never synced)

The following application-level items require manual reconfiguration after import and are not automatically restored by the collection:

- Execution node re-registration (execution node records migrate in the database dump, but the reconcile phase deprovisions nodes with no recent heartbeat; nodes must be re-registered through the Ansible Automation Platform UI)
- System settings not stored in the platform database
- Custom TLS certificates
- Custom automation controller configuration files from `/etc/tower/conf.d/` (exported into the artifact but not applied during OpenShift Container Platform import, as OCP deployments use operator-managed configuration instead of file-based settings)
- Host metrics and facts (regenerated after the first inventory sync)

Authentication settings configured through the automation controller or gateway UI (LDAP, SAML, social authentication) are stored in the component databases and migrate automatically with the database dump. No manual reconfiguration is required for these settings unless hostname or redirect URI changes are needed in the external identity provider.
