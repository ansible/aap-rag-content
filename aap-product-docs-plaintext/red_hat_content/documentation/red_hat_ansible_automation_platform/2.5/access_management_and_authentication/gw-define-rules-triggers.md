# 2. Configuring authentication in the Ansible Automation Platform
## 2.3. Creating an authentication method
### 2.3.2. Defining authentication mapping rules and triggers




Authentication map types can be used with any type of authenticator. Each map has a trigger that defines when the map should be evaluated as true.

**Procedure**

1. From the navigation panel, selectAccess Management→Authentication Methods.
1. In the list view, select the authenticator name displayed in the **Name** column.
1. Select the **Mapping** tab from the **Details** page of your authenticator.
1. ClickCreate mapping.
1. Select a map type from the **Authentication mapping** list. See [Authenticator map types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-authenticator-map-types) for detailed descriptions of the different map types. Choices include:


-  [Allow](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-allow-mapping)
-  [Organization](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-controller-organization-mapping)
-  [Team](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#proc-controller-team-mapping)
-  [Role](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-role-mapping)
-  [Is Superuser](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-superuser-mapping)

1. Enter a unique rule **Name** to identify the rule.
1. Select a **Trigger** from the list. See [Authenticator map triggers](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-authenticator-map-triggers) for more details. Choices include:


-  **Always**
-  **Never**
-  **Group**
-  **Attribute**

1. ClickCreate mapping.
1. Repeat this procedure to create additional mapping rules and triggers for the authenticator.
1. Proceed to [Adjust the Mapping order](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/access_management_and_authentication/index#gw-adjust-mapping-order) to optionally reorder the mappings for your authenticator.

Note
The mapping order setting is only available if there is more than one authenticator map defined.






