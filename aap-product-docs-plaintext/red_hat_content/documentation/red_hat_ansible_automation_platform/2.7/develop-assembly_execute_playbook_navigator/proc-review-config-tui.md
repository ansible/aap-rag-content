# Run playbooks locally with automation content navigator
## View Ansible configuration file contents in text-based format
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
