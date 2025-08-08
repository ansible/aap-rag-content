# 2. Ansible Automation Platform containerized installation
## 2.2. System requirements
### 2.2.1. Prerequisites




- Ensure a dedicated non-root user is configured on the Red Hat Enterprise Linux host.


- This user requires `        sudo` or other Ansible supported privilege escalation ( `        sudo` is recommended) to perform administrative tasks during the installation.
- This user is responsible for the installation of containerized Ansible Automation Platform.
- This user is also the service account for the containers running Ansible Automation Platform.

- For managed nodes, ensure a dedicated user is configured on each node. Ansible Automation Platform connects as this user to run tasks on the node. For more information about configuring a dedicated user on each node, see [Preparing the managed nodes for containerized installation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/aap-containerized-installation#preparing-the-managed-nodes-for-containerized-installation) .
- For remote host installations, ensure SSH public key authentication is configured for the non-root user. For guidelines on setting up SSH public key authentication for the non-root user, see [How to configure SSH public key authentication for passwordless login](https://access.redhat.com/solutions/4110681) .
- Ensure internet access is available from the Red Hat Enterprise Linux host if you are using the default online installation method.
- Ensure the appropriate network ports are open if a firewall is in place. For more information about the ports to open, see [Container topologies](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/tested_deployment_models/container-topologies) in _Tested deployment models_ .


Important
Storing container images on an NFS share is not supported by Podman. To use an NFS share for the user home directory, set up the Podman storage backend path outside of the NFS share. For more information, see [Rootless Podman and NFS](https://www.redhat.com/en/blog/rootless-podman-nfs) .



