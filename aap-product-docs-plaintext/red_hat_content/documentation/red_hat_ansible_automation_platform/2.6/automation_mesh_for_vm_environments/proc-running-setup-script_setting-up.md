# 2. Setting up automation mesh
## 2.3. Running the Red Hat Ansible Automation Platform installer setup script




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

**Next steps**

If you want to add additional nodes to your automation mesh after the initial setup, edit the inventory file to add the new node, then rerun the `    setup.sh` script.


**Containerized installer**

To install a containerized Ansible Automation Platform using the installation playbook, use the method described in [Install containerized Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/installing-containerized-aap)




