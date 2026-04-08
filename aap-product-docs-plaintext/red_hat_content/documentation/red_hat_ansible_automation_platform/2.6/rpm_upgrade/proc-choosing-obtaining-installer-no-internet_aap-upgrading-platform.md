# 2. Upgrading to Red Hat Ansible Automation Platform 2.6
## 2.2. Choosing and obtaining a Red Hat Ansible Automation Platform installer
### 2.2.2. Installing without internet access




Use the Red Hat Ansible Automation Platform **Bundle** installation program if you are unable to access the internet, or would prefer not to install separate components and dependencies from online repositories. Access to Red Hat Enterprise Linux repositories is still needed. The `tar` archive includes all other dependencies.

**Procedure**

1. Navigate to the [Red Hat Ansible Automation Platform download](https://access.redhat.com/downloads/content/480/ver=2.6/rhel---9/2.6/x86_64/product-software) page.
1. In the **Product software** tab, clickDownload Nowfor the **Ansible Automation Platform <latest-version> Setup Bundle** .
1. Extract the files:


```
$ tar xvzf ansible-automation-platform-setup-bundle-&lt;latest-version&gt;.tar.gz
```




