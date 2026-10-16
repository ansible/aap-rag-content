# Install automation portal on OpenShift using the operator

Install Ansible automation portal on OpenShift Container Platform using the automation portal operator. This installation method is available as a Technology Preview.

Important:

The automation portal operator is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production.

The automation portal operator automates the deployment and configuration of Ansible automation portal on OpenShift. The operator manages the full lifecycle of the automation portal, including installation, configuration, and upgrades.

The operator follows a compose-via-CRD pattern. It generates portal-specific configuration and creates a custom resource that reconciles into a running automation portal deployment.
