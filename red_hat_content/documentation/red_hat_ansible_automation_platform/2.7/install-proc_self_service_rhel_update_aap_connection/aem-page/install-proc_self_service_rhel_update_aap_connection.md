+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_update_aap_connection"
title = "Update the Ansible Automation Platform connection - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_upgrade/", "Upgrade the Ansible automation portal RHEL appliance"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_update_aap_connection/aem-page/install-proc_self_service_rhel_update_aap_connection.html"
last_crumb = "Update the Ansible Automation Platform connection"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Update the Ansible Automation Platform connection"
oversized = "false"
page_slug = "install-proc_self_service_rhel_update_aap_connection"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_update_aap_connection"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_self_service_rhel_update_aap_connection/toc/toc.json"
type = "aem-page"
+++

# Update the Ansible Automation Platform connection

Change the Ansible Automation Platform host URL, OAuth client ID, API token, or OAuth client secret after deploying the Ansible automation portal RHEL appliance.

## About this task

To change the Ansible Automation Platform host URL or OAuth client ID after deployment, edit the configuration file directly. To update secrets (API token, OAuth client secret), use Podman secrets.

## Procedure

1.  To update the Ansible Automation Platform host URL or OAuth client ID, edit the configuration file:
  

```terminal
$ sudo vi /etc/portal/configs/app-config/app-config.production.yaml
```
    Update `ansible.rhaap.baseUrl` and `auth.providers.rhaap.production.clientId` to the new values. Save the file.

2.  To rotate the Ansible Automation Platform API token:
  

```terminal
$ temp_file=$(mktemp -p /dev/shm)
$ printf '%s' '<new-aap-token>' > "$temp_file"
$ sudo podman secret create --replace portal_aap_token "$temp_file"
$ rm -f "$temp_file"
```

3.  To rotate the OAuth client secret:
  

```terminal
$ temp_file=$(mktemp -p /dev/shm)
$ printf '%s' '<new-oauth-client-secret>' > "$temp_file"
$ sudo podman secret create --replace portal_aap_oauth_client_secret "$temp_file"
$ rm -f "$temp_file"
```

4.  Restart the Ansible automation portal service:
  

```terminal
$ sudo systemctl restart portal
```

## Results

The Ansible automation portal reconnects to the Ansible Automation Platform instance using the updated credentials. Verify the connection by signing in to the portal and confirming that job templates are synchronized.
