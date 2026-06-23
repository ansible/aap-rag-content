# Horizontally scale in Event-Driven Ansible
## Horizontal scaling in Event-Driven Ansible controller

With Event-Driven Ansible controller, you can set up horizontal scaling for events automation. This multi-node deployment allows you to define as many nodes as preferred during installation. You can also increase or decrease the node count at any time to meet organizational needs.

The following node types are used in this deployment:

API node type
Responds to the HTTP REST API of Event-Driven Ansible controller.

Worker node type
Runs an Event-Driven Ansible worker, which is the component of Event-Driven Ansible that not only manages projects and activations, but also executes the activations themselves.

Hybrid node type
Is a combination of the API node and the worker node.

