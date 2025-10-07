# 2. Configuring authentication in the Ansible Automation Platform
## 2.7. Mapping
### 2.7.11. Using Jinja-like syntax in authenticator maps




Platform gateway supports a Jinja-like templating syntax in authenticator maps to dynamically assign users to organizations, teams, and roles. The syntax that can be used in a map is `{% for_attr_value(&lt;attribute_name&gt;) %}` . This causes platform gateway to iterate over attribute values from an external provider, creating a separate mapping for each value.

**Example 1: Single attribute**

An **Organization** authenticator map is created with the following configuration:

-  **Organization** field: Enter **Org {% for_attr_value(users_orgs) %}** .
-  **Attribute** value: Enter **users_orgs** .
-  **External data received** : ["Database", "Networking"] (The attribute values returned by the Identity Provider)


This results in the authenticator map being evaluated twice, once for `Org Database` and once for `Org Networking` .

**Example 2: Multiple attributes**

Additionally, you can also use this syntax more than once in a single attribute map. For example, having a syntax like `Organization {% for\_attr\_value(org) %} \- Department {% for attr\_value(dept) %}` with attributes `org` having the values `a` and `b` and `dept` having the values `Y` and `Z` results in the map being run 4 times with the values:

- Organization a \- Department Y
- Organization a \- Department Z
- Organization b \- Department Y
- Organization b \- Department Z


**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. Select your authenticator from the list.
1. Select the **Mapping** tab and clickCreate mapping.
1. In **Authentication mapping** , choose the appropriate mapping type: **Organization** , **Team** , or **Role** .
1. In the **Trigger** field, select **Attributes** .
1. In the corresponding field, such as the **Organization** field for an Organization map, enter the Jinja-like syntax to dynamically generate the name.


- For example, to create an organization name based on an attribute called `        users_orgs` , enter `        Org {% for_attr_value(users_orgs) %}` .

1. In the **Attribute** field, specify the name of the attribute from your external provider that has values you want to loop through, such as `    users_orgs` .
1. Complete any other required fields for the mapping, see [Authenticator map triggers](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-configure-authentication#gw-authenticator-map-triggers) for more information.
1. ClickCreate mapping. Platform gateway uses this template to create and manage user assignments based on the values of the specified attribute.

Note
The system raises a validation error if the templating syntax is mistyped and the new authenticator map is not created. During an authentication, if the external provider does not provide the specified attribute or the user does not have values associated with the attribute specified by the Jinja syntax the map is triggered and a message indicating why is put into the platform gateway logs.






