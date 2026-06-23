# Edit the inventory file
## Run the setup script

Run the installation program setup script after updating the inventory file with all the required parameters to begin the installation and configuration of the platform.

### About this task

**RPM installer**

### Procedure

Run the `setup.sh` script

```
$ sudo ./setup.sh
```


Note:

If you are running the setup as a non-root user with `sudo` privileges, you can use the following command:

```
$ ANSIBLE_BECOME_METHOD='sudo'
ANSIBLE_BECOME=True ./setup.sh
```

### Results

Installation of Red Hat Ansible Automation Platform will begin.

### What to do next

If you want to add additional nodes to your automation mesh after the initial setup, edit the inventory file to add the new node, then rerun the `setup.sh` script.

**Containerized installer**

For information on installing containerized Ansible Automation Platform, see [Installing containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_installing_containerized_aap "Run the install playbook to install containerized Ansible Automation Platform after preparing the Red Hat Enterprise Linux host, downloading the installation program, and configuring the inventory file.")

