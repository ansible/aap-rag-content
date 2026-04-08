# 4. Installing Red Hat Ansible Automation Platform
## 4.4. Running the Red Hat Ansible Automation Platform installer setup script




Run the installation program setup script after updating the inventory file with all the required parameters to begin the installation and configuration of the platform.

**RPM installer**

**Procedure**

- Run the `    setup.sh` script


```
$ sudo ./setup.sh
```

Note
If you are running the setup as a non-root user with `    sudo` privileges, you can use the following command:


```
$ ANSIBLE_BECOME_METHOD='sudo'    ANSIBLE_BECOME=True ./setup.sh
```



Installation of Red Hat Ansible Automation Platform will begin.




