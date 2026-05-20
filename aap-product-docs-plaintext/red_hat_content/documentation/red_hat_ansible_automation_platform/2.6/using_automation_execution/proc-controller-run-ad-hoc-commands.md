# 14. Inventories
## 14.6. Running Ad Hoc commands

Learn how to run ad hoc commands against hosts in an inventory.

*Ad hoc* refers to using Ansible to perform a quick command, using /usr/bin/ansible, rather than the orchestration language, which is /usr/bin/ansible-playbook. An example of an ad hoc command might be rebooting 50 machines in your infrastructure. Anything you can do ad hoc can be accomplished by writing a playbook. Playbooks can also glue many other operations together.

**Procedure**

1. From the navigation panel, select Automation Execution → Infrastructure → Inventories.

2. Select the inventory name you want to run an ad hoc command with.

3. Select an inventory source from the **Hosts** or **Groups** tab. The inventory source can be a single group or host, a selection of many hosts, or a selection of many groups.

4. Click Run Command. The Run command window opens.

5. Enter the following information:


- **Module**: Select one of the modules that the supports running commands against.

| <br>  command | <br>  apt_repository | <br>  mount | <br>  win_service |
| --- | --- | --- | --- |
| <br>  shell | <br>  apt_rpm | <br>  ping | <br>  win_updates |
| <br>  yum | <br>  service | <br>  SELinux | <br>  win_group |
| <br>  apt | <br>  group | <br>  setup | <br>  win_user |
| <br>  apt_key | <br>  user | <br>  win_ping | <br>  win_user |

- **Arguments**: Provide arguments to be used with the module you selected.

- **Limit**: Enter the limit used to target hosts in the inventory. To target all hosts in the inventory enter `all` or `*`, or leave the field blank. This is automatically populated with whatever was selected in the previous view before clicking the launch button.

- **Machine Credential**: Select the credential to use when accessing the remote hosts to run the command. Choose the credential containing the username and SSH key or password that Ansible needs to log in to the remote hosts.

- **Verbosity**: Select a verbosity level for the standard output.

- **Forks**: If needed, select the number of parallel or simultaneous processes to use while executing the command.

- **Show Changes**: Select to enable the display of Ansible changes in the standard output. The default is OFF.

- **Enable Privilege Escalation**: If enabled, the playbook is run with administrator privileges. This is the equivalent of passing the `--become` option to the `ansible` command.

- **Extra Variables**: Provide extra command line variables to be applied when running this inventory. Enter variables using either JSON or YAML syntax. Use the radio button to toggle between the two.

6. Click Next to select the execution environment you want the ad hoc command to be run against.

7. Click Next to select the credential you want to use.

8. Click Launch. The results display in the **Output** tab of the module’s job window.

