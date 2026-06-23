# Trigger automation with webhooks
## Set up a GitLab webhook

Automation controller has the ability to run jobs based on a triggered webhook event coming in. Job status information (pending, error, success) can be sent back only for pull request events.

### About this task

If automation controller is not required to post job statuses back to the webhook service, go directly to step 3.

### Procedure

1.  Generate a *Personal Access Token* (PAT) for use with automation controller:
1.  From the navigation panel in GitLab, select your avatar and Edit profile.
2.  From the navigation panel, select Access tokens.
3.  Complete the following fields:

- **Token name**: Enter a brief description about what this PAT is used for.
- **Expiration date**: Skip this field unless you want to set an expiration date for your webhook.
- **Select scopes**: Select those that are applicable to your integration. For automation controller, **api** is the only selection necessary.

4.  Click Create personal access token.  Important:
When the token is generated, ensure that you copy the PAT, as you need it in step 2. You cannot access this token again in GitLab.

2.  Use the PAT to optionally create a GitLab credential:
1.  Go to your instance, and create a new credential for the GitLab PAT, using the generated token.
2.  Make note of the name of this credential, as you use it in the job template that posts back to GitLab.
![GitLab PAT token](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-webhooks-create-credential-gitlab-pat-token.png)
3.  Go to the job template with which you want to enable webhooks, and select the webhook service and credential you created in the preceding step.
![GitLab webhook credential](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-gitlab-webhook-credential.png)
4.  Click Save. Your job template is set up to post back to GitLab.
3.  Go to a GitLab repository where you want to configure webhooks.
4.  From the navigation panel, select Settings> (and then)Integrations.
5.  To complete the **Add webhook** page, you must check the **Enable Webhook** option in a job template or workflow job template. For more information, see step 3 in both [Creating a job template](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_controller_create_job_template#controller-create-job-template "A job template is a definition and set of parameters for running an Ansible job. Use job templates to launch jobs.") and [Creating a workflow job template](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_controller_create_workflow_template#controller-create-workflow-template "To create a new workflow job template, complete the following steps:").
6.  Complete the following fields:

- **URL**: Copy the contents of the **Webhook URL** from the job template and paste it here. The results are sent to this address from GitLab.
- **Secret Token**: Copy the contents of the **Webhook Key** from the job template and paste it here.
- **Trigger**: Select the types of events you want to trigger a webhook. Any such event will trigger the job or workflow. To have job status (pending, error, success) sent back to GitLab, you must select **Merge request events** in the **Trigger** section.
- **SSL verification**: Leave **Enable SSL verification** selected.

7.  Click Add webhook.
8.  When your webhook is configured, it is displayed in the list **Project Webhooks** for your repository, along with the ability to test events, edit or delete the webhook. Testing a webhook event displays the results on each page whether it succeeded or failed.

