# 2. Configuring authentication in the Ansible Automation Platform
## 2.3. Creating an authentication method
### 2.3.2. Defining authentication mapping rules and triggers

Authentication map types can be used with any type of authenticator. Each map has a trigger that defines when the map should be evaluated as true.

**Procedure**

1. From the navigation panel, select Access Management → Authentication Methods.

2. In the list view, select the authenticator name displayed in the **Name** column.

3. Select the **Mapping** tab from the **Details** page of your authenticator.

4. Click Create mapping.

5. Select a map type from the **Authentication mapping** list. See [Authenticator map types](#gw-authenticator-map-types "2.7.2.&nbsp;Authenticator map types") for detailed descriptions of the different map types. Choices include:


- [Allow](#gw-allow-mapping "2.7.5.&nbsp;Allow mapping")
- [Organization](#proc-controller-organization-mapping "2.7.6.&nbsp;Organization mapping")
- [Team](#proc-controller-team-mapping "2.7.7.&nbsp;Team mapping")
- [Role](#gw-role-mapping "2.7.8.&nbsp;Role mapping")
- [Is Superuser](#gw-superuser-mapping "2.7.9.&nbsp;Superuser mapping")

6. Enter a unique rule **Name** to identify the rule.

7. Select a **Trigger** from the list. See [Authenticator map triggers](#gw-authenticator-map-triggers "2.7.3.&nbsp;Authenticator map triggers") for more details. Choices include:


- **Always**
- **Never**
- **Group**
- **Attribute**

8. Click Create mapping.

9. Repeat this procedure to create additional mapping rules and triggers for the authenticator.

10. Proceed to [Adjust the Mapping order](#gw-adjust-mapping-order "2.3.3.&nbsp;Adjusting the Mapping order") to optionally reorder the mappings for your authenticator.


Note
The mapping order setting is only available if there is more than one authenticator map defined.

