# 1. View key usage metrics with automation dashboard
## 1.5. Uninstalling automation dashboard




Uninstall automation dashboard and its dependencies by using a single command, ensuring a clean removal from your host.

**Procedure**

- Run the following command to uninstall automation dashboard and its dependencies, including the PostgreSQL database container:


```
ansible-playbook -i inventory    ansible.containerized_installer.dashboard_uninstall
```




