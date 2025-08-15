# 1. Red Hat Ansible Automation Platform installation overview
## 1.2. Managing Ansible Automation Platform licensing, updates and support
### 1.2.7. Activating Red Hat Ansible Automation Platform




If you are an organization administrator, you must [create a service account](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/creating_and_managing_service_accounts/proc-ciam-svc-acct-overview-creating-service-acct#proc-ciam-svc-acct-create-creating-service-acct) and use the client ID and client secret to activate your subscription.

If you do not have administrative access, you can enter your Red Hat username and password in the Client ID and Client secret fields, to locate and add your subscription to your Ansible Automation Platform instance.

Note
If you enter your client ID and client secret but cannot locate your subscription, you might not have the correct permissions set on your service account. For more information and troubleshooting guidance for service accounts, see [Configure Ansible Automation Platform to authenticate through service account credentials](https://access.redhat.com/articles/7112649) .



For Red Hat Satellite, input your Satellite username and Satellite password in the fields below.

Red Hat Ansible Automation Platform uses available subscriptions or a subscription manifest to authorize the use of Ansible Automation Platform. To obtain a subscription, you can do either of the following:

1. Use your Red Hat username and password, service account credentials, or Satellite credentials when you launch Ansible Automation Platform.
1. Upload a subscriptions manifest file either using the Red Hat Ansible Automation Platform interface or manually in an Ansible Playbook.


#### 1.2.7.1. Activate with credentials




When Ansible Automation Platform launches for the first time, the Ansible Automation Platform Subscription screen automatically displays. If you are an organization administrator, you can use your Red Hat service account to retrieve and import your subscription directly into Ansible Automation Platform.

If you do not have administrative access, you can enter your Red Hat username and password in the Client ID and Client secret fields, respectively, to locate and add your subscription to your Ansible Automation Platform instance.

Note
You are opted in for Automation Analytics by default when you activate the platform on first time log in. This helps Red Hat improve the product by delivering you a much better user experience. You can opt out, after activating Ansible Automation Platform, by doing the following:

1. From the navigation panel, selectSettings→Automation Execution→System.
1. Clear the **Gather data for Automation Analytics** option.
1. ClickSave.




**Procedure**

1. Log in to Red Hat Ansible Automation Platform.
1. Select **Service Account / Red Hat Satellite** .
1. Enter your **Client ID / Satellite username** and **Client secret / Satellite password** .
1. Select your subscription from the **Subscription** list.

Note
You can also use your Satellite username and password if your cluster nodes are registered to Satellite through Subscription Manager.




1. Review the End User License Agreement and select **I agree to the End User License Agreement** .
1. ClickFinish.


**Verification**

After your subscription has been accepted, subscription details are displayed. A status of _Compliant_ indicates your subscription is in compliance with the number of hosts you have automated within your subscription count. Otherwise, your status will show as _Out of Compliance_ , indicating you have exceeded the number of hosts in your subscription. Other important information displayed include the following:


#### 1.2.7.2. Activate with a manifest file




If you have a subscriptions manifest, you can upload the manifest file either by using the Red Hat Ansible Automation Platform interface.

Note
You are opted in for Automation Analytics by default when you activate the platform on first time log in. This helps Red Hat improve the product by delivering you a much better user experience. You can opt out, after activating Ansible Automation Platform, by doing the following:

1. From the navigation panel, selectSettings→Automation Execution→System.
1. Uncheck the **Gather data for Automation Analytics** option.
1. ClickSave.




**Prerequisites**

You must have a Red Hat Subscription Manifest file exported from the Red Hat Customer Portal. For more information, see [Obtaining a manifest file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_installation/index#assembly-aap-obtain-manifest-files) .


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


