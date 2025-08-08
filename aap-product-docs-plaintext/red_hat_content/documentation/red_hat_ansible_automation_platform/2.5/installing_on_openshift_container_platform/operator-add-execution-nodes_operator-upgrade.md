# Chapter 9. Adding execution nodes to Red Hat Ansible Automation Platform Operator




You can enable the Ansible Automation Platform Operator with execution nodes by downloading and installing the install bundle.


<span id="add-operator-execution-nodes_operator-upgrade"></span>
**Prerequisites**

- An automation controller instance.
- The receptor collection package is installed.
- The Ansible Automation Platform repository `    ansible-automation-platform-2.5-for-rhel-{RHEL-RELEASE-NUMBER}-x86_64-rpms` is enabled.



**Procedure**

1. Log in to Red Hat Ansible Automation Platform.
1. In the navigation panel, selectAutomation Execution→Infrastructure→Instances.
1. ClickAdd.
1. Input the Execution Node domain name or IP in the **Host Name** field.
1. Optional: Input the port number in the **Listener Port** field.
1. ClickSave.
1. Click the download icon![download](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Installing_on_OpenShift_Container_Platform-en-US/images/8a61e20c21c53f44e207c84d454159ec/download.png)
next to **Install Bundle** . This starts a download, take note of where you save the file
1. Untar the gz file.

Note
To run the `    install_receptor.yml` playbook you must install the receptor collection from Ansible Galaxy: `    Ansible-galaxy collection install -r requirements.yml`




1. Update the playbook with your user name and SSH private key file. Note that `    ansible_host` pre-populates with the hostname you input earlier.


```
all:       hosts:          remote-execution:    	        ansible_host: example_host_name # Same with configured in AAP WebUI    	        ansible_user: &lt;username&gt; #user provided    	        Ansible_ssh_private_key_file: ~/.ssh/id_example
```


1. Open your terminal, and navigate to the directory where you saved the playbook.
1. To install the bundle run:


```
ansible-playbook install_receptor.yml -i inventory.yml
```


1. When installed you can now upgrade your execution node by downloading and re-running the playbook for the instance you created.


**Verification**

To verify receptor service status run the following command:


```
sudo systemctl status receptor.service
```

Make sure the service is in `active (running)` state

To verify if your playbook runs correctly on your new node run the following command:

```
watch podman ps
```

**Additional resources**

-  [Managing Instance Groups](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-instance-groups)


