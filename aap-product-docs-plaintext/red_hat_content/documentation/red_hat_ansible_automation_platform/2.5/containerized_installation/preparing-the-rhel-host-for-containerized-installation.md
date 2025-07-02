# 2. Ansible Automation Platform containerized installation
## 2.3. Preparing the Red Hat Enterprise Linux host for containerized installation




Containerized Ansible Automation Platform runs the component services as Podman based containers on top of a Red Hat Enterprise Linux host. Prepare the Red Hat Enterprise Linux host to ensure a successful installation.

**Procedure**

1. Log in to the Red Hat Enterprise Linux host as your non-root user.
1. Ensure the hostname associated with your host is set as a fully qualified domain name (FQDN).


1. To check the hostname associated with your host, run the following command:


```
hostname -f
```

Example output:


```
aap.example.org
```


1. If the hostname is not a FQDN, you can set it with the following command:


```
sudo hostnamectl set-hostname &lt;your_hostname&gt;
```



1. Register your Red Hat Enterprise Linux host with `    subscription-manager` :


```
sudo subscription-manager register
```


1. Verify that only the BaseOS and AppStream repositories are enabled on the host:


```
$ sudo dnf repolist
```

Example output:


```
Updating Subscription Management repositories.    repo id                                                    repo name    rhel-9-for-x86_64-appstream-rpms                           Red Hat Enterprise Linux 9 for x86_64 - AppStream (RPMs)    rhel-9-for-x86_64-baseos-rpms                              Red Hat Enterprise Linux 9 for x86_64 - BaseOS (RPMs)
```


1. Ensure the host can resolve host names and IP addresses using DNS. This is essential to ensure services can talk to one another.
1. Install `    ansible-core` :


```
sudo dnf install -y ansible-core
```


1. Optional: You can install additional utilities that can be useful for troubleshooting purposes, for example `    wget` , `    git-core` , `    rsync` , and `    vim` :


```
sudo dnf install -y wget git-core rsync vim
```


1. Optional: To have the installation program automatically pick up and apply your Ansible Automation Platform subscription manifest license, follow the steps in [Obtaining a manifest file](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/assembly-gateway-licensing#assembly-aap-obtain-manifest-files) .


**Additional resources**

- For more information about registering your Red Hat Enterprise Linux host and attaching a subscription, see [Attaching your Red Hat Ansible Automation Platform Subscription](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication/assembly-gateway-licensing#proc-attaching-subscriptions) .
- For information about configuring unbound DNS, see [Setting up an unbound DNS server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_networking_infrastructure_services/assembly_setting-up-an-unbound-dns-server_networking-infrastructure-services) .
- For information about configuring DNS using BIND, see [Setting up and configuring a BIND DNS server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_networking_infrastructure_services/assembly_setting-up-and-configuring-a-bind-dns-server_networking-infrastructure-services) .
- For more information about `    ansible-core` , see [Ansible Core Documentation](https://docs.ansible.com/ansible/latest/) .


