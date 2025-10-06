# 2. Automation controller configuration
## 2.1. Configuring system settings




You can use the **System** menu to define automation controller system settings.

**Procedure**

1. From the navigation panel, selectSettings→Automation Execution→System. The **System Settings** page is displayed.
1. ClickEdit.
1. You can configure the following options:


-  **Base URL of the service** : This setting is used by services such as notifications to render a valid URL to the service.
-  **Proxy IP allowed list** : If the service is behind a reverse proxy or load balancer, use this setting to configure the proxy IP addresses from which the service should trust custom `        REMOTE_HOST_HEADERS` header values.

If this setting is an empty list (the default), the headers specified by `        REMOTE_HOST_HEADERS` are trusted unconditionally.


-  **Red Hat Client ID for anaytics** Client ID used to send data to Automation Analytics.
-  **Red Hat Client Secret for analytics** Client secret used to send data to Automation Analytics.
-  **Red Hat Client ID for subscriptions** Client ID used to retrieve subscription and content information.
-  **Red Hat Client Secret for Subsciptions** Client secret used to retrieve subscription and content information
-  **Global default execution environment** : The execution environment to be used when one has not been configured for a job template.
-  **Custom virtual environment paths** : Paths where automation controller looks for custom virtual environments.

Enter one path per line.


-  **Automation Analytics Gather Interval** : Interval (in seconds) between data gathering.

If **Gather data for Automation Analytics** is set to false, this value is ignored.


-  **Remote Host Headers** : HTTP headers and meta keys to search to decide remote hostname or IP. Add additional items to this list, such as `        HTTP_X_FORWARDED_FOR` , if behind a reverse proxy. For more information, see [Configuring proxy support for Red Hat Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/operating_ansible_automation_platform/assembly-configuring-proxy-support) .
-  **Automation Analytics upload URL** : This value has been set manually in a settings file. This setting is used to configure the upload URL for data collection for Automation Analytics.
-  **Defines subscription usage model and shows Host Metrics** :

You can select the following options:


- No subscription: Deletion of host_metrics will not be considered for purposes of managed host counting.
- Usage based on unique managed nodes ina large hostorical time frame and delete functionality for no longer used managed nodes.


1. You can set the following options:


-  **Enable Activity Stream** : Set to enable capturing activity for the activity stream.
-  **Enable Activity Stream for Inventory Sync** : Set to enable capturing activity for the activity stream when running inventory sync.
-  **All Users Visible to Organization Admins** : Set to control whether any organization administrator can view all users and teams, even those not associated with their organization.
-  **Organization Admins Can Manage Users and Teams** : Set to control whether an organization administrator has the privileges to create and manage users and teams.

You might want to disable this ability if you are using an LDAP or SAML integration.


-  **Gather data for Automation Analytics** : Set to enable the service to gather data on automation and send it to Automation Analytics.

1. ClickSave


