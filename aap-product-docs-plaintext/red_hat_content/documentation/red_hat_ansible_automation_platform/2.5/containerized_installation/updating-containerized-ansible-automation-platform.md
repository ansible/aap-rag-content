# 7. Maintaining containerized Ansible Automation Platform
## 7.1. Updating containerized Ansible Automation Platform




Perform a patch update for a container-based installation of Ansible Automation Platform from 2.5 to 2.5.x.

Upgrades from 2.4 Containerized Ansible Automation Platform Tech Preview to 2.5 Containerized Ansible Automation Platform are not supported.

**Prerequisites**

- You have reviewed the release notes for the associated patch release. For more information, see [Ansible Automation Platform Release notes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/release_notes) .
- You have a backup of your Ansible Automation Platform deployment. For more information, see [Backing up container-based Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/maintaining-containerized-aap#backing-up-containerized-ansible-automation-platform) .


**Procedure**

1. Log in to the Red Hat Enterprise Linux host as your dedicated non-root user.
1. Follow the steps in [Downloading Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/preparing-containerized-installation#downloading-ansible-automation-platform) to download the latest version of containerized Ansible Automation Platform.
1. Copy the downloaded installation program to your Red Hat Enterprise Linux Host.
1. Edit the `    inventory` file to match your required configuration. You can keep the same parameters from your existing Ansible Automation Platform deployment or you can change the parameters to match any modifications to your environment.
1. Run the `    install` playbook:


```
$ ansible-playbook -i inventory ansible.containerized_installer.install
```


- If your privilege escalation requires a password to be entered, append `        -K` to the command. You will then be prompted for the `        BECOME` password.
- You can use increasing verbosity, up to 4 v’s ( `        -vvvv` ) to see the details of the installation process. However it is important to note that this can significantly increase installation time, so it is recommended that you use it only as needed or requested by Red Hat support.

1. The update begins.


**Additional resources**

-  [Ansible Automation Platform Release notes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/release_notes)
-  [Backing up container-based Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/aap-containerized-installation#backing-up-containerized-ansible-automation-platform)


