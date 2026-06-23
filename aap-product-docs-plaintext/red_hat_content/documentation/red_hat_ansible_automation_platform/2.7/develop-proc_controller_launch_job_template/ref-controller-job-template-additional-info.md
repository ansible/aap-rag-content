# Launch a job template
## Additional information requested when launching a job template

A job can require additional information to run. The following data can be requested at launch:

- Credentials that were setup
- The option **Prompt on Launch** is selected for any parameter
- Passwords or passphrases that have been set to **Ask**
- A survey, if one has been configured for the job templates
- Extra variables, if requested by the job template


Note:

If a job has user-provided values, then those are respected upon relaunch. If the user did not specify a value, then the job uses the default value from the job template. Jobs are not relaunched as-is. They are relaunched with the user prompts re-applied to the job template.

If you give values on one tab, return to a previous tab, continuing to the next tab results in having to re-provide values on the rest of the tabs. Ensure that you complete the tabs in the order that the prompts appear.

When launching, automation controller automatically redirects the web browser to the **Job Status** page for this job under the **Jobs** tab.

You can re-launch the most recent job from the list view to re-run on all hosts or just failed hosts in the specified inventory. For more information, see the [Jobs in automation controller](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_jobs#controller-jobs "A job is an instance of automation controller launching an Ansible Playbook against an inventory of hosts.") section.

When slice jobs are running, job lists display the workflow and job slices, and a link to view their details individually.

Note:

You can launch jobs in bulk by using the newly added endpoint in the API, `/api/v2/bulk/job_launch`. This endpoint accepts JSON and you can specify a list of unified job templates (such as job templates and project updates) to launch. The user must have the appropriate permission to launch all the jobs. If all jobs are not launched an error is returned indicating why the operation was not able to complete. Use the `OPTIONS` request to return relevant schema. For more information, see [Use the REST API to browse, query, filter, and authenticate](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_api_tools "Representational State Transfer (REST) relies on a stateless, client/server, and cacheable communications protocol, usually the HTTP protocol.")

