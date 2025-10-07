# 6. Job templates
## 6.8. Scheduling job templates




Access the schedules for a particular job template from the **Schedules** tab.

**Procedure**

- To schedule a job template, select the **Schedules** tab from the job template, and select the appropriate method:


- If schedules are already set up, review, edit, enable or disable your schedule preferences.
- If schedules have not been set up, see [Schedules](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-schedules) for more information.



If you select **Prompt on Launch** for the **Credentials field** , and you create or edit scheduling information for your job template, a **Prompt** option displays on the Schedules form.

You cannot remove the default machine credential in the **Prompt** dialog without replacing it with another machine credential before you can save it.

Note
To set `extra_vars` on schedules, you must select **Prompt on Launch** for **Variables** on the job template, or configure and enable a survey on the job template.

The answered survey questions then become `extra_vars` .



