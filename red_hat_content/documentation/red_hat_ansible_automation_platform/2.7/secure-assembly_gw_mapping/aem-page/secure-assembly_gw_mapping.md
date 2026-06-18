+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping"
title = "Map external authenticators to Ansible Automation Platform - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping/aem-page/secure-assembly_gw_mapping.html"
last_crumb = "Map external authenticators to Ansible Automation Platform"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Map external authenticators to Ansible Automation Platform"
oversized = "false"
page_slug = "secure-assembly_gw_mapping"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping/toc/toc.json"
type = "aem-page"
+++

# Map external authenticators to Ansible Automation Platform

To control which users are allowed into the Ansible Automation Platform server, and placed into Ansible Automation Platform organizations or teams based on their attributes (such as username and email address) or what groups they belong to, you can configure authenticator maps.

Use authenticator maps to add conditions that must be met before a user is given or denied access to a resource type. Authenticator maps are associated with an authenticator and are given an order. The maps are processed in order when the user logs in. These are similar to firewall rules or mail filters.

## Understand authenticator mapping

Review how authenticator maps evaluate trigger conditions sequentially to govern user authorization. Understanding this process helps ensure that Ansible Automation Platform assigns the correct resource permissions when users log in.

Authentication
Validates a user’s identity, typically through a username and password or a trust system.

Authorization
Determines what an authenticated user can do once they are authenticated.

In Ansible Automation Platform, authenticators manage authentication, validating users and returning details such as their username, given name, email, and group memberships (for example, LDAP groups). Authorization comes from the authenticator’s associated maps.

During the authentication process, after a user has authenticated, the authorization system starts with a default set of permissions in memory. Then sequentially, the authenticator maps are processed and adjust permissions based on their trigger conditions. When all the authenticator’s maps are processed, the in-memory representation of the user’s permissions are reconciled with their existing permissions.

For example, here is a simplified in-memory representation of the default permissions as follows:

```
Access allowed = True
Superuser permission = Undefined
Admin of teams = None
```
And, you might have maps that need to be processed are processed in the following order:

1. **Allow** rule set to never
2. **Allow** rule based on group
3. **Superuser** rule based on user attributes
4. **Team** admin rule based on user group


The first **Allow** map, set to never, denies access to the system and the in-memory representation looks like:

```
Access allowed = False
Superuser permission = Undefined
Admin of teams = None
```
However, if the user matches the second **Allow** map (the group-based allow), the permissions change to the following:

```
Access allowed = True
Superuser permission = Undefined
Admin of teams = None
```
Where the user is subsequently granted access to Ansible Automation Platform because they have the required groups.

Next, the **Superuser** map checks user attributes. If no match is found, it does not revoke existing permissions by default. Therefore, the permissions remain the same as the results from the previous map:

```
Access allowed = True
Superuser permission = Skipped
Admin of teams = None
```
To revoke superuser access, you can select the **Revoke** option on the **Superuser** map. That way, when the user does not meet the attribute criteria, the permissions update to False such as the following:

```
Access allowed = True
Superuser permission = False
Admin of teams = None
```
The final **Team** map checks the user’s groups coming from the authenticator for admin access on the team “My Team”. If the user has the required group, the permissions update to the following:

```
Access allowed = True
Superuser permission = False
Admin of teams = “My Team”
```
If the user lacks the required group, permissions remain unchanged unless the **Revoke** option has been selected on the map, in which case permissions update to the following:

```
Access allowed = True
Superuser permission = False
Admin of teams = Revoke admin of “My Team”
```
After processing all maps in the order defined, the final permissions reconcile, updating the user’s access based on the map rules.

In summary, authenticators validate users and delegate system authorization to the authenticator maps. Authenticator maps are executed in order creating an in-memory representation of the users' permissions which get reconciled with the actual permissions after all maps are executed.

By default, authenticator maps return either **ALLOW** or **SKIPPED**.

ALLOW
Means that a match is detected and the platform should grant the user access to the corresponding role or permission (such as, superuser, or team member).

