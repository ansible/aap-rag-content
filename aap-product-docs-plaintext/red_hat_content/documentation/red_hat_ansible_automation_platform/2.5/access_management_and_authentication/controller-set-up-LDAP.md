# 3. Configuring authentication in the Ansible Automation Platform
## 3.5. Configuring an authentication type
### 3.5.2. Configuring LDAP authentication




As a platform administrator, you can configure LDAP as the source for account authentication information for Ansible Automation Platform users.

Note
If the LDAP server you want to connect to has a certificate that is self-signed or signed by an internal certificate authority (CA), the CA certificate must be added to the system’s trusted CAs. Otherwise, connection to the LDAP server will result in an error that the certificate issuer is not recognized.



When LDAP is configured, an account is created for any user who logs in with an LDAP username and password and they can be automatically placed into organizations as either regular users or organization administrators.

Ansible Automation Platform treats usernames as case-insensitive in LDAP. It sends the username that was entered without modification to the LDAP provider for authentication. After successful authentication, the platform converts the username to lowercase and stores it in the database. For example, if a user logs in as `JDOE` , their platform username will be `jdoe` . If the user logs in again as `JDoe` , their username will still be `jdoe` .

However, if Ansible Automation Platform is configured with multiple LDAP authenticators, and the same user IDs exist across them, their usernames might differ. For instance, `JDOE` might have the username `jdoe` , while `jDOE` could be assigned `jdoe-&lt;some hash&gt;` .

Note
If a user previously logged in using different case variations of their username, Ansible Automation Platform maps all case variations to the lowercase username. Existing users with other case variations are not valid for interactive log in. However, any existing OAuth tokens for the mixed case username still allow authentication. A system administrator can delete those case variation users if needed.



Users created through an LDAP login should not change their username, first name, last name, or set a local password for themselves. Any changes made to this information is overwritten the next time the user logs in to the platform.

Important
Migration of LDAP authentication settings are not supported for 2.4 to 2.5 in the platform UI. If you are upgrading from Ansible Automation Platform 2.4 to 2.5, be sure to save your authentication provider data before upgrading.



**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. ClickCreate authentication.
1. Enter a **Name** for this authentication configuration.
1. Select **LDAP** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.
1. Select a legacy authenticator method from the **Auto migrate users from** list. After upgrading from 2.4 to 2.5, this is the legacy authenticator from which to automatically migrate users to this new authentication configuration. Refer to [Ansible Automation Platform post-upgrade steps](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_upgrade_and_migration/aap-post-upgrade) in the RPM upgrade and migration guide for important information about migrating users.
1. In the **LDAP Server URI** field, enter or modify the list of LDAP servers to which you want to connect. This field supports multiple addresses.
1. In the **LDAP Bind DN text** field, enter the Distinguished Name (DN) to specify the user that the Ansible Automation Platform uses to connect to the LDAP server as shown in the following example:


```
CN=josie,CN=users,DC=website,DC=com
```


1. In the **LDAP Bind Password** text field, enter the password to use for the binding user.
1. Select a group type from the **LDAP Group Type** list.

The group type defines the class name of the group, which manages the groups associated with users in your LDAP directory and is returned by the search specified in Step 14 of this procedure. The group type, along with group parameters and the group search, is used to find and assign groups to users during log in, and can also be evaluated during the mapping process. The following table lists the available group types, along with their descriptions and the necessary parameters for each. By default, LDAP groups will be mapped to Django groups by taking the first value of the cn attribute. You can specify a different attribute with `    name_attr` . For example, `    name_attr='cn'` .


<span id="idm140050077903840"></span>
**Table 3.1. Available LDAP group types**

|  **LDAP Group Type** |  **Description** |  **Initializer method ( _init_ )** |
| --- | --- | --- |
|  `PosixGroupType` | Handles the `posixGroup` object class. This checks for both primary group and group membership. |  `name_attr='cn'` |
|  `MemberDNGroupType` | Handles the grouping mechanisms wherein the group object contains a list of its member DNs. |  `member_attr, name_attr='cn'` |
|  `GroupOfNamesType` | Handles the `groupOfNames` object class. Equivalent to `MemberDNGroupType('member')` . |  `name_attr='cn'` |
|  `GroupOfUniqueNamesType` | Handles the `groupOfUniqueNames` object class. Equivalent to `MemberDNGroupType('uniqueMember')` . |  `name_attr='cn'` |
|  `ActiveDirectoryGroupType` | Handles the Active Directory groups. Equivalent to `MemberDNGroupType('member')` . |  `name_attr='cn'` |
|  `OrganizationalRoleGroupType` | Handles the `organizationalRole` object class. Equivalent to `MemberDNGroupType('roleOccupant')` . |  `name_attr='cn'` |
|  `NestedGroupOfNamesType` | Handles the `groupOfNames` object class. Equivalent to `NestedMemberDNGroupType('member')` . |  `member_attr, name_attr='cn'` |
|  `NestedGroupOfUniqueNamesType` | Handles the `groupOfUniqueNames` object class. Equivalent to `NestedMemberDNGroupType('uniqueMember')` . |  `name_attr='cn'` |
|  `NestedActiveDirectoryGroupType` | Handles the Active Directory groups. Equivalent to `NestedMemberDNGroupType('member')` . |  `name_attr='cn'` |
|  `NestedOrganizationalRoleGroupType` | Handles the `organizationalRole` object class. Equivalent to `NestedMemberDNGroupType('roleOccupant')` . |  `name_attr='cn'` |




