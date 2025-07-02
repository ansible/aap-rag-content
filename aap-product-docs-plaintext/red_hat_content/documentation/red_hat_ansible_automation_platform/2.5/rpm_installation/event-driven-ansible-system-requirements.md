# 2. System requirements
## 2.5. Event-Driven Ansible controller system requirements




The Event-Driven Ansible controller is a single-node system capable of handling a variable number of long-running processes (such as rulebook activations) on-demand, depending on the number of CPU cores.

Note
If you want to use Event-Driven Ansible 2.5 with a 2.4 automation controller version, see [Using Event-Driven Ansible 2.5 with Ansible Automation Platform 2.4](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html-single/using_event-driven_ansible_2.5_with_ansible_automation_platform_2.4/index) .



Use the following minimum requirements to run, by default, a maximum of 12 simultaneous activations:

| Requirement | Required |
| --- | --- |
|  **RAM** | 16 GB |
|  **CPUs** | 4 |
|  **Local disk** | - Hard drive must be 40 GB minimum with at least 20 GB available under /var.
- Storage volume must be rated for a minimum baseline of 3000 IOPS.
- If the cluster has many large projects or decision environment images, consider doubling the GB in /var to avoid disk space errors. |


Important
- If you are running Red Hat Enterprise Linux 8 and want to set your memory limits, you must have cgroup v2 enabled before you install Event-Driven Ansible. For specific instructions, see the Knowledge-Centered Support (KCS) article, [Ansible Automation Platform Event-Driven Ansible controller for Red Hat Enterprise Linux 8 requires cgroupv2](https://access.redhat.com/solutions/7054905) .
- When you activate an Event-Driven Ansible rulebook under standard conditions, it uses about 250 MB of memory. However, the actual memory consumption can vary significantly based on the complexity of your rules and the volume and size of the events processed. In scenarios where a large number of events are anticipated or the rulebook complexity is high, conduct a preliminary assessment of resource usage in a staging environment. This ensures that your maximum number of activations is based on the capacity of your resources.


For an example of setting Event-Driven Ansible controller maximumrunning activations, see [Single automation controller, single automation hub, and single Event-Driven Ansible controller node with external (installer managed) database](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_installation/index#ref-gateway-controller-hub-eda-ext-db) .



