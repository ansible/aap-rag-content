# Known limitations

The control-plane execution environment Technology Preview has the following known limitations.

- `control-plane-ee` is a Technology Preview and is not enabled by default. `ee-supported` remains the default.
- `control-plane-ee` is used for project updates and constructed inventory updates. Regular inventory sources use the execution environment configured for the inventory source, when one is set, or the execution environment resolved for the inventory update.
- `control-plane-ee` has only the dependencies required for internal automation controller operations and is not intended for customer workloads.
- The OpenShift Container Platform and containerized installer procedures use different configuration methods.
