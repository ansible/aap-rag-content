# New features and enhancements
## Event-Driven Ansible ansible.eda and ansible-rulebook changes

- New ansible-rulebook built-in modules The following event sources and event filters will be available as built-in modules in 'ansible-rulebook', and removed from 'ansible.collection'.


The following is the list of new built-in modules:

'eda.builtin.dashes_to_underscores'(filter) 'eda.builtin.generic'(source) 'eda.builtin.insert_hosts_to_meta'(filter) 'eda.builtin.json_filter'(filter) 'eda.builtin.normalize_keys'(filter) 'eda.builtin.pg_listener'(source) 'eda.builtin.range'(source) 'eda.builtin.webhook'(source)

For backwards compatibility, these plugins remain available in the ansible.eda namespace and are automatically mapped to eda.builtin. However, they are no longer actively maintained in the ansible.eda collection. If you currently have rulebooks that use these filters or sources, update your rulebooks to use the eda.builtin namespace instead of the ansible.eda namespace.

AWS and Azure event sources movement to the cloud collections The following list of event sources is being deprecated in ansible.eda collection and moving to the corresponding certified cloud collections. The DE-supported decision environments have been updated to incorporate amazon.aws and azure.azcollection. If you update the DE-supported decision environment, make sure to update your ansible-rulebooks namespace to refer to the updated namespace as mentioned below:

'ansible.eda.aws_cloudtrail to amazon.aws.aws_cloudtrail' 'ansible.eda.aws_sqs_queue to amazon.aws.aws_sqs_queue' 'ansible.eda.azure_service_bus' 'azure.azcollection.azure_service_bus'

