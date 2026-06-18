+++
title = "Configure role-based access control for Ansible automation portal - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/configure_portal_rbac"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/configure_portal_rbac/aem-page/configure_portal_rbac.html"
last_crumb = "Configure role-based access control for Ansible automation portal"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure role-based access control for Ansible automation portal"
oversized = "false"
page_slug = "configure_portal_rbac"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/configure_portal_rbac"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/configure_portal_rbac/toc/toc.json"
type = "aem-page"
+++

# Configure role-based access control for Ansible automation portal

Configure RBAC permissions in Ansible automation portal to control which users can view and execute templates, and which sidebar items are visible to non-admin users.

After you install Ansible automation portal and synchronize it with Ansible Automation Platform, only users with AAP administrator privileges can view the auto-generated templates. You must configure role-based access control (RBAC) permissions to allow non-admin users to view and execute templates.

Ansible automation portal uses two categories of permissions:

- **Catalog and scaffolder permissions** control whether users can view templates, execute actions, and manage tasks.
- **Navigation permissions** control which sidebar items and pages are visible to users. Without the required navigation permission, a sidebar item and its associated pages are hidden.


Important:

RBAC differs by template type:

- **Auto-generated templates:** Permissions are synchronized from Ansible Automation Platform. Users must have permissions on the underlying AAP job template.
- **Custom templates:** Permissions must be explicitly configured within Ansible automation portal. Users must also have permissions to run the associated job templates in Ansible Automation Platform.

## Understand the permission model

Ansible automation portal and Ansible Automation Platform use separate but related permission systems. Ansible Automation Platform RBAC is the source of truth for synchronization scope and execution permissions.

**Ansible automation portal RBAC:**

- Controls which users can view templates in the Ansible automation portal catalog.
- Controls which users can access portal templates and submit jobs.
- Controls which navigation items are visible in the sidebar.


**Ansible Automation Platform RBAC:**

- **Controls synchronization scope:** Only Ansible Automation Platform job templates accessible by the configured API token (`ansible.rhaap.token`) are synchronized to Ansible automation portal.
- **Controls job template visibility and execution:** Ansible Automation Platform permissions determine whether authenticated users can view and execute job templates in Ansible automation portal.
- **Validates execution permissions:** When a user executes a template, Ansible Automation Platform checks that user's execute permissions before launching the job.


If a user can see a template in the catalog but lacks Ansible Automation Platform execute permissions for the associated job template, the user cannot run the job.

## Configure RBAC for synchronization

Synchronization uses the Ansible Automation Platform API token configured in Ansible automation portal to determine which data to synchronize from Ansible Automation Platform.

Before you begin:

- You have credentials for an Ansible Automation Platform administrator.
- Synchronization of Ansible Automation Platform organization information from Ansible Automation Platform is complete.
- Users who execute job templates through Ansible automation portal must have job template execute permissions assigned in Ansible Automation Platform.
- The **Allow external users to create OAuth2 tokens** setting is enabled in Settings> (and then)Platform gateway settings in Ansible Automation Platform.


Procedure:

1. Log in to Ansible automation portal as an administrator.

2. Navigate to Administration> (and then)RBAC.

3. Click **Create Role** and provide a name (for example, `portal-user`).

4. In the **Users and Groups** section, select the Ansible Automation Platform teams and users to assign to this role. Click **Next**. You can only select teams and users from the Ansible Automation Platform organization that you configured for synchronization with Ansible automation portal.

5. In the **Add permission policies** section, select the **Catalog** plugin from the dropdown menu and enable `catalog.entity.read`.

6. Select the **Scaffolder** plugin and enable the following permissions:
  - `scaffolder.template.parameter.read`
  - `scaffolder.template.step.read`
  - `scaffolder.action.execute`
  - `scaffolder.task.create`
  - `scaffolder.task.read` — Required for users to view previous task runs on the **History** page.
  - `scaffolder.task.cancel`

7. Add the base navigation permissions so users can see the **Templates** and **History** sidebar items:
  - `ansible.templates.view`
  - `ansible.history.view`

8. Click **Next** to review your settings, then click **Create**.

Your new role appears in the **All roles** list under Administration> (and then)RBAC.

Important:

If you are upgrading from plug-in version 2.1, you must add `ansible.templates.view` and `ansible.history.view` to existing roles. Without these permissions, non-admin users cannot see the **Templates** and **History** navigation items. For more information, see the upgrade guide for your platform.

## Configure navigation permissions

Ansible automation portal controls the visibility of sidebar items through navigation permissions. Each sidebar item requires a corresponding permission. Users without the required permission do not see the sidebar item or its associated pages.

## Base navigation permissions

The following permissions control core Ansible automation portal sidebar items. Grant these to all portal users.

| Permission               | Controls                                                        |
| ------------------------ | --------------------------------------------------------------- |
| `ansible.templates.view` | **Templates** sidebar item — template catalog and launch wizard |
| `ansible.history.view`   | **History** sidebar item — task execution history and logs      |

## Execution environment builder navigation permissions

The following permissions control execution environment builder sidebar items. Grant these to users who need access to execution environment builder features.

| Permission                            | Controls                                                                 |
| ------------------------------------- | ------------------------------------------------------------------------ |
| `ansible.execution-environments.view` | **Execution Environments** sidebar item — creation wizard and EE catalog |
| `ansible.collections.view`            | **Collections** sidebar item — collection catalog for EE definitions     |
| `ansible.git-repositories.view`       | **Git Repositories** sidebar item — saving and syncing EE definitions    |


