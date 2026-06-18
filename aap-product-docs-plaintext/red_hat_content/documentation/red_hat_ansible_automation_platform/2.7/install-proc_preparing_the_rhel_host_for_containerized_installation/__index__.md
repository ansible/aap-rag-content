# Prepare the Red Hat Enterprise Linux host

Containerized Ansible Automation Platform runs the component services as Podman based containers on top of a Red Hat Enterprise Linux host. Prepare the Red Hat Enterprise Linux host to ensure a successful installation.

## Procedure

1.  Log in to the Red Hat Enterprise Linux host as your non-root user.
2.  Ensure that the hostname of your host uses a fully qualified domain name (FQDN).   1.  To check the hostname of your host, run the following command:


```
hostname -f
```
Example output:

```
aap.example.org
```

2.  If the hostname is not a FQDN, you can set it with the following command:


```
$ sudo hostnamectl set-hostname <your_hostname>
```

3.  Register your Red Hat Enterprise Linux host with `subscription-manager`:


```
$ sudo subscription-manager register
```

4.  Verify that only the BaseOS and AppStream repositories are enabled on the host:


```
$ sudo dnf repolist
```
Example output for RHEL 9:

```
Updating Subscription Management repositories.
repo id                                                    repo name
rhel-9-for-x86_64-appstream-rpms                           Red Hat Enterprise Linux 9 for x86_64 - AppStream (RPMs)
rhel-9-for-x86_64-baseos-rpms                              Red Hat Enterprise Linux 9 for x86_64 - BaseOS (RPMs)
```
Example output for RHEL 10:

```
Updating Subscription Management repositories.
repo id                                                    repo name
rhel-10-for-x86_64-appstream-rpms                          Red Hat Enterprise Linux 10 for x86_64 - AppStream (RPMs)
rhel-10-for-x86_64-baseos-rpms                             Red Hat Enterprise Linux 10 for x86_64 - BaseOS (RPMs)
```
- For disconnected installations, follow the steps in [Obtain and configure RPM source dependencies](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_aap_containerized_disconnected_installation#obtaining-and-configuring-rpm-dependencies "The Ansible Automation Platform containerized setup bundle installation program does not include RPM source dependencies from the BaseOS and AppStream repositories. It relies on the host system’s package manager to resolve these dependencies.") to access these repositories.

5.  Ensure the host can resolve host names and IP addresses using DNS. This is essential to ensure services can talk to one another.
6.  Install `ansible-core`:


```
$ sudo dnf install -y ansible-core
```

7.  Optional: Install additional utilities that are useful for troubleshooting purposes, for example `wget`, `git-core`, `rsync`, and `vim`:


```
$ sudo dnf install -y wget git-core rsync vim
```

8.  Optional: To have the installation program automatically pick up and apply your Ansible Automation Platform subscription manifest license, follow the steps in [Obtain a manifest file](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_aap_activate_1#assembly-aap-obtain-manifest-files "You can obtain a subscription manifest in the Subscription Allocations section of Red Hat Subscription Management.").
