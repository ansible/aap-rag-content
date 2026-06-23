# Event-Driven Ansible custom resources
## EDA [eda.ansible.com/v1alpha1]
### Example custom resource

```
apiVersion: eda.ansible.com/v1alpha1
kind: EDA
metadata:
name: my-eda
spec:
automation_server_ssl_verify: 'no'
api:
replicas: 2
activation_worker:
replicas: 2
event_stream:
replicas: 2
```

