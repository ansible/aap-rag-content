# 11. Subscription management in Ansible Automation Platform and automation controller
## 11.2. Activating Red Hat Ansible Automation Platform
### 11.2.1. Activate with credentials




When Ansible Automation Platform launches for the first time, the Ansible Automation Platform subscription wizard automatically displays. If you are an organization administrator, you can [create a Red Hat service account](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/creating_and_managing_service_accounts/proc-ciam-svc-acct-overview-creating-service-acct#proc-ciam-svc-acct-create-creating-service-acct) and use the client ID and client secret to retrieve and import your subscription directly into Ansible Automation Platform.

If you do not have administrative access, you can enter your Red Hat username and password in the **Username and password** tab to locate and add your subscription to your Ansible Automation Platform instance.

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


