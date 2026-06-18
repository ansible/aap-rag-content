# Prepare the managed nodes

Managed nodes, or hosts, are the devices managed by Ansible Automation Platform. To ensure a secure containerized setup, create a dedicated user on each node for Ansible Automation Platform to use when connecting and running tasks.

## Procedure

1.  Log in to the host as the root user.
2.  Create a new user. Replace `<username>` with the username you want, for example `aap`.

```
$ sudo adduser <username>
```

3.  Set a password for the new user. Replace `<username>` with the username you created.

```
$ sudo passwd <username>
```

4.  Configure the user to run `sudo` commands. For a secure and maintainable installation, configure `sudo` privileges for the installation user in a dedicated file within the `/etc/sudoers.d/` directory.

1.  Create a dedicated `sudoers` file for the user:


```
$ sudo visudo -f /etc/sudoers.d/<username>
```

2.  Add the following line to the file, replacing `<username>` with the username you created:


```
<username> ALL=(ALL) NOPASSWD: ALL
```

3.  Save and exit the file.
