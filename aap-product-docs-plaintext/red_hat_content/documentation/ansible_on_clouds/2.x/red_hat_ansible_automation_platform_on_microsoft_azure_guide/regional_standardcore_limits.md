# 2. Prerequisites for Installing Red Hat Ansible Automation Platform on Microsoft Azure
## 2.3. Azure resource quotas and infrastructure limits
### 2.3.2. Regional StandardCore limits




The `StandardCore` limit is a compute metric for the resources that are temporarily consumed when deploying the managed application.

It is possible that the Ansible Automation Platform on Microsoft Azure can deploy without hitting the `StandardCore` limit. When a deployment fails because the consumed resources hit the `StandardCore` limit, the error message includes `container group quota 'StandardCores' exceeded` :

```
code: DeploymentFailed
message:
At least one resource deployment operation failed. Please list deployment operations for details.
Please see https://aka.ms/DeployOperations for usage details.
details:
- code: DeploymentScriptContainerGroupInvalidSettings
message:
Resource type 'Microsoft.ContainerInstance/containerGroups'
container group quota 'StandardCores' exceeded in region 'eastus'.
Limit: '10', Usage: '10' Requested: '1'.
```

