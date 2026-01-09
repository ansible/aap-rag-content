# 6. Configuring Ansible Automation Platform
## 6.1. Configuring subscriptions




You can use the **Subscription** menu to view the details of your subscription, such as compliance, host-related statistics, or expiry, or you can apply a new subscription.

Ansible subscriptions require a service account from console.redhat.com. You must [create a service account](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/creating_and_managing_service_accounts/proc-ciam-svc-acct-overview-creating-service-acct#proc-ciam-svc-acct-create-creating-service-acct) and use the client ID and client secret to activate your subscription.

Note
If you enter your client ID and client secret but cannot locate your subscription, you might not have the correct permissions set on your service account. For more information and troubleshooting guidance for service accounts, see [Configure Ansible Automation Platform to authenticate through service account credentials](https://access.redhat.com/articles/7112649) .



For Red Hat Satellite, input your Satellite username and Satellite password in the fields below.

**Procedure**

1. From the navigation panel, selectSettings→Subscription. The **Subscription** page is displayed.
1. ClickEdit subscription.
1. You can either enter your service account or Satellite credentials, or attach a current subscription manifest in the **Welcome** page.
1. ClickNextand agree to the terms of the license agreement.
1. ClickNextto review the subscription settings.
1. ClickFinishto complete the configuration.


