# Integrate with the cloud.terraform collection
## Create and launch a job template

Create and launch a job template to complete the integration and use the automation features in Ansible Automation Platform.

### Procedure

1.  From the navigation panel, select **Automation Execution> (and then)Templates**.
2.  Select **Create template > Create Job Template**.
3.  From the **Execution Environment** list, select the environment you created.
4.  From the **Credentials** list, select the credentials instance you created previously. If you do not see the credentials, click Browse to see more options in the list.
5.  Enter any additional information for the required fields.
6.  Click Create job template.
7.  Click Launch template.
8.  To launch the job, click Next and Finish. The job output shows that the job has run.

### Results

To see that the job has run successfully from the Terraform user interface, select **Workspaces > Ansible-Content-Integration > Run**. The Run list shows the state of the Triggered via CLI job. You can see it go from the Queued to the Plan Finished state.
