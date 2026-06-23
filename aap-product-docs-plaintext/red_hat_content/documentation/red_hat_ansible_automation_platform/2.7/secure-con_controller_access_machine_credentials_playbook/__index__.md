# Access machine credentials in an ansible playbook

You can get username and password from Ansible facts:

```
vars:
machine:
username: '{{ ansible_user }}'
password: '{{ ansible_password }}'
```