SKIPPED
Means that the user did not match the trigger in the map and, the platform skips processing this map and continues to check the remaining maps. This is useful if you want to grant users additional permissions in the system without having to change the authenticator maps.

However, when the **Revoke** option is selected, **SKIPPED** becomes **DENY** and users who do not meet the required trigger criteria are denied access to the corresponding role or permission. This ensures that only users with matching trigger conditions are granted access.

## Authenticator map types

Ansible Automation Platform supports the following rule types:

Allow
Determine if the user is allowed to log in to the system.

Organization
Determine if a user should be put into an organization.

Team
Determine if the user should be a member of a team.

Role
Determine if the user is a member of a role (for example, *System Auditor*).

Is Superuser
Determine if the user is a superuser in the system.

These authentication map types can be used with any type of authenticator.

## Authenticator map triggers

Each map has a trigger that defines when the map should be evaluated as true. Trigger types include the following:

Always
The trigger should always be fired.

Never
The trigger should never be fired.

Group
The map is true or false based on a user having, not having, or having multiple groups in the source system.

When defining a group trigger, the authentication mapping expands to include the following selections:

- **Operation:** This field includes conditional settings that trigger the handling of the rule based on the specified **Groups** criteria. The choices include **and** and **or**. For example, if you select **and** the user logging in must be a member of all of the groups specified in the **Groups** field for this trigger to be true. Alternatively, if you select **or** the user logging in must be a member of any of the specified **Groups** in order for the trigger to fire.  Note:
      If you are only keying off one group it does not matter if you select **"and"** or **"or"**.

- **Groups:** This is a list of one or more groups coming from the authentication system that the user must be a member of. The first time you create a **Groups** entry, you must manually enter the values. Once entered, that selection will be available from the **Groups** list. See the **Operation** field to determine the behavior of the trigger if more than one group is specified in the trigger.

   Note:
      You must enter group identifiers in lowercase. For example, `cn=johnsmith,dc=example,dc=com` instead of `CN=JohnSmith,DC=Example,DC=COM`.

Attribute
The map is true or false based on a users attributes coming from the source system.

When defining an attribute trigger, the authentication mapping expands to include the following selections:

- **Operation:** This field includes conditional settings that trigger the handling of the rule based on the specified **Attribute** criteria. In version 2.6 this field indicates what will happen if the source system returns a list of attributes instead of a single value. For example, if the source system returns multiple emails for a user and **Operation** was set to **and**, all of the given emails must match the **Comparison** for the trigger to be *True*. If **Operation** was set to **or**, any of the returned emails will set the trigger to *True* if they match the **Comparison** in the trigger.  Note:
      If you want to experiment with multiple attribute maps you can do that through the API but the UI form will remove multi-attribute maps if the authenticator is saved through the UI. When adding multiple attributes to a map, the **Operation** will also apply to the attributes.

