# 3. Example: Automate Red Hat Enterprise Linux firewall configuration
## 3.4. Creating a new playbook to automate the firewall configuration




Create a new playbook and use the RHEL System Role collection to automate your Red Hat Enterprise Linux firewall configuration.

1. In your Dev Spaces instance, clickFile→New File.
1. Enter `    firewall.yml` for the filename and click **OK** to save it in the root directory.
1. Add the following lines to your `    firewall.yml` file:


```
---    - name: Open HTTPS and SSH on firewall      hosts: rhel      become: true      tasks:        - name: Use rhel system roles to allow https and ssh traffic          vars:            firewall:              - service: https                state: enabled                permanent: true                immediate: true                zone: public              - service: ssh                state: enabled                permanent: true                immediate: true                zone: public          ansible.builtin.include_role:            name: redhat.rhel_system_roles.firewall
```




Note
You can use Ansible Lightspeed with IBM watsonx Code Assistant from the Ansible VS Code extension to help you generate playbooks. For more information, refer to the [Ansible Lightspeed with IBM watsonx Code Assistant User Guide](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index) .



