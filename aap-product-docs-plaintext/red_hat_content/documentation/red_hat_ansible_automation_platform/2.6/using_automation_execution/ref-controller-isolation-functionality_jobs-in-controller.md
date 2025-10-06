# 5. Jobs in automation controller
## 5.3. Playbook run jobs
### 5.3.4. Isolation functionality and variables




Automation controller uses container technology to isolate jobs from each other. By default, only the current project is exposed to the container running a job template.

If you need to expose additional directories, you must customize your playbook runs. To configure job isolation, you can set variables.

By default, automation controller uses the system’s `tmp` directory ( `/tmp` by default) as its staging area. You can change this in the **Job Execution Path** field of the **Jobs settings** page, or in the REST API at `/api/v2/settings/jobs` :

```
AWX_ISOLATION_BASE_PATH = "/opt/tmp"
```

If there are any additional directories that should specifically be exposed from the host to the container that playbooks run in, you can specify those in the **Paths to expose to isolated jobs** field of the **Jobs Settings** page, or in the REST API at `/api/v2/settings/jobs` :

```
AWX_ISOLATION_SHOW_PATHS = ['/list/of/', '/paths']
```

Note
- If a path to a specific file is entered, then the entire directory containing that file will be mounted inside the execution environment.
- If your playbooks need to use keys or settings defined in `    AWX_ISOLATION_SHOW_PATHS` , then add this file to `    /var/lib/awx/.ssh` .




The fields described here can be found on the **Jobs settings** page:

![Jobs settings options](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/58190ad7732bec65d93b6d8c5c26c585/job-settings-full.png)


