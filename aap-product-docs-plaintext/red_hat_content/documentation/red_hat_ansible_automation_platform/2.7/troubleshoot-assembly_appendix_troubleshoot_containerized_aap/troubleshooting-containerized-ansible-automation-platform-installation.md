# Troubleshoot your containerized deployment
## Troubleshoot your containerized installation

Use this information to troubleshoot your containerized installation of Ansible Automation Platform.

**The installation takes a long time, or has errors, what should I check?**

1. Ensure your system meets the minimum requirements as outlined in [System requirements](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_cont_aap_system_requirements "Use this information when planning your installation of containerized Ansible Automation Platform."). Factors such as improper storage choices and high latency when distributing across many hosts will all have an impact on installation time.
2. Review the installation log file which is located by default at `./aap_install.log`. You can change the log file location within the `ansible.cfg` file in the installation directory.
3. Enable task profiling callbacks on an ad hoc basis to give an overview of where the installation program spends the most time. To do this, use the local `ansible.cfg` file. Add a callback line under the `[defaults]` section, for example:

```
$ cat ansible.cfg
[defaults]
callbacks_enabled = ansible.posix.profile_tasks
```

**Automation controller returns an error of 413**

This error occurs when `manifest.zip` license files that are larger than the `controller_nginx_client_max_body_size` setting. If this error occurs, update the inventory file to include the following variable:

```
controller_nginx_client_max_body_size=5m
```
The default setting of `5m` should prevent this issue, but you can increase the value as needed.

**When attempting to install containerized Ansible Automation Platform in Amazon Web Services you receive output that there is no space left on device**

```
TASK [ansible.containerized_installer.automationcontroller : Create the receptor container] ***************************************************
fatal: [ec2-13-48-25-168.eu-north-1.compute.amazonaws.com]: FAILED! => {"changed": false, "msg": "Can't create container receptor", "stderr": "Error: creating container storage: creating an ID-mapped copy of layer \"98955f43cc908bd50ff43585fec2c7dd9445eaf05eecd1e3144f93ffc00ed4ba\": error during chown: storage-chown-by-maps: lchown usr/local/lib/python3.9/site-packages/azure/mgmt/network/v2019_11_01/operations/__pycache__/_available_service_aliases_operations.cpython-39.pyc: no space left on device: exit status 1\n", "stderr_lines": ["Error: creating container storage: creating an ID-mapped copy of layer \"98955f43cc908bd50ff43585fec2c7dd9445eaf05eecd1e3144f93ffc00ed4ba\": error during chown: storage-chown-by-maps: lchown usr/local/lib/python3.9/site-packages/azure/mgmt/network/v2019_11_01/operations/__pycache__/_available_service_aliases_operations.cpython-39.pyc: no space left on device: exit status 1"], "stdout": "", "stdout_lines": []}
```
If you are installing a `/home` filesystem into a default Amazon Web Services marketplace RHEL instance, it might be too small since `/home` is part of the root `/` filesystem. To resolve this issue you must make more space available. For more information about the system requirements, see [System requirements](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-ref_cont_aap_system_requirements "Use this information when planning your installation of containerized Ansible Automation Platform.").

**"Install container tools" task fails due to unavailable packages**

This error can be seen in the installation process output as the following:

```
TASK [ansible.containerized_installer.common : Install container tools] **********************************************************************************************************
fatal: [192.0.2.1]: FAILED! => {"changed": false, "failures": ["No package crun available.", "No package podman available.", "No package slirp4netns available.", "No package fuse-overlayfs available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
fatal: [192.0.2.2]: FAILED! => {"changed": false, "failures": ["No package crun available.", "No package podman available.", "No package slirp4netns available.", "No package fuse-overlayfs available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
fatal: [192.0.2.3]: FAILED! => {"changed": false, "failures": ["No package crun available.", "No package podman available.", "No package slirp4netns available.", "No package fuse-overlayfs available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
fatal: [192.0.2.4]: FAILED! => {"changed": false, "failures": ["No package crun available.", "No package podman available.", "No package slirp4netns available.", "No package fuse-overlayfs available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
fatal: [192.0.2.5]: FAILED! => {"changed": false, "failures": ["No package crun available.", "No package podman available.", "No package slirp4netns available.", "No package fuse-overlayfs available."], "msg": "Failed to install some of the specified packages", "rc": 1, "results": []}
```
To fix this error, run the following command on the target hosts:

```
sudo subscription-manager register
```

