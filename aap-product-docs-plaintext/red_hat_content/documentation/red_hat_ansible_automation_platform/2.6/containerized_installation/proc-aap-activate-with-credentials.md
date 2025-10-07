# 1. Managing Ansible Automation Platform licensing, updates, and support
## 1.7. Activating Red Hat Ansible Automation Platform
### 1.7.1. Activate with credentials




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


