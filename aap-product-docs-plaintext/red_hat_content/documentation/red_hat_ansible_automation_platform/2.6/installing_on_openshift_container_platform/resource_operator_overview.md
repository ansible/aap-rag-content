# 13. Ansible Automation Platform Resource Operator
## 13.1. Resource Operator overview




Resource Operator is a custom resource (CR) that you can deploy after you have created your platform gateway deployment.

With Resource Operator you can define resources such as projects, job templates, and inventories in YAML files.

automation controller then uses the YAML files to create these resources. You can create the YAML through the **Form view** that prompts you for keys and values for your YAML code. Alternatively, to work with YAML directly, you can select **YAML view** .

The Resource Operator provides the following CRs:

- AnsibleJob
- JobTemplate
- Automation controller project
- Automation controller schedule
- Automation controller workflow
- Automation controller workflow template:
- Automation controller inventory
- Automation controller credential


For more information on any of the above custom resources, see [Using automation execution](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution) .

