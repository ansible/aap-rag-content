# 3. Installing the Ansible plug-ins with the Operator on OpenShift Container Platform
## 3.10. Configuring Role Based Access Control




Red Hat Developer Hub offers Role-based Access Control (RBAC) functionality. RBAC can then be applied to the Ansible plug-ins content.

**Procedure**

- Assign the following roles:


- Members of the `        admin:superUsers` group can select templates in the **Create** tab of the Ansible plug-ins to create playbook and collection projects.
- Members of the `        admin:users` group can view templates in the **Create** tab of the Ansible plug-ins.

The following example adds RBAC to Red Hat Developer Hub.


```
data:          app-config-rhdh.yaml: |            plugins:            ...            permission:              enabled: true              rbac:                admin:                  users:                    - name: user:default/&lt;user-scm-ida&gt;                  superUsers:                    - name: user:default/&lt;user-admin-idb&gt;
```

For more information about permission policies and managing RBAC, refer to the [Authorization in Red Hat Developer Hub](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.6/html-single/authorization_in_red_hat_developer_hub/index) guide for Red Hat Developer Hub.





