# Run jobs on execution nodes

You must specify where jobs run from, or they default to running in the control cluster. To do this, set up a Job Template. For more information about Job Templates, see [Standardize and streamline automation with automation job templates](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_job_templates "You can create both Job templates and Workflow job templates from Automation Execution > Templates .").

## Procedure

1.  The **Templates** list view shows job templates that are currently available. From this screen you can launch ![Launch](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/rightrocket.png), edit ![Edoit](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/leftpencil.png), and duplicate ![Duplicate](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/copy.png) a workflow job template.
2.  Select the job you want and click the ![Launch](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/rightrocket.png) icon.
3.  Select the **Instance Group** on which you want to run the job. Note that a System Administrator must grant you or your team permissions to be able to use an instance group in a job template. If you select multiple jobs templates, the order in which you select them sets the execution precedence.
4.  Click Next.
5.  Click Launch.

