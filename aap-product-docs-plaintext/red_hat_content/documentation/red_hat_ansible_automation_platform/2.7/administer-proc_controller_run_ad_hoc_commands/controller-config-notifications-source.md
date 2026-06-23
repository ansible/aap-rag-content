# Run ad hoc commands against a host in an inventory
## Configure notifications for the source

After you create a source for an inventory in automation controller, you can configure notifications for that source.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want to configure notifications for.
3.  In the inventory **Details** page, select the **Notifications** tab. Note:
The **Notifications** tab is only present when you have saved the newly-created source.

4.  If notifications are already set up, use the toggles to enable or disable the notifications to use with your particular source. For more information, see [Enable and Disable Notifications](/documentation/en-us/red_hat_ansible_automation_platform/2.7/observe-con_controller_configure_hostname_notifications#controller-enable-disable-notifications "You can set up notifications to notify you when a specific job starts, and on the success or failure at the end of the job run. Note the following behaviors:").
5.  If you have not set up notifications, see [Notifiers](/documentation/en-us/red_hat_ansible_automation_platform/2.7/observe-assembly_ug_controller_notifications#controller-notifications "A Notification Type such as Email, Slack or a Webhook, is an instance of a Notification Template, and has a name, description and configuration defined in the Notification template.") for more information.
6.  Review your entries and selections.
7.  Click Save.

### What to do next

When you define a source, it is displayed in the list of sources associated with the inventory. From the **Sources** tab you can perform a sync on a single source, or sync all of them at once. You can also perform additional actions such as scheduling a sync process, and edit or delete the source.

