+++
template = "docs/aem-title.html"
title = "Set a custom user-accessible URL or port - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_configure_url"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-con_self_service_rhel_appliances/", "Deploy Ansible automation portal RHEL appliance"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_configure_url/aem-page/install-proc_self_service_rhel_configure_url.html"
last_crumb = "Set a custom user-accessible URL or port"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Set a custom user-accessible URL or port"
oversized = "false"
page_slug = "install-proc_self_service_rhel_configure_url"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_configure_url"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_configure_url/toc/toc.json"
type = "aem-page"
+++

# Set a custom user-accessible URL or port

The Ansible automation portal RHEL appliance auto-detects the user-accessible URL from the VM IP address at each boot. To set a custom hostname or port, update the configuration file and restart the service.

## Before you begin

- SSH access to the appliance.
- The hostname or IP address and port that users will use to access Ansible automation portal.

## Procedure

1.  Edit the configuration file:
  

```terminal
$ sudo vi /etc/portal/configs/app-config/app-config.production.yaml
```

2.  Update the following three values.
      This example uses port 8443. If you are using the standard port 443, you do not need to specify the port:

```yaml
app:
  baseUrl: "https://portal.example.com:8443"
backend:
  baseUrl: "https://portal.example.com:8443"
  cors:
    origin: "https://portal.example.com:8443"
```

3.  Save the file and restart the Ansible automation portal service.
      Restarting the `portal` service also restarts `postgres` and `devtools` due to service dependencies:

```terminal
$ sudo systemctl restart portal
```

4.  If you set a custom port, open that port on any firewall and, for Red Hat OpenShift Virtualization deployments, update the OpenShift route.
5.  Update the OAuth redirect URI in Ansible Automation Platform to match the new URL.

## Results

Verify that Ansible automation portal is accessible at the new URL:

```terminal
$ curl -fk https://*new-url*
```
A successful response confirms that the URL and port are configured correctly.
