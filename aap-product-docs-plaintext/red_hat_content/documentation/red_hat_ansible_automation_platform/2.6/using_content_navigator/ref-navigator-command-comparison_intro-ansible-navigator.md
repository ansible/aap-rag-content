# 1. Introduction to automation content navigator
## 1.4. Relationship between Ansible and automation content navigator commands

The automation content navigator commands run familiar Ansible CLI commands in `-m stdout` mode. You can use all the subcommands and options available in the related Ansible CLI command. Use `ansible-navigator --help` for details.

**Table 1.2. Comparison of automation content navigator and Ansible CLI commands**

| automation content navigator command | Ansible CLI command |
| --- | --- |
| <br> `ansible-navigator collections` | <br> `ansible-galaxy collection` |
| <br> `ansible-navigator config` | <br> `ansible-config` |
| <br> `ansible-navigator doc` | <br> `ansible-doc` |
| <br> `ansible-navigator inventory` | <br> `ansible-inventory` |
| <br> `ansible-navigator run` | <br> `ansible-playbook` |

