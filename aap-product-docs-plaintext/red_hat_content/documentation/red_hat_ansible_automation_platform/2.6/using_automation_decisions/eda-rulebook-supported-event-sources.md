# 7. Rulebook activations
## 7.1. Supported event sources




Event sources are a fundamental component of Event-Driven Ansible because they determine where a rulebook can receive events from. The effectiveness of a rulebook activation depends on selecting an event source that is compatible with your automation environment. Certain event sources are designed for use with the web-based Event-Driven Ansible controller, while others, due to their reliance on local host functionality, are exclusive to the `ansible-rulebook` command-line interface (CLI). Understanding this distinction is crucial for successful rulebook activations.

The following list includes currently supported event sources for use with the web-based Event-Driven Ansible controller. You can decide which event sources provide the desired outcome for your rulebook activations.

-  `    alertmanager`
-  `    aws_cloudtrail`
-  `    aws_sqs_queue`
-  `    azure_service_bus`
-  `    kafka`
-  `    pg_listener`
-  `    webhook`


