# 6. Jobs
## 6.2. Issue - Jobs failing with timeout waiting for privilege escalation prompt




This error can happen when the timeout value is too small, causing the job to stop before completion. The default timeout value for connection plugins is `10` .

To resolve the issue, increase the timeout value by completing one of the following methods.

Note
The following changes will affect all of the jobs in automation controller. To use a timeout value for a specific project, add an `ansible.cfg` file in the root of the project directory and add the `timeout` parameter value to that `ansible.cfg` file.



**Procedure**

- Increase the timeout value by using one of the following methods:


-  **Add ANSIBLE_TIMEOUT as an environment variable in the automation controller UI:**


1. Go to automation controller.
1. From the navigation panel, selectSettings→Jobs settings.
1. Under **Extra Environment Variables** add the following:


```
{            "ANSIBLE_TIMEOUT": 60            }
```



-  **Add a timeout value in the [defaults] section of the ansible.cfg file:**


1. Edit the `            /etc/ansible/ansible.cfg` file and add the following:


```
[defaults]            timeout = 60
```



-  **Run ad hoc commands with a timeout:**


1. To run an ad hoc playbook in the command line, add the `            --timeout` flag to the `            ansible-playbook` command, for example:


```
# ansible-playbook --timeout=60 &lt;your_playbook.yml&gt;
```