Note
The group types that are supported by Ansible Automation Platform use the underlying [django-auth-ldap library](https://django-auth-ldap.readthedocs.io/en/latest/reference.html#django_auth_ldap.config.LDAPGroupType) . To specify the parameters for the selected group type, see Step 14 of this procedure.




1. You can use **LDAP User DN Template** as an alternative to user search. This approach is more efficient for user lookups than searching if it is usable in your organizational environment. Enter the name of the template as shown in the following example:


```
uid=%(user)s,cn=users,cn=accounts,dc=example,dc=com
```

where: `    uid` is the user identifier, `    cn` is the common name and `    dc` is the domain component.

Note
If this setting has a value it will be used instead of the **LDAP User Search** setting.




1.  **LDAP Start TLS** is disabled by default. StartTLS allows your LDAP connection to be upgraded from an unencrypted connection to a secure connection using Transport Layer Security (TLS). To enable StartTLS when the LDAP connection is not using SSL, set the switch to **On** .
1. Optional: Enter any **Additional Authenticator Fields** that this authenticator can take. These fields are not validated and are passed directly back to the authenticator.

Note
Values defined in this field override the dedicated fields provided in the UI. Any values not defined here are not provided to the authenticator.




1. Enter any **LDAP Connection Options** to set for the LDAP connection. LDAP referrals are not disabled by default. Disable this setting to prevent login flow timeouts and ensure successful user logins. Option names should be strings as shown in the following example:


```
OPT_REFERRALS: 0    OPT_NETWORK_TIMEOUT: 30
```

See the [python-LDAP Reference](https://www.python-ldap.org/en/python-ldap-3.4.3/reference/ldap.html#options) for possible options and values that can be set.


1. Depending on the selected **LDAP Group Type** , different parameters are available in the **LDAP Group Type Parameters** field to account for this. `    LDAP_GROUP_TYPE_PARAMS` is a dictionary, which is converted to `    kwargs` and passed to the **LDAP Group Type** class selected. There are two common parameters used by group types: `    name_attr` and `    member_attr` . Where `    name_attr` defaults to `    cn` and `    member_attr` defaults to `    member` :


```
{"name_attr": "cn", "member_attr": "member"}
```

To determine the parameters that a specific **LDAP Group Type** requires, refer to the [django_auth_ldap documentation](https://django-auth-ldap.readthedocs.io/en/latest/reference.html#django_auth_ldap.config.LDAPGroupType) on the classes `    init` parameters.


1. In the **LDAP Group Search** field, specify which groups should be searched and how to search them as shown in the following example:


```
[    "dc=example,dc=com",    "SCOPE_SUBTREE",    "(objectClass=group)"     ]
```


1. In the **LDAP User Attribute Map** field, enter user attributes to map LDAP fields to your Ansible Automation Platform users, for example, `    email` or `    first_name` as shown in the following example:


```
{    "first_name": "givenName",    "last_name": "sn",    "email": "mail"    }
```


1. In the **LDAP User Search** field, enter where to search for users during authentication as shown in the following example:


```
[    "OU=Users,DC=website,DC=com",    "SCOPE_SUBTREE",    "(cn=%(user)s)"    ]
```

If the **LDAP User DN Template** is not set, the Ansible Automation Platform authenticates to LDAP using the **Bind DN Template** and **LDAP Bind Password** . After authentication, an LDAP search is performed to locate the user specified by this field. If the user is found, Ansible Automation Platform validates the provided password against the user found by the LDAP search. Multiple search queries are supported for users with `    LDAPUnion` by entering multiple search terms as shown in the following example:


```
[        [            "ou=users,dc=example,dc=com",            "SCOPE_SUBTREE",            "uid=%(user)s"        ],         [            "ou=employees,dc=subdivision,dc=com",            "SCOPE_SUBTREE",            "uid=%(user)s"         ]    ]
```

If non-unique users are found during multiple searches, those users will not be able to log in to Ansible Automation Platform. Based on the example provided, if a user with `    uid=jdoe` was found in both the `    ou=users,dc=example,dc=com` and `    ou=employees,dc=subdivision,dc=com` , neither `    jdoe` user would be able to log in. All other unique users that are found in either branch would still be able to log in.

Note
If the field **LDAP User DN Template** is populated, it takes precedence over the **LDAP User Search** field and only the template will be used to authenticate users.




1. To automatically create organizations, users, and teams upon successful login, select **Create objects** .
1. To enable this authentication method upon creation, select **Enabled** .
1. To remove a user for any groups they were previously added to when they authenticate from this source, select **Remove users** .
1. ClickCreate Authentication Method.


**Next steps**

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (like username and email address) or to what groups they belong, continue to [Mapping](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-mapping) .


