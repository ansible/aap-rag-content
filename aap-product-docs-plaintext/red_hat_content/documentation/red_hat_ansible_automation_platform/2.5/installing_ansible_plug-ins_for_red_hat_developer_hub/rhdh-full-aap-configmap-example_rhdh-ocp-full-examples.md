# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.7. Full examples
### 2.7.1. Full app-config-rhdh ConfigMap example for Ansible plug-ins entries




```
kind: ConfigMap
...
metadata:
name: app-config-rhdh
...
data:
app-config-rhdh.yaml: |-
ansible:
creatorService:
baseUrl: 127.0.0.1
port: '8000'
# Optional integrations
rhaap:
baseUrl: '&lt;https://MyControllerUrl&gt;'
token: '&lt;AAP Personal Access Token&gt;'
checkSSL: &lt;true or false&gt;
devSpaces:
baseUrl: '&lt;https://MyDevSpacesURL&gt;'
automationHub:
baseUrl: '&lt;https://MyPrivateAutomationHubURL&gt;'

...
catalog:
locations:
- type: url
target: https://github.com/ansible/ansible-rhdh-templates/blob/main/all.yaml
rules:
- allow: [Template]
...
```

