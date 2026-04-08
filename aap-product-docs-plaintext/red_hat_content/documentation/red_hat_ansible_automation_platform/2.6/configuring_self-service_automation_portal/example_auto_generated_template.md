# 4. Configuring template RBAC and display logic
## 4.3. Example: Auto-generated template




The following YAML example uses the `spec.type` field to restrict the template view to the **EE definition files** page.

```
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
name: ansible-execution-environment-template
title: EE template
description: Ansible Execution Environment Template
tags:
- ansible
- execution-environment
# ...
spec:
type: execution-environment  # Restricts the template view to the Execution Environment page.
parameters:
# ...
```

