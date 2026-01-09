# 7. Rulebook activations
## 7.1. Supported event sources




Event sources are the foundation of Event-Driven Ansible, as they define where your rulebooks receive incoming signals.

Selecting a compatible source is critical for successful deployment, as some are exclusive to the web-based Event-Driven Ansible controller and others only work with the `ansible-rulebook` command-line interface (CLI).

The following list includes event sources currently supported for use directly within the web-based Event-Driven Ansible controller:

-  `    alertmanager`
-  `    aws_cloudtrail`
-  `    aws_sqs_queue`
-  `    azure_service_bus`
-  `    kafka`
-  `    pg_listener`
-  `    webhook`


