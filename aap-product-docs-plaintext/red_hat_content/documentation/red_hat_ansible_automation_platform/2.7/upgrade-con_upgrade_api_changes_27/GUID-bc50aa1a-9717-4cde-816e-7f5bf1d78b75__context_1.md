# API changes in Ansible Automation Platform 2.7
## Update collection versions
### About this task

If your automation content still targets component endpoints or uses outdated collection versions, your playbooks and integrations will fail after the upgrade.

You must complete two actions to ensure your automation content works with Ansible Automation Platform 2.7:

- Upgrade all component collections to the latest versions for Ansible Automation Platform 2.7. The minimum required collection versions for Ansible Automation Platform 2.7 are as follows:
* `ansible.controller: 4.8.0`
* `ansible.hub: 1.0.6`
* `ansible.eda: 2.12.0`
* `ansible.platform: 2.7.0`
- Update connection values in your playbooks, inventory variables, and Configuration as Code content to use platform gateway.

### Procedure

1.  Update collection version pins in your `requirements.yml `file to require the latest versions:


```
collections:
- name: ansible.controller version: ">=4.8.0"
- name: ansible.hub version: ">=1.0.6"
- name: ansible.eda version: ">=2.12.0"
- name: ansible.platform version: ">=2.7.0"
```

2.  Rebuild your execution environments to include the updated collections.
3.  Refresh project and collection dependencies in automation controller.
4.  Verify the installed collection versions:


```
ansible-galaxy collection list | grep -E "ansible\.(controller|hub|eda|platform)"
```

5.  Run a test playbook against your upgraded Ansible Automation Platform 2.7 environment to confirm that API calls route through platform gateway.

