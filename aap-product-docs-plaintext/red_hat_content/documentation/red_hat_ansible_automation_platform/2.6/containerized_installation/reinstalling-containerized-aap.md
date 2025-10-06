# 2. Ansible Automation Platform containerized installation
## 2.13. Reinstalling containerized Ansible Automation Platform




To reinstall a containerized deployment after uninstalling and preserving the database, follow the steps in [Installing containerized Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/aap-containerized-installation#installing-containerized-aap) and include the existing secret key value in the playbook command:

```
$ ansible-playbook -i inventory ansible.containerized_installer.install -e controller_secret_key=&lt;secret_key_value&gt;
```

**Additional resources**

-  [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/appendix-inventory-files-vars)


