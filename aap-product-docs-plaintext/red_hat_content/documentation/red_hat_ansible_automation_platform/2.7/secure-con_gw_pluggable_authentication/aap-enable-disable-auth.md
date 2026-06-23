# Pluggable authentication
## Enable and disable the local authenticator

As a platform administrator, you can enable or disable authenticators. However, disabling your local authenticator can have significant impacts and should only be done under specific circumstances. Before you disable your local authenticator, you must consider the following:

### Before you begin

- You have at least one other authenticator method configured.
- You have at least one administrator account that can authenticate using your alternate authenticator.


CAUTION:

Disabling the local authenticator without an alternative authentication in place can result in a locked environment.

### About this task

Local account inaccessibility
Disabling the local authenticator prevents all local accounts, including the default `admin` account from logging in.

Potential inaccessibility
Disabling the local authenticator without having at least one other configured authenticator can render the Ansible Automation Platform environment completely inaccessible.

Dependency on enterprise authentication provider
If the local authenticator is disabled and an issue occurs with the configured enterprise authentication provider, the platform will become inaccessible until the enterprise authentication provider issue is resolved.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Ensure that at least one other authenticator type is configured and enabled.
3.  Select your **Local Authenticator**.
4.  Toggle the **Enabled** switch to the off position to disable the local authenticator.

If the local authenticator is disabled without another authentication method configured, or if an issue arises with your configured enterprise authentication provider, making the Ansible Automation Platform inaccessible, you can re-enable the local authenticator from the command line as follows:

1. List the available authenticators and retrieve the ID of your local authenticator by running the following command:

```
aap-gateway-api authenticators --list
```

2. Enable the local authenticator using its ID:

```
aap-gateway-manage authenticators --enable :id
```
where: `:id` is the ID of the local authenticator obtained from the previous step.

