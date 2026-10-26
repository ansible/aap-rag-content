# Control how many collection versions are synced

Configure the number of collection versions downloaded during sync operations.

## Before you begin

You have administrator permissions for Ansible Automation Platform.

## About this task

By default, new remote configurations download every version of each collection specified in the requirements.yml file during a sync operation. You can change this behavior by configuring the Sync highest versions field on the remote configuration form.

This setting applies to all collections under the remote. You cannot configure a different sync limit for individual collections.

## Procedure

1. From the navigation panel, select Automation Content> (and then)Remotes.
2. Find the remote you want to configure and click the pencil icon to edit.
3. In the Sync highest versions field, enter one of the following values:
| Value                      | Behavior                                                             |
| -------------------------- | -------------------------------------------------------------------- |
| `1`                        | Sync only the highest stable version of each collection.             |
| *N* (any positive integer) | Sync the*N* highest stable versions of each collection.              |
| Empty (no value)           | Sync all available versions of each collection. This is the default. |

4. Click Save remote.
5. Sync the repository to apply the new setting.
From the navigation panel, select Automation Content> (and then)Repositories, then click the ⋮ icon in the row containing the repository and select Sync repository.

## Results

The remote configuration now limits the number of synced versions based on your setting.

**How version selection works:**

- **Stable versions are preferred.** When determining the highest versions, automation hub selects stable releases over pre-release versions. For example, if a collection has versions `2.1.0`, `2.0.0`, and `3.0.0-beta1`, setting the field to `1` syncs `2.1.0`, not the pre-release.
- **Version specifiers in requirements files take precedence.** If your requirements file includes version constraints (for example, `>=2.0.0,<3.0.0`), those constraints are applied first. The Sync highest versions setting then selects from the versions that match the constraints.

## What to do next

**Behavior after upgrading to Ansible Automation Platform 2.6:**

Existing remote configurations are not affected by this feature. After upgrading, remotes that previously synced all versions continue to sync all versions.

To limit the number of synced versions for an existing or new remote, edit the remote configuration and set the Sync highest versions field to the desired value. This feature is not enabled automatically; you must explicitly configure it for each remote.
