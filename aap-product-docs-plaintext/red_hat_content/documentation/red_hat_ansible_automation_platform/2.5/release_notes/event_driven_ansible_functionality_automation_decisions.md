# 2. New features and enhancements
## 2.4. Event-Driven Ansible functionality (Automation decisions)




With Ansible Automation Platform 2.5, Event-Driven Ansible functionality has been enhanced with the following features:

- Enterprise single-sign on and role-based access control are available through a new Ansible Automation Platform UI, which enables a single point of authentication and access to all functional components as follows:


- Automation Execution (automation controller)
- Automation Decision (Event-Driven Ansible)
- Automation Content (automation hub)
- Automation Analytics
- Access Management
- Red Hat Ansible Lightspeed

- Simplified event routing capabilities introduce event streams. Event streams are an easy way to connect your sources to your rulebooks. This new capability lets you create a single endpoint to receive alerts from an event source and then use the events in multiple rulebooks. This simplifies rulebook activation setup, reduces maintenance demands, and helps lower risk by eliminating the need for additional ports to be open to external traffic.
- Event-Driven Ansible in the Ansible Automation Platform 2.5 now supports horizontal scaling, allowing you to install multiple Event-Driven Ansible nodes to handle increased event volume.
- Migration to the new platform-wide Red Hat Ansible Automation Platform credential type replaces the legacy controller token for enabling rulebook activations to call jobs in the automation controller.
- Event-Driven Ansible now has the ability to manage credentials that can be added to rulebook activations. These credentials can be used in rulebooks to authenticate to event sources. In addition, you can now attach vault credentials to rulebook activations so that you can use vaulted variables in rulebooks. Encrypted credentials and vaulted variables enable enterprises to secure the use of Event-Driven Ansible within their environment.
- New modules are added to the **ansible.eda** collection to enable users to automate the configuration of the Event-Driven Ansible controller using Ansible playbooks.


