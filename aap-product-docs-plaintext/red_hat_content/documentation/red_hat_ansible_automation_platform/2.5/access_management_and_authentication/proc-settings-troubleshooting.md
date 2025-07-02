# 7. Configuring Ansible Automation Platform
## 7.4. Troubleshooting options




You can use the **Troubleshooting** page to enable or disable certain flags that aid in debugging issues within Ansible Automation Platform.

**Procedure**

1. From the navigation panel, selectSettings→Automation Execution→Troubleshooting.
1. The **Troubleshooting** page is displayed.
1. ClickEdit.
1. You can select the following options:


-  **Enable or Disable tmp dir cleanup** : Select this to enable or disable the cleanup of tmp directories generated during execution of a job after job execution completes.
-  **Debug Web Requests** : Select this to enable or disable web request profiling for debugging slow web requests.
-  **Release Receptor Work** : Select this to turn on or off the deletion of job pods after they complete or fail. This can be helpful in debugging why a job failed.
-  **Keep receptor work on error** : Select this to prevent receptor work from being released when an error is detected.

1. ClickSaveto save your changes.



<span id="idm140322435663072"></span>
