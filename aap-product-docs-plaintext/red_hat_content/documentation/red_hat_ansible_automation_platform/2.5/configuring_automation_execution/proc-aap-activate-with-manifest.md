# 11. Subscription management in Ansible Automation Platform and automation controller
## 11.2. Activating Red Hat Ansible Automation Platform
### 11.2.2. Activate with a manifest file




If you have a subscriptions manifest, you can upload the manifest file by using the Red Hat Ansible Automation Platform interface.

Note
You are opted in for Automation Analytics by default when you activate the platform on first login. This helps Red Hat improve the product by delivering you a much better user experience. You can opt out after activating Ansible Automation Platform by taking the following steps:

1. From the navigation panel, selectSettings→Automation Execution→System.
1. Clear the **Gather data for Automation Analytics** option.
1. ClickSave.




**Prerequisites**

You must have a Red Hat subscription manifest file exported from the Red Hat Customer Portal. For more information, see [Obtaining a manifest file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/assembly-platform-install-overview#assembly-aap-obtain-manifest-files) .


**Procedure**

1. Log in to Red Hat Ansible Automation Platform.


1. If you are not immediately taken to the subscription wizard, go toSettings→Subscription.

1. Select the **Subscription manifest** tab.
1. ClickBrowseand select your manifest file.
1. Review the End User License Agreement and select **I agree to the End User License Agreement** .
1. ClickFinish.

Note
If theBROWSEbutton is disabled on the subscription wizard page, clear the **USERNAME** and **PASSWORD** fields.






**Verification**

After your subscription has been accepted, subscription details are displayed. A status of _Compliant_ indicates your subscription is in compliance with the number of hosts you have automated within your subscription count. Otherwise, your status shows as _Out of Compliance_ , indicating you have exceeded the number of hosts in your subscription. Other important information displayed include the following:


**Next steps**

- You can return to the subscription wizard by selectingSettings→Subscriptionfrom the navigation panel and clickingEdit subscription.


