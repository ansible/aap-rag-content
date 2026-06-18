# Use automation controller credentials in a playbook

You can access automation controller credentials in an Ansible Playbook by using environment variables. You can get credential parameters from a job runtime environment:

Note:

In Ansible Automation Platform 2.7, the `CONTROLLER_HOST` environment variable contains the platform gateway URL, not the direct automation controller URL. This ensures all API access goes through platform gateway.

The following playbook is an example of how to use automation controller credentials in your playbook.

```
- hosts: all

vars:
machine:
username: '{{ ansible_user }}'
password: '{{ ansible_password }}'
controller:
host: '{{ lookup("env", "CONTROLLER_HOST") }}'
username: '{{ lookup("env", "CONTROLLER_USERNAME") }}'
password: '{{ lookup("env", "CONTROLLER_PASSWORD") }}'
network:
username: '{{ lookup("env", "ANSIBLE_NET_USERNAME") }}'
password: '{{ lookup("env", "ANSIBLE_NET_PASSWORD") }}'
aws:
access_key: '{{ lookup("env", "AWS_ACCESS_KEY_ID") }}'
secret_key: '{{ lookup("env", "AWS_SECRET_ACCESS_KEY") }}'
security_token: '{{ lookup("env", "AWS_SECURITY_TOKEN") }}'
vmware:
host: '{{ lookup("env", "VMWARE_HOST") }}'
username: '{{ lookup("env", "VMWARE_USER") }}'
password: '{{ lookup("env", "VMWARE_PASSWORD") }}'
gce:
email: '{{ lookup("env", "GCE_EMAIL") }}'
project: '{{ lookup("env", "GCE_PROJECT") }}'
azure:
client_id: '{{ lookup("env", "AZURE_CLIENT_ID") }}'
secret: '{{ lookup("env", "AZURE_SECRET") }}'
tenant: '{{ lookup("env", "AZURE_TENANT") }}'
subscription_id: '{{ lookup("env", "AZURE_SUBSCRIPTION_ID") }}'

tasks:
- debug:
var: machine

- debug:
var: controller

- debug:
var: network

- debug:
var: aws

- debug:
var: vmware

- debug:
var: gce

- shell: 'cat {{ gce.pem_file_path }}'
delegate_to: localhost

- debug:
var: azure
```

## Use 'delegate_to' and any lookup variable

```
- command: somecommand
environment:
USERNAME: '{{ lookup("env", "USERNAME") }}'
PASSWORD: '{{ lookup("env", "PASSWORD") }}'
delegate_to: somehost
```
