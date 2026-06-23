# Configuration as Code with the ansible.platform collection
## Module defaults for connection parameters

The `ansible.platform` collection defines an action group called `gateway` that includes all modules. Use `module_defaults` to set connection parameters once instead of repeating them in every task:

```yaml
- name: Configure Ansible Automation Platform resources
hosts: localhost
gather_facts: false
module_defaults:
group/ansible.platform.gateway:
aap_hostname: "{{ aap_hostname }}"
aap_username: "{{ aap_username }}"
aap_password: "{{ aap_password }}"
aap_validate_certs: "{{ aap_validate_certs }}"
tasks:
- name: Ensure organization exists
ansible.platform.organization:
name: "My Organization"
state: present

- name: Ensure team exists
ansible.platform.team:
name: "My Team"
organization: "My Organization"
state: present
```
You can also use environment variables instead of specifying connection parameters in your playbook. The recommended naming convention is to use `AAP_` prefixed variable names, but `GATEWAY_` prefixed names are also accepted for backward compatibility:

- `AAP_HOSTNAME` or `GATEWAY_HOSTNAME`
- `AAP_USERNAME` or `GATEWAY_USERNAME`
- `AAP_PASSWORD` or `GATEWAY_PASSWORD`
- `AAP_TOKEN` or `GATEWAY_API_TOKEN` (the naming is asymmetric by design)
- `AAP_VALIDATE_CERTS` or `GATEWAY_VERIFY_SSL`
- `AAP_REQUEST_TIMEOUT` or `GATEWAY_REQUEST_TIMEOUT`

