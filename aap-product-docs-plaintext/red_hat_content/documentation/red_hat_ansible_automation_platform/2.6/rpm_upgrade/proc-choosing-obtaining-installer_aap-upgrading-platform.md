# 2. Upgrading to Red Hat Ansible Automation Platform 2.6
## 2.2. Choosing and obtaining a Red Hat Ansible Automation Platform installer
### 2.2.1. Installing with internet access




Choose the Red Hat Ansible Automation Platform installation program if your Red Hat Enterprise Linux environment is connected to the internet. Installing with internet access retrieves the latest required repositories, packages, and dependencies.

Choose one of the following ways to set up your Ansible Automation Platform installation program.

**Procedure**

-  **Tarball install**


1. Navigate to the [Red Hat Ansible Automation Platform download](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software) page.
1. In the **Product software** tab, clickDownload Nowfor the **Ansible Automation Platform <latest-version> Setup** .
1. Extract the files:


```
$ tar xvzf ansible-automation-platform-setup-&lt;latest-version&gt;.tar.gz
```



-  **RPM install**


1. Install the Ansible Automation Platform Installer Package.

v.2.6 for RHEL 9 for x86-64:


```
$ sudo dnf install --enablerepo=ansible-automation-platform-2.6-for-rhel-9-x86_64-rpms ansible-automation-platform-installer
```

Note
`        dnf install` enables the repo as the repo is disabled by default.



When you use the RPM installer, the files are placed under the `        /opt/ansible-automation-platform/installer` directory.





