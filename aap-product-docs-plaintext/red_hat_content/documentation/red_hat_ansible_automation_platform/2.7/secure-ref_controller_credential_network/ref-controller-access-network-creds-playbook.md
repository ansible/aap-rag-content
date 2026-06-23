# Network credential type
## Access network credentials in an Ansible Playbook

When using the **Controller Access Network Credentials** credential type, you can access the username and password parameters in your Ansible Playbook by using the following environment variables:

-  `ANSIBLE_NET_USERNAME`
-  `ANSIBLE_NET_PASSWORD`


You can get the username and password parameters from a job runtime environment:

```
vars:
network:
username: '{{ lookup("env", "ANSIBLE_NET_USERNAME") }}'
password: '{{ lookup("env", "ANSIBLE_NET_PASSWORD") }}'
```

