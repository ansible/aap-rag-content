+++
template = "docs/aem-title.html"
title = "Connect and verify Ansible automation portal - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_connect_verify"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_appliances/", "Deploy Ansible automation portal RHEL appliance"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_connect_verify/aem-page/install-proc_self_service_connect_verify.html"
last_crumb = "Connect and verify Ansible automation portal"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Connect and verify Ansible automation portal"
oversized = "false"
page_slug = "install-proc_self_service_connect_verify"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_self_service_connect_verify"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_connect_verify/toc/toc.json"
type = "aem-page"
+++

# Connect and verify Ansible automation portal

After deploying the Ansible automation portal appliance, update the OAuth redirect URI, verify service health, and sign in to the portal.

## About this task

Complete these post-installation steps after deploying the Ansible automation portal appliance on any platform.

## Procedure

Update the OAuth redirect URI

1.  Log in to Ansible Automation Platform as an administrator.
2.  Navigate to Access Management> (and then)OAuth Applications> (and then)automation-portal.
3.  Update Redirect URIs to `https://<portal-address>/api/auth/rhaap/handler/frame`.

  - For RHEL with KVM: use the VM IP address.
  - For Red Hat OpenShift Virtualization: use the route hostname.
  - For VMware `vSphere`: use the VM IP address or hostname.

4.  Click Save.


Verify service health

5.  SSH into the Ansible automation portal RHEL appliance and check the service status.
  

```terminal
$ sudo systemctl status portal postgres devtools
```
    Example output for a healthy Ansible automation portal RHEL appliance:

```terminal
portal.service - Automation portal
     Active: active (running) since ...
postgres.service - PostgreSQL database
     Active: active (running) since ...
devtools.service - Ansible development tools
     Active: active (running) since ...
```
    All three services should show `active (running)`.

    To view detailed logs for a specific service:

```terminal
$ sudo journalctl -u portal -n 100 --no-pager
```

Sign in to Ansible automation portal

6.  Open `https://<portal-address>` in a browser.
7.  Click Sign in with RHAAP.
8.  Authenticate with your Ansible Automation Platform credentials.

## Results

A successful login confirms that the OAuth integration with Ansible Automation Platform is working. The Ansible automation portal catalog displays synchronized job templates from Ansible Automation Platform. If no templates appear, verify that the API token has access to job templates in Ansible Automation Platform.
