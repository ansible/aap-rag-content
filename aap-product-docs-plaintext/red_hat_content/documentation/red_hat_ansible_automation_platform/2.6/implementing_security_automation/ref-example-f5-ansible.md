# 4. Event-Driven Ansible for reacting to security-related events
## 4.3. Example using F5 and Event-Driven Ansible




Example code using F5 and Event-Driven Ansible is available on GitHub. This code notes each instance of the watcher finding a match in its filter and then copies the source IP from that code into a CSV list. The list is then sent as a variable within the webhook along with the message to execute the code.

This high level workflow is described in the following diagram and code workflow example:

+![F5 and Ansible workflow](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Implementing_security_automation-en-US/images/0bc4a618b9b07c2e16efe7d2f5db38e5/f5-and-ansible.png)


The workflow steps are:

1. The F5 BIG-IP pushes the monitoring logs to Elastic.
1. Elastic takes that data and stores it while using a watcher with its filters and criteria.
1. The Watcher detects an event that matches its criteria and sends the webhook with payload to Event-Driven Ansible.
1. Event-Driven Ansible’s rulebook triggers from the event which triggers a job template within Ansible Automation Platform, that sends the payload provided by Elastic.
1. Ansible Automation Platform’s template executes a playbook to secure the F5 BIG-IP using the payload provided by Event-Driven Ansible (originally provided by Elastic).


