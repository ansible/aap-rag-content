# Automation controller custom resources
## AutomationController and AutomationControllerMeshIngress [automationcontroller.ansible.com]
### Example AutomationController custom resource

```
apiVersion: automationcontroller.ansible.com/v1beta1
kind: AutomationController
metadata:
name: my-controller
spec:
uwsgi_processes: 4
task_resource_requirements:
requests:
cpu: 200m
memory: 512Mi
limits:
cpu: 2000m
memory: 2Gi
web_resource_requirements:
requests:
cpu: 200m
memory: 512Mi
limits:
cpu: 1000m
memory: 2Gi
```

