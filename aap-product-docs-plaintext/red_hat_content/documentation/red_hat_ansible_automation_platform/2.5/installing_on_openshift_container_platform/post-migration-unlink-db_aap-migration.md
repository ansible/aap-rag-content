# 5. Migrating Red Hat Ansible Automation Platform to Red Hat Ansible Automation Platform Operator
## 5.4. Post migration cleanup
### 5.4.2. Unlinking the old database configuration secret post migration




After a successful migration you must unlink your old database configuration secret.

**Procedure**

1. Log in to **Red Hat OpenShift Container Platform** .
1. Navigate toOperators→Installed Operators.
1. Select the Ansible Automation Platform Operator installed on your project namespace.
1. Select the **Automation Controller** tab.
1. Click your **AutomationController** object. You can then view the object through the **Form view** or **YAML view** . The following inputs are available through the **YAML view** .
1. Locate the `    old_postgres_configuration_secret` item within the spec section of the YAML contents.
1. Delete the line that contains this item.
1. ClickSave.


