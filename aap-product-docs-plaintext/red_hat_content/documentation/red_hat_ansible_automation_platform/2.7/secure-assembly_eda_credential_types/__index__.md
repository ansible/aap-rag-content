# Connect to external secret management systems with built-in credentials

Event-Driven Ansible controller includes built-in credentials to sync projects, run rulebooks, execute job templates, fetch container images, and process data through event streams.

These built-in credential types are not editable. So if you want credential types that support authentication with other systems, you can create your own credential types that can be used in your source plugins. Each credential type contains an input configuration and an injector configuration that can be passed to an Ansible rulebook to configure your sources. For more information, see Create custom credentials for Event-Driven Ansible.

If you will be executing job templates through automation controller, you can retrieve credential values from external secret management systems listed in External secret management credential types.

