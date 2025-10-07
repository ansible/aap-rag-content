# 3. Getting started as an automation developer
## 3.13. Create and run a rulebook activation
### 3.13.1. Setting up a rulebook activation




**Prerequisites**

- You have set up a project.
- You have set up a decision environment.


**Procedure**

1. From the navigation panel, selectAutomation Decisions→Rulebook Activations.
1. ClickCreate rulebook activation.
1. Enter the following information:


-  **Name** : Insert the name.
-  **Description** : This field is optional.
-  **Organization** : This field is optional.
-  **Project** : This field is optional.
-  **Rulebook** : Rulebooks are displayed according to the project you selected.
-  **Credential** : Select 0 or more credentials for this rulebook activation. This field is optional.

Note
The credentials that display in this field are customized based on your rulebook activation and only include the following credential types: Vault, Red Hat Ansible Automation Platform, or any custom credential types that you have created. For more information about credentials, see [Credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_decisions/eda-credentials) in the Using automation decisions guide.




-  **Decision environment** : A decision environment is a container image to run Ansible rulebooks.

Note
In Event-Driven Ansible controller, you cannot customize the pull policy of the decision environment. By default, it follows the behavior of the **always** policy. Every time an activation is started, the system tries to pull the most recent version of the image.




-  **Restart policy** : This is the policy that determines how an activation should restart after the container process running the source plugin ends. Select from the following options:


-  **Always** : This restarts the rulebook activation immediately, regardless of whether it ends successfully or not, and occurs no more than 5 times.
-  **Never** : This never restarts a rulebook activation when the container process ends.
-  **On failure** : This restarts the rulebook activation after 60 seconds by default, only when the container process fails, and occurs no more than 5 times.

-  **Log level** : This field defines the severity and type of content in your logged events. Select from one of the following options:


-  **Error** : Logs that contain error messages that are displayed in the **History** tab of an activation.
-  **Info** : Logs that contain useful information about rulebook activations, such as a success or failure, triggered action names and their related action events, and errors.
-  **Debug** : Logs that contain information that is only useful during the debug phase and might be of little value during production. This log level includes both error and log level data.

-  **Service name** : This defines a service name for Kubernetes to configure inbound connections if the activation exposes a port. This field is optional.
-  **Rulebook activation enabled?** : Toggle to automatically enable the rulebook activation to run.
-  **Variables** : The variables for the rulebook are in JSON or YAML format. The content would be equivalent to the file passed through the `        --vars` flag of ansible-rulebook command.
-  **Options** : Check the **Skip audit events** option if you do not want to see your events in the Rule Audit.

1. ClickCreate rulebook activation.


Your rulebook activation is now created and can be managed on the **Rulebook Activations** page.

After saving the new rulebook activation, the rulebook activation’s details page is displayed, with either a **Pending** , **Running** , or **Failed** status. From there or the **Rulebook Activations** list view, you can restart or delete it.

Note
Occasionally, when a source plugin shuts down, it causes a rulebook to exit gracefully after a certain amount of time. When a rulebook activation shuts down, any tasks that are waiting to be performed will be canceled, and an info level message is sent to the activation log. For more information, see [Rulebooks](https://ansible.readthedocs.io/projects/rulebook/en/stable/rulebooks.html#) .



#### 3.13.1.1. Rulebook activation list view




On the **Rulebook Activations** page, you can view the rulebook activations that you have created along with the **Status** , **Number of rules** with the rulebook, the **Fire count** , and **Restart count** .

If the **Status** is **Running** , it means that the rulebook activation is running in the background and executing the required actions according to the rules declared in the rulebook.

You can view more details by selecting the activation from the **Rulebook Activations** list view.

For all activations that have run, you can view the **Details** and **History** tabs to get more information about what happened.

