# Improve the security of nodes managed by Ansible Automation Platform

Ansible Automation Platform is an agentless technology that relies on making a remote connection to the devices it manages, called managed nodes, to run automation tasks.

Note:

Managed node configuration can vary significantly based on factors such as operating system, compliance profiles, configuration, and organizational policies.

Any recommendations on managed node configuration presented here must be thoroughly tested and reviewed before implementation to ensure that they meet organizational policies and requirements.

## Red Hat Enterprise Linux managed node configuration

The following section provides guidance for *Red Hat Enterprise Linux* (RHEL) managed nodes, but the concepts may be applicable to other Linux distributions as well.

Examples are provided for manual configuration of RHEL managed nodes. These steps can also be automated with Ansible Automation Platform, or they can be added to a *Standard Operating Environment* (SOE) or "golden image" created with a tool such as the Red Hat Lightspeed image builder.

## Create a dedicated service account with access limits

Ansible Automation Platform can be configured to use various users or accounts for connecting to managed nodes.

Create a single, dedicated service account for this purpose. This service account must be a local account on each managed node to ensure automation jobs continue to run, even if an external authentication mechanism experiences an outage. This recommendation applies unless organizational policy mandates centrally managed service accounts. The service account must be clearly named to indicate its purpose, for instance, `ansible` or `aapsvc`.

"Ansible" is used here as the assumed name for a local service account in the examples.

The local service account is configured as follows:

- It is granted sufficient privileges to run any automation job required.
- It is limited to SSH key authentication only. No password authentication is allowed.
- Access is only granted to connections made from the Ansible Automation Platform {ControllerNames}s and execution nodes. Note:
To execute tasks in an Ansible playbook or job template as a user other than the service account, use the `become` and `become_user` keywords. Connecting to the managed node as a different user is not necessary.

- The `useradd` command can be used to create a local service account. For example:

```
sudo useradd ansible \
--system --create-home \
--comment "Ansible Automation Platform service account"
```

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

## Require SSH key authentication for service account

The service account must not be permitted to use password authentication with SSH connections to the managed node.

### About this task

Given that password authentication is prohibited, at least one SSH public key must be appended to the service account’s authorized_keys file (typically located at `/home/ansible/.ssh/authorized_keys`).

These public keys must correspond with the private keys used to establish Machine credentials in Ansible Automation Platform, as these credentials facilitate connections to the RHEL managed nodes.

This section advocates for a single service account for connections to managed RHEL nodes, but this does not mean using a single SSH key across all nodes is required. In larger organizations, individual teams managing RHEL servers can generate their own machine credentials within Ansible Automation Platform. Teams can then add the corresponding keys to the authorized keys file on their specific RHEL servers. This approach ensures consistent access to managed nodes organization-wide by using a common service account, while enabling each team to independently manage the credentials for their assigned nodes.

Use the following procedure to configure the SSH daemon:

### Procedure

1.  Create the file `/etc/sshd/sshd_config.d/60-ansible.conf`, and include the following content:


```
# sshd config applied to the ansible service account
Match User ansible
PasswordAuthentication no
Match all
```

2.  Verify that the file uses the proper syntax:
`sudo sshd -t`

3.  Restart the SSH daemon
`sudo systemctl restart sshd.service`

## Enable and configure pam_access controls for service accounts

To restrict remote login access to connections originating from the Ansible Automation Platform automation controller and execution nodes and ensure the service account is exclusively used by Ansible Automation Platform, use the following procedure:

### Procedure

1.  Use the FQDNs of your automation controller and execution nodes to add the following content to the `/etc/security/access.conf` file, using the FQDNs of your controller nodes and execution nodes:


```
# allow the ansible service account to log in from local sources and
# the hybrid controller or execution nodes, and deny all other sources
+:ansible:LOCAL controller1.example.com controller2.example.com en1.example.com
-:ansible:ALL
```

2.  Enable the `with-pamaccess` feature in the current authselect profile. All authselect profiles included by default with RHEL have this feature.  `sudo authselect enable-feature with-pamaccess`
