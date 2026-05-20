# 1. Introduction to automation content navigator
## 1.3. Automation content navigator commands

The automation content navigator commands run familiar Ansible CLI commands in `-m stdout` mode. You can use all the subcommands and options from the related Ansible CLI command. Use `ansible-navigator --help` for details.

**Table 1.1. Automation content navigator commands**

| Command | Description | CLI example |
| --- | --- | --- |
| <br>  collections | <br>  Explore available collections | <br> `ansible-navigator collections --help` |
| <br>  config | <br>  Explore the current Ansible configuration | <br> `ansible-navigator config --help` |
| <br>  doc | <br>  Review documentation for a module or plugin | <br> `ansible-navigator doc --help` |
| <br>  images | <br>  Explore execution environment images | <br> `ansible-navigator images --help` |
| <br>  inventory | <br>  Explore an inventory | <br> `ansible-navigator inventory --help` |
| <br>  replay | <br>  Explore a previous run using a playbook artifact | <br> `ansible-navigator replay --help` |
| <br>  run | <br>  Run a playbook | <br> `ansible-navigator run --help` |
| <br>  welcome | <br>  Start at the welcome page | <br> `ansible-navigator welcome --help` |

