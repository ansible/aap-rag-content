# 7. Choosing and obtaining a Red Hat Ansible Automation Platform installer
## 7.1. Installing with internet access




Choose the Red Hat Ansible Automation Platform installer if your Red Hat Enterprise Linux environment is connected to the internet. Installing with internet access retrieves the latest required repositories, packages, and dependencies. Choose one of the following ways to set up your Ansible Automation Platform installer.

**Tarball install**

1. Navigate to the [Red Hat Ansible Automation Platform download](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software) page.
1. ClickDownload Nowfor the **Ansible Automation Platform <latest-version> Setup** .
1. Transfer the file to the target server using `    scp` or `    curl` :


1. Using `        scp` :


1. Run the following command, replacing `            private_key.pem` , `            user` , and `            server_ip` with your appropriate values:




```
$ scp -i private_key.pem aap-bundled-installer.tar.gz user@server_ip:
```

1. Using `    curl` :


1. If the setup file URL is available, you can download it directly to the target server using `        curl` . Replace `        &lt;download_url&gt;` with the file URL:



```
$ curl -0 &lt;download_url&gt;
```

Note
If the file needs to be extracted after downloading, run the following command:

```
$ tar xvzf aap-bundled-installer.tar.gz
```



**RPM install**

1. Install Ansible Automation Platform Installer Package

v.2.6 for RHEL 8 for x86_64


```
$ sudo dnf install --enablerepo=ansible-automation-platform-2.5-for-rhel-8-x86_64-rpms ansible-automation-platform-installer
```

v.2.6 for RHEL 9 for x86_64


```
$ sudo dnf install --enablerepo=ansible-automation-platform-2.5-for-rhel-9-x86_64-rpms ansible-automation-platform-installer
```




Note
`dnf install` enables the repo as the repo is disabled by default.



When you use the RPM installer, the files are placed under the `/opt/ansible-automation-platform/installer` directory.