- **Attribute:** The name of the attribute coming from the source system this trigger will be evaluated against. For example, if you wanted the trigger to fire based on the user’s surname and the last name field in the source system was called `users_last_name` you would enter the value "users_last_name" in this field.
- **Comparison:** Tells the trigger how to evaluate the value of the users. **Attribute** in the source system compared to the **Value** specified on the trigger. Available options are: **contains**, **matches**, **ends with**, **in**, or **equals**. Below is a breakdown of each **Comparison** type:
  * **contains**: The specified character sequence in **Value** is contained within the attributes value returned from the source. For example, given an attribute value of "John" from the source the contains **Comparison** would set the trigger to *True* if the trigger **Value** was set to "Jo" and *False* if the trigger **Value** was "Joy".
  * **matches**: The **Value** on the trigger is treated as a python regular expression and does a regular expression match (with case ignore on) between the specified **Value** and the value returned from the source system. For example, if the trigger’s **Value** was "Jo" the trigger would return *True* if the value from the source was "John" or "Joanne" or any other value which matched the regular expression "Jo". The trigger would return *False* if the sources value for the attribute was "Dan" because "Dan" does not match the regular expression "Jo".
  * **ends with**: The trigger will see if the value provided by the source ends with the specified **Value** of the trigger. For example, if the source provided a value of "John" the trigger would be *True* if its **Value** was set to "n" or "on". The trigger would be *False* if its **Value** was set to "z" because the value "John" coming from the source does not end with the value "z" specified by the trigger.
  * **equal**: The trigger will see if the value provided by the source is equal to (in its entirety) the specified **Value** of the trigger. For example, if the source returned the value "John", the trigger would be *True* if its **Value** was set to "John". Any value other than "John" returned from the source would set this trigger to *False*.
  * **in**: The **in** condition checks if the value matches one of several values. When **in** is specified as the **Comparison**, the **Value** field can be a comma-separated list. For example, if a trigger had a **Value** of "John,Donna" the trigger would be *True* if the attribute coming from the source had either the value "John" or "Donna". Otherwise, the trigger would be *False*.
  * **Value**: The value that a users attribute will be matched against based on the **Comparison** field. See examples in the **Comparison** definition.  Note:
            If the **Comparison** type is **in**, this field can be a comma-separated list (without spaces).

## Authenticator map examples

Use the following examples to explore the different conditions, such as groups and attribute values you can implement to control user access to the platform.

 **Add users to an organization based on an attribute**

In this example, you will add a user to the **Networking** organization if they have an `Organization` attribute with the value of `Networking`:


![Add users to an organization mapping example fully annotated with callout numbers that correlate with the following list that describes the function of each field](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/am-org-mapping-full-annotation.png)  


1. The **Organization** title of the page indicates that you are configuring settings permissions on an organization.
2. `Network Organization` is entered in this field and is the unique, descriptive name for this map configuration.
3. **Attributes** is selected from the **Trigger** list to configure authentication based on an attribute from the source system, which in this example is `Organization`.
4. The operation is defined as `or` meaning that at least one condition must be true for authentication to succeed.
5. The **Attribute** coming from the source system is Organization.
6. The **Comparison** value is set to `matches` which means that when a user has the attribute **Value** of `Networking`, they are added to the **Networking** organization.
7. The attribute **Value** coming from the source system is `Networking`.
8. The name of the **Organization** to which you are adding members is `Networking`.
9. Users are added to the **Networking** organization with the `Organization Member` role.


 **Add users to a team based on the users group**

In this example, you will add user to the `Apple` team if they have either of the following groups:

```
cn=administrators,ou=aap,ou=example,o=com
```
or

```
cn=operators,ou=aap,ou=example,co=com
```

![Add user to a team mapping example](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/am-apple-team-map-example.png)  


 **Do not escalate privileges**

In this example, you never escalate users to a superuser. But note, this rule does not revoke a user’s superuser permission because the revoke option is not set.


![Do not escalate privileges mapping example](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/am-do-not-escalate-privileges.png)  


 **Escalate privileges based on a user having a group**

In this example, you escalate user privileges to superuser if they belong to the following group:

```
cn=administrators,ou=aap
```

![Escalate privileges mapping example](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/am-escalate-privileges.png)  


 **Using mapping order to create exceptions**

Since maps are executed in order, it is possible to create exceptions. Expanding on the previous example for *Do not escalate privileges*, you can add another rule with a higher order, such as, *Escalate privileges*.

The first rule (*Do not escalate privileges*) prevents any user from being escalated to a superuser, but the second rule (*Escalate privileges*) alters that decision to grant superuser privileges to a user if they are in the `Administrators` group.


![Mapping order example](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/am-mapping-order.png)  

## Control user access to the system with allow mapping

With allow mapping, you can control which users have access to the system by defining the conditions that must be met.

### Procedure

