# Red Hat Ansible Automation Platform credential type
## Access automation controller credentials in an Ansible Playbook

You can get the host, username, and password parameters from a job runtime environment:

```
vars:
controller:
host: '{{ lookup("env", "CONTROLLER_HOST") }}'
username: '{{ lookup("env", "CONTROLLER_USERNAME") }}'
password: '{{ lookup("env", "CONTROLLER_PASSWORD") }}'
```
