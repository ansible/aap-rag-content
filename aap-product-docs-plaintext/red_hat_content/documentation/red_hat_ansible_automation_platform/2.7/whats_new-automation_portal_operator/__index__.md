# Automation portal operator

The automation portal operator deploys and manages Ansible automation portal on OpenShift using a declarative custom resource.

The automation portal operator follows a compose-via-CRD pattern with two operators working together. The automation portal operator reads the `AutomationPortal` custom resource, validates credentials, generates plugin configuration, and creates a custom resource. The Red Hat Developer Hub (RHDH) Operator reads the custom resource and creates the Deployment, Service, Route, and PostgreSQL database. When you create an `AutomationPortal` custom resource, the operator automatically installs the RHDH Operator if it is not already present on the cluster.

The operator reports five status conditions on the `AutomationPortal` custom resource. The overall `Ready` condition is `True` only when all other conditions are `True`.

For more information, see *Install automation portal on OpenShift using the operator*.
