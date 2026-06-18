+++
title = "Configure RADIUS authentication - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-configure_radius_authentication"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-configure_radius_authentication/aem-page/secure-configure_radius_authentication.html"
last_crumb = "Configure RADIUS authentication"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure RADIUS authentication"
oversized = "false"
page_slug = "secure-configure_radius_authentication"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-configure_radius_authentication"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-configure_radius_authentication/toc/toc.json"
type = "aem-page"
+++

# Configure RADIUS authentication

You can configure Ansible Automation Platform to centrally use RADIUS as a source for authentication information.

## Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods .
2.  Click Create authentication .
3.  Enter a **Name** for this authentication configuration.
4.  Select **Radius** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.
5.  Enter the host or IP of the RADIUS server in the **RADIUS Server** field. If you leave this field blank, RADIUS authentication is disabled.
6.  Enter the **Shared secret** for authenticating to RADIUS server.
7.  Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator. Note:
      Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.

8.  To automatically create organizations, users, and teams upon successful login, select **Create objects** .
9.  To enable this authentication method upon creation, select **Enabled** .
10.  To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users** .
11.  Click Create Authentication Method .

## What to do next

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (like username and email address) or to what groups they belong, continue to [Mapping](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-mapping "To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or what groups they belong to, you can configure authenticator maps.") .
