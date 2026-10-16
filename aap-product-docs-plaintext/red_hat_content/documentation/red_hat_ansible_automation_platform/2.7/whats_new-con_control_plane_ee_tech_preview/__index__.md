# Control-plane execution environment (Technology Preview)

As a Technology Preview, you can configure automation controller to use `control-plane-ee` for internal operations.

Important:

`control-plane-ee` is a Technology Preview feature. Technology Preview features are not supported with Red Hat production service level agreements (SLAs), might not be functionally complete, and are not recommended for production. These features provide early access to upcoming product features so that you can test functionality and provide feedback.

For this Technology Preview, the control-plane execution environment is used for internal automation controller operations such as:

- Project updates from Git, Subversion, remote archives, and Red Hat Insights
- Constructed inventory source updates

Regular inventory sources, such as cloud inventory sources, use the execution environment configured for the inventory source, when one is set. Otherwise, automation controller uses the execution environment resolved for the inventory update. Regular inventory sources do not automatically use `control-plane-ee`.

`ee-supported` remains the default. The control-plane execution environment does not run customer automation jobs.

Important:

`control-plane-ee` is intended only for internal automation controller operations. It is maintained for automation controller needs, not customer workloads, and its content updates do not provide customer notifications. It contains only dependencies for internal operations and does not include the collections, Python packages, and system tools that customer playbooks might require. Customer playbooks can fail. Do not select it for a job template or use it for customer workloads.
