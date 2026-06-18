+++
title = "Locate and manage authentication configurations - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_managing_authentication"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_managing_authentication/aem-page/secure-assembly_gw_managing_authentication.html"
last_crumb = "Locate and manage authentication configurations"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Locate and manage authentication configurations"
oversized = "false"
page_slug = "secure-assembly_gw_managing_authentication"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_managing_authentication"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_managing_authentication/toc/toc.json"
type = "aem-page"
+++

# Locate and manage authentication configurations

After you have configured your authentication settings, you can view a list of authenticators, search, sort and view the details for each authenticator configured on the system.

## Authentication list view

On the **Authentication Methods** page, you can view and manage the configured authentication methods for your organization.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods. The **Authentication Methods** page is displayed.

2.  Click Create authentication and follow the steps for creating an authentication method in [Configuring an authentication type](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_config_authentication_type#gw-config-authentication-type "Ansible Automation Platform provides multiple authenticator plugins that you can configure to simplify the login experience for your organization."). Otherwise, proceed to step 3.
3.  From the menu bar, you can sort the list of authentication methods by using the arrows in the menu bar for **Order**, **Name** and **Authentication type**.
4.  Click the toggles to **Enable** or **Disable** authenticators.

## Search for an authenticator

You can search for a previously configured authenticator from the Authentication list view.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  In the search bar, enter an appropriate keyword for the authentication method you want to search for and click the arrow icon.
3.  If you do not find what you are looking for, you can narrow your search. From the filter list, select **Name** or **Authentication type** depending on the search term you want to use.
4.  Scroll through the list of search results and select the authenticator you want to review.

## Display authenticator details

After you locate the authenticator you want to review, you can display the configuration details:

### Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  In the list view, select the authenticator name displayed in the **Name** column. The authenticator **Details** page is displayed.

3.  From the **Details** page, you can review the configuration settings applied to the authenticator.

## Edit an authenticator

You can change the settings of previously configured authenticators from the **Authentication** list view.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  In the list view, you can either:
  1.  Select the Edit![Edit](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftpencil.png) icon next to authenticator you want to modify, or
  2.  Select the authenticator name displayed in the **Name** column and click Edit authenticator from the **Details** page.
3.  Change the authentication details or mapping configurations as required.
4.  Click Save.

## Delete an authenticator

Delete unused authenticators to prevent users from logging in through outdated identity providers. Remove these configurations to ensure your Ansible Automation Platform environment remains secure and organized.

### About this task

You can change the settings of previously configured authenticators from the **Authentication** list view.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  In the list view, select the checkbox next to the authenticator you want to delete.
3.  Select **Delete authentication** from the **⋮** list.  Note:
      You can delete many authenticators by selecting the checkbox next to each authenticator you want to remove, and clicking **Delete selected authentication** from the **⋮** list on the menu bar.
