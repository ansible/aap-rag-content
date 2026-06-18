+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-proc_self_service_sign_in"
template = "docs/aem-title.html"
title = "Sign in to Ansible automation portal - Red Hat Ansible Automation Platform 2.6"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_self_service_login/", "Launch automation templates from Ansible automation portal"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-proc_self_service_sign_in/aem-page/develop-proc_self_service_sign_in.html"
last_crumb = "Sign in to Ansible automation portal"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Sign in to Ansible automation portal"
oversized = "false"
page_slug = "develop-proc_self_service_sign_in"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-proc_self_service_sign_in"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-proc_self_service_sign_in/toc/toc.json"
type = "aem-page"
+++

# Sign in to Ansible automation portal

Log in to the deployed Ansible automation portal using your existing Ansible Automation Platform credentials. The portal uses these credentials for authentication.

## Before you begin

- You have configured an OAuth application in Ansible Automation Platform for Ansible automation portal.
- You have configured a user account in Ansible Automation Platform.

## Procedure

1.  In a browser, navigate to the URL for Ansible automation portal to open the sign-in page.  
![Self-service sign-in page](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/self-service-sign-in-page.png)  
2.  Click Sign In.
3.  The sign-in page for Ansible Automation Platform appears:  
![Ansible Automation Platform sign-in page](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/rhaap-sign-in-page.png)  
4.  Enter your Ansible Automation Platform credentials and click **Log in**.
5.  The Ansible automation portal web console opens.

If you are using custom or self-signed SSL certificates and when attempting to log in to Ansible automation portal, it displays the error:

`Login failed; caused by Error: Failed to send POST request: fetch failed`

This error indicates that Ansible automation portal cannot verify the SSL certificate from your Ansible Automation Platform instance.

To resolve this issue, configure Ansible automation portal to trust your custom CA certificate.

 Note:

While you can disable SSL validation by setting `checkSSL: false` in the Helm chart configuration, this approach is not recommended for production environments as it reduces security. Instead, configure Ansible automation portal to trust your custom CA certificate.

## View templates

View your accessible automation templates, displayed as tiles, on the **Templates** landing page of the Ansible automation portal console.

### Before you begin

- You have signed in to Ansible automation portal.

### Procedure

1.  In a browser, sign in to Ansible automation portal.
2.  In the navigation pane, select **Templates** to open a landing page where tiles are displayed, representing the templates that you have access to.  
![Templates view](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/self-service-templates-view.png)  

## Synchronize auto-generated templates

The auto-generated self-service templates are synchronized from the job templates in Ansible Automation Platform to Ansible automation portal. You can manually trigger a sync from the **Templates** page.

### About this task

 Note:

This synchronization fetches updates for auto-generated self-service templates only.

### Procedure

1.  In a browser, sign in to Ansible automation portal.
2.  In the navigation pane, select **Templates** to display the templates that you have access to.  
![Templates view](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/self-service-templates-view.png)  
3.  Select **Sync now** to launch a synchronization.
