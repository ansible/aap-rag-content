# Network credential type
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

