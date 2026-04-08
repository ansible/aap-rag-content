# 2. System requirements
## 2.4. Automation controller system requirements




Automation controller is a distributed system, where different software components can be co-located or deployed across many compute nodes. The installation program provides four node types as abstractions to help you design the topology appropriate for your use case: control, hybrid, execution, and hop nodes.

Use the following recommendations for node sizing:


<span id="idm140368655054288"></span>
**Table 2.3. Recommended Resource Sizing for Automation controller Node Types**

| Node Type | RAM (Minimum) | vCPU (Minimum) | Disk IOPS (Minimum) | Storage and Notes |
| --- | --- | --- | --- | --- |
|  **Execution Node** | 16 GB | 4 vCPU | 3000 | Runs automation. Increase RAM/CPU to increase capacity for concurrent job **forks** . Performance depends heavily on the number of jobs run simultaneously. |
|  **Control Node** | 16 GB | 4 vCPU | 3000 | Processes events and runs cluster jobs (e.g., project updates). * **Storage:** 80GB minimum, with at least 20GB available under `/var/lib/awx` . * **Storage Requirement:** Volume must be rated for a minimum baseline of 3000 IOPS. |
|  **Hybrid Node** | 16 GB | 4 vCPU | 3000 | A combination of Control and Execution node functions. Storage requirements generally match the Control Node. |
|  **Hop Node** | 16 GB | 4 vCPU | 3000 | Routes traffic within the automation mesh (e.g., bastion host). RAM can affect throughput, but CPU activity is typically low. Network latency is a more important factor than RAM or CPU. |




- Actual RAM requirements vary based on how many hosts automation controller manages simultaneously (which is controlled by the `    forks` parameter in the job template or the system `    ansible.cfg` file). To avoid possible resource conflicts, Ansible recommends 1 GB of memory per 10 forks and 2 GB reservation for automation controller. See [Automation controller capacity determination and job impact](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/controller-jobs#controller-capacity-determination) . If `    forks` is set to 400, 42 GB of memory is recommended.
- A larger number of hosts can be addressed, but if the fork number is less than the total host count, more passes across the hosts are required. You can avoid these RAM limitations by using any of the following approaches:


- Use rolling updates.
- Use the provisioning callback system built into automation controller, where each system requesting configuration enters a queue and is processed as quickly as possible.
- In cases where automation controller is producing or deploying images such as AMIs.



**Additional resources**

-  [Attaching your Red Hat Ansible Automation Platform subscription](https://access.redhat.com/articles/5807761)
-  [Red Hat Customer Portal](https://access.redhat.com/)


