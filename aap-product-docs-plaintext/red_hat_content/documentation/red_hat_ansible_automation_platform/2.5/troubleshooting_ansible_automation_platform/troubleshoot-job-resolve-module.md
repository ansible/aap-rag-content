# 6. Jobs
## 6.1. Issue - Jobs are failing with “ERROR! couldn’t resolve module/action” error message




Jobs are failing with the error message “ERROR! couldn’t resolve module/action 'module name'. This often indicates a misspelling, missing collection, or incorrect module path”.

This error can happen when the collection associated with the module is missing from the execution environment.

The recommended resolution is to create a custom execution environment and add the required collections inside of that execution environment. For more information about creating an execution environment, see [Using Ansible Builder](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/creating_and_using_execution_environments/assembly-using-builder) in _Creating and using execution environments_ .

Alternatively, you can complete the following steps:

**Procedure**

1. Create a `    collections` folder inside of the project repository.
1. Add a `    requirements.yml` file inside of the `    collections` folder and add the collection:


```
collections:    -<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;collection_name&gt;</span></em></span>
```


<span id="troubleshoot-job-timeout"></span>
= Issue - Jobs are failing with “Timeout (12s) waiting for privilege escalation prompt” error message





This error can happen when the timeout value is too small, causing the job to stop before completion. The default timeout value for connection plugins is `10` .

To resolve the issue, increase the timeout value by completing one of the following methods.

Note
The following changes will affect all of the jobs in automation controller. To use a timeout value for a specific project, add an `ansible.cfg` file in the root of the project directory and add the `timeout` parameter value to that `ansible.cfg` file.



**Add ANSIBLE_TIMEOUT as an environment variable in the automation controller UI**

1. Go to automation controller.
1. From the navigation panel, selectSettings→Jobs settings.
1. Under **Extra Environment Variables** add the following:


```
{    "ANSIBLE_TIMEOUT": 60    }
```




**Add a timeout value in the [defaults] section of the ansible.cfg file by using the CLI**

- Edit the `    /etc/ansible/ansible.cfg` file and add the following:


```
[defaults]    timeout = 60
```




**Running ad hoc commands with a timeout**

- To run an ad hoc playbook in the command line, add the `    --timeout` flag to the `    ansible-playbook` command, for example:


```
# ansible-playbook --timeout=60<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;your_playbook.yml&gt;</span></em></span>
```




**Additional resources**

-  [DEFAULT_TIMEOUT](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#default-timeout)


