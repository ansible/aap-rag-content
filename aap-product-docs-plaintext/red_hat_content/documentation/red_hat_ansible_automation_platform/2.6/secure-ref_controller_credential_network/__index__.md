# Network credential type

You can create Network credential types in automation controller to manage network devices that use Ansible networking modules.

Note:

Select the Network credential type if you are using a *local* connection with *provider* to use Ansible networking modules to connect to and manage networking devices.

If you assign both a Machine credential and a Network credential to the same job template, automation controller injects them independently. The Machine credential controls SSH authentication, while the Network credential sets the `ANSIBLE_NET_USERNAME` and `ANSIBLE_NET_PASSWORD` environment variables.

- For `local` connections using `provider`, credential type should be **Network**.

- For all other network connections (`httpapi`, `netconf`, and `network_cli`), the credential type should be **Machine**. For more information about connection types available for network devices, see [Multiple Communication Protocols](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-multiple-connection-protocols).

For information on combining credential types, see [Using Machine and Network credentials together](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-ref_controller_credential_network#GUID-3c4a0885-148a-4476-8996-4b04997a5f9b "You can assign both Machine and Network credentials to a single job template to manage network devices that require multi-hop SSH access, such as connecting through a jumphost.").

Automation controller uses the following environment variables for Network credentials:



```
ANSIBLE_NET_USERNAME
ANSIBLE_NET_PASSWORD
```

Provide the following information for network credentials:

- **Username**: The username to use in conjunction with the network device.
- **Password**: The password to use in conjunction with the network device.
- **SSH Private Key**: Copy or drag-and-drop the actual SSH Private Key to be used to authenticate the user to the network through SSH.
- **Private Key Passphrase**: The passphrase for the private key to authenticate the user to the network through SSH.
- **Authorize**: Select this to control whether or not to enter privileged mode.   * If **Authorize** is checked, enter a password in the **Authorize Password** field to access privileged mode. For more information, see [Porting Ansible Network Playbooks with New Connection Plugins](https://www.ansible.com/blog/porting-ansible-network-playbooks-with-new-connection-plugins).

## Access network credentials in an Ansible Playbook

When using the **Controller Access Network Credentials** credential type, you can access the username and password parameters in your Ansible Playbook by using the following environment variables:

-  `ANSIBLE_NET_USERNAME`
-  `ANSIBLE_NET_PASSWORD`


You can get the username and password parameters from a job runtime environment:

```
vars:
network:
username: '{{ lookup("env", "ANSIBLE_NET_USERNAME") }}'
password: '{{ lookup("env", "ANSIBLE_NET_PASSWORD") }}'
```

## Multiple communication protocols

Ansible network modules can communicate with network devices by using different protocols.

Because network modules run on the control node instead of on the managed nodes, they can support multiple communication protocols. The communication protocols (XML over SSH, CLI over SSH, or API over HTTPS) selected for each network module depend on the platform and the purpose of the module. Some network modules support only one protocol, while some offer a choice.

The most common protocol is CLI over SSH. You set the communication protocol with the ansible_connection variable:

| Value of ansible\_connection         | Protocol                | Requires                | Persistent? |
| ------------------------------------ | ----------------------- | ----------------------- | ----------- |
| <br> `ansible.netcommon.network_cli` | <br>CLI over SSH        | <br>network\_os setting | <br>yes     |
| <br> `ansible.netcommon.netconf`     | <br>XML over SSH        | <br>network\_os setting | <br>yes     |
| <br> `ansible.netcommon.httpapi`     | <br>API over HTTP/HTTPS | <br>network\_os setting | <br>yes     |
| <br> `local`                         | <br>depends on provider | <br>provider setting    | <br>no      |


The `ansible_connection: local` is deprecated. Use one of the persistent connection types listed above instead. With persistent connections, you can define the hosts and credentials only once, rather than in every task. You must also set the `network_os` variable for the specific network platform you are communicating with.

## Using Machine and Network credentials together

You can assign both Machine and Network credentials to a single job template to manage network devices that require multi-hop SSH access, such as connecting through a jumphost.

### About this task

When you assign multiple credential types to a job template, {ControllerName} injects each credential into the job environment differently:

- **Machine credentials** set the SSH username, password, and key used by Ansible Automation Platform to connect to hosts. These values are passed through the `ansible -u` flag and SSH authentication.
- **Network credentials** set the `ANSIBLE_NET_USERNAME` and `ANSIBLE_NET_PASSWORD` environment variables, which Ansible Automation Platform networking modules use to authenticate to network devices.


Note:

The credential type must match the connection type used by the network device:

- For `local` connections using `provider`, use the **Network** credential type
- For `httpapi`, `netconf`, and `network_cli` connections, use the **Machine** credential type, not the Network credential type.

**Prerequisites**

- You have created a Machine credential for the jumphost or bastion host.
- You have created a Network credential for the target network device (if using `local` connection with `provider`), or a second Machine credential (if using `network_cli`, `netconf`, or `httpapi`).
- Your inventory is configured with appropriate connection variables, such as `ansible_ssh_common_args` for ProxyCommand settings

### Procedure

1.  From the navigation panel, select Automation execution> (and then)Templates.
2.  Create or edit a job template.
3.  In the **Credentials** field, select the ![Search icon](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/search.png) icon.
4.  Add the **Machine** credential for the jumphost.
5.  Add the **Network** credential for the network device (or a second Machine credential, depending on your connection type).
6.  Configure your inventory or playbook variables with the appropriate SSH proxy settings. For example, to use a jumphost with ProxyCommand:
`ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q user@gateway.example.com"`

7.  Click Save and then Launch template.

### What to do next

**Verification**

Review the job output to confirm that both credentials were injected and the playbook successfully authenticated to the target network devices through the jumphost.
