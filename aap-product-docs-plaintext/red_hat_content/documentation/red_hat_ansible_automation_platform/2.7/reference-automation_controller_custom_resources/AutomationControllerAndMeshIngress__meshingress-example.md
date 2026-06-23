# Automation controller custom resources
## AutomationController and AutomationControllerMeshIngress [automationcontroller.ansible.com]
### Example AutomationControllerMeshIngress custom resource

```
apiVersion: automationcontroller.ansible.com/v1alpha1
kind: AutomationControllerMeshIngress
metadata:
name: my-mesh-ingress
namespace: aap
spec:
deployment_name: my-controller
```

