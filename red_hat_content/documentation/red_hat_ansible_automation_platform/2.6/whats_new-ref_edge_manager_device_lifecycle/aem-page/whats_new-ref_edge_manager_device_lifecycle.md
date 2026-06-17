+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_device_lifecycle"
title = "Run user-defined commands with device lifecycle hooks - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_device_lifecycle/aem-page/whats_new-ref_edge_manager_device_lifecycle.html"
last_crumb = "Run user-defined commands with device lifecycle hooks"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Run user-defined commands with device lifecycle hooks"
oversized = "false"
page_slug = "whats_new-ref_edge_manager_device_lifecycle"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_device_lifecycle"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-ref_edge_manager_device_lifecycle/toc/toc.json"
type = "aem-page"
+++

# Run user-defined commands with device lifecycle hooks

The Red Hat Edge Manager agent uses lifecycle hooks to run user-defined commands at specific stages. For example, you can add a backup script to back up application data that must be completed before an operating system update can begin.

As another example, certain applications or system services do not automatically reload their configuration file when the file changes on the disk. You can manually reload the configuration file by specifying a command as another hook, which is called after the agent completes the update process.

The following device lifecycle hooks are supported:

| Lifecycle Hook         | Description                                                                                                                                                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `beforeUpdating`  | <br>This hook is called after the agent completed preparing for the update and before actually making changes to the system. If an action in this hook returns with failure, the agent cancels the update.                        |
| <br> `afterUpdating`   | <br>This hook is called after the agent has written the update to disk. If an action in this hook returns with failure,the agent cancels and rolls back the update.                                                               |
| <br> `beforeRebooting` | <br>This hook is called before the system reboots. The agent blocks the reboot until running the action has completed or timed out. If any action in this hook returns with failure, the agent cancels and rolls back the update. |
| <br> `afterRebooting`  | <br>This hook is called when the agent first starts after a reboot. If any action in this hook returns with failure, the agent reports this but continues starting up.                                                            |

## Rule files

You can define device lifecycle hooks by adding rule files to one of the following locations in the device file system:

- Rules in the `/usr/lib/flightctl/hooks.d/<lifecycle_hook_name>/` drop-in directory are read-only. To add rules to the `/usr` directory, you must add them to the operating system image during image building.
- Rules in the `/etc/flightctl/hooks.d/<lifecycle_hook_name>/` drop-in directory are read-writable. You can update the rules at runtime by using several methods.


When creating and placing the files, you must consider the following practices:

- The name of the rule must be all lower case.
- If you define rules in both locations, the rules are merged.
- If you add more than one rule files to a lifecycle hook directory, the files are processed in lexical order of the file names.
- If you define files with identical file names in both locations, the file in the `/etc` folder takes precedence over the file of the same name in the `/usr` folder.


A rule file is written in YAML format and has a list of one or more actions. An action can be an instruction to run an external command.

When you specify many actions for a hook, the actions are performed in sequence, finishing one action before starting the next.

If an action returns with a failure, the following actions are skipped.

A `run` action takes the following parameters:

| Parameter      | Description                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `Run`     | <br>The absolute path to the command to run, followed by any flags or arguments, for example `/usr/bin/nmcli connection reload`. The command is not executed in a shell, so you cannot use shell variables, such as `$PATH` or `$HOME`, or chain commands, such as `|` or `;`. If necessary, you can start a shell by specifying the shell as command to run, for example `/usr/bin/bash -c 'echo $SHELL $HOME $USER'`. |
| <br> `EnvVars` | <br>Optional. A list of key-value pairs to set as environment variables for the command.                                                                                                                                                                                                                                                                                                                                |
| <br> `WorkDir` | <br>Optional. The directory the command is run from.                                                                                                                                                                                                                                                                                                                                                                    |
| <br> `Timeout` | <br>Optional. The maximum duration that is allowed for the action to complete. Specify the duration as a single positive integer followed by a time unit. The `s`, `m`, and `h` units are supported for seconds, minutes, and hours.                                                                                                                                                                                    |
| <br> `If`      | <br>Optional. A list of conditions that must be true for the action to be run. If not provided, actions run unconditionally.                                                                                                                                                                                                                                                                                            |


By default, the system performs actions every time the hook is triggered. However, for the `afterUpdating` hook, you can use the `If` parameter to add conditions that must be true for an action to be performed. Otherwise, the action is skipped.

For example, to run an action only if a given file or directory changes during the update, you can define a path condition that takes the following parameters:

| Parameter       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `Job type` | <br>An absolute path to a file or directory that must change during the update as a condition for the action to be performed. Specify paths by using forward slashes (/):<br>If the path is to a directory, it must end with a forward slash (`/`).If you specify a path to a file, the file must have changed to satisfy the conditionIf you specify a path to a directory, a file in that directory or any of its subdirectories must have changed to satisfy the condition |
| <br> `Op`       | <br>A list of file operations, such as `created`, `updated`, and `removed`, to limit the type of changes to the specified path as a condition for the action to be performed.                                                                                                                                                                                                                                                                                                 |


If you specify a path condition for an action in the `afterUpdating` hook, you have the following variables that you can include in arguments to your command and are replaced with the absolute paths to the changed files:

| Variable                 | Description                                                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| <br> `${ Path }`         | <br>The absolute path to the file or directory specified in the path condition.                                                      |
| <br> `${ Files }`        | <br>A space-separated list of absolute paths of the files that changed during the update and are covered by the path condition.      |
| <br> `${ CreatedFiles }` | <br>A space-separated list of absolute paths of the files that were created during the update and are covered by the path condition. |
| <br> `${ UpdatedFiles }` | <br>A space-separated list of absolute paths of the files that were updated during the update and are covered by the path condition. |
| <br> `${ RemovedFiles }` | <br>A space-separated list of absolute paths of the files that were removed during the update and are covered by the path condition. |


The Red Hat Edge Manager agent includes a built-in set of rules defined in `/usr/lib/flightctl/hooks.d/afterupdating/00-default.yaml`. The following commands are executed if certain files are changed:

| File                                           | Command                        | Description                                                                                                                                                                                                                  |
| ---------------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `/etc/systemd/system/`                    | <br> `systemctl daemon-reload` | <br>Changes to `systemd` units are activated by signaling the `systemd` daemon to reload the `systemd` manager configuration. This reruns all generators, reloads all unit files, and re-creates the entire dependency tree. |
| <br> `/etc/NetworkManager/system-connections/` | <br> `nmcli conn reload`       | <br>Changes to `NetworkManager` system connections are activated by signaling the `NetworkManager` daemon to reload all connections. For more information, see the *Additional resources* section.                           |
| <br> `/etc/firewalld/`                         | <br> `firewall-cmd --reload`   | <br>Changes to the permanent configuration of `firewalld` are activated by signaling `firewalld` to reload firewall rules as new runtime configuration.                                                                      |
