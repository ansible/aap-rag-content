# Access Google Compute Engine credentials in an Ansible Playbook

You can access Google Compute Engine (GCE) credentials in an Ansible Playbook by using environment variables.

You can get GCE credential parameters from a job runtime environment:

```
vars:
gce:
email: '{{ lookup("env", "GCE_EMAIL") }}'
project: '{{ lookup("env", "GCE_PROJECT") }}'
pem_file_path: '{{ lookup("env", "GCE_PEM_FILE_PATH") }}'
```
