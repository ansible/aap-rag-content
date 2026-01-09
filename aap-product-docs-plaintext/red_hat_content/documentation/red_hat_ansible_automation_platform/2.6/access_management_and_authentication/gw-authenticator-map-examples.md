# 2. Configuring authentication in the Ansible Automation Platform
## 2.7. Mapping
### 2.7.4. Authenticator map examples




Use the following examples to explore the different conditions, such as groups and attribute values you can implement to control user access to the platform.

**Add users to an organization based on an attribute**

In this example, you will add a user to the **Networking** organization if they have an `Organization` attribute with the value of `Networking` :

![Add users to an organization mapping example fully annotated with callout numbers that correlate with the following list that describes the function of each field](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Access_management_and_authentication-en-US/images/1c9a5e0970eddcaaed6e1c084d68b05a/am-org-mapping-full-annotation.png)


1. The **Organization** title of the page indicates that you are configuring settings permissions on an organization.
1.  `    Network Organization` is entered in this field and is the unique, descriptive name for this map configuration.
1.  **Attributes** is selected from the **Trigger** list to configure authentication based on an attribute from the source system, which in this example is `    Organization` .
1. The operation is defined as `    or` meaning that at least one condition must be true for authentication to succeed.
1. The **Attribute** coming from the source system is Organization.
1. The **Comparison** value is set to `    matches` which means that when a user has the attribute **Value** of `    Networking` , they are added to the **Networking** organization.
1. The attribute **Value** coming from the source system is `    Networking` .
1. The name of the **Organization** to which you are adding members is `    Networking` .
1. Users are added to the **Networking** organization with the `    Organization Member` role.


**Add users to a team based on the users group**

In this example, you will add user to the `Apple` team if they have either of the following groups:

```
cn=administrators,ou=aap,ou=example,o=com
```

or

```
cn=operators,ou=aap,ou=example,co=com
```

![Add user to a team mapping example](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Access_management_and_authentication-en-US/images/c042e34a642a888c9802793b67bf468d/am-apple-team-map-example.png)


**Do not escalate privileges**

In this example, you never escalate users to a superuser. But note, this rule does not revoke a user’s superuser permission because the revoke option is not set.

![Do not escalate privileges mapping example](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Access_management_and_authentication-en-US/images/331950d755c96f1644de7bdd0dced24b/am-do-not-escalate-privileges.png)


**Escalate privileges based on a user having a group**

In this example, you escalate user privileges to superuser if they belong to the following group:

```
cn=administrators,ou=aap
```

![Escalate privileges mapping example](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Access_management_and_authentication-en-US/images/018d28310df7776dd32ec6bd14c8de02/am-escalate-privileges.png)


**Using mapping order to create exceptions**

Since maps are executed in order, it is possible to create exceptions. Expanding on the previous example for _Do not escalate privileges_ , you can add another rule with a higher order, such as, _Escalate privileges_ .

The first rule ( _Do not escalate privileges_ ) prevents any user from being escalated to a superuser, but the second rule ( _Escalate privileges_ ) alters that decision to grant superuser privileges to a user if they are in the `Administrators` group.

![Mapping order example](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Access_management_and_authentication-en-US/images/88b556d07c8867bedcff63f183595e0f/am-mapping-order.png)


