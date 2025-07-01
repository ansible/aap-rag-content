# Chapter 6. Changed features




Changed features are not deprecated and will continue to be supported until further notice.

The following table provides information about features that are changed in Ansible Automation Platform 2.5:

| Component | Feature |
| --- | --- |
| Automation hub | Error codes are now changed from 403 to 401. Any API client usage relying on specific status code 403 versus 401 will have to update their logic. Standard UI usage will work as expected. |
| Event-Driven Ansible | The endpoints `/extra_vars` are now moved to a property within `/activations` . |
| Event-Driven Ansible | The endpoint `/credentials` was replaced with `/eda-credentials` . This is part of an expanded credentials capability for Event-Driven Ansible. For more information, see the chapter [Setting up credentials for Event-Driven Ansible controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html/event-driven_ansible_controller_user_guide/eda-credentials) in the _Event-Driven Ansible controller user guide_ . |
| Event-Driven Ansible | Event-Driven Ansible can no longer add, edit, or delete the platform gateway-managed resources. Creating, editing, or deleting organizations, teams, or users is available through platform gateway endpoints only. The platform gateway endpoints also enable you to edit organization or team memberships and configure external authentication. |
| API | Auditing of users has now changed. Users are now audited through the platform API, not through the controller API. This change applies to the Ansible Automation Platform in both cloud service and on-premise deployments. |
| Automation controller,
automation hub,
platform gateway, and
Event-Driven Ansible | User permission audits the sources of truth for the platform gateway. When an IdP (SSO) is used, then the IdP should be the source of truth for user permission audits. When the Ansible Automation Platform platform gateway is used without SSO, then the platform gateway should be the source of truth for user permissions, not the app-specific UIs or APIs. |


