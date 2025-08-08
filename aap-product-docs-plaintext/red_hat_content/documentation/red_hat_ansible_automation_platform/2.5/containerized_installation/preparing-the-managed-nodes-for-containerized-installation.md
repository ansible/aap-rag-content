# 2. Ansible Automation Platform containerized installation
## 2.4. Preparing the managed nodes for containerized installation




Managed nodes, also referred to as hosts, are the devices that Ansible Automation Platform is configured to manage.

To ensure a consistent and secure setup of containerized Ansible Automation Platform, create a dedicated user on each host. Ansible Automation Platform connects as this user to run tasks on the host.

Once configured, you can define the dedicated user for each host by adding `ansible_user=&lt;username&gt;` in your inventory file, for example: `aap.example.org ansible_user=aap` .

Complete the following steps for each host:

**Procedure**

1. Log in to the host as the root user.
1. Create a new user. Replace `    &lt;username&gt;` with the username you want, for example `    aap` .


```
$ adduser &lt;username&gt;
```


1. Set a password for the new user. Replace `    &lt;username&gt;` with the username you created.


```
$ passwd &lt;username&gt;
```


1. Configure the user to run sudo commands.


1. To do this open the sudoers file:


```
$ vi /etc/sudoers
```


1. Add the following line to the file (replacing `        &lt;username&gt;` with the username you created):


```
&lt;username&gt; ALL=(ALL) NOPASSWD: ALL
```


1. Save and exit the file.



