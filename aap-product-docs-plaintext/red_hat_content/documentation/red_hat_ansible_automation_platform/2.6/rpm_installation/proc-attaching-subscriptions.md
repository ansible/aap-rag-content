# 1. Red Hat Ansible Automation Platform installation overview
## 1.2. Managing Ansible Automation Platform subscriptions, updates, and support
### 1.2.4. Attaching your Red Hat Ansible Automation Platform subscription




You **must** have valid subscriptions on all nodes before installing Red Hat Ansible Automation Platform.

Note
Simple Content Access (SCA) is now the default subscription method for all Red Hat accounts. With SCA, you must register your systems to Red Hat Subscription Management (RHSM) or Satellite to access content. Traditional pool-based subscription attachment commands (such as `subscription-manager attach --pool` or `subscription-manager attach --auto` ) are no longer required. For more information, see [Simple Content Access](https://access.redhat.com/articles/simple-content-access) .



**Procedure**

1. Register your system with Red Hat Subscription Management:


```
$ sudo subscription-manager register --username &lt;$INSERT_USERNAME_HERE&gt; --password &lt;$INSERT_PASSWORD_HERE&gt;
```

With Simple Content Access (SCA), registration is the only step required to access Ansible Automation Platform content.

Note
For accounts still using legacy subscription pools, you might have to manually attach subscriptions using the commands shown in the troubleshooting section.






**Verification**

1. Refresh the subscription information on your system:


```
$ sudo subscription-manager refresh
```


1. Verify your registration:


```
$ sudo subscription-manager identity
```

This command displays your system identity, name, organization name, and organization ID, confirming successful registration.




**Troubleshooting**

- For legacy accounts not using SCA, you might have to manually attach subscriptions:


```
$ sudo subscription-manager list --available --all | grep "Ansible Automation Platform" -B 3 -A 6    $ sudo subscription-manager attach --pool=&lt;pool_id&gt;
```

Note
Do not use MCT4022 as a `    pool_id` as it can cause subscription attachment to fail.




- For legacy accounts not using SCA, if you are unable to locate certain packages that came bundled with the Ansible Automation Platform installer, or if you are seeing a `    <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">Repositories disabled by configuration</span></em></span>` message, use the following steps to identify and enable the required repository:


1. List available repositories:


```
$ sudo subscription-manager repos --list | grep -i ansible-automation-platform
```


1. Identify the repository name that matches your RHEL version, Ansible Automation Platform version, and architecture (for example, `        ansible-automation-platform-2.6-for-rhel-9-x86_64-rpms` ).
1. Enable the repository:


```
$ sudo subscription-manager repos --enable &lt;repository_name&gt;
```





