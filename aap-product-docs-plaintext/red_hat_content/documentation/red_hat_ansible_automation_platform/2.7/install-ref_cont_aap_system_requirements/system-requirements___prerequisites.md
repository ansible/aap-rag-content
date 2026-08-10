# System requirements
## Prerequisites

- Configure a dedicated non-root user on the Red Hat Enterprise Linux host.   * This user requires `sudo` or other Ansible supported privilege escalation (`sudo` is recommended) to perform administrative tasks during the installation.
* This user is responsible for the installation of containerized Ansible Automation Platform.
* This user is also the service account for the containers running Ansible Automation Platform.
- For each Red Hat Enterprise Linux host in your containerized deployment, configure a dedicated user. The containerized installation program connects as this user to run tasks on the host. For more information about configuring a dedicated user on each host, see [Create the installation user](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_preparing_the_managed_nodes_for_containerized_installation "To ensure a secure containerized setup, create a dedicated user on each Red Hat Enterprise Linux host for the containerized installation program to use when connecting and running tasks.").
- For remote host installations, configure SSH public key authentication for the non-root user. For guidelines on setting up SSH public key authentication for the non-root user, see [How to configure SSH public key authentication for passwordless login](https://access.redhat.com/solutions/4110681).
- Ensure the Red Hat Enterprise Linux host has internet access if you are using the default online installation method.
- Open the appropriate network ports if you have a firewall in place. For more information about the ports to open, see [Container enterprise topology](/documentation/en-us/red_hat_ansible_automation_platform/2.7/plan-ref_cont_b_env_a "The container-based enterprise topology provides redundancy and higher compute for large volumes of automation.") in *Tested deployment models*.

Important:

Podman does not support storing container images on an NFS share. To use an NFS share for the user home directory, set up the Podman storage backend path outside of the NFS share. For more information, see [Rootless Podman and NFS](https://www.redhat.com/en/blog/rootless-podman-nfs).

