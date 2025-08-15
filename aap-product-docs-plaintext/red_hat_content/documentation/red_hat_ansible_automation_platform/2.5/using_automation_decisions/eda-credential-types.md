# Chapter 3. Credential types




Event-Driven Ansible controller comes with several built-in credental types that you can use for syncing projects, running rulebook activations, executing job templates through Automation Execution (automation controller), fetching images from container registries, and processing data through event streams.

These built-in credential types are not editable. So if you want credential types that support authentication with other systems, you can create your own credential types that can be used in your source plugins. Each credential type contains an input configuration and an injector configuration that can be passed to an Ansible rulebook to configure your sources.

For more information, see [Custom credential types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-credential-types#eda-custom-credential-types) .

