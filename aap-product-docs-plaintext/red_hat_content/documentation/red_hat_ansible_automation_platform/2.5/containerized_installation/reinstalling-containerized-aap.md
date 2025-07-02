# 2. Ansible Automation Platform containerized installation
## 2.13. Reinstalling containerized Ansible Automation Platform




To reinstall a containerized deployment after uninstalling and preserving the database, run the `install` playbook and include the existing secret key value:

```
$ ansible-playbook -i inventory ansible.containerized_installer.install -e controller_secret_key=&lt;secret_key_value&gt;
```

For more information about the `*_secret_key` variables, see [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars) .

