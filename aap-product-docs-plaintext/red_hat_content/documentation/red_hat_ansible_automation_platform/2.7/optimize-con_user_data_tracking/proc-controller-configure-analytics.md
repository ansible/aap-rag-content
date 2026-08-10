# Get insights on automation across your environment with Automation Analytics
## Configure Automation Analytics (Optional)

Ansible Automation Platform automatically authenticates analytics transmission using your platform subscription certificate. If you prefer to use explicit credential management, you can optionally configure a service account.

### Before you begin

- A service account created with the **Automation Analytics Viewer** role in console.redhat.com. For more information, see [Creating a service account](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/creating_and_managing_service_accounts/proc-ciam-svc-acct-overview-creating-service-acct#proc-ciam-svc-acct-create-creating-service-acct).

### About this task

Use this procedure if you want to configure a service account for analytics instead of using automatic certificate-based authentication.

### Procedure

1.  From the navigation panel, select Settings> (and then)Automation Execution> (and then)System.
2.  Click Edit.
3. **Optional:** In the field labeled **Red Hat Client ID for Analytics**, enter the client ID you received when you created your service account to retrieve subscription and content information.
4. **Optional:** In the field labeled **Red Hat Client Secret for Analytics**, enter the client secret you received when you created your service account to send data to Automation Analytics.
5.  In the **Options** list select the checkbox to **Gather data for Automation Analytics**.
6.  Click Save.

### Results

Analytics data is transmitted to Red Hat automatically. If you configured a service account, run a test job to verify the configuration.

1. From the navigation panel, select Automation Execution> (and then)Jobs to launch a job.
2. Check [analytics at console.redhat.com](https://console.redhat.com/ansible/automation-analytics/reports) to confirm that the data is being posted.

