# 1. Managing Ansible Automation Platform licensing, updates and support
## 1.7. Activating Red Hat Ansible Automation Platform




If you are an organization administrator, you must [create a service account](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/creating_and_managing_service_accounts/proc-ciam-svc-acct-overview-creating-service-acct#proc-ciam-svc-acct-create-creating-service-acct) and use the client ID and client secret to activate your subscription.

If you do not have administrative access, you can enter your Red Hat username and password in the Client ID and Client secret fields, to locate and add your subscription to your Ansible Automation Platform instance.

Note
If you enter your client ID and client secret but cannot locate your subscription, you might not have the correct permissions set on your service account. For more information and troubleshooting guidance for service accounts, see [Configure Ansible Automation Platform to authenticate through service account credentials](https://access.redhat.com/articles/7112649) .



For Red Hat Satellite, input your Satellite username and Satellite password in the fields below.

Red Hat Ansible Automation Platform uses available subscriptions or a subscription manifest to authorize the use of Ansible Automation Platform. To obtain a subscription, you can do either of the following:

1. Use your Red Hat username and password, service account credentials, or Satellite credentials when you launch Ansible Automation Platform.
1. Upload a subscriptions manifest file either using the Red Hat Ansible Automation Platform interface or manually in an Ansible Playbook.


