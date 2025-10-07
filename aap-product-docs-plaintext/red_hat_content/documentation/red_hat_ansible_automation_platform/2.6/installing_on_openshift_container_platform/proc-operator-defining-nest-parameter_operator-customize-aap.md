# 3. Customizing your Red Hat Ansible Automation Platform Operator on OpenShift Container Platform
## 3.3. Defining a parameter on a nested component




To define a parameter, such as the `resource_requirements` for Automation Controller, you add the configuration to the parent Ansible Automation Platform CR YAML. This ensures that the Ansible Automation Platform CR is the single source of truth for your deployment.

**Procedure**

1. Log in to OpenShift Container Platform.
1. Navigate toOperators→Installed Operators.
1. Select your Ansible Automation Platform Operator deployment.
1. Go to the Ansible Automation Platform tab and click the name of your CR.
1. In the **YAML view** tab, locate the **spec** section.
1. Add the `    automationcontroller` parameter with the nested `    resource_requirements` parameter and its value:


```
spec:      database:        resource_requirements:          requests:            cpu: 200m            memory: 512Mi        storage_requirements:          requests:            storage: 100Gi
```


1. ClickSaveto apply the changes. The operator automatically applies this configuration to the automation controller component.


