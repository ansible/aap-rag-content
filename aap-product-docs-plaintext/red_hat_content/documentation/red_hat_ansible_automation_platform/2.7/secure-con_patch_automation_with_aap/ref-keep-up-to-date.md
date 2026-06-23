# Automate software patching
## Keep everything up to date

For non-production systems like labs, you can automate weekly patching using a job template. This example playbook updates all RPMs to the latest versions on a regular cadence to keep your servers current.

```
- name: Install all available RPM updates
hosts: target_hosts
become: true

tasks:
- name: Install latest RPMs
ansible.builtin.dnf:
name: '*'
state: latest
```

