+++
title = "ANSIBLE_BASE_JWT_VALIDATE_CERT default change for Red Hat Ansible Lightspeed - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-ansible_base_jwt_validate_cert_default_change"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-ansible_base_jwt_validate_cert_default_change/", "ANSIBLE_BASE_JWT_VALIDATE_CERT default change for Red Hat Ansible Lightspeed"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-ansible_base_jwt_validate_cert_default_change/aem-page/extend-ansible_base_jwt_validate_cert_default_change.html"
last_crumb = "ANSIBLE_BASE_JWT_VALIDATE_CERT default change for Red Hat Ansible Lightspeed"
latest = "true"
modified = "2026-10-06T15:21:13.207Z"
multi_page_path = ""
name = "ANSIBLE_BASE_JWT_VALIDATE_CERT default change for Red Hat Ansible Lightspeed"
oversized = "false"
page_slug = "extend-ansible_base_jwt_validate_cert_default_change"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-ansible_base_jwt_validate_cert_default_change"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-ansible_base_jwt_validate_cert_default_change/toc/toc.json"
type = "aem-page"
+++

# ANSIBLE_BASE_JWT_VALIDATE_CERT default change for Red Hat Ansible Lightspeed

Starting with Ansible Automation Platform 2.7, the `ANSIBLE_BASE_JWT_VALIDATE_CERT` setting defaults to `True`.

On-premise deployments that use self-signed certificates between the Lightspeed service and the platform gateway must install a trusted CA certificate or explicitly disable validation to maintain connectivity.

Important:

If your deployment uses self-signed certificates, the Lightspeed service fails to authenticate users after upgrading. Add your CA certificate to the trust store or disable certificate validation.
