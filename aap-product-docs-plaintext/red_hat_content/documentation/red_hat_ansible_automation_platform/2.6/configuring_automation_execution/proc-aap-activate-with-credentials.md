# 11. Subscription management in Ansible Automation Platform and automation controller
## 11.2. Activating Red Hat Ansible Automation Platform
### 11.2.1. Activate with credentials




Activate your Ansible Automation Platform subscription at the first launch by providing either Red Hat service account credentials or your personal Red Hat username and password. This process automatically retrieves and imports the required license, which grants the platform access to Red Hat content and entitlement services.

Note
You are opted in for Automation Analytics by default when you activate the platform on first login. This helps Red Hat improve the product by delivering you a much better user experience. You can opt out after activating Ansible Automation Platform by taking the following steps:

1. From the navigation panel, selectSettings→Automation Execution→System.
1. Clear the **Gather data for Automation Analytics** option.
1. ClickSave.




**Procedure**

1. Log in to Red Hat Ansible Automation Platform.
1. Select the **Service Account** tab in the subscription wizard.
1. Enter your **Client ID** and **Client secret** .
1. Select your subscription from the **Subscription** list.

Note
You can also enter your Satellite username and password in the **Satellite** tab if your cluster nodes are registered to Satellite through Subscription Manager.




1. Review the End User License Agreement and select **I agree to the End User License Agreement** .
1. ClickFinish.


**Verification**

After your subscription has been accepted, subscription details are displayed. A status of _Compliant_ indicates your subscription is in compliance with the number of hosts you have automated within your subscription count. Otherwise, your status shows as _Out of Compliance_ , indicating you have exceeded the number of hosts in your subscription. Other important information displayed include the following:


