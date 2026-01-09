# 8. About the installation program inventory file
## 8.3. Inventory variables




Inventory variables control the installation program’s behavior and configure Ansible Automation Platform components during deployment. Understand how to apply variables globally or to specific hosts to customize your installation.

The second part of the example inventory file, following `[all:vars]` , is a list of variables used by the installation program. Using `all` means the variables apply to all hosts.

To apply variables to a particular host, use `[hostname:vars]` . For example, `[automationhub:vars]` .

