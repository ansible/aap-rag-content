+++
title = "What survives an upgrade - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_self_service_rhel_upgrade_survival"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_upgrade/", "Upgrade the Ansible automation portal RHEL appliance"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_self_service_rhel_upgrade_survival/aem-page/install-ref_self_service_rhel_upgrade_survival.html"
last_crumb = "What survives an upgrade"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "What survives an upgrade"
oversized = "false"
page_slug = "install-ref_self_service_rhel_upgrade_survival"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-ref_self_service_rhel_upgrade_survival"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-ref_self_service_rhel_upgrade_survival/toc/toc.json"
type = "aem-page"
+++

# What survives an upgrade

The following table describes what happens to each type of content during a bootc upgrade of the Ansible automation portal RHEL appliance.

| Content                    | Location                                    | Survives upgrade | Notes                                        |
| -------------------------- | ------------------------------------------- | ---------------- | -------------------------------------------- |
| Portal configuration       | /etc/portal/configs/                        | Yes              | Three-way merge preserves your modifications |
| SSL certificates           | /etc/portal/ssl/                            | Yes              | Three-way merge                              |
| Quadlet drop-ins           | /etc/containers/systemd/portal.container.d/ | Yes              | Three-way merge                              |
| Quadlet port customization | /etc/containers/systemd/                    | Yes              | Three-way merge                              |
| PostgreSQL data            | /var/lib/portal/postgres-data/              | Yes              | Never touched by bootc                       |
| Backups                    | /var/lib/portal/backups/                    | Yes              | Never touched by bootc                       |
| Podman secrets             | /var/lib/containers/                        | Yes              | Never touched by bootc                       |
| Ansible plugins            | /usr/share/portal/plugins/                  | Updated          | New plugins from the new image               |
| Portal scripts             | /usr/share/portal/scripts/                  | Updated          | New scripts from the new image               |
| Dynamic plugin configs     | /var/lib/portal/dynamic-plugins-root/       | Cleared          | Regenerated from new plugins on first start  |

## Post-upgrade reconciliation

After reboot, the appliance automatically reconciles Ansible plugins and configuration with the new image version:

1. Clears the dynamic plugins directory so that plugins are regenerated from the new image.
2. Clears generated configuration files (regenerated on portal start).
3. Creates any new directories required by the new image version.
4. Fixes file ownership for portal and PostgreSQL directories.
