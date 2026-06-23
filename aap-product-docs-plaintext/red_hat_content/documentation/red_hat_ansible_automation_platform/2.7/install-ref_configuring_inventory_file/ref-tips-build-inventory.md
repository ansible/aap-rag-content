# Configure the inventory file
## Tips for building inventories

When building inventories for Ansible automation, consider the following best practices to ensure efficient and effective management of your hosts.

- Ensure that group names are meaningful and unique.
- Group names are also case sensitive.
- Do not use spaces, hyphens, or preceding numbers (use `floor_19`, not `19th_floor`) in group names.
- Group hosts in your inventory logically according to their What, Where, and When:
* What: Group hosts according to the topology, for example: db, web, leaf, spine, metrics.
* Where: Group hosts by geographic location, for example: data center, region, floor, building.
* When: Group hosts by stage, for example: development, test, staging, production.
- Metrics service must be included when automation controller is present. In containerized deployments, use a dedicated host for metrics service (separate from controller, hub, gateway, and EDA).