1.  After configuring the authentication details for your authentication method, select the **Mapping** tab.
2.  Select **Allow** from the **Add authentication mapping** list.
3.  Enter a unique rule **Name** to identify the rule.
4.  Select a **Trigger** from the list. See [Authenticator map triggers](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-authenticator-map-triggers "Each map has a trigger that defines when the map should be evaluated as true. Trigger types include the following:") for more information about map triggers.
5.  Select **Revoke** to deny user access to the system when the trigger conditions are not matched.
6.  Click Next.

### What to do next

1. You can manage the authentication mappings order by clicking Manage mappings.
2. Drag and drop the mapping up or down in the list.  Note:
      The mapping precedence is determined by the order in which the mappings are listed.

3. Click Apply.

## Map users to organizations

You can control which users are placed into which Ansible Automation Platform organizations based on attributes such as their username and email address or based on groups provided from an authenticator.

### About this task

When organization mapping is positively evaluated, a specified organization is created, if it does not exist if the authenticator tied to the map is allowed to create objects.

### Procedure

1.  After configuring the authentication details for your authentication method, select the **Mapping** tab.
2.  Select **Organization** from the **Add authentication mapping** list.
3.  Enter a unique rule **Name** to identify the rule.
4.  Select a **Trigger** from the list. See [Authenticator map triggers](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-authenticator-map-triggers "Each map has a trigger that defines when the map should be evaluated as true. Trigger types include the following:") for more information about map triggers.
5.  Select **Revoke** to remove the user’s access to the selected organization role when the trigger conditions are not matched.
6.  Select the **Organization** to which matching users are added or blocked.
7.  Select a **Role** to be applied or removed for matching users (for example, **Organization Admin** or **Organization Member**).
8.  Click Next.

### What to do next

1. You can manage the authentication mappings order by clicking Manage mappings.
2. Drag and drop the mapping up or down in the list.  Note:
      The mapping precedence is determined by the order in which the mappings are listed.

3. Click Apply.

## Map users to teams

Team mapping is the mapping of team members (users) from authenticators.

### About this task

You can define the options for each team’s membership. For each team, you can specify which users are automatically added as members of the team and also which users can administer the team.

You can specify Team mappings separately for each account authentication.

When Team mapping is positively evaluated, a specified team and its organization are created, if they do not exist if the related authenticator is allowed to create objects.

 Important:

When configuring team mappings with an Attribute trigger, use the `or` operation. The `and` operation requires every single value in a list to match the comparison criteria for the trigger to be successful. This is rarely the intended behavior, as you typically want a match on at least one value in the list.

### Procedure

1.  After configuring the authentication details for your authentication method, select the **Mapping** tab.
2.  Select **Team** from the **Add authentication mapping** list.
3.  Enter a unique rule **Name** to identify the rule.
4.  Select a **Trigger** from the list. See [Authenticator map triggers](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-authenticator-map-triggers "Each map has a trigger that defines when the map should be evaluated as true. Trigger types include the following:") for more information about map triggers.
5.  Select **Revoke** to remove the user’s access to the selected organization role and deny user access to the system when the trigger conditions are not matched.
6.  Select the **Team** and **Organization** to which matching users are added or blocked.
7.  Select a **Role** to be applied or removed for matching users (for example, **Team Admin** or **Team Member**).
8.  Click Next.

### What to do next

1. You can manage the authentication mappings order by clicking Manage mappings.
2. Drag and drop the mapping up or down in the list.  Note:
      The mapping precedence is determined by the order in which the mappings are listed.

3. Click Apply.

## Map users to roles

Role mapping is the mapping of a user either to a global role, such as Platform Auditor, or team or organization role.

### About this task

When a Team or Organization is specified together with the appropriate Role, the behavior is the same with Organization mapping or Team mapping.

You can specify role mapping separately for each account authentication.

### Procedure

1.  After configuring the authentication details for your authentication method, select the **Mapping** tab.
2.  Select **Role** from the **Add authentication mapping** list.
3.  Enter a unique rule **Name** to identify the rule.
4.  Select a **Trigger** from the list. See [Authenticator map triggers](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-authenticator-map-triggers "Each map has a trigger that defines when the map should be evaluated as true. Trigger types include the following:") for more information about map triggers.
5.  Select **Revoke** to remove the role for the user when none of the trigger conditions are matched.
6.  Select a **Role** to be applied or removed for matching users.
7.  Click Next.

