# Upload, group, and approve your organization’s content collections
## Repository management with automation hub
### Types of repositories in automation hub

In automation hub you can publish collections to two types of repositories, depending on whether you want your collection to be verified:

Staging repositories
Any user with permission to upload to a namespace can publish collections into these repositories. Collections in these repositories are not available in the search page. Instead, they are displayed on the approval dashboard for an administrator to verify. Staging repositories are marked with the `pipeline=staging` label.

Custom repositories
Any user with write permissions on the repository can publish collections to these repositories. Custom repositories can be public where all users can see them, or private where only users with view permissions can see them. These repositories are not displayed on the approval dashboard. If the repository owner enables search, the collection can appear in search results.

By default, automation hub includes one staging repository that is automatically used when a repository is not specified for uploading collections.
