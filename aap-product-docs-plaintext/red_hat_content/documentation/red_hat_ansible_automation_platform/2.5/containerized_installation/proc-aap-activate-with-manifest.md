# 1. Managing Ansible Automation Platform licensing, updates and support
## 1.7. Activating Red Hat Ansible Automation Platform
### 1.7.2. Activate with a manifest file




If you have a subscriptions manifest, you can upload the manifest file either by using the Red Hat Ansible Automation Platform interface.

Note
You are opted in for Automation Analytics by default when you activate the platform on first time log in. This helps Red Hat improve the product by delivering you a much better user experience. You can opt out, after activating Ansible Automation Platform, by doing the following:

1. From the navigation panel, selectSettings→Automation Execution→System.
1. Uncheck the **Gather data for Automation Analytics** option.
1. ClickSave.




**Prerequisites**

You must have a Red Hat Subscription Manifest file exported from the Red Hat Customer Portal. For more information, see [Obtaining a manifest file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/containerized_installation/index#assembly-aap-obtain-manifest-files) .


**Procedure**

1. Log in to Red Hat Ansible Automation Platform.
1. If you are not immediately prompted for a manifest file, go toSettings→Subscription.
1. Select **Subscription manifest** .
1. ClickBrowseand select the manifest file.
1. Review the End User License Agreement and select **I agree to the End User License Agreement** .
1. ClickFinish.


Note
If theBROWSEbutton is disabled on the License page, clear the **USERNAME** and **PASSWORD** fields.



**Verification**

After your subscription has been accepted, subscription details are displayed. A status of _Compliant_ indicates your subscription is in compliance with the number of hosts you have automated within your subscription count. Otherwise, your status will show as _Out of Compliance_ , indicating you have exceeded the number of hosts in your subscription. Other important information displayed include the following:


**Next steps**

- You can return to the license screen by selectingSettings→Subscriptionfrom the navigation panel and clickingEdit subscription.


