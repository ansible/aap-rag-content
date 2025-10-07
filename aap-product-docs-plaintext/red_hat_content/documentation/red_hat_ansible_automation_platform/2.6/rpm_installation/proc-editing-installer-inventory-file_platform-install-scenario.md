# 3. Installing Red Hat Ansible Automation Platform
## 3.1. Editing the Red Hat Ansible Automation Platform installer inventory file




You can use the Red Hat Ansible Automation Platform installer inventory file to specify your installation scenario.

**Procedure**

1. Navigate to the installer:


1. [RPM installed package]


```
$ cd /opt/ansible-automation-platform/installer/
```


1. [bundled installer]


```
$ cd ansible-automation-platform-setup-bundle-&lt;latest-version&gt;
```


1. [online installer]


```
$ cd ansible-automation-platform-setup-&lt;latest-version&gt;
```



1. Open the `    inventory` file with a text editor.
1. Edit `    inventory` file parameters to specify your installation scenario. You can use one of the supported [Installation scenario examples](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/rpm_installation/index#con-install-scenario-examples) as the basis for your `    inventory` file.


**Additional resources**

- For a comprehensive list of pre-defined variables used in Ansible installation inventory files, see [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/rpm_installation/index#appendix-inventory-files-vars) .


