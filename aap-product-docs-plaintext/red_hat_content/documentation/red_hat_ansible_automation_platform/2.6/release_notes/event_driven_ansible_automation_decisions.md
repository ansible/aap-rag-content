# 2. New features and enhancements
## 2.6. Event-Driven Ansible (Automation decisions)




Event-Driven Ansible includes several key enhancements in the Ansible Automation Platform 2.6 release that improve performance, simplify operations, and expand the platform’s capabilities across security, networking, and event processing.

-  **External secret management** : Event-Driven Ansible now supports external secret management systems, achieving parity with Automation controller. This includes support for HashiCorp Vault, CyberArk, Microsoft Azure Key Vault, and AWS Secrets Manager.
-  **Editable project URLs** : You can now edit the source control URL for existing Event-Driven Ansible projects, providing greater flexibility to adapt to repository changes.
-  **Improved job auditing** : A new label is automatically added to jobs triggered by Event-Driven Ansible, along with support for custom labels. This allows for more efficient tracing and auditing of event-triggered automations.
-  **Kafka enhancements** : The Kafka source plugin now supports multiple topics and allows the use of regular expressions and wildcards. Additionally, it now supports GSSAPI for enhanced authentication.
-  **New event filter** : A new filter plugin, `    event_splitter` , is available to handle and process nested events more effectively.
-  **Rulebook concurrency key** : Rulebooks now support a concurrency key, enabling you to group events by resource to ensure they are processed sequentially.


