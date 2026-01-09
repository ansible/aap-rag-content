# 8. Disconnected installation
## 8.1. Obtaining and configuring RPM source dependencies




The Ansible Automation Platform containerized setup bundle installation program does not include RPM source dependencies from the BaseOS and AppStream repositories. It relies on the host system’s package manager to resolve these dependencies.

To access these dependencies in a disconnected environment, you can use one of the following methods:

- Use [Red Hat Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html/installing_satellite_server_in_a_disconnected_network_environment/index) to synchronize repositories in your disconnected environment.
- Use a local repository that you create with the `    reposync` command on a Red Hat Enterprise Linux host that has an active internet connection.
- Use a local repository that you create from a mounted Red Hat Enterprise Linux Binary DVD ISO image.


