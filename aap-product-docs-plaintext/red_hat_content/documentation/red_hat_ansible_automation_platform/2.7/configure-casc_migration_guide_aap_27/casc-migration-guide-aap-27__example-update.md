# Configuration as Code migration guide for Ansible Automation Platform 2.7
## Example: Update a playbook for 2.7

The following example shows how to update a playbook that uses deprecated parameters.

**Before (2.6)**

```yaml
- name: Create user with org membership
ansible.platform.user:
username: "demo-user"
organizations:
- "Demo-Organization"
is_platform_auditor: true
```
**After (2.7)**

```yaml
- name: Create user
ansible.platform.user:
username: "demo-user"
state: present

- name: Assign organization role to user
ansible.platform.role_user_assignment:
user: "demo-user"
role_definition: "Organization Member"
object_ids:
- "Demo-Organization"
state: present

- name: Assign Platform Auditor role to user
ansible.platform.role_user_assignment:
user: "demo-user"
role_definition: "Platform Auditor"
# object_ids is not required for platform-wide roles
state: present
```
