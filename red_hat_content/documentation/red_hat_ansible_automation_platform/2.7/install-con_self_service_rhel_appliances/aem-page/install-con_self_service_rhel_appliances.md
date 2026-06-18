+++
title = "Deploy Ansible automation portal RHEL appliance - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_appliances"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_appliances/", "Deploy Ansible automation portal RHEL appliance"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_appliances/aem-page/install-con_self_service_rhel_appliances.html"
last_crumb = "Deploy Ansible automation portal RHEL appliance"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Deploy Ansible automation portal RHEL appliance"
oversized = "false"
page_slug = "install-con_self_service_rhel_appliances"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_appliances"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_appliances/toc/toc.json"
type = "aem-page"
+++

# Deploy Ansible automation portal RHEL appliance

The Ansible automation portal RHEL virtual machine appliances provide pre-configured virtual machines that you can deploy across multiple virtualization platforms.

The appliances are available in the following formats:

- **QCOW2** - For Red Hat OpenShift Virtualization and KVM-based environments
- **VMDK** - For VMware `vSphere` infrastructure


## Supported platforms

You can deploy Ansible automation portal appliances on the following platforms:

Red Hat OpenShift Virtualization
Deploy the appliance as a virtual machine within your Red Hat OpenShift Container Platform environment using the QCOW2 image format.

VMware `vSphere`
Deploy the appliance on VMware infrastructure using ESXi hosts and VMFS datastores with the VMDK image format.

QEMU for local testing
Deploy the appliance on your local machine for testing and demonstrations using the QCOW2 image format. This deployment model is not supported for production environments.

Note:

Ansible automation portal appliances support AMD64/x86_64 platforms only.

## Initial configuration

The appliance requires configuration at first boot to connect to Ansible Automation Platform and start portal services. You must provide configuration through one of the following methods, listed in priority order:

Baked-in configuration
For advanced installations using the Ansible collection to build a customized appliance image with pre-baked settings.

VMware `guestinfo` properties
For VMware deployments, provide SSH keys and portal configuration through `guestinfo` properties set in `vSphere`.

cloud-init user-data
For cloud and Red Hat OpenShift Virtualization deployments, provide SSH keys and portal configuration through cloud-init user-data. The appliance configures itself automatically on first boot.

Pre-seeded configuration file
Place a YAML configuration file at /etc/portal/config.yaml before first boot for automated deployment.

If no configuration source is found at first boot, portal services do not start. You can provide configuration after deployment by editing /etc/portal/configs/app-config/app-config.production.yaml and restarting the portal service.

The initial configuration includes:

- SSH key authentication for administrative access
- Ansible Automation Platform URL, OAuth application credentials, and admin token
- Database settings (built-in or external PostgreSQL)
- Base URL and network configuration


Note:

The `admin` user account is locked by default and console login is disabled. Administrative access is available only through SSH using the key you provided during configuration.

## Disconnected environments

You can deploy Ansible automation portal appliances in disconnected or air-gapped environments. The pre-built appliance images include all required container images and plug-ins, so no external network access is required during initial deployment.

For appliance upgrades in disconnected environments, a mirror registry or OCI archive provides the updated container images. Use the `ansible-portal registry-login` command to authenticate to a private registry mirror.

## Understanding the appliance

Before configuring or managing the appliance, review how its key components work together.

## Configuration files

The Ansible automation portal RHEL appliance uses two YAML configuration files at /etc/portal/configs/app-config/:

`app-config.yaml`
Infrastructure configuration including the base URL, database connection, TLS, and system defaults. This file is set during initial deployment and is not typically modified.

`app-config.production.yaml`
Application configuration including Ansible Automation Platform connection, OAuth settings, SCM integrations, and catalog synchronization. Edit this file for day-to-day configuration changes. To apply changes, edit the file and restart the Ansible automation portal service. Changes take effect after the restart, which takes approximately 60 seconds.

## Service management

The Ansible automation portal RHEL appliance runs three `systemd` services that manage Podman containers:

`portal.service`
Ansible automation portal application. Listens on port 443 (HTTPS).

`postgres.service`
PostgreSQL database. Listens on port 5432 (internal container network only). This service is skipped when an external database is configured.

`devtools.service`
Ansible development tools. Provides Ansible Navigator and content creator services for building execution environments and developing Ansible content from the Ansible automation portal interface.

Note:

Restarting the `portal` service also restarts `postgres` and `devtools` due to service dependencies.

Use standard `systemctl` and `journalctl` commands to manage and inspect these services:

```terminal
$ sudo systemctl restart portal
$ sudo journalctl -u portal -f
```

## SSL certificates

The appliance generates self-signed SSL certificates at first boot and stores them at /etc/portal/ssl/. Replace these with certificates from a trusted certificate authority for production use.
