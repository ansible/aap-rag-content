# 2. Ansible Automation Platform containerized installation
## 2.5. Downloading Ansible Automation Platform




Choose the installation program you need based on your Red Hat Enterprise Linux environment internet connectivity and download the installation program to your Red Hat Enterprise Linux host.

**Prerequisites**

- You have logged in to the Red Hat Enterprise Linux host as your non-root user.


**Procedure**

1. Download the latest version of containerized Ansible Automation Platform from the [Ansible Automation Platform download page](https://access.redhat.com/downloads/content/480/ver=2.5/rhel---9/2.5/x86_64/product-software) .


1. For online installations: **Ansible Automation Platform 2.5 Containerized Setup**
1. For offline or bundled installations: **Ansible Automation Platform 2.5 Containerized Setup Bundle**

1. Copy the installation program `    .tar.gz` file and the optional manifest `    .zip` file onto your Red Hat Enterprise Linux host.


1. You can use the `        scp` command to securely copy the files. The basic syntax for `        scp` is:


```
scp [options] &lt;path_to_source_file&gt; &lt;path_to_destination&gt;
```

Use the following `        scp` command to copy the installation program `        .tar.gz` file to an AWS EC2 instance with a private key (replace the placeholder `        &lt;&gt;` values with your actual information):


```
scp -i &lt;path_to_private_key&gt; ansible-automation-platform-containerized-setup-&lt;version_number&gt;.tar.gz ec2-user@&lt;remote_host_ip_or_hostname&gt;:&lt;path_to_destination&gt;
```



1. Decide where you want the installation program to reside on the file system. This is referred to as your installation directory.


1. Installation related files are created under this location and require at least 15 GB for the initial installation.

1. Unpack the installation program `    .tar.gz` file into your installation directory, and go to the unpacked directory.


1. To unpack the online installer:


```
$ tar xfvz ansible-automation-platform-containerized-setup-&lt;version_number&gt;.tar.gz
```


1. To unpack the offline or bundled installer:


```
$ tar xfvz ansible-automation-platform-containerized-setup-bundle-&lt;version_number&gt;-&lt;arch_name&gt;.tar.gz
```





**Additional resources**

-  [scp(1) - Linux manual page](https://man7.org/linux/man-pages/man1/scp.1.html)