### What to do next

1. You can manage the authentication mappings order by clicking Manage mappings.
2. Drag and drop the mapping up or down in the list.  Note:
      The mapping precedence is determined by the order in which the mappings are listed.

3. Click Apply.

## Map users to the superuser role

Superuser mapping is the mapping of a user to the superuser role, such as System Administrator.

### Procedure

1.  After configuring the authentication details for your authentication method, select the **Mapping** tab.
2.  Select **Superuser** from the **Add authentication mapping** list.
3.  Enter a unique rule **Name** to identify the rule.
4.  Select a **Trigger** from the list. See [Authenticator map triggers](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_gw_mapping#gw-authenticator-map-triggers "Each map has a trigger that defines when the map should be evaluated as true. Trigger types include the following:") for more information about map triggers.
5.  Select **Revoke** to remove the superuser role from the user when none of the trigger conditions are matched.
6.  Click Next.

### What to do next

1. You can manage the authentication mappings order by clicking Manage mappings.
2. Drag and drop the mapping up or down in the list.  Note:
      The mapping precedence is determined by the order in which the mappings are listed.

3. Click Apply.

## Review authenticator map results

Platform administrators can review authenticator map evaluation results through the user API endpoint.

The results show how the maps are processed during the user’s login:

```
api/gateway/v1/users/X
```

## Use Jinja-like syntax in authenticator maps

Platform gateway supports a Jinja-like templating syntax in authenticator maps to dynamically assign users to organizations, teams, and roles based on attribute values from an external provider.

### About this task

The syntax that can be used in a map is `{% for_attr_value(<attribute_name>) %}`. This causes platform gateway to iterate over attribute values from an external provider, creating a separate mapping for each value.

**Example 1: Single attribute**

An **Organization** authenticator map is created with the following configuration:

- **Organization** field: Enter `Org {% for_attr_value(users_orgs) %}`.
- **Attribute** value: Enter `users_orgs`.
- **External data received**: `["Database", "Networking"]` (The attribute values returned by the Identity Provider)


This results in the authenticator map being evaluated twice, once for `Org Database` and once for `Org Networking`.

**Example 2: Multiple attributes**

You can also use this syntax more than once in a single attribute map. For example, having a syntax like `Organization {% for_attr_value(org) %} - Department {% for_attr_value(dept) %}` with attributes `org` having the values `a` and `b` and `dept` having the values `Y` and `Z` results in the map being run 4 times with the values:

- Organization a - Department Y
- Organization a - Department Z
- Organization b - Department Y
- Organization b - Department Z

### Procedure

1.  From the navigation panel, select Access Management> (and then)Authentication Methods.
2.  Select your authenticator from the list.
3.  Select the **Mapping** tab and click Create mapping.
4.  In **Authentication mapping**, choose the appropriate mapping type: **Organization**, **Team**, or **Role**.
5.  In the **Trigger** field, select **Attributes**.
6.  In the corresponding field, such as the **Organization** field for an Organization map, enter the Jinja-like syntax to dynamically generate the name.
      For example, to create an organization name based on an attribute called `users_orgs`, enter `Org {% for_attr_value(users_orgs) %}`.

7.  In the **Attribute** field, specify the name of the attribute from your external provider that has values you want to loop through, such as `users_orgs`.
8.  Complete any other required fields for the mapping.
9.  Click Create mapping.
      Platform gateway uses this template to create and manage user assignments based on the values of the specified attribute.

### Results

 Note:

The system raises a validation error if the templating syntax is mistyped and the new authenticator map is not created. During an authentication, if the external provider does not provide the specified attribute or the user does not have values associated with the attribute specified by the Jinja syntax, the map is triggered and a message indicating why is put into the platform gateway logs.
