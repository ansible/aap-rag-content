# Resource Operator custom resources
## Resource Operator custom resources [tower.ansible.com/v1alpha1]
### Connection secret

All Resource Operator custom resources require a `connection_secret` field that references a Kubernetes secret containing the platform gateway URL and an OAuth2 token. Create this secret before using any Resource Operator custom resources.

```
apiVersion: v1
kind: Secret
metadata:
name: aap-access
type: Opaque
stringData:
token: <generated-token>
host: https://my-aap-gateway.example.com/
```

