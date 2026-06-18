# Run playbooks locally with automation content navigator

Use automation content navigator to run playbooks and interactively delve into play and task results. Compare execution inside and outside of execution environments to identify and troubleshoot problems.

## Run a playbook from automation content navigator

You can run Ansible playbooks with the automation content navigator text-based user interface to follow the execution of the tasks and delve into the results of each task.

### Before you begin

- A playbook.
- A valid inventory file if not using `localhost` or an inventory plugin.

### Procedure

1.  Start automation content navigator


```
$ ansible-navigator
```

2.  Run the playbook.

```
$ :run
```

3.  Optional: type `ansible-navigator run simple-playbook.yml -i inventory.yml` to run the playbook.
4.  Verify or add the inventory and any other command line parameters.

```
INVENTORY OR PLAYBOOK NOT FOUND, PLEASE CONFIRM THE FOLLOWING
─────────────────────────────────────────────────────────────────────────
Path to playbook: /home/ansible-navigator_demo/simple_playbook.yml
Inventory source: /home/ansible-navigator-demo/inventory.yml
Additional command line parameters: Please provide a value (optional)
──────────────────────────────────────────────────────────────────────────
Submit Cancel
```

5.  Tab to `Submit` and hit Enter. You should see the tasks executing.
![Executing playbook tasks](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-play-list.png)
6.  Type the number next to a play to step into the play results, or type `:<number>` for numbers above 9.
![Task list](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-task-list.png)
Notice failed tasks show up in red if you have colors enabled for automation content navigator.

7.  Type the number next to a task to review the task results, or type `:<number>` for numbers above 9.
![Failed task results](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-task-output-failed.png)
8.  Optional: type `:doc` bring up the documentation for the module or plugin used in the task to aid in troubleshooting.

```
ANSIBLE.BUILTIN.PACKAGE_FACTS (MODULE)
0│---
1│doc:
2│  author:
3│  - Matthew Jones (@matburt)
4│  - Brian Coca (@bcoca)
5│  - Adam Miller (@maxamillion)
6│  collection: ansible.builtin
7│  description:
8│  - Return information about installed packages as facts.
<... output omitted ...>
11│  module: package_facts
12│  notes:
13│  - Supports C(check_mode).
14│  options:
15│    manager:
16│      choices:
17│      - auto
18│      - rpm
19│      - apt
20│      - portage
21│      - pkg
22│      - pacman

<... output truncated ...>
```

## Review playbook results

Automation content navigator saves playbook runs as JSON artifact files. You can use these files to share, review, or troubleshoot results without requiring access to the original playbook or inventory.

### Before you begin

- A automation content navigator artifact JSON file from a playbook run.

### Procedure

Start automation content navigator with the artifact file.

```
$ ansible-navigator replay simple_playbook_artifact.json
```

1.  Review the playbook results that match when the playbook ran.
![Playbook results](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-artifact-replay.png)

### Results

You can now type the number next to the plays and tasks to step into each to review the results, as you would after executing the playbook.

## View Ansible configuration file contents in text-based format

As a content creator, you can review your Ansible configuration with automation content navigator and interactively delve into settings.

### Review your Ansible configuration from automation content navigator

Use the automation content navigator interactive interface to review Ansible settings. The tool pulls data from your configuration file or returns defaults if no configuration file is present.

#### Before you begin

- You have authenticated to the Red Hat registry if you need to access additional automation execution environments. See [Red Hat Container Registry Authentication](https://access.redhat.com/RegistryAuthentication) for details.

#### Procedure

1.  Start automation content navigator


```
$ ansible-navigator
```
Optional: type `ansible-navigator config` from the command line to access the Ansible configuration settings.

2.  Review the Ansible configuration.

```
:config
```

![Ansible configuration](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-ansible-config.png)
Some values reflect settings from within the automation execution environments needed for the automation execution environments to function. These display as non-default settings you cannot set in your Ansible configuration file.

3.  Type the number corresponding to the setting you want to delve into, or type `:<number>` for numbers greater than 9.

```
ANSIBLE COW ACCEPTLIST (current: ['bud-frogs', 'bunny', 'cheese']) (default:
0│---
1│current:
2│- bud-frogs
3│- bunny
4│- cheese
5│default:
6│- bud-frogs
7│- bunny
8│- cheese
9│- daemon
```
The output shows the current `setting` as well as the `default`. Note the `source` in this example is `env` since the setting comes from the automation execution environments.

#### Results

- Review the configuration output.
![Configuration output](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/navigator-ansible-config.png)
