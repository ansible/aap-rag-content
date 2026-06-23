# Configuration as Code with the ansible.platform collection
## The four-state model

Most modules in the `ansible.platform` collection support a four-state model for managing resources:

present
Create the resource if it does not exist, or update it if it does. Only the parameters you specify are set; other fields retain their current values.

absent
Delete the resource if it exists.

exists
Check whether the resource exists without creating or modifying it. Use this state to verify that prerequisites are in place before running further tasks.

enforced
Create or update the resource, and reset any parameters you did not specify to their API default values. Use this state when you want to ensure the complete desired state of a resource, not just the fields you explicitly define.

The following example uses the `enforced` state to ensure that an organization has only the specified description. Any other fields that were previously set on this organization are reset to their default values:

```yaml
- name: Enforce organization configuration
ansible.platform.organization:
name: "Production"
description: "Production automation resources"
state: enforced
```


Note:

Not all modules support every state. The `settings` module has no `state` parameter and always applies changes. The `token` module supports only `present` and `absent` and is not idempotent. The `feature_flag` module defaults to `exists` instead of `present`, so you must explicitly set `state: present` to modify a flag. For a complete list of supported states per module, see the module reference.

