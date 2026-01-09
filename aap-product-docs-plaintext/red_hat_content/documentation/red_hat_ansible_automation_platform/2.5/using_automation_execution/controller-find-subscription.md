# 2. Logging into Ansible Automation Platform after installation
## 2.1. Finding your subscription with service account credentials




When you log in to Ansible Automation Platform for the first time, you must add your subscription information.

If you have already added your subscription, you can update your subscription details in the subscription wizard by going toSettings→Subscription→Edit subscription.

**Prerequisites**

- You are an organization administrator.
- You have [created a service account](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/creating_and_managing_service_accounts/proc-ciam-svc-acct-overview-creating-service-acct#proc-ciam-svc-acct-create-creating-service-acct) and saved the client ID and client secret.


Note
If you do not have administrative access, you can enter your Red Hat username and password in the **Username and password** tab to locate and add your subscription to your Ansible Automation Platform instance.



**Procedure**

1. Enter your service account credentials to find the subscription associated with your profile:


1. To find your subscription, click the tab labeled **Service Account** .
1. In the **Client ID** field, enter the client ID you received when you created your service account.
1. In the **Client secret** field, enter the client secret you received when you created your service account. Your subscription appears in the list menu labeled **Subscription** . Select your subscription.

1. After you have added your subscription, clickNext.
1. Check the box indicating that you agree to the **End User License Agreement** .
1. Review your information and click **Finish** .


Note
If you enter your client ID and client secret but cannot locate your subscription, you might not have the correct permissions set on your service account. For more information and troubleshooting guidance for service accounts, see [Configure Ansible Automation Platform to authenticate through service account credentials](https://access.redhat.com/articles/7112649) .



