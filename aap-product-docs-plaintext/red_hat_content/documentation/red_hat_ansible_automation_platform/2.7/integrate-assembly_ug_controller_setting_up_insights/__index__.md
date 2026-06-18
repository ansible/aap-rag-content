# Integrate with Red Hat Lightspeed (formerly Insights)

Automation controller supports integration with Red Hat Lightspeed.

When a host is registered with Red Hat Lightspeed, it is scanned continually for vulnerabilities and known configuration conflicts. Each problem identified can have an associated fix in the form of an Ansible Playbook.

Red Hat Lightspeed users create a maintenance plan to group the fixes and can create a playbook to mitigate the problems. Automation controller tracks the maintenance plan playbooks through a Red Hat Lightspeed project.

Authentication to Red Hat Lightspeed through Basic Authorization is backed by a special credential, which must first be established in automation controller.

To run a Red Hat Lightspeed maintenance plan, you need a Red Hat Lightspeed project and inventory.

## Create Red Hat Lightspeed credentials

To create a Red Hat Lightspeed credential, use the following procedure.

### Before you begin

- To use token-based authentication, you must [create a Red Hat service account](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/creating_and_managing_service_accounts/proc-ciam-svc-acct-overview-creating-service-acct#proc-ciam-svc-acct-create-creating-service-acct) to generate a **Client ID** and **Client secret**.
- Assign this service account to the appropriate **User Access** group with necessary permissions.


To enable integration between Ansible Automation Platform and Red Hat Lightspeed, assign the service account the following permissions:

- **inventory:hosts:read** (included in the Inventory Hosts viewer role)
- **patch:read** (included in the Patch viewer role)
- **remediations:remediation:read** and **playbook-dispatcher:run:read** (included in the Remediations user role)


You might consider associating your service account with an existing user access group that already has the required permissions, or creating a new user access group.

Note:

In adherence to security guidelines, service accounts are not automatically included in the default access group. To grant access, you must manually add them to the appropriate user access groups.

If you are not an organization administrator, you can create a service account and then ask your administrator to add your account to the appropriate user access groups.

After you have created a service account and assigned it the appropriate permissions, you can create a new credential for use with Red Hat Lightspeed.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Credentials.
2.  Click Create credential.
3.  Enter the appropriate details in the following fields:

- **Name**: Enter the name of the credential.
- Optional: **Description**: Enter a description for the credential.
- Optional: **Organization**: Enter the name of the organization with which the credential is associated, or click the search ![Search](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/search.png) icon and select it from the **Select organization** window.
- **Credential type**: Enter **Red Hat Lightspeed** or select it from the list.  Note:
Use the **Username** and **Password** fields for Basic authentication. You can leave these blank if using **Client ID** and **Client secret**.

- **Client ID**: Enter the client ID you received when you created your service account.
- **Client secret**: Enter the client secret you received when you created your service account.

4.  Click Create credential. You can now use this credential in an [Source an inventory from Red Hat Lightspeed](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-inv-source-rhlightspeed "You can create an inventory source that uses Red Hat Lightspeed as the source of hosts.") and [Red Hat Lightspeed project](/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-assembly_ug_controller_setting_up_insights#controller-create-insights-project "Create an automation controller project linked to Red Hat Lightspeed and retrieve remediation playbooks. This streamlines your efforts to address vulnerabilities and keep system configurations.").

- If you receive a project sync failure, see the steps in [Remediating a Red Hat Lightspeed inventory](/documentation/en-us/red_hat_ansible_automation_platform/2.7/integrate-assembly_ug_controller_setting_up_insights#controller-remediate-insights-inventory "Remediation of a Red Hat Lightspeed inventory enables automation controller to run Red Hat Lightspeed playbooks with a single click.") and check your analytics logs.


Important:

You must recreate existing credentials and reassociate them with existing projects and inventory sources to support token-based authentication.

## Create a Red Hat Lightspeed project

Create an automation controller project linked to Red Hat Lightspeed and retrieve remediation playbooks. This streamlines your efforts to address vulnerabilities and keep system configurations.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Projects.
2.  Click Create project.
3.  Enter the appropriate details in the following fields. Note that the following fields require specific Red Hat Lightspeed related entries:

- **Name**: Enter the name for your Red Hat Lightspeed project.
- Optional: **Description**: Enter a description for the project.
- **Organization**: Enter the name of the organization with which the credential is associated, or click the search ![Search](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/search.png) icon and select it from the **Select organization** window.
- Optional: **Execution environment**: The execution environment that is used for jobs that use this project.
- **Source control type**: Select **Red Hat Lightspeed**.
- Optional: **Content signature validation credential**: Enable content signing to verify that the content has remained secure when a project is synced.
- **Red Hat Lightspeed credential**: This is pre-populated with the Red Hat Lightspeed credential you created before. If not, enter the credential, or click the search ![Search](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/search.png) icon and select it from the **Select Red Hat Lightspeed Credential** window.

4.  Select the update options for this project from the **Options** field and provide any additional values, if applicable. For more information about each option click the tooltip ![tooltip](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/question-circle.png) icon next to each one.
![Red Hat Lightspeed create project](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-insights-create-project-insights-form.png)
5.  Click Create project. All SCM and project synchronizations occur automatically the first time you save a new project.

### What to do next

If you want them to be updated to what is current in Red Hat Lightspeed, manually update the SCM-based project by clicking the **Update**![Update](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-update-button.png) icon under the project’s available actions.

This process syncs your Red Hat Lightspeed project with your Red Hat Lightspeed account solution. Note that the status dot beside the name of the project updates once the sync has run.

## Create a Red Hat Lightspeed inventory

The Red Hat Lightspeed playbook contains a `hosts:` line where the value is the hostname supplied to Red Hat Lightspeed, which can be different from the hostname supplied to automation controller.

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
