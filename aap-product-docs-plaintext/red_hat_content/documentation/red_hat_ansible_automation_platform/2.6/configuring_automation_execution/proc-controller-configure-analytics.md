# 2. Automation controller configuration
## 2.4. Configuring Automation Analytics




When you imported your license for the first time, you were automatically opted in for the collection of data that powers Automation Analytics, a cloud service that is part of the Ansible Automation Platform subscription.

**Prerequisites**

- A service account created with the **Automation Analytics Viewer** role in console.redhat.com. For more information, see [Creating a service account](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/creating_and_managing_service_accounts/proc-ciam-svc-acct-overview-creating-service-acct#proc-ciam-svc-acct-create-creating-service-acct) .


**Procedure**

1. From the navigation panel, selectSettings→Automation Execution→System.
1. ClickEdit.
1. In the field labeled **Red Hat Client ID for Analytics** , enter the client ID you received when you created your service account to retrieve subscription and content information.
1. In the field labeled **Red Hat Client Secret for Analytics** , enter the client secret you received when you created your service account to send data to Automation Analytics.
1. In the **Options** list select the checkbox to **Gather data for Automation Analytics** .
1. ClickSave.


**Verification**

After configuring the service account, run a test job to ensure everything is set up correctly.


1. From the navigation panel, selectAutomation Execution→Jobsto launch a job.
1. Check [analytics at console.redhat.com](https://console.redhat.com/ansible/automation-analytics/reports) to confirm that the data is being posted.


