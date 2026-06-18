# GitLab Personal Access Token credential type

Select this credential to access GitLab by using a *Personal Access Token* (PAT), which you can get through GitLab.

For more information, see [Setting up a GitLab webhook](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_work_with_webhooks#controller-set-up-gitlab-webhook "Automation controller has the ability to run jobs based on a triggered webhook event coming in. Job status information (pending, error, success) can be sent back only for pull request events.").

GitLab PAT credentials require a value in the **Token** field, which is provided in your GitLab profile settings.

Use this credential to establish an API connection to GitLab for use in webhook listener jobs, to post status updates.
