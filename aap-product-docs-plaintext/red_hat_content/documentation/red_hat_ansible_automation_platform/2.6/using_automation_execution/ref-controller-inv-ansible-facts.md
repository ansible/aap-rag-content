# 14. Inventories
## 14.2. Constructed Inventories
### 14.2.4. Ansible facts




To create an inventory with Ansible facts, you must run a playbook against the inventory that has the setting `gather_facts: true` . The facts differ system-to-system. The following examples are not intended to address all known scenarios.

#### 14.2.4.1. Filter on environment variables




The following example involves filtering on environmental variables using the YAML format:

```
source_vars:

plugin: constructed
strict: true
groups:
hosts_using_xterm: ansible_env.TERM == "xterm"

limit: hosts_using_xterm
```

#### 14.2.4.2. Filter hosts by processor type




The following example involves filtering hosts by processor type (Intel) using the YAML format:

```
source_vars:

plugin: constructed
strict: true
groups:
intel_hosts: "GenuineIntel" in ansible_processor

limit: intel_hosts
```

Note
Hosts in constructed inventories are not counted against your license allotment because they are referencing the original inventory host. Additionally, hosts that are disabled in the original inventories are not included in the constructed inventory.



An inventory update run using `ansible-inventory` creates the constructed inventory contents.

This is always configured to update-on-launch before a job, but you can still select a cache timeout value in case this takes too long.

When creating a constructed inventory, the API ensures that it always has one inventory source associated with it. All inventory updates have an associated inventory source, and the fields needed for constructed inventory ( `source_vars` and `limit` ) are fields already present on the inventory source model.

