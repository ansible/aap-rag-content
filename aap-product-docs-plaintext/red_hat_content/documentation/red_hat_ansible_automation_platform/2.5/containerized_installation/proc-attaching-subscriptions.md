# 1. Managing Ansible Automation Platform licensing, updates and support
## 1.5. Attaching your Red Hat Ansible Automation Platform subscription




You **must** have valid subscriptions attached on all nodes before installing Red Hat Ansible Automation Platform. Attaching your Ansible Automation Platform subscription provides access to subscription-only resources necessary to proceed with the installation.

**Procedure**

1. Make sure your system is registered:


```
$ sudo subscription-manager register --username &lt;$INSERT_USERNAME_HERE&gt; --password &lt;$INSERT_PASSWORD_HERE&gt;
```


1. Obtain the `    pool_id` for your Red Hat Ansible Automation Platform subscription:


```
$ sudo subscription-manager list --available --all | grep "Ansible Automation Platform" -B 3 -A 6
```

Note
Do not use MCT4022 as a `    pool_id` for your subscription because it can cause Ansible Automation Platform subscription attachment to fail.




1. Attach the subscription:


```
$ sudo subscription-manager attach --pool=&lt;pool_id&gt;
```

You have now attached your Red Hat Ansible Automation Platform subscriptions to all nodes.


1. To remove this subscription, enter the following command:


```
$ sudo subscription-manager remove --pool=&lt;pool_id&gt;
```




**Verification**

- Verify the subscription was successfully attached:


```
$ sudo subscription-manager list --consumed
```

**Troubleshooting**

- If you are unable to locate certain packages that came bundled with the Ansible Automation Platform installer, or if you are seeing a `    <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">Repositories disabled by configuration</span></em></span>` message, try enabling the repository by using the command:

Red Hat Ansible Automation Platform 2.5 for RHEL 8


```
$ sudo subscription-manager repos --enable ansible-automation-platform-2.5-for-rhel-8-x86_64-rpms
```

Red Hat Ansible Automation Platform 2.5 for RHEL 9


```
$ sudo subscription-manager repos --enable ansible-automation-platform-2.5-for-rhel-9-x86_64-rpms
```




