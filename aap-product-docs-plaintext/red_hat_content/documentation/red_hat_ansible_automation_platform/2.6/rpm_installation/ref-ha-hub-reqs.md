# 2. System requirements
## 2.4. Automation hub system requirements
### 2.4.1. High availability automation hub requirements




Before deploying a high availability (HA) automation hub, ensure that you have a shared storage file system installed in your environment and that you have configured your network storage system, if applicable.

#### 2.4.1.1. Required shared storage




Shared storage is required when installing more than one Automation hub with a `file` storage backend. The supported shared storage type for RPM-based installations is Network File System (NFS).

Before you run the Red Hat Ansible Automation Platform installer, verify that you installed the `/var/lib/pulp` directory across your cluster as part of the shared storage file system installation. The Red Hat Ansible Automation Platform installer returns an error if `/var/lib/pulp` is not detected in one of your nodes, causing your high availability automation hub setup to fail.

If you receive an error stating `/var/lib/pulp` is not detected in one of your nodes, ensure `/var/lib/pulp` is properly mounted in all servers and re-run the installer.

#### 2.4.1.2. Installing firewalld for HA hub deployment




If you intend to install a HA automation hub using a network storage on the automation hub nodes itself, you must first install and use `firewalld` to open the necessary ports as required by your shared storage system before running the Ansible Automation Platform installer.

Install and configure `firewalld` by executing the following commands:

1. Install the `    firewalld` daemon:


```
$ dnf install firewalld
```


1. Add your network storage under <service> using the following command:


```
$ firewall-cmd --permanent --add-service=&lt;service&gt;
```

Note
For a list of supported services, use the `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">$ firewall-cmd --get-services</span></strong></span>` command




1. Reload to apply the configuration:


```
$ firewall-cmd --reload
```




