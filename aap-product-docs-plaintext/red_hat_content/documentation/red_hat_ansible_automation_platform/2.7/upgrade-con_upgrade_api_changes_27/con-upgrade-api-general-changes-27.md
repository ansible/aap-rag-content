# API changes in Ansible Automation Platform 2.7
## General API changes

In Ansible Automation Platform 2.7, direct API access to individual platform components has been removed. All API access must go through platform gateway.

Important:

Service-specific API endpoints have been removed in Ansible Automation Platform 2.7. Direct component API access is no longer available. All API access must go through platform gateway.

| Component             | 2.4 and earlier endpoints start with... | 2.5 and 2.6 endpoints start with... | 2.7 endpoints start with...                      |
| --------------------- | --------------------------------------- | ----------------------------------- | ------------------------------------------------ |
| Automation controller | `/api/v2/`                              | `/api/controller/v2/`               | Must use platform gateway: `/api/controller/v2/` |
| Automation hub        | `/api/automation-hub`                   | `/api/galaxy/v1`                    | Must use platform gateway: `/api/galaxy/v1`      |
| Platform gateway      | Not applicable                          | `/api/gateway/v1/`                  | `/api/gateway/v1/`                               |
| Event-Driven Ansible  | Not applicable                          | `/api/eda/v1/`                      | Must use platform gateway: `/api/eda/v1/`        |


In Red Hat Ansible Automation Platform 2.7, these API endpoints are only accessible through the platform gateway hostname. Direct access to component hostnames (such as `controller.example.com` or `hub.example.com`) returns an HTTP 401 Unauthorized error.

**Example:**

- Works in 2.7: `https://gateway.example.com/api/controller/v2/ping/`
- Blocked in 2.7: `https://controller.example.com/api/v2/ping/`

