# Activate with a manifest file

If you have a subscriptions manifest, you can upload the manifest file by using the Red Hat Ansible Automation Platform interface.

## Before you begin

You must have a Red Hat subscription manifest file exported from the Red Hat Customer Portal. For more information, see [Obtaining a manifest file](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_aap_manifest_files#assembly-aap-obtain-manifest-files "You can obtain a subscription manifest in the Subscription Allocations section of Red Hat Subscription Management.").

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
