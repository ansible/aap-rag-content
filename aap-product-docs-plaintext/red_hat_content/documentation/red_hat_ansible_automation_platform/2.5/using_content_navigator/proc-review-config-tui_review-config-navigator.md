# 7. Reviewing your Ansible configuration with automation content navigator
## 7.1. Reviewing your Ansible configuration from automation content navigator




You can review your Ansible configuration with the automation content navigator text-based user interface in interactive mode and delve into the settings. Automation content navigator pulls in the results from an accessible Ansible configuration file, or returns the defaults if no configuration file is present.

**Prerequisites**

- You have authenticated to the Red Hat registry if you need to access additional automation execution environments. See [Red Hat Container Registry Authentication](https://access.redhat.com/RegistryAuthentication) for details.


**Procedure**

1. Start automation content navigator


```
$ ansible-navigator
```

Optional: type `    ansible-navigator config` from the command line to access the Ansible configuration settings.


1. Review the Ansible configuration.


```
:config
```

![Ansible configuration](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/060e3e3a6b8d3acd2dbfa26e0a789d44/navigator-ansible-config.png)


Some values reflect settings from within the automation execution environments needed for the automation execution environments to function. These display as non-default settings you cannot set in your Ansible configuration file.


1. Type the number corresponding to the setting you want to delve into, or type `    :&lt;number&gt;` for numbers greater than 9.


```
ANSIBLE COW ACCEPTLIST (current: ['bud-frogs', 'bunny', 'cheese']) (default:     0│---     1│current:     2│- bud-frogs     3│- bunny     4│- cheese     5│default:     6│- bud-frogs     7│- bunny     8│- cheese     9│- daemon
```




The output shows the current `setting` as well as the `default` . Note the `source` in this example is `env` since the setting comes from the automation execution environments.

**Verification**

- Review the configuration output.

![Configuration output](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/060e3e3a6b8d3acd2dbfa26e0a789d44/navigator-ansible-config.png)





**Additional resources**

-  [ansible-config](https://docs.ansible.com/ansible/latest/cli/ansible-config.html) .
-  [Introduction to Ansible configuration](https://docs.ansible.com/ansible/latest/installation_guide/intro_configuration.html) .


