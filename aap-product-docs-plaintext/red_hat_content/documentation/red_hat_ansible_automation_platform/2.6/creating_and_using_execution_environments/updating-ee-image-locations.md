# 3. Using Ansible Builder
## 3.10. Updating execution environment image locations




If you installed private automation hub separately from Ansible Automation Platform, you can update your execution environment image locations to point to your private automation hub.

**Procedure**

1. Go to the directory that contains `    setup.sh`
1. Create `    ./group_vars/automationcontroller` by running the following command:


```
touch ./group_vars/automationcontroller
```


1. Paste the following content into `    ./group_vars/automationcontroller` . Adjust the settings to fit your environment:


```
# Automation Hub Registry    registry_username: 'your-automation-hub-user'    registry_password: 'your-automation-hub-password'    registry_url: 'automationhub.example.org'    registry_verify_ssl: False        ## Execution Environments    control_plane_execution_environment: 'automationhub.example.org/ee-supported-rhel8:latest'        global_job_execution_environments:      - name: "Default execution environment"        image: "automationhub.example.org/ee-supported-rhel8:latest"      - name: "Minimal execution environment"        image: "automationhub.example.org/ee-minimal-rhel8:latest"
```

Note
For information on obtaining `    registry_username` and `    registry_password` , see [Setting registry_username and registry_password](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/index#proc-set-registry-username-password)




1. Run the `    ./setup.sh` script


```
$ ./setup.sh
```




**Verification**

1. Log in to Ansible Automation Platform as a user with system administrator access.
1. Go toAutomation Execution→Infrastructure→Execution Environments.
1. In the **Image** column, confirm that the execution environment image location has changed from the default value of `    &lt;registry url&gt;/ansible-automation-platform-&lt;version&gt;/&lt;image name&gt;:&lt;tag&gt;` to `    &lt;automation hub url&gt;/&lt;image name&gt;:&lt;tag&gt;` .


