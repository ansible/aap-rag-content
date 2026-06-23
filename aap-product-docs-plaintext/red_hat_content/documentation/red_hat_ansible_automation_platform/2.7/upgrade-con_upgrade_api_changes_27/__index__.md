# API changes in Ansible Automation Platform 2.7

Ansible Automation Platform 2.7 completes the migration of all API access to platform gateway. Direct API access to individual services that was deprecated in versions 2.5 and 2.6 has been removed in this release.

These changes impact your organization if you have API calls, scripts, or integrations that connect directly to automation controller, automation hub, or Event-Driven Ansible hosts. All API requests must now use platform gateway endpoints. Requests sent directly to component hosts return an HTTP 401 Unauthorized error.

This section highlights the changed APIs between 2.6 and 2.7.

