# 4. Management Jobs
## 4.1. Removing old activity stream data
### 4.1.1. Scheduling deletion




Use the following procedure to review or set a schedule for purging data marked for deletion:

**Procedure**

1. For a particular cleanup job, click the **Schedules** tab.

![Schedules tab](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuring_automation_execution-en-US/images/3bc3694e0bbb3759b5e87257e85e4c6f/management-jobs-remove-activity-stream-schedule.png)



1. Click the name of the job, **Cleanup Activity Schedule** in this example, to review the schedule settings.
1. ClickEdit scheduleto change them. You can also clickCreate scheduleto create a new schedule for this management job.

![Create new schedule](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuring_automation_execution-en-US/images/b03ad4c801185a680eac37c5eac53509/management-jobs-remove-activity-stream-schedule-details.png)



1. Enter the appropriate details into the following fields and click **Next** :


-  **Schedule name** required
-  **Start date/time** required
-  **Time zone** the entered Start Time should be in this time zone.
-  **Repeat frequency** the appropriate options display as the update frequency is modified including data you do not want to include by specifying exceptions.
-  **Days of data to keep** required - specify how much data you want to retain.



The **Details** tab displays a description of the schedule and a list of the scheduled occurrences in the selected Local Time Zone.

Note
Jobs are scheduled in UTC. Repeating jobs that run at a specific time of day can move relative to a local time zone when Daylight Saving Time shifts occur.



