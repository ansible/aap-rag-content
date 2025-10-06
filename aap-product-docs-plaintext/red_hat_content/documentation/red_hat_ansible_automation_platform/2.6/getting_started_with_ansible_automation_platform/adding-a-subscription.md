# 2. Getting started as a platform administrator
## 2.2. Adding your subscription




To add your subscription information, you can either upload your subscription manifest, or use your service account credentials to find the subscription associated with your account.

**Prerequisites**

To add your subscription by uploading a subscription manifest, you must first:


- Obtain your manifest file. See [Obtaining a manifest file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/assembly-gateway-licensing#assembly-aap-obtain-manifest-files) in the Access management and authentication guide for steps on how to do this.


To add your subscription using your service account credentials, you must first:

- Have [created a service account](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/creating_and_managing_service_accounts/proc-ciam-svc-acct-overview-creating-service-acct#proc-ciam-svc-acct-create-creating-service-acct) and saved the client ID and client secret.
- Add your service account to the Subscription viewer user group to give it the ability to see your subscriptions. See the "Updates to subscription management" section in the Knowledgebase article [Configure Ansible Automation Platform to authenticate through service account credentials](https://access.redhat.com/articles/7112649) for instructions on how to do so.


**Procedure**

To add your subscription by uploading a subscription manifest:


- Drag the file to the field beneath **Red Hat subscription manifest** or browse for the file on your local machine.


To add your subscription with your service account credentials:

1. Click the **Service Account / Red Hat Satellite** tab.
1. Enter the **client ID** you received when you created your service account in the field labeled Client ID / Satellite username.
1. Enter the **client secret** you received when you created your service account in the field labeled Client secret / Satellite password. Your subscription appears in the **Subscription** list. Select your subscription.
1. After you have added your subscription, clickNext.
1. Check the box indicating that you agree to the **End User License Agreement** .
1. Review your information and clickFinish.


Note
If you enter your client ID and client secret but cannot locate your subscription, you might not have the correct permissions set on your service account. For more information and troubleshooting guidance for service accounts, see [Configure Ansible Automation Platform to authenticate through service account credentials](https://access.redhat.com/articles/7112649) .



Tip
After logging in, review the quick starts section in the navigation panel for useful guidance.



