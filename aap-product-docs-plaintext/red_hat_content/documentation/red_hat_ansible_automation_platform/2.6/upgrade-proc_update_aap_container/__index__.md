# Upgrade your containerized deployment of Ansible Automation Platform

Perform an upgrade of containerized Ansible Automation Platform.

## Before you begin

- You have reviewed the release notes for the associated release. For more information, see [Release notes](/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-platform_intro "Ansible Automation Platform unifies comprehensive automation capabilities, a robust ecosystem, and flexible deployment options into one strategic solution. It enables customers to automate and orchestrate workflows across domains for efficient, resilient, and consistent IT operations at scale.").
- You have a backup of your Ansible Automation Platform deployment. For more information, see [Back up containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.6/administer-back_up_and_restore_your_containerized_deployment#backing-up-containerized-ansible-automation-platform "Perform a backup of your container-based installation of Ansible Automation Platform.").

## Procedure

1.  Log in to the Red Hat Enterprise Linux host as your dedicated non-root user.
2.  Follow the steps in [Download Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-proc_downloading_containerized_aap "Choose the installation program you need based on your Red Hat Enterprise Linux environment internet connectivity and download the installation program to your Red Hat Enterprise Linux host.") to download the latest version of containerized Ansible Automation Platform.
3.  Copy the downloaded installation program to your Red Hat Enterprise Linux Host.
4.  Edit the `inventory` file to match your required configuration. You can keep the same parameters from your existing Ansible Automation Platform deployment or you can change the parameters to match any modifications to your environment.
5.  Run the `install` playbook:


```
$ ansible-playbook -i inventory ansible.containerized_installer.install
```
- If your privilege escalation requires a password to be entered, append `-K` to the command. You will then be prompted for the `BECOME` password.
- You can use increasing verbosity, up to 4 v’s (`-vvvv`) to see the details of the installation process. However it is important to note that this can significantly increase installation time, so it is recommended that you use it only as needed or requested by Red Hat support.
