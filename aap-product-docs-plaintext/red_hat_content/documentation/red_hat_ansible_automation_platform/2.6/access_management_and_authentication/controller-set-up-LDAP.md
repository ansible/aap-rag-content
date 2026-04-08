# 2. Configuring authentication in the Ansible Automation Platform
## 2.5. Configuring an authentication type
### 2.5.4. Configuring LDAP authentication




As a platform administrator, you can configure LDAP as the source for account authentication information for Ansible Automation Platform users.

Note
If the LDAP server you want to connect to has a certificate that is self-signed or signed by an internal certificate authority (CA), the CA certificate must be added to the system’s trusted CAs. Otherwise, connection to the LDAP server will result in an error that the certificate issuer is not recognized.



Your LDAP certificate is not automatically migrated if you use the default Red Hat Enterprise Linux truststore. If you are upgrading Ansible Automation Platform and your LDAP authentication relies on a certificate added to the system’s truststore, this LDAP certificate configuration is not automatically migrated for you to platform gateway in Ansible Automation Platform 2.6.

-  **For upgrades from Ansible Automation Platform 2.4 to Ansible Automation Platform 2.6** :


- The migration of all authenticator configurations from automation controller to platform gateway are automated. This includes moving third-party authentication configuration and sensitive configuration data, such as SAML private keys or OAuth secret keys, from automation controller to platform gateway. However, if you are using custom LDAP certificates you still need to complete the following procedure for these certificates.
- The `        is_superuser` and `        is_system_auditor` flags in your `        LDAP AUTH_LDAP_USER_FLAGS_BY_GROUP` settings are successfully migrated to the new platform gateway. However, the `        is_active flag` is not available in platform gateway and therefore is not migrated. Instead you can use a deny rule to prevent access to the system by users.

-  **For upgrades from Ansible Automation Platform 2.5 to Ansible Automation Platform 2.6** : Authenticator configurations are not automatically migrated from automation controller. If you configured authentication in Ansible Automation Platform 2.5, those settings remain as currently configured after upgrading to 2.6. If you used a custom certificate in 2.5 for LDAP you need to migrate that as well.


**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. ClickCreate authentication.
1. Enter a **Name** for this authentication configuration.
1. Select **LDAP** from the **Authentication type** list. The **Authentication details** section automatically updates to show the fields relevant to the selected authentication type.
1. In the **LDAP Server URI** field, enter or modify the list of LDAP servers to which you want to connect. This field supports multiple addresses.
1. In the **LDAP Bind DN text** field, enter the Distinguished Name (DN) to specify the user that the Ansible Automation Platform uses to connect to the LDAP server as shown in the following example:


```
cn=josie,cn=users,dc=website,dc=com
```


1. In the **LDAP Bind Password** text field, enter the password to use for the binding user.
1. Select a group type from the **LDAP Group Type** list.

The group type defines the class name of the group, which manages the groups associated with users in your LDAP directory and is returned by the search specified in Step 14 of this procedure. The group type, along with group parameters and the group search, is used to find and assign groups to users during log in, and can also be evaluated during the mapping process. The following table lists the available group types, along with their descriptions and the necessary parameters for each. By default, LDAP groups will be mapped to Django groups by taking the first value of the cn attribute. You can specify a different attribute with `    name_attr` . For example, `    name_attr='cn'` .


<span id="idm139625898481632"></span>
**Table 2.1. Available LDAP group types**

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




1. Enter any **LDAP Connection Options** to set for the LDAP connection. By default, LDAP referrals are disabled to prevent certain LDAP queries from hanging with Active Directory. Option names should be strings as shown in the following example:


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
{    "first_name": "givenname",    "last_name": "sn",    "email": "mail"    }
```


1. In the **LDAP User Search** field, enter where to search for users during authentication as shown in the following example:


```
[    "ou=users,dc=website,dc=com",    "SCOPE_SUBTREE",    "(cn=%(user)s)"    ]
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

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or to what groups they belong, continue to [Mapping](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/access_management_and_authentication/index#gw-mapping) .


#### 2.5.4.1. Importing a certificate authority in automation controller for LDAPS integration




You can authenticate to the automation controller server by using LDAP. However, if you change to using LDAPS (LDAP over SSL/TLS) to authenticate and the TLS certificate is not trusted by platform gateway, it fails with an error such as:

```
2025-08-26 16:40:56,141 WARNING   django_auth_ldap Caught LDAPError while authenticating: SERVER_DOWN({'result': -1, 'desc': "Can't contact LDAP server", 'ctrls': [], 'info': 'error:0A000086:SSL routines::certificate verify failed (self-signed certificate)'})
```

To get Ansible Automation Platform to trust the certificate coming from LDAP, perform the following procedure on all platform gateway instances.

**Procedure**

1. Place a copy of the LDAP servers certificate in the directory, `    /etc/pki/ca-trust/source/anchors/` .
1. Run the command:


```
update-ca-trust
```




