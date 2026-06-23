# Configure the Ansible plug-ins
## Add Ansible plug-ins software templates

Add Ansible Automation Platform software templates to your Red Hat Developer Hub instance so users can create new Ansible playbooks and collection projects based on Ansible best practices.

### Procedure

1.  Edit your custom Red Hat Developer Hub config map, for example `app-config-rhdh`.
2.  Add the following code to your Red Hat Developer Hub `app-config-rhdh.yaml` file.

```
data:
app-config-rhdh.yaml: |
catalog:
...
locations:
...
- type: url
target: https://github.com/ansible/ansible-rhdh-templates/blob/main/all.yaml
rules:
- allow: [Template]
```

