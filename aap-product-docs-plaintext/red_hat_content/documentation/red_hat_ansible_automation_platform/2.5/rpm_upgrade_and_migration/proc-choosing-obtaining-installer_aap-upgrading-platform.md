# 2. Upgrading to Red Hat Ansible Automation Platform 2.5
## 2.3. Choosing and obtaining a Red Hat Ansible Automation Platform installer




Choose the Red Hat Ansible Automation Platform installer you need based on your Red Hat Enterprise Linux environment internet connectivity. Review the following scenarios and decide on which Red Hat Ansible Automation Platform installer meets your needs.

Note
A valid Red Hat customer account is required to access Red Hat Ansible Automation Platform installer downloads on the Red Hat Customer Portal.



Choose the Red Hat Ansible Automation Platform installer if your Red Hat Enterprise Linux environment is connected to the internet. Installing with internet access retrieves the latest required repositories, packages, and dependencies. Choose one of the following ways to set up your Ansible Automation Platform installer.

**Procedure**

-  **Tarball install**


1. Navigate to the [Red Hat Ansible Automation Platform download](https://access.redhat.com/downloads/content/480/ver=2.5/rhel---9/2.5/x86_64/product-software) page.
1. In the **Product software** tab, clickDownload Nowfor the **Ansible Automation Platform <latest-version> Setup** .
1. Extract the files:


```
$ tar xvzf ansible-automation-platform-setup-&lt;latest-version&gt;.tar.gz
```



-  **RPM install**


1. Install the Ansible Automation Platform Installer Package.

v.2.5 for RHEL 8 for x86_64:


```
$ sudo dnf install --enablerepo=ansible-automation-platform-2.5-for-rhel-8-x86_64-rpms ansible-automation-platform-installer
```

v.2.5 for RHEL 9 for x86-64:


```
$ sudo dnf install --enablerepo=ansible-automation-platform-2.5-for-rhel-9-x86_64-rpms ansible-automation-platform-installer
```

Note
`        dnf install` enables the repo as the repo is disabled by default.



When you use the RPM installer, the files are placed under the `        /opt/ansible-automation-platform/installer` directory.





