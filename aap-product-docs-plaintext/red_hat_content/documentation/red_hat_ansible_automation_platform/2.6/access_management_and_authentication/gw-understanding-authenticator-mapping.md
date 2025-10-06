# 2. Configuring authentication in the Ansible Automation Platform
## 2.7. Mapping
### 2.7.1. Understanding authenticator mapping




In Ansible Automation Platform, authenticators manage authentication, validating users and returning details such as their username, first name, email, and group memberships (for example, LDAP groups). Authorization comes from the authenticator’s associated maps.

During the authentication process, after a user has authenticated, the authorization system starts with a default set of permissions in memory. Then sequentially, the authenticator maps are processed and adjust permissions based on their trigger conditions. When all the authenticator’s maps are processed, the in-memory representation of the user’s permissions are reconciled with their existing permissions.

For example, here is a simplified in-memory representation of the default permissions as follows:

```
Access allowed = True
Superuser permission = Undefined
Admin of teams = None
```

And, you might have maps that need to be processed are processed in the following order:

1.  **Allow** rule set to never
1.  **Allow** rule based on group
1.  **Superuser** rule based on user attributes
1.  **Team** admin rule based on user group


The first **Allow** map, set to never, denies access to the system and the in-memory representation looks like:

```
Access allowed =<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">False</span></strong></span>Superuser permission = Undefined
Admin of teams = None
```

However, if the user matches the second **Allow** map (the group-based allow), the permissions change to the following:

```
Access allowed =<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">True</span></strong></span>Superuser permission = Undefined
Admin of teams = None
```

Where the user is subsequently granted access to Ansible Automation Platform because they have the required groups.

Next, the **Superuser** map checks user attributes. If no match is found, it does not revoke existing permissions by default. Therefore, the permissions remain the same as the results from the previous map:

```
Access allowed = True
Superuser permission =<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">Skipped</span></strong></span>Admin of teams = None
```

To revoke superuser access, you can select the **Revoke** option on the **Superuser** map. That way, when the user does not meet the attribute criteria, the permissions update to False like in the following:

```
Access allowed = True
Superuser permission =<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">False</span></strong></span>Admin of teams = None
```

The final **Team** map checks the user’s groups coming from the authenticator for admin access on the team “My Team”. If the user has the required group, the permissions update to the following:

```
Access allowed = True
Superuser permission = False
Admin of teams = “<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">My Team</span></strong></span>”
```

If the user lacks the required group, permissions remain unchanged unless the **Revoke** option has been selected on the map, in which case permissions update to the following:

```
Access allowed = True
Superuser permission = False
Admin of teams =<span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">Revoke admin of “My Team”</span></strong></span>
```

After processing all maps in the order defined, the final permissions reconcile, updating the user’s access based on the map rules.

In summary, authenticators validate users and delegate system authorization to the authenticator maps. Authenticator maps are executed in order creating an in-memory representation of the users' permissions which get reconciled with the actual permissions after all maps are executed.

By default, authenticator maps return either **ALLOW** or **SKIPPED** .

However, when the **Revoke** option is selected, **SKIPPED** becomes **DENY** and users who do not meet the required trigger criteria are denied access to the corresponding role or permission. This ensures that only users with matching trigger conditions are granted access.

