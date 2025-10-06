# 5. Disconnected installation
## 5.2. Ansible Automation Platform installation on disconnected RHEL
### 5.2.2. RPM Source




RPM dependencies for Ansible Automation Platform that come from the BaseOS and AppStream repositories are not included in the setup bundle. To add these dependencies, you must first obtain access to BaseOS and AppStream repositories. Use Satellite to sync repositories and add dependencies. If you prefer an alternative tool, you can choose between the following options:

- Reposync
- The RHEL Binary DVD


Note
The RHEL Binary DVD method requires the DVD for supported versions of RHEL. See [Red Hat Enterprise Linux Life Cycle](https://access.redhat.com/support/policy/updates/errata) for information on which versions of RHEL are currently supported.



**Additional resources**

-  [Installing Satellite Server in a disconnected network environment](https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html/installing_satellite_server_in_a_disconnected_network_environment)


