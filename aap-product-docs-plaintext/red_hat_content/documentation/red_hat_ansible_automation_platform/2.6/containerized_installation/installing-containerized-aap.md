# 2. Ansible Automation Platform containerized installation
## 2.8. Installing containerized Ansible Automation Platform




After you prepare the Red Hat Enterprise Linux host, download Ansible Automation Platform, and configure the inventory file, run the `install` playbook to install containerized Ansible Automation Platform.

**Prerequisites**

You have done the following:


-  [Prepared the Red Hat Enterprise Linux host](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/aap-containerized-installation#preparing-the-rhel-host-for-containerized-installation)
-  [Prepared the managed nodes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/aap-containerized-installation#preparing-the-managed-nodes-for-containerized-installation)
-  [Downloaded Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/aap-containerized-installation#downloading-ansible-automation-platform)
-  [Configured the inventory file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/aap-containerized-installation#configuring-inventory-file)
- Logged in to the Red Hat Enterprise Linux host as your non-root user


**Procedure**

1. Go to the installation directory on your Red Hat Enterprise Linux host.
1. Run the `    install` playbook:


```
ansible-playbook -i &lt;inventory_file_name&gt; ansible.containerized_installer.install
```

For example:


```
ansible-playbook -i inventory ansible.containerized_installer.install
```

You can add additional parameters to the installation command as needed:


```
ansible-playbook -i &lt;inventory_file_name&gt; -e @&lt;vault_file_name&gt; --ask-vault-pass -K -v ansible.containerized_installer.install
```

For example:


```
ansible-playbook -i inventory -e @vault.yml --ask-vault-pass -K -v  ansible.containerized_installer.install
```


-  `        -i &lt;inventory_file_name&gt;` - The inventory file to use for the installation.
-  `        -e @&lt;vault_file_name&gt; --ask-vault-pass` - (Optional) If you are using a vault to store sensitive variables, add this to the installation command.
-  `        -K` - (Optional) If your privilege escalation requires you to enter a password, add this to the installation command. You are then prompted for the BECOME password.
-  `        -v` - (Optional) You can use increasing verbosity, up to 4 v’s ( `        -vvvv` ) to see the details of the installation process. However, it is important to note that this can significantly increase installation time, so use it only as needed or requested by Red Hat support.

1. The installation of containerized Ansible Automation Platform begins.


**Verification**

- After the installation completes, verify that you can access the platform UI which is available by default at the following URL:


```
https://&lt;gateway_node&gt;:443
```


- Log in as the admin user with the credentials you created for `    gateway_admin_username` and `    gateway_admin_password` .
- The default ports and protocols used for Ansible Automation Platform are 80 (HTTP) and 443 (HTTPS). You can customize the ports with the following variables:


```
envoy_http_port=80    envoy_https_port=443
```


- If you want to disable HTTPS, set `    envoy_disable_https` to `    true` :


```
envoy_disable_https: true
```




**Additional resources**

-  [Understanding privilege escalation: become](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_privilege_escalation.html)
-  [Sensitive variables in the installation inventory](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/hardening_and_compliance/hardening-aap#ref-sensitive-variables-install-inventory_hardening-aap)
-  [Getting started with Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/getting_started_with_ansible_automation_platform)
-  [Troubleshooting containerized Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/troubleshooting-containerized-ansible-automation-platform)


