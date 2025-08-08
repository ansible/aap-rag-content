# 1. Introduction to automation content navigator
## 1.4. Relationship between Ansible and automation content navigator commands




The automation content navigator commands run familiar Ansible CLI commands in `-m stdout` mode. You can use all the subcommands and options available in the related Ansible CLI command. Use `ansible-navigator --help` for details.


<span id="idm140640039866976"></span>
**Table 1.2. Comparison of automation content navigator and Ansible CLI commands**

| automation content navigator command | Ansible CLI command |
| --- | --- |
|  `ansible-navigator collections` |  `ansible-galaxy collection` |
|  `ansible-navigator config` |  `ansible-config` |
|  `ansible-navigator doc` |  `ansible-doc` |
|  `ansible-navigator inventory` |  `ansible-inventory` |
|  `ansible-navigator run` |  `ansible-playbook` |




