# Integrate with Red Hat Lightspeed (formerly Insights)
## Remediate a Red Hat Lightspeed inventory

Remediation of a Red Hat Lightspeed inventory enables automation controller to run Red Hat Lightspeed playbooks with a single click.

### About this task

You can do this by creating a job template to run the Red Hat Lightspeed remediation.

### Procedure

1.  From the navigation menu, select Automation Execution> (and then)Templates.
2.  On the **Templates** list view, click Create template and select from the list.
3.  Enter the appropriate details in the following fields. Note that the following fields require specific Red Hat Lightspeed related entries:

- **Name**: Enter the name of your Maintenance Plan.
- Optional: **Description**: Enter a description for the job template.
- **Job Type**: If not already populated, select **Run** from the job type list.
- **Inventory**: Select the Red Hat Lightspeed inventory that you previously created.
- **Project**: Select the Red Hat Lightspeed project that you previously created.
- Optional: **Execution Environment**: The container image to be used for execution.
- **Playbook**: Select a playbook associated with the Maintenance Plan that you want to run from the playbook list.
- Optional: **Credentials**: Enter the credential to use for this project or click the search (![Search](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/magnify.png)) icon and select it from the pop-up window. The credential does not have to be a Red Hat Lightspeed credential.
- **Verbosity**: Keep the default setting, or select the required verbosity from the list.
![Red Hat Lightspeed job template](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-insights-create-job-template.png)

4.  Click Create job template.
5.  Click the launch ![Launch](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/rightrocket.png) icon to launch the job template.

### Results

When complete, the job results in the **Job Details** page.
