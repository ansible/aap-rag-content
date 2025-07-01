# 2. Installing automation content navigator on RHEL
## 2.1. Installing automation content navigator on RHEL from an RPM




You can install automation content navigator on Red Hat Enterprise Linux (RHEL) from an RPM.

**Prerequisites**

- You have installed Python 3.10 or later.
- You have installed RHEL 8.6 or later.
- You registered your system with Red Hat Subscription Manager.


Note
Ensure that you only install the navigator matching your current Red Hat Ansible Automation Platform environment.



**Procedure**

1. Attach the Red Hat Ansible Automation Platform SKU:


```
$ subscription-manager attach --pool=&lt;sku-pool-id&gt;
```


1. Install automation content navigator with the following command:

v.2.5 for RHEL 8 for x86_64


```
$ sudo dnf install --enablerepo=ansible-automation-platform-2.4-for-rhel-8-x86_64-rpms ansible-navigator
```

v.2.5 for RHEL 9 for x86-64


```
$ sudo dnf install --enablerepo=ansible-automation-platform-2.4-for-rhel-9-x86_64-rpms ansible-navigator
```




**Verification**

- Verify your automation content navigator installation:


```
$ ansible-navigator --help
```




The following example demonstrates a successful installation:

![automation content navigator successful installation](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/3f44ec9dee1f94319e6a57e78c6c5f6b/navigator-stdout.png)


