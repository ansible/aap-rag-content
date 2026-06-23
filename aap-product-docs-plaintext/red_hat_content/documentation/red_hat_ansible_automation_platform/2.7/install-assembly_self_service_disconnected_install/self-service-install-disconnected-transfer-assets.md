# Install Ansible automation portal in air-gapped OpenShift Container Platform environments
## Transfer assets to the disconnected environment

Transfer the modified Helm chart package from the connected bastion host to a machine inside your disconnected network. This action stages the installation assets for deployment within the isolated OpenShift environment.

### Procedure

1.  Copy the modified Helm chart `.tgz` file or files (for example, `redhat-rhaap-portal-1.0.1.tgz`) from your connected bastion host to a machine or jump box within your disconnected OpenShift network.
2.  If you use the HTTP plug-in registry method, transfer the plug-in tarball files to the disconnected environment.

