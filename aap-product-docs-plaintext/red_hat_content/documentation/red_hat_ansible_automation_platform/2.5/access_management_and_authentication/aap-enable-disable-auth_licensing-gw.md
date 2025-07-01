# 3. Configuring authentication in the Ansible Automation Platform
## 3.4. Enabling and disabling the local authenticator




As a platform administrator, you can enable or disable authenticators. However, disabling your local authenticator can have significant impacts and should only be done under specific circumstances. Before you disable your local authenticator, you must consider the following:

**Prerequisites**

- You have at least one other authenticator method configured.
- You have at least one administrator account that can authenticate using your alternate authenticator.


Procedure
Disabling the local authenticator without an alternative authentication in place can result in a locked environment.



1. From the navigation panel, selectAccess Management→Authentication Methods.
1. Ensure that at least one other authenticator type is configured and enabled.
1. Select your **Local Authenticator** .
1. Toggle the **Enabled** switch to the off position to disable the local authenticator.


**Troubleshooting**

If the local authenticator is disabled without another authentication method configured, or if an issue arises with your configured enterprise authentication provider, making the Ansible Automation Platform inaccessible, you can re-enable the local authenticator from the command line as follows:


1. List the available authenticators and retrieve the ID of your local authenticator by running the following command:


```
aap-gateway-api authenticators --list
```


1. Enable the local authenticator using its ID:


```
aap-gateway-manage authenticators --enable :id
```

where: `    :id` is the ID of the local authenticator obtained from the previous step.




