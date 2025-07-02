# Chapter 2. Credentials




You can use credentials to store secrets that can be used for authentication purposes with resources, such as decision environments, rulebook activations and projects for Event-Driven Ansible controller, and projects for automation controller.

Credentials authenticate users when launching jobs against machines and importing project content from a version control system.

You can grant users and teams the ability to use these credentials without exposing the credential to the user. If a user moves to a different team or leaves the organization, you do not have to rekey all of your systems just because that credential was previously available.

Note
In the context of automation controller and Event-Driven Ansible controller, you can use both `extra_vars` and credentials to store a variety of information. However, credentials are the preferred method of storing sensitive information such as passwords or API keys because they offer better security and centralized management, whereas `extra_vars` are more suitable for passing dynamic, non-sensitive data.



