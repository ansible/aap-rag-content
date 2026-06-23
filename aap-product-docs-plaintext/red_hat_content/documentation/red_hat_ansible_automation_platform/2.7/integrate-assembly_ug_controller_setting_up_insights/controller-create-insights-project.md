# Integrate with Red Hat Lightspeed (formerly Insights)
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

