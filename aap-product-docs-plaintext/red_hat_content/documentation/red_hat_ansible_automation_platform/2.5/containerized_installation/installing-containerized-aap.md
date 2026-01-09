# Chapter 6. Installing containerized Ansible Automation Platform




Run the `install` playbook to install containerized Ansible Automation Platform after preparing the Red Hat Enterprise Linux host, downloading the installation program, and configuring the inventory file.

**Prerequisites**

- You have [prepared the Red Hat Enterprise Linux host](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/preparing-containerized-installation#preparing-the-rhel-host-for-containerized-installation)
- You have [prepared the managed nodes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/preparing-containerized-installation#preparing-the-managed-nodes-for-containerized-installation)
- You have [downloaded Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/preparing-containerized-installation#downloading-ansible-automation-platform)
- You have [configured the inventory file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/preparing-containerized-installation#configuring-inventory-file)
- You are logged in to the Red Hat Enterprise Linux host as your non-root user


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
-  `        -K` - (Optional) If your privilege escalation (becoming root) requires you to enter a password, add this to the installation command. You are then prompted for the BECOME password.
-  `        -v` - (Optional) You can use increasing verbosity, up to 4 ( `        -vvvv` ) to see installation process details. This can significantly increase installation time. Use it only as needed or when requested by Red Hat support.



**Verification**

- After the installation completes, verify that you can access Ansible Automation Platform which is available by default at the following URL:


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
-  [Sensitive variables in the installation inventory](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/hardening_and_compliance/hardening-aap#ref-sensitive-variables-install-inventory_hardening-aap)
-  [Getting started with Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_ansible_automation_platform)
-  [Troubleshooting containerized Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/troubleshooting-containerized-ansible-automation-platform)


