# Out of scope

Understand which Ansible Automation Platform components and configurations require manual re-creation in the target environment and are not covered by the migration process.

Migration covers core Ansible Automation Platform components. Some components and configurations are out of scope and require manual re-creation in the target environment:

- Event-Driven Ansible: Manually recreate configuration and content for Event-Driven Ansible in the target environment.
- Instance groups: Manually recreate instance group configurations after migration.
- Hub content: Manually re-import or reconfigure content hosted in automation hub.
- Custom Certificate Authority (CA) for receptor mesh: Manually reconfigure custom CA configurations for receptor mesh.
- Disconnected environments: The migration process does not cover disconnected environments.
- Execution environments (other than the default one): Manually rebuild or re-import custom execution environments.


Manually re-create, import, or configure these items in the target environment.
