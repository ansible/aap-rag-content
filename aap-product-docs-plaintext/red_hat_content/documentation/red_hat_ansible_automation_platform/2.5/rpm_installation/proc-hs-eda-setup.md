# 4. Horizontal Scaling in Red Hat Ansible Automation Platform
## 4.1. Horizontal scaling in Event-Driven Ansible controller
### 4.1.2. Setting up horizontal scaling for Event-Driven Ansible controller




To scale up (add more nodes) or scale down (remove nodes), you must update the content of the inventory file to add or remove nodes and rerun the installation program.

**Procedure**

1. Update the inventory to add two more worker nodes:


```
[automationedacontroller]        3.88.116.111 routable_hostname=automationedacontroller-api.example.com eda_node_type=api        3.88.116.112 routable_hostname=automationedacontroller-api.example.com eda_node_type=worker        # two more worker nodes    3.88.116.113 routable_hostname=automationedacontroller-api.example.com eda_node_type=worker        3.88.116.114 routable_hostname=automationedacontroller-api.example.com eda_node_type=worker
```


1. Re-run the installer.


