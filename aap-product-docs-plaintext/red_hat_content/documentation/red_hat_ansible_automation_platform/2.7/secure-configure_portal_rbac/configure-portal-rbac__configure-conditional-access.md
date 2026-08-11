# Configure role-based access control for Ansible automation portal
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

**Restrict visibility of custom templates**

Auto-generated templates inherit visibility from Ansible Automation Platform permissions. Custom templates require a different approach because they are visible to all users by default. Use tag-based conditional policies to restrict which users can see specific custom templates.

1. Add a tag to the custom template YAML file in the `metadata.tags` field:

```yaml
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
name: deploy-to-prod
title: Deploy to Production
tags:
- restricted
```

2. Log in to Ansible automation portal as an administrator.
3. Navigate to Administration> (and then)RBAC.
4. Create a role for users who should see the restricted template (for example, `template-admins`). Assign the role to the appropriate teams or users. Grant `catalog.entity.read` and all scaffolder permissions without conditions.
5. Edit the default authenticated user role to add a conditional policy that hides templates tagged `restricted`:
- Select the **Catalog** plugin and enable `catalog.entity.read`.
- Click **Conditional** to configure a condition-based policy.
- **Rule:** Select `HAS_METADATA`.
- **Key:** Enter `tags`.
- **Value:** Enter `restricted`.
- Set the condition to **NOT** so that users in this role can see all templates *except* those tagged `restricted`.
6. Click **Next** to review your settings, then click **Create** or **Save**.

Users assigned to the `template-admins` role see all templates. Users in the default role see all templates except those tagged `restricted`.

Tip:

To verify which conditional rules are available in your portal instance, query the `GET /api/plugins/condition-rules` API endpoint. Use `HAS_METADATA` with `key: tags` for catalog-level visibility filtering.

