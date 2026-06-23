# Automate nodes that comply with security profiles
## Option 2: Create custom fapolicyd rules

Where the `fapolicyd` service must enforce its rules, consider crafting a custom set of rules to permit Ansible Automation Platform to run its Python code.

### About this task

The following example procedure treats the "ansible" service account as a trusted entity and enables it to run content in the local Ansible temporary directory (by default, `$HOME/.ansible/tmp`).

### Procedure

1.  Create the file `/etc/fapolicy/rules.d/50-ansible.rules` with the following content:
`allow perm=any uid=ansible trust=1 : dir=/home/ansible/.ansible/tmp/`

2.  Restart the fapolicyd service:
`sudo systemctl restart fapolicyd.service`

This example rule might require modification to work with any other `fapolicyd` rules that exist on the managed RHEL nodes, and must be thoroughly tested and approved by your security auditor before being put into production.
