# Improve the security of nodes managed by Ansible Automation Platform
## Configure sudo privileges for service account

The service account requires sufficient privileges to run any current or future automation job on the managed node. This section describes the use of `sudo`, though other privilege escalation methods are available.

### About this task

Since Ansible Automation Platform defaults to using the `ansible.builtin.sudo`[become plugin](https://docs.ansible.com/projects/ansible/latest/plugins/become.html) on Linux-based managed nodes, the service account must be permitted to run any command on the RHEL managed node using the sudo command.

To configure this, use the following procedure:

### Procedure

1.  Create the file `/etc/sudoers.d/ansible`, and include the following content:


```
# Rules for the ansible service account
ansible ALL=(ALL) NOPASSWD: ALL
```

2.  Set restrictive permissions on the file:
`` sudo chmod 0440 /etc/sudoers.d/ansible` ``

3.  Verify the file uses the proper syntax:
`sudo visudo -cf /etc/sudoers.d/ansible`

