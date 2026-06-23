# Amazon Web Services credential type
## Access Amazon EC2 credentials in an Ansible Playbook

You can get AWS credential parameters from a job runtime environment:

```
vars:
aws:
access_key: '{{ lookup("env", "AWS_ACCESS_KEY_ID") }}'
secret_key: '{{ lookup("env", "AWS_SECRET_ACCESS_KEY") }}'
security_token: '{{ lookup("env", "AWS_SECURITY_TOKEN") }}'
```
