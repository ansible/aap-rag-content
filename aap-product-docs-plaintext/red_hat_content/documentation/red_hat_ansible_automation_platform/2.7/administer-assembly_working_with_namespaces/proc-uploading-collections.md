# Manage collection access and permissions with namespaces
## Upload collections to a namespace

Upload internally-developed collections in `tar.gz` file format to your private automation hub namespace for review and approval by an automation hub administrator.

### Before you begin

- You have a namespace to which you can upload the collection.


Important:

Attempting to upload very large collections will result in an error.

Limit collection size to 200 mb when uploading to console.redhat.com or private automation hub.

In scenarios that require a complete environment with multiple collections and dependencies, use an execution environment. See [Pull execution environments for use in automation hub](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-con_container_registry#obtain-images "Before you can push execution environments to your private automation hub, you must first pull them from an existing registry and tag them for use.")for more information.

Note:

In Ansible Automation Platform 2.7, collection uploads route through platform gateway. If uploads fail with an HTTP 413 error, you may need to increase the gateway `GRPC_SERVER_MAX_RECEIVE_MESSAGE_LENGTH` setting. See [Configure platform gateway route timeouts](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-con_gateway_route_timeouts#con-gateway-route-timeouts "In Ansible Automation Platform 2.7, all API access to platform components goes through platform gateway. Gateway-level timeout settings control how long platform gateway waits for backend services to respond before closing a connection.")for more information.

### About this task

When approved, the collection moves to the **Published** content repository where automation hub users can view and download it.

Note:

Format your collection file name as follows: <my_namespace-my_collection-1.0.0.tar.gz>

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Content> (and then)Namespaces and select a namespace.
3.  Select the **Collections** tab.
4.  Click Upload collection.
5.  Click Browse next to the **Collection file** field.
6.  Select the collection to upload.
7.  Select one of the following options:

-  **Staging repos**
-  **Repositories without pipeline**

8.  Click Upload collection.

### Results

To verify whether the collection uploaded successfully or if it failed, navigate to Automation Content> (and then)Namespaces and click the More Actions icon **⋮**, then select **Imports**. There you will find a summary of tests indicating whether the import was successful.

