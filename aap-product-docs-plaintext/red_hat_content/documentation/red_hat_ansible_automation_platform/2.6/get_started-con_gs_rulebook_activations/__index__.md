# Configure rulebooks to take action in response to events or conditions

In Event-Driven Ansible, a rulebook activation is a process running in the background defined by a decision environment executing a specific rulebook.

## Set up a rulebook activation

Follow the steps in this procedure to set up a rulebook activation.

### Before you begin

- You have set up a project.
- You have set up a decision environment.

### Procedure

1.  From the navigation panel, select Automation Decisions> (and then)Rulebook Activations.
2.  Click Create rulebook activation.
3.  Enter the following information:

- **Name**: Insert the name.
- **Description**: This field is optional.
- **Organization**: This field is optional.
- **Project**: This field is optional.
- **Rulebook**: Rulebooks are displayed according to the project you selected.
- **Credential**: Select 0 or more credentials for this rulebook activation. This field is optional. Note:
The credentials that display in this field are customized based on your rulebook activation and only include the following credential types: Vault, Red Hat Ansible Automation Platform, or any custom credential types that you have created. For more information about credentials, see [Credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_credentials "You can use credentials to store secrets that can be used for authentication purposes with resources, such as decision environments, rulebook activations and projects for Event-Driven Ansible controller, and projects for automation controller.") .

- **Decision environment**: A decision environment is a container image to run Ansible rulebooks. Note:
In Event-Driven Ansible controller, you cannot customize the pull policy of the decision environment. By default, it follows the behavior of the **always** policy. Every time an activation is started, the system tries to pull the most recent version of the image.

- **Restart policy**: This is the policy that determines how an activation should restart after the container process running the source plugin ends. Select from the following options:
* **Always**: This restarts the rulebook activation immediately, regardless of whether it ends successfully or not, and occurs no more than 5 times.
* **Never**: This never restarts a rulebook activation when the container process ends.
* **On failure**: This restarts the rulebook activation after 60 seconds by default, only when the container process fails, and occurs no more than 5 times.
- **Log level**: This field defines the severity and type of content in your logged events. Select from one of the following options:
* **Error**: Logs that contain error messages that are displayed in the **History** tab of an activation.
* **Info**: Logs that contain useful information about rulebook activations, such as a success or failure, triggered action names and their related action events, and errors.
* **Debug**: Logs that contain information that is only useful during the debug phase and might be of little value during production. This log level includes both error and log level data.
- **Service name**: This defines a service name for Kubernetes to configure inbound connections if the activation exposes a port. This field is optional.
- **Rulebook activation enabled?**: Toggle to automatically enable the rulebook activation to run.
- **Variables**: The variables for the rulebook are in JSON or YAML format. The content would be equivalent to the file passed through the `--vars` flag of ansible-rulebook command.
- **Options**: Check the **Skip audit events** option if you do not want to see your events in the Rule Audit.

4.  Click Create rulebook activation.

### Results

Your rulebook activation is now created and can be managed on the **Rulebook Activations** page.

Note:

Occasionally, when a source plugin shuts down, it causes a rulebook to exit gracefully after a certain amount of time. When a rulebook activation shuts down, any tasks that are waiting to be performed will be canceled, and an info level message is sent to the activation log. For more information, see [Rulebooks](https://docs.ansible.com/projects/rulebook/en/latest/rulebooks.html#).

After saving the new rulebook activation, the rulebook activation’s details page is displayed, with either a **Pending**, **Running**, or **Failed** status. From there or the **Rulebook Activations** list view, you can restart or delete it.

## Rulebook activation list view

Use the **Rulebook Activations** list view to quickly monitor the operational status, event fire count, and restart frequency of all your deployed automation services.

If the **Status** is **Running**, it means that the rulebook activation is running in the background and executing the required actions according to the rules declared in the rulebook.

You can view more details by selecting the activation from the **Rulebook Activations** list view.

For all activations that have run, you can view the **Details** and **History** tabs to get more information about what happened.

## Enable and disable rulebook activations

Toggle the state of an activation to start or stop event processing instantly, allowing for temporary pauses, maintenance, or troubleshooting without deletion.

### Procedure

1.  Select the switch on the row level to enable or disable your chosen rulebook.
2.  In the window, select Yes, I confirm that I want to enable/disable these X rulebook activations.
3.  Select Enable/Disable rulebook activation.

## Restart rulebook activations

Restart an activation to immediately apply configuration changes, update rulebook content, or quickly recover from unexpected failures.

### About this task

Note:

You can only restart a rulebook activation if it is currently enabled and the restart policy was set to **Always** when it was created.

### Procedure

1.  Select the More Actions icon **⋮** next to **Rulebook Activation enabled/disabled** toggle.
2.  Select Restart rulebook activation.
3.  In the window, select Yes, I confirm that I want to restart these X rulebook activations.
4.  Select Restart rulebook activations.

## Delete rulebook activations

End and permanently remove a rulebook activation and its configuration when its automated event-driven workflow is no longer required.

### Procedure

1.  Select the More Actions icon **⋮** next to the **Rulebook Activation enabled/disabled** toggle.
2.  Select Delete rulebook activation.
3.  In the window, select Yes, I confirm that I want to delete these X rulebook activations.
4.  Select Delete rulebook activations.

## Activate webhook-based automation in Openshift

In Openshift environments, you can activate webhooks by creating a route to expose the activation’s service, enabling external systems to send events and trigger automation.

### Before you begin

- You have created a rulebook activation.


Note:

The following is an example of rulebook with a given webhook:

```
- name: Listen for storage-monitor events
hosts: all
sources:
- ansible.eda.webhook:
host: 0.0.0.0
port: 5000
rules:
- name: Rule - Print event information
condition: event.meta.headers is defined
action:
run_job_template:
name: StorageRemediation
organization: Default
job_args:
extra_vars:
message: from eda
sleep: 1
```

### Procedure

1.  Create a Route (on OpenShift Container Platform) to expose the service. The following is an example Route for an ansible-rulebook source that expects POST’s on port 5000 on the decision environment pod:


```
kind: Route
apiVersion: route.openshift.io/v1
metadata:
name: test-sync-bug
namespace: dynatrace
labels:
app: eda
job-name: activation-job-1-5000
spec:
host: test-sync-bug-dynatrace.apps.aap-dt.ocp4.testing.ansible.com
to:
kind: Service
name: activation-job-1-5000
weight: 100
port:
targetPort: 5000
tls:
termination: edge
insecureEdgeTerminationPolicy: Redirect
wildcardPolicy: None
```

2.  When you create the Route, test it with a **Post to the Route URL**:

Note:
You do not need the port as it is specified on the Route (targetPort).

```
curl -H "Content-Type: application/json" -X POST
test-sync-bug-dynatrace.apps.aap-dt.ocp4.testing.ansible.com -d
'{}'
```
