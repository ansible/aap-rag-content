# 7. Maintaining containerized Ansible Automation Platform
## 7.5. Reinstalling containerized Ansible Automation Platform




To reinstall a containerized deployment after uninstalling and preserving the database, follow the steps in [Installing containerized Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/installing-containerized-aap) and include the existing secret key value in the playbook command:

```
$ ansible-playbook -i inventory ansible.containerized_installer.install -e controller_secret_key=&lt;secret_key_value&gt;
```

**Additional resources**

-  [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars)


