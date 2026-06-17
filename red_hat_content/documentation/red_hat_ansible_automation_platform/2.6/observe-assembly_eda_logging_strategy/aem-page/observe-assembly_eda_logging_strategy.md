+++
template = "docs/aem-title.html"
title = "Configure logging for Event-Driven Ansible - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-assembly_eda_logging_strategy"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-assembly_eda_logging_strategy/", "Configure logging for Event-Driven Ansible"]]
category = "Observe"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-assembly_eda_logging_strategy/aem-page/observe-assembly_eda_logging_strategy.html"
last_crumb = "Configure logging for Event-Driven Ansible"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure logging for Event-Driven Ansible"
oversized = "false"
page_slug = "observe-assembly_eda_logging_strategy"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/observe-assembly_eda_logging_strategy"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-assembly_eda_logging_strategy/toc/toc.json"
type = "aem-page"
+++

# Configure logging for Event-Driven Ansible

Event-Driven Ansible offers an audit logging solution over its resources. Each supported create, read, update and delete (CRUD) operation is logged against rulebook activations, event streams, decision environments, projects, and activations.

Some of these resources support further operations, such as sync, enable, disable, restart, start, and stop; for these operations, logging is supported as well. These logs are only retained for the life cycle of its associated container.

See the following sample logs for each supported logging operation.

## Log samples

Review logging samples for various API operations (CRUD, sync, and the like) to understand the expected audit format and efficiently monitor resource changes.

Rulebook activation
```
1. Create
    1. 2024-08-15 14:13:20,384 aap_eda.api.views.activation INFO   Action: Create / ResourceType: RulebookActivation / ResourceName: quick_start_project / ResourceID: 53 / Organization: Default
2. Read
    1. 2024-08-15 14:21:26,844 aap_eda.api.views.activation INFO   Action: Read / ResourceType: RulebookActivation / ResourceName: quick_start_activation / ResourceID: 1 / Organization: Default
3. Disable
    1. 2024-08-15 14:23:57,798 aap_eda.api.views.activation INFO   Action: Disable / ResourceType: RulebookActivation / ResourceName: quick_start_activation / ResourceID: 1 / Organization: Default
4. Enable
    1. 2024-08-15 14:24:16,472 aap_eda.api.views.activation INFO   Action: Enable / ResourceType: RulebookActivation / ResourceName: quick_start_activation / ResourceID: 1 / Organization: Default
5. Delete
    1. 2024-08-15 14:24:53,847 aap_eda.api.views.activation INFO   Action: Delete / ResourceType: RulebookActivation / ResourceName: quick_start_activation / ResourceID: 1 / Organization: Default
6. Restart
    2024-08-15 14:24:34,169 aap_eda.api.views.activation INFO      Action: Restart / ResourceType: RulebookActivation / ResourceName: quick_start_activation / ResourceID: 1 / Organization: Default
```

EventStream Logs
```
1. Create
    1. 2024-08-15 13:46:26,903 aap_eda.api.views.webhook INFO     Action: Create / ResourceType: EventStream / ResourceName: ZackTest / ResourceID: 1 / Organization: Default
2. Update
    1. 2024-08-15 13:56:17,440 aap_eda.api.views.webhook INFO     Action: Update / ResourceType: EventStream / ResourceName: ZackTest / ResourceID: 1 / Organization: Default
3. Read
    1. 2024-08-15 13:56:56,271 aap_eda.api.views.webhook INFO     Action: Read / ResourceType: EventStream / ResourceName: ZackTest / ResourceID: 1 / Organization: Default
4. List
    1. 2024-08-15 13:56:17,492 aap_eda.api.views.webhook INFO     Action: List / ResourceType: EventStream / ResourceName: * / ResourceID: * / Organization: *
5. Delete
    1. 2024-08-15 13:57:13,124 aap_eda.api.views.webhook INFO     Action: Delete / ResourceType: EventStream / ResourceName: ZackTest / ResourceID: None / Organization: Default
```

Decision Environment
```
1. Create
    1. 2024-08-15 14:10:53,311 aap_eda.api.views.decision_environment INFO     Action: Create / ResourceType: DecisionEnvironment / ResourceName: quick_start_de / ResourceID: 86 / Organization: Default
2. Read
    1. 2024-08-15 14:10:53,349 aap_eda.api.views.decision_environment INFO     Action: Read / ResourceType: DecisionEnvironment / ResourceName: quick_start_de / ResourceID: 86 / Organization: Default
3. Update
    2024-08-15 14:11:20,970 aap_eda.api.views.decision_environment INFO     Action: Update / ResourceType: DecisionEnvironment / ResourceName: quick_start_de / ResourceID: 86 / Organization: Default
4. Delete
2024-08-15 14:11:42,369 aap_eda.api.views.decision_environment INFO     Action: Delete / ResourceType: DecisionEnvironment / ResourceName: quick_start_de / ResourceID: None / Organization: Default
```

Project
```
1. Create
    1. 2024-08-15 14:05:26,874 aap_eda.api.views.project INFO     Action: Create / ResourceType: Project / ResourceName: quick_start_project / ResourceID: 86 / Organization: Default
2. Read
    1. 2024-08-15 14:05:26,913 aap_eda.api.views.project INFO     Action: Read / ResourceType: Project / ResourceName: quick_start_project / ResourceID: 86 / Organization: Default
3. Update
    1. 2024-08-15 14:06:08,255 aap_eda.api.views.project INFO     Action: Update / ResourceType: Project / ResourceName: quick_start_project / ResourceID: 86 / Organization: Default
4. Sync
    1. 2024-08-15 14:06:30,580 aap_eda.api.views.project INFO     Action: Sync / ResourceType: Project / ResourceName: quick_start_project / ResourceID: 86 / Organization: Default
5. Delete
    1. 2024-08-15 14:06:49,481 aap_eda.api.views.project INFO     Action: Delete / ResourceType: Project / ResourceName: quick_start_project / ResourceID: 86 / Organization: Default
```

Activation Start/Stop
```
1. Start
    1. 2024-08-15 14:21:29,076 aap_eda.services.activation.activation_manager INFO     Requested to start activation 1, starting.
    2024-08-15 14:21:29,093 aap_eda.services.activation.activation_manager INFO     Creating a new activation instance for activation: 1
    2024-08-15 14:21:29,104 aap_eda.services.activation.activation_manager INFO     Starting container for activation instance: 1
2. Stop
    1. eda-activation-worker-1  | 2024-08-15 14:40:52,547 aap_eda.services.activation.activation_manager INFO     Stop operation requested for activation id: 2 Stopping activation.
    eda-activation-worker-1  | 2024-08-15 14:40:52,550 aap_eda.services.activation.activation_manager INFO     Activation 2 is already stopped.
    eda-activation-worker-1  | 2024-08-15 14:40:52,550 aap_eda.services.activation.activation_manager INFO     Activation manager activation id: 2 Activation restart scheduled for 1 second.
    eda-activation-worker-1  | 2024-08-15 14:40:52,562 rq.worker INFO     activation: Job OK (activation-2)
```
