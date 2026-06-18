+++
title = "Activate with a manifest file - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_aap_activate_with_manifest"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_aap_activate/", "Activate your subscription"]]
category = "Install"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_aap_activate_with_manifest/aem-page/install-proc_aap_activate_with_manifest.html"
last_crumb = "Activate with a manifest file"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Activate with a manifest file"
oversized = "false"
page_slug = "install-proc_aap_activate_with_manifest"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/install-proc_aap_activate_with_manifest"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/install-proc_aap_activate_with_manifest/toc/toc.json"
type = "aem-page"
+++

# Activate with a manifest file

If you have a subscriptions manifest, you can upload the manifest file by using the Red Hat Ansible Automation Platform interface.

## Before you begin

You must have a Red Hat subscription manifest file exported from the Red Hat Customer Portal. For more information, see [Obtaining a manifest file](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_aap_activate_1#assembly-aap-obtain-manifest-files "You can obtain a subscription manifest in the Subscription Allocations section of Red Hat Subscription Management.").

## About this task

Note:

You are opted in for Automation Analytics by default when you activate the platform on first login. This helps Red Hat improve the product by delivering you a much better user experience. You can opt out after activating Ansible Automation Platform by taking the following steps:

1. From the navigation panel, select Settings> (and then)Automation Execution> (and then)System.
2. Clear the **Gather data for Automation Analytics** option.
3. Click Save.

## Procedure

1.  Log in to Red Hat Ansible Automation Platform.   1.  If you are not immediately taken to the subscription wizard, go to Settings> (and then)Subscription.
2.  Select the **Subscription manifest** tab.
3.  Click Browse and select your manifest file.
4.  Review the End User License Agreement and select **I agree to the End User License Agreement**.
5.  Click Finish. Note:
      If the BROWSE button is disabled on the subscription wizard page, clear the **USERNAME** and **PASSWORD** fields.

## Results

After your subscription has been accepted, subscription details are displayed. A status of *Compliant* indicates your subscription is in compliance with the number of hosts you have automated within your subscription count. Otherwise, your status shows as *Out of Compliance*, indicating you have exceeded the number of hosts in your subscription. Other important information displayed include the following:

Hosts automated
Host count automated by the job, which uses the subscription count

Hosts imported
Host count considering all inventory sources (does not impact hosts remaining)

Hosts remaining
Total host count minus hosts automated

## What to do next

- You can return to the subscription wizard by selecting Settings> (and then)Subscription from the navigation panel and clicking Edit subscription.
