# 2. Integrating from Ansible Automation Platform
## 2.3. Creating and launching a job template




Create and launch a job template to complete the integration and use the automation features in Ansible Automation Platform.

**Procedure**

1. From the navigation panel, select **Automation Execution→Templates** .
1. Select **Create template > Create Job Template** .
1. From the **Execution Environment** list, select the environment you created.
1. From the **Credentials** drop-down list, select the credentials instance you created previously. If you do not see the credentials, select **Browse** to see more options in the list.
1. Enter any additional information for the required fields.
1. ClickCreate job template.
1. ClickLaunch template.
1. To launch the job, clickNextandFinish. The job output shows that the job has run.


**Verification**

To see that the job has run successfully from the Terraform user interface, select **Workspaces > Ansible-Content-Integration > Run** . The Run list shows the state of the Triggered via CLI job. You can see it go from the Queued to the Plan Finished state.


**Additional resources**

-  [Adding an execution environment to a job template](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/assembly-controller-execution-environments#proc-controller-use-an-exec-env)
-  [Configuring automation execution](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/index)
-  [Hashicorp Terraform Enterprise documentation](https://developer.hashicorp.com/terraform/enterprise)


