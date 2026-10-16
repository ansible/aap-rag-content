# Install automation portal on OpenShift Container Platform

Install Ansible automation portal on OpenShift Container Platform. Choose the installation method that matches your operational requirements.

## Choose your installation method

Ansible automation portal supports two installation methods on OpenShift Container Platform. For VM-based deployments on RHEL, see *Deploy the Ansible automation portal RHEL appliance*.

| Installation method               | Platform                                       | Lifecycle management                                                         | Disconnected support                                                                | When to use                                                                           |
| --------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Helm chart**                    | OpenShift Container Platform                   | Helm. Manual`helm upgrade` for configuration changes and version updates.    | Yes. Mirror container images and Helm chart packages.                               | You have an existing Helm-based deployment or prefer Helm-based lifecycle management. |
| **Operator** (Technology Preview) | OpenShift Container Platform 4.18 through 4.23 | Operator Lifecycle Manager (OLM). Automated install, upgrade, and uninstall. | Yes. Mirror operator bundle, catalog, and container images to an internal registry. | You want declarative, operator-managed deployments on OpenShift.                      |
