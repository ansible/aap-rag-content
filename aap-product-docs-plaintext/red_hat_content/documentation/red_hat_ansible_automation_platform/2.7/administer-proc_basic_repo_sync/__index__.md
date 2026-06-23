# Synchronize repositories in automation hub

Synchronize repositories in automation hub to update your custom repository with the latest collections from a configured remote.

## Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Repositories.
3.  Locate your repository in the list and click More Actions icon **⋮**, then select **Sync repository**. All collections in the configured remote are downloaded to your custom repository. To check the status of the collection sync, select Automation Content> (and then)Task Management from the navigation panel.

Note:
To limit repository synchronization to specific collections within a remote, you can identify specific collections to be pulled by using a `requirements.yml` file.