Each permission can be assigned individually for granular control.

## Grant navigation permissions to a role

Before you begin:

- You have configured base RBAC roles as described in the [Configure RBAC for synchronization](#configure-portal-rbac__configure-rbac-for-synchronization) section.
- You have the AAP Administrator role and access to Administration> (and then)RBAC in Ansible automation portal.


Procedure:

1. In Ansible automation portal, navigate to Administration> (and then)RBAC in the sidebar.
2. Select an existing role to edit, or click **Create Role** to create a new role (for example, `ee-builder-users`).
3. In the permissions section, add the navigation permissions your users require:
  - For all portal users: `ansible.templates.view` and `ansible.history.view`.
  - For execution environment builder users: `ansible.execution-environments.view`, `ansible.collections.view`, and `ansible.git-repositories.view`.
4. If creating a new role, assign the role to the appropriate users or groups.
5. Click **Save**.


To hide specific sidebar items from a user group, remove the corresponding permissions from their assigned roles.

Note:

Importing and deleting EE templates are AAP administrator-only actions. Users with the AAP Administrator role can perform these actions without additional permission grants.

Verification:

- Log out and log in as a user assigned to the modified role.
- Verify that the expected sidebar items are visible based on the permissions you assigned.
- If you granted execution environment builder access, navigate to Execution Environments> (and then)Create and verify that templates are visible and the wizard launches.

## Configure conditional access

You can configure conditional RBAC policies to filter role access by tag. This restricts specific teams or users to a subset of job templates. Ansible Automation Platform labels applied to job templates are synchronized to Ansible automation portal as tags.

Note:

Ansible Automation Platform labels are converted to lowercase tags with special characters replaced by hyphens. For example, the Ansible Automation Platform label `Network-Automation` becomes the tag `network-automation`.

Before you begin:

- Ansible Automation Platform job templates must have Ansible Automation Platform labels applied and synchronized with Ansible automation portal.
- Users who execute job templates through Ansible automation portal must have job template execute permissions assigned in Ansible Automation Platform.


Procedure:

1. Log in to Ansible automation portal as an administrator.
2. Navigate to Administration> (and then)RBAC.
3. Click **Create Role** and provide a name (for example, `network-portal-user`).
4. In the **Users and Groups** section, select the Ansible Automation Platform teams and users to assign to this role (for example, the `network-team`). Click **Next**.
5. In the **Add permission policies** section, select the **Catalog** plugin and enable `catalog.entity.read`.
6. Click **Conditional** to configure a condition-based policy:
  - **Rule:** Select `HAS_METADATA`.
  - **Key:** Enter `tags`.
  - **Value:** Enter the tag value to filter by (for example, `network-automation`).
7. Select the **Scaffolder** plugin and enable all scaffolder permissions listed in the previous procedure.
8. Click **Next** to review your settings, then click **Create**.


Verification:

- If you configured conditional access by tag, the user should see only templates with the specified tags.
- If you did not configure conditional access, the user should see all Ansible Automation Platform job templates for which they have execute permissions in Ansible Automation Platform.
- To verify execution permissions, attempt to execute a template. If the user has execute permissions in Ansible Automation Platform for the template, the job launches successfully.

## Permissions reference

| Permission                            | Resource type       | Policy | Description                                                                   |
| ------------------------------------- | ------------------- | ------ | ----------------------------------------------------------------------------- |
| `catalog.entity.read`                 | catalog-entity      | read   | View synchronized AAP job templates in the Ansible automation portal catalog. |
| `scaffolder.template.parameter.read`  | scaffolder-template | read   | Read template parameters in the launch wizard.                                |
| `scaffolder.template.step.read`       | scaffolder-template | read   | Read template steps in the launch wizard.                                     |
| `scaffolder.action.execute`           | scaffolder-action   | use    | Execute actions through templates.                                            |
| `scaffolder.task.create`              | scaffolder-task     | create | Trigger the execution of job templates.                                       |
| `scaffolder.task.read`                | scaffolder-task     | read   | View task execution history and logs on the **History** page.                 |
| `scaffolder.task.cancel`              | scaffolder-task     | use    | Cancel running templates.                                                     |
| `ansible.templates.view`              | —                   | —      | Show the **Templates** sidebar item and pages. Required for all portal users. |
| `ansible.history.view`                | —                   | —      | Show the **History** sidebar item and pages. Required for all portal users.   |
| `ansible.execution-environments.view` | —                   | —      | Show the **Execution Environments** sidebar item and pages.                   |
| `ansible.collections.view`            | —                   | —      | Show the **Collections** sidebar item and pages.                              |
| `ansible.git-repositories.view`       | —                   | —      | Show the **Git Repositories** sidebar item and pages.                         |

## Adjust synchronization frequency

Ansible automation portal synchronizes users, teams, organization, and job template information from Ansible Automation Platform at regular intervals. By default, synchronization occurs hourly.

To change the synchronization frequency:

- **RHEL appliance:** Edit /etc/portal/configs/app-config/app-config.production.yaml and update the `schedule.frequency` value under the `catalog.providers.rhaap` section. Restart the portal service after saving.
- **OpenShift Container Platform:** Update the `schedule.frequency` value in the Helm chart values file and upgrade the Helm release.
