# 9. Patch releases
## 9.1. Ansible Automation Platform patch release May 4, 2026
### 9.1.5. Bug fixes

#### 9.1.5.1. Ansible Automation Platform gateway

- Fixed an issue where organization administrators could not view, modify, or remove permissions on teams outside of their organization.(AAP-72502)

#### 9.1.5.2. Automation hub

- Fixed an issue where the Automation Hub OpenAPI specification was missing service_index endpoints.(AAP-72227)
- Fixed an issue where artifact download view counting could return an error instead of correctly using name/namespace.(AAP-71346)

#### 9.1.5.3. Red Hat Lightspeed

- Fixed an issue where the containerized Red Hat Lightspeed install did not correctly configure the Azure OpenAI provider base URL for Llama Stack 0.4.3.(AAP-72046)
- Fixed an issue where the containerized Red Hat Lightspeed install did not correctly configure the Azure OpenAI provider base URL for Llama Stack 0.4.3.(AAP-71979)
- Fixed an issue where the /api/lightspeed/v1/ai/chat endpoint response schema could deviate from the documented API specification.(AAP-70666)
- Fixed an issue where MCP-enabled prompts could fail due to max_tokens handling and provider defaults in lightspeed-stack-providers.(AAP-70396)
- Fixed an issue where the wisdom-manage shell command output was impacted by the Django 5.2 verbosity level change.(AAP-69164)
- Fixed an issue where ALIA/Lightspeed backups were abnormally large due to unnecessary files being included.(AAP-68774)
- Fixed an issue where ALIA/Lightspeed backups were abnormally large due to unnecessary files being included.(AAP-67911)

#### 9.1.5.4. Container-based installer Ansible Automation Platform

- Fixed an issue where component TLS certificates were not regenerated on certain CA certificate changes.(AAP-71956)
- Fixed an issue where the Redis hostname could fail to be set in disconnected containerized installer environments.(AAP-71493)
- Fixed an issue where the 2.6 bundle installer could fail when PCP was enabled with a metrics service host in inventory, by ensuring the PCP image is loaded on Automation Metrics nodes.(AAP-71026)

#### 9.1.5.5. Django ansible base

- Fixed an issue where a fresh installation could immediately show a “RoleDefinition matching query does not exist” error during resource sync.(AAP-71868)
- Fixed an issue where periodic resource sync between Controller and Gateway could delete valid role assignments when pagination failed mid-fetch.(AAP-71775)

#### 9.1.5.6. Content

- Fixed an issue where the ansible.controller collection job_template module did not support Bitbucket webhooks.(AAP-71827)

#### 9.1.5.7. Event-Driven Ansible

- Fixed an issue where projects could be deleted while a project sync was running.(AAP-71406)
- Fixed an issue where the EDA event-stream node tag in gateway config could be incorrect, causing routing issues to EDA event-stream.(AAP-69827)

#### 9.1.5.8. Automation controller

- Fixed an issue where nested workflows could apply incorrect variable precedence when set_stats artifacts were passed via extra_vars.(AAP-70756)
- Fixed an issue where object creation could be significantly slower in organizations with large numbers of resources, by reducing RoleEvaluation object creation overhead.(AAP-70752)
- Fixed an issue where inventory imports with large numbers of changes could take an excessive amount of time.(AAP-70377)
- Fixed an issue where concurrent jobs could incorrectly clear host facts due to a race condition.(AAP-69262)
- Fixed an issue where job cancellation did not reliably propagate to dependent jobs in workflows.(AAP-68975)
- Fixed an issue where project_update.yml could fail with a jinja2 error when using custom execution environment images with newer ansible-core versions.(AAP-68783)

#### 9.1.5.9. Ansible Automation Platform Operator

- Fixed an issue where the Gateway Operator stored database passwords unencrypted, by removing postgresql-init ConfigMap and switching to runtime-executed postgresql modules.(AAP-70404)
- Fixed an issue where Automation Hub backup ignored postgres_image and postgres_image_version, causing it to always use the default PostgreSQL image.(AAP-69856)
- Fixed an issue where operator event creation could fail with a time-parsing error that masked the underlying error message.(AAP-69634)
- Fixed an issue where CRD validation for _image and _image_version fields was missing for installer operators.(AAP-68765)
- Fixed an issue where users could not override nested restore parameters (including no_log) in AnsibleAutomationPlatformRestore.(AAP-68242)

#### 9.1.5.10. Ansible Automation Platform ui

- Fixed an issue where unthrottled WebSocket refresh events caused excessive Jobs list API requests, leading to queued requests and an unresponsive UI under high concurrency.(AAP-70349)
- Fixed an issue where the Assign Roles wizard did not correctly show “System” as a resource type when assigning custom roles.(AAP-67506)
- Fixed an issue where OAuth authorization could fail to redirect correctly after Keycloak SSO because the next parameter was not preserved.(AAP-59343)

#### 9.1.5.11. Receptor

- Fixed an issue where the work results command could emit misleading warnings during connection shutdown.(AAP-43847)

