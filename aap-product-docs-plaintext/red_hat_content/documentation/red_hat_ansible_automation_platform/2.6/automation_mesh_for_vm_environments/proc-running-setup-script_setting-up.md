# 2. Setting up automation mesh
## 2.3. Running the Red Hat Ansible Automation Platform installer setup script




After you update the inventory file with required parameters, run the installer setup script.

**Procedure**

- Run the `    setup.sh` script


```
$ sudo ./setup.sh
```




Note
If you are running the setup as a non-root user with `sudo` privileges, you can use the following command:

```
$ ANSIBLE_BECOME_METHOD='sudo'
ANSIBLE_BECOME=True ./setup.sh
```



Installation of Red Hat Ansible Automation Platform will begin.

**Additional resources**

See [Understanding privilege escalation](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_privilege_escalation.html) for additional `setup.sh` script examples.


If you want to add additional nodes to your automation mesh after the initial setup, edit the inventory file to add the new node, then rerun the `setup.sh` script.

