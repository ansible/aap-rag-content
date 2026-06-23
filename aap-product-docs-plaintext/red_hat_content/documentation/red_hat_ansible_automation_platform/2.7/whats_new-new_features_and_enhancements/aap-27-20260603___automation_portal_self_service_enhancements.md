# New features and enhancements
## Automation portal self-service enhancements

**Role-based access control**: Automation portal now supports RBAC-based navigation menus. Administrators can control which users can access Templates, History, execution environment definitions, collections, Git repositories, and synchronization actions. Configure permitted roles in the portal administration section.

**GitHub Apps authentication**: Configure GitHub Apps as an authentication method for source control integration, in addition to personal access tokens. GitHub Apps provide fine-grained repository permissions and higher API rate limits.

**Disconnected environment support**: Additional disconnected environment support for registries and self-signed certificates.

**Job template filtering**: Use the excludeLabels Helm chart setting to filter which job templates are visible in automation portal. Templates with matching labels are excluded from the catalog.

