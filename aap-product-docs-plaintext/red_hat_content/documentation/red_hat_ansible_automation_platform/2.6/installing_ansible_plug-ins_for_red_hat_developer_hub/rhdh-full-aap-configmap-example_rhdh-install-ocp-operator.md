# 3. Installing the Ansible plug-ins with the Operator on OpenShift Container Platform
## 3.13. Full app-config-rhdh ConfigMap example for Ansible plug-ins entries




This example details necessary settings like the creatorService URL, optional integrations for Ansible Automation Platform and OpenShift Dev Spaces, and the addition of Ansible software templates to the catalog.

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

