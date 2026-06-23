# Network credential type

You can create Network credential types in automation controller to manage network devices that use Ansible networking modules.

Note:

Select the Network credential type if you are using a *local* connection with *provider* to use Ansible networking modules to connect to and manage networking devices.

If you assign both a Machine credential and a Network credential to the same job template, automation controller injects them independently. The Machine credential controls SSH authentication, while the Network credential sets the `ANSIBLE_NET_USERNAME` and `ANSIBLE_NET_PASSWORD` environment variables.

- For `local` connections using `provider`, credential type should be **Network**.

- For all other network connections (`httpapi`, `netconf`, and `network_cli`), the credential type should be **Machine**. For more information about connection types available for network devices, see [Multiple Communication Protocols](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-multiple-connection-protocols).

For information on combining credential types, see [Using Machine and Network credentials together](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_network#GUID-3c4a0885-148a-4476-8996-4b04997a5f9b "You can assign both Machine and Network credentials to a single job template to manage network devices that require multi-hop SSH access, such as connecting through a jumphost.").

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

