# 1. View key usage metrics with Automation Dashboard
## 1.4. Uninstalling Automation Dashboard




Uninstall Automation Dashboard and its dependencies by using a single command, ensuring a clean removal from your host.

**Procedure**

- Run the following command to uninstall Automation Dashboard and its dependencies, including the PostgreSQL database container:


```
ansible-playbook -i inventory    ansible.containerized_installer.dashboard_uninstall
```




