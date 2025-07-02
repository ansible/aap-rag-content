# 6. Running Ansible playbooks with automation content navigator
## 6.1. Executing a playbook from automation content navigator




You can run Ansible playbooks with the automation content navigator text-based user interface to follow the execution of the tasks and delve into the results of each task.

**Prerequisites**

- A playbook.
- A valid inventory file if not using `    localhost` or an inventory plugin.


**Procedure**

1. Start automation content navigator


```
$ ansible-navigator
```


1. Run the playbook.


```
$ :run
```


1. Optional: type `    ansible-navigator run simple-playbook.yml -i inventory.yml` to run the playbook.
1. Verify or add the inventory and any other command line parameters.


```
INVENTORY OR PLAYBOOK NOT FOUND, PLEASE CONFIRM THE FOLLOWING    ─────────────────────────────────────────────────────────────────────────       Path to playbook: /home/ansible-navigator_demo/simple_playbook.yml       Inventory source: /home/ansible-navigator-demo/inventory.yml      Additional command line parameters: Please provide a value (optional)    ──────────────────────────────────────────────────────────────────────────                                                               Submit Cancel
```


1. Tab to `    Submit` and hit Enter. You should see the tasks executing.

![Executing playbook tasks](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/a3706c3ec1968a9904cfe1698883df98/navigator-play-list.png)



1. Type the number next to a play to step into the play results, or type `    :&lt;number&gt;` for numbers above 9.

![Task list](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/7dc3cc85136b2385479f478dfec6a029/navigator-task-list.png)


Notice failed tasks show up in red if you have colors enabled for automation content navigator.


1. Type the number next to a task to review the task results, or type `    :&lt;number&gt;` for numbers above 9.

![Failed task results](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/0d794db8521c4137d71804bd6c91da52/navigator-task-output-failed.png)



1. Optional: type `    :doc` bring up the documentation for the module or plugin used in the task to aid in troubleshooting.


```
ANSIBLE.BUILTIN.PACKAGE_FACTS (MODULE)      0│---      1│doc:      2│  author:      3│  - Matthew Jones (@matburt)      4│  - Brian Coca (@bcoca)      5│  - Adam Miller (@maxamillion)      6│  collection: ansible.builtin      7│  description:      8│  - Return information about installed packages as facts.    &lt;... output omitted ...&gt;     11│  module: package_facts     12│  notes:     13│  - Supports C(check_mode).     14│  options:     15│    manager:     16│      choices:     17│      - auto     18│      - rpm     19│      - apt     20│      - portage     21│      - pkg     22│      - pacman        &lt;... output truncated ...&gt;
```




**Additional resources**

-  [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html)
-  [Ansible playbooks](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html)


