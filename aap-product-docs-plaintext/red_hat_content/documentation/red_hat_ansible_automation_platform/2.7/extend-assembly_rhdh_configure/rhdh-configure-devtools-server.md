# Configure the Ansible plug-ins
## Configure the Ansible Dev Tools Server

The `creatorService` URL is required for the Ansible plug-ins to provision new projects using the provided software templates.

### Procedure

Add the following code to your Red Hat Developer Hub `app-config-rhdh.yaml` file.

```
kind: ConfigMap
apiVersion: v1
metadata:
name: app-config-rhdh
...
data:
app-config-rhdh.yaml: |-
ansible:
creatorService:
baseUrl: 127.0.0.1
port: '8000'
...
```

