# Understand metrics service architecture
## Deployment topology options

**AIO Growth (All-in-One) topology**

A single host runs all Ansible Automation Platform components, including metrics service. The `[automationmetrics]` inventory group points to the same host as `[automationcontroller]`.

Characteristics:

- All components share the same host
- Simplest deployment for small to medium environments
- Metrics service, controller, and databases on one node
- Suitable for development, testing, or small production environments

To skip metrics service installation, set `automationmetrics_skip_install=true` in `[all:vars] `and omit the `[automationmetrics]` inventory group.

**Enterprise / Multi-Node topology**

Metrics service runs on a dedicated node. You define which node hosts metrics service by using the `[automationmetrics]` inventory group. In the growth topology (all-in-one), metrics service shares the single host with all other components. In the enterprise topology, metrics service requires its own dedicated node. Unlike controller, hub, and EDA, metrics service does not support multi-node or high-availability deployment.

Characteristics:

- Flexible topology: metrics service can run on any node
- Scaled independently from controller
- Metrics processing isolated from automation execution
- Suitable for large-scale production environments

To skip metrics service installation, set `automationmetrics_skip_install=true` in `[all:vars]` and omit the `[automationmetrics]` inventory group.

