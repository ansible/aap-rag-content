+++
template = "docs/aem-title.html"
title = "Configure subscriptions - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-proc_controller_configure_subscriptions"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-assembly_gw_settings/", "Configure Ansible Automation Platform"]]
category = "Configure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure-proc_controller_configure_subscriptions/aem-page/configure-proc_controller_configure_subscriptions.html"
last_crumb = "Configure subscriptions"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure subscriptions"
oversized = "false"
page_slug = "configure-proc_controller_configure_subscriptions"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/configure-proc_controller_configure_subscriptions"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure-proc_controller_configure_subscriptions/toc/toc.json"
type = "aem-page"
+++

# Configure subscriptions

You can use the **Subscription** menu to view the details of your subscription, such as compliance, host-related statistics, or expiry, or you can apply a new subscription.

## About this task

Ansible subscriptions require a service account from console.redhat.com. You must [create a service account](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/creating_and_managing_service_accounts/proc-ciam-svc-acct-overview-creating-service-acct#proc-ciam-svc-acct-create-creating-service-acct) and use the client ID and client secret to activate your subscription.

Note:

If you enter your client ID and client secret but cannot locate your subscription, you might not have the correct permissions set on your service account. For more information and troubleshooting guidance for service accounts, see [Configure Ansible Automation Platform to authenticate through service account credentials](https://access.redhat.com/articles/7112649).

For Red Hat Satellite, input your Satellite username and Satellite password in the fields below.

## Procedure

1.  From the navigation panel, select Settings> (and then)Subscription. The **Subscription** page is displayed.
2.  Click Edit subscription.
3.  You can either enter your service account or Satellite credentials, or attach a current subscription manifest in the **Welcome** page.
4.  Click Next and agree to the terms of the license agreement.
5.  Click Next to review the subscription settings.
6.  Click Finish to complete the configuration.
