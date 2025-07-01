# 2. Ansible Automation Platform containerized installation
## 2.12. Uninstalling containerized Ansible Automation Platform




Uninstall your container-based installation of Ansible Automation Platform.

**Prerequisites**

You have done the following:


- Logged in to the Red Hat Enterprise Linux host as your dedicated non-root user.


**Procedure**

- If you intend to reinstall Ansible Automation Platform and want to use the preserved databases, you must collect the existing secret keys by running the following command:


```
$ podman secret inspect --showsecret &lt;secret_key_variable&gt; | jq -r .[].SecretData
```

For example:


```
$ podman secret inspect --showsecret controller_secret_key | jq -r .[].SecretData
```


- For more information about the `    *_secret_key` variables, see [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars) .
- Run the `    uninstall` playbook:


```
$ ansible-playbook -i inventory ansible.containerized_installer.uninstall
```

This stops all systemd units and containers and then deletes all resources used by the containerized installer such as:

- configuration and data directories and files
- systemd unit files
- Podman containers and images
- RPM packages


To keep container images, set the `container_keep_images` parameter to `true` .

```
$ ansible-playbook -i inventory ansible.containerized_installer.uninstall -e container_keep_images=true
```

To keep PostgreSQL databases, set the `postgresql_keep_databases` parameter to `true` .

```
$ ansible-playbook -i inventory ansible.containerized_installer.uninstall -e postgresql_keep_databases=true
```

