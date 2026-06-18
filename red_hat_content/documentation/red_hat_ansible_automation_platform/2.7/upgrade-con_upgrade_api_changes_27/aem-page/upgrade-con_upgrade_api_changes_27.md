+++
template = "docs/aem-title.html"
title = "API changes in Ansible Automation Platform 2.7 - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-con_upgrade_api_changes_27"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-con_upgrade_api_changes_27/", "API changes in Ansible Automation Platform 2.7"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_upgrade_api_changes_27/aem-page/upgrade-con_upgrade_api_changes_27.html"
last_crumb = "API changes in Ansible Automation Platform 2.7"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "API changes in Ansible Automation Platform 2.7"
oversized = "false"
page_slug = "upgrade-con_upgrade_api_changes_27"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-con_upgrade_api_changes_27"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-con_upgrade_api_changes_27/toc/toc.json"
type = "aem-page"
+++

# API changes in Ansible Automation Platform 2.7

Ansible Automation Platform 2.7 completes the migration of all API access to platform gateway. Direct API access to individual services that was deprecated in versions 2.5 and 2.6 has been removed in this release.

These changes impact your organization if you have API calls, scripts, or integrations that connect directly to automation controller, automation hub, or Event-Driven Ansible hosts. All API requests must now use platform gateway endpoints. Requests sent directly to component hosts return an HTTP 401 Unauthorized error.

This section highlights the changed APIs between 2.6 and 2.7.

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

## Specific API changes

In Red Hat Ansible Automation Platform 2.7, all API access must go through the platform gateway hostname. Direct access to component hostnames has been removed.

| Old (Ansible Automation Platform 2.6)          | New (Ansible Automation Platform 2.7)             | Status   |
| ---------------------------------------------- | ------------------------------------------------- | -------- |
| `https://controller.example.com/api/v2/*`      | `https://gateway.example.com/api/controller/v2/*` | Required |
| `https://hub.example.com/api/automation-hub/*` | `https://gateway.example.com/api/galaxy/*`        | Required |
| `https://eda.example.com/api/eda/v1/*`         | `https://gateway.example.com/api/eda/v1/*`        | Required |


Note:

Attempting to access component hostnames directly (`controller.example.com`, `hub.example.com`, `eda.example.com`) returns HTTP 401 Unauthorized in Red Hat Ansible Automation Platform 2.7.

## Update collection versions

Older collection versions construct URLs and authentication flows that target component APIs directly. Only the latest collection versions route requests through platform gateway.

### Before you begin

- You have access to your project's `requirements.yml` or execution environment definition files.
- You have permissions to rebuild execution environments in your deployment.

### About this task

If your automation content still targets component endpoints or uses outdated collection versions, your playbooks and integrations will fail after the upgrade.

You must complete two actions to ensure your automation content works with Ansible Automation Platform 2.7:

- Upgrade all component collections to the latest versions for Ansible Automation Platform 2.7. The minimum required collection versions for Ansible Automation Platform 2.7 are as follows:
  * `ansible.controller: 4.8.0`
  * `ansible.hub: 1.0.6`
  * `ansible.eda: 2.12.0`
  * `ansible.platform: 2.7.0`
- Update connection values in your playbooks, inventory variables, and Configuration as Code content to use platform gateway.

### Procedure

1.  Update collection version pins in your `requirements.yml `file to require the latest versions:
  

```
collections:
  - name: ansible.controller version: ">=4.8.0"
  - name: ansible.hub version: ">=1.0.6"
  - name: ansible.eda version: ">=2.12.0"
  - name: ansible.platform version: ">=2.7.0"
```

2.  Rebuild your execution environments to include the updated collections.
3.  Refresh project and collection dependencies in automation controller.
4.  Verify the installed collection versions:
  

```
ansible-galaxy collection list | grep -E "ansible\.(controller|hub|eda|platform)"
```

5.  Run a test playbook against your upgraded Ansible Automation Platform 2.7 environment to confirm that API calls route through platform gateway.

## Migrate playbook connection values to platform gateway

After upgrading to Ansible Automation Platform 2.7, all host, username, password, and token values in your playbooks must reference platform gateway. Connection values that target component hosts directly (such as `controller.example.com` or `hub.example.com`) cause authentication failures.

### Before you begin

- Ansible Automation Platform 2.7 is deployed and accessible through the platform gateway.
- You have administrator access to platform gateway for creating credentials and tokens.
- You have updated your collections to the latest versions for Ansible Automation Platform 2.7.

### Procedure

1.  Create credentials, OAuth2 applications, and API tokens in platform gateway. In the Ansible Automation Platform UI, navigate to Access> (and then)Applicationsto register OAuth2 applications, and Access> (and then)Tokensto generate tokens.
2.  Identify all playbooks, inventory variables, and Configuration as Code definitions that reference component-specific hosts, usernames, passwords, or tokens.
3.  Replace component-specific connection values with platform gateway values.
  The following table shows common variables and their required changes:
    | Variable                | Before (2.6 and earlier)         | After (2.7)                   |
    | ----------------------- | -------------------------------- | ----------------------------- |
    | `controller_host`       | `https://controller.example.com` | `https://gateway.example.com` |
    | `ah_host` / `hub_host`  | `https://hub.example.com`        | `https://gateway.example.com` |
    | `eda_host`              | `https://eda.example.com`        | `https://gateway.example.com` |
    | `controller_username`   | Component-scoped user            | Platform gateway user         |
    | `controller_password`   | Component-scoped password        | Platform gateway password     |
    | `controller_oauthtoken` | Controller-issued PAT            | Platform gateway-issued token |

4.  Update your inventory files or environment variables to reflect the new values.
5.  Test your updated playbooks against the upgraded environment.

### Example: Migrate a job launch playbook

The following example shows a playbook that launches a job template. The "before" version targets automation controller directly. The "after" version targets platform gateway.

**Before (targets automation controller directly)**

```
- name: Launch a job template
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
    aap_controller_host: "https://controller.example.com"
    aap_controller_username: "{{ lookup('env', 'AAP_CONTROLLER_USERNAME') }}"
    aap_controller_password: "{{ lookup('env', 'AAP_CONTROLLER_PASSWORD') }}"  

  tasks:
   - name: Launch the job
     ansible.controller.job_launch:
       job_template: "Deploy Application"
       controller_host: "{{ aap_controller_host }}"
       controller_username: "{{ aap_controller_username }}"
       controller_password: "{{ aap_controller_password }}"
```

This playbook fails after upgrading to Ansible Automation Platform 2.7 because `ansible.controller `can no longer authenticate directly against the controller host.

**After (targets platform gateway)**

```
- name: Launch a job template
  hosts: localhost
  connection: local
  gather_facts: false

  vars:
   aap_gateway_host: "https://gateway.example.com"
   aap_gateway_username: "{{ lookup('env', 'AAP_GATEWAY_USERNAME') }}"
   aap_gateway_password: "{{ lookup('env', 'AAP_GATEWAY_PASSWORD') }}"

 tasks:
   - name: Launch the job
     ansible.controller.job_launch:
       job_template: "Deploy Application"
       controller_host: "{{ aap_gateway_host }}"
       controller_username: "{{ aap_gateway_username }}"
       controller_password: "{{ aap_gateway_password }}"
```

The `controller_host` parameter now points to the platform gateway URL. The username and password are credentials created in platform gateway. The `ansible.controller` collection (latest version) routes the API request through platform gateway.
