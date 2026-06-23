# Configuration as Code migration guide for Ansible Automation Platform 2.7
## Collection version requirements

Important:

You must upgrade to the latest version of all component collections shipped for Ansible Automation Platform 2.7 before running automation against the upgraded platform. Older collection versions might construct URLs or authentication flows that target component APIs directly, resulting in HTTP 404 errors or authentication failures after direct access removal.

| Collection           | Purpose                                                                             |
| -------------------- | ----------------------------------------------------------------------------------- |
| `ansible.controller` | Automation controller API modules and resource management through platform gateway. |
| `ansible.hub`        | Automation hub and Galaxy API modules through platform gateway.                     |
| `ansible.eda`        | Event-Driven Ansible API modules through platform gateway.                          |
| `ansible.platform`   | Platform gateway authentication, tokens, and platform-wide resource management.     |


After you upgrade the collections, complete the following tasks:

- Pin or upgrade collections in `requirements.yml` and execution environments to the latest versions available for your release.
- Rebuild execution environments and refresh project and collection dependencies.
- Verify collection versions in use before running production playbooks.

