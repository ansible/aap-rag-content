# VMware vCenter credential type
## Access VMware vCenter credentials in an Ansible Playbook

You can get VMware vCenter credential parameters from a job runtime environment:

```
vars:
vmware:
host: '{{ lookup("env", "VMWARE_HOST") }}'
username: '{{ lookup("env", "VMWARE_USER") }}'
password: '{{ lookup("env", "VMWARE_PASSWORD") }}'
```
