# 5. Connecting to Red Hat Ansible Automation Platform
## 5.4. Accessing Red Hat Ansible Automation Platform on Microsoft Azure




When you initiate the deployment of the Red Hat Ansible Automation Platform managed app from Azure marketplace, a form displays in the **Create Red Hat Ansible Automation Platform on Microsoft Azure** window. Complete the form to provision Ansible Automation Platform infrastructure and resources into your Azure tenant.

**Procedure**

1. In a web browser, navigate to the **Managed Applications** section in the Azure console.
1. Select the instance of Ansible Automation Platform on Microsoft Azure that you deployed.
1. Select **Parameters and Outputs** in the **Settings** section in the left navigation menu.


- If this is your first time accessing your Ansible Automation Platform through the Azure portal, you must select and copy the deploymentEngineUrl under the **output** section to continue setting up your deployment. After you set up your instance through the deploymentEngineUrl, it is removed from the outputs section because it is no longer needed.
- If you have already set up your Ansible Automation Platform deployment, you can go directly to it by copying the platformUrl output.

1. Paste the selected URL into your browser search bar and hit enter. This brings you to your Ansible Automation Platform deployment.
1. The first time you log in to Ansible Automation Platform with the URL, you must configure the subscription. For help see the _Logging in for the first time_ section of the [Getting started with Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/getting_started_with_ansible_automation_platform/index) guide.


