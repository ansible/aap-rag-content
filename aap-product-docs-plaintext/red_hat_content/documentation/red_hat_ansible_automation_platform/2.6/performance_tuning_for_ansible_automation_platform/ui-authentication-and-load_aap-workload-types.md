# 1. Types of workloads
## 1.1. UI authentication and platform load




Users can access the Ansible Automation Platform UI by using enterprise authentication methods. UI clients apply load to the platform gateway proxy and the gRPC authentication service, the web servers of all components, and the database, because most UI-driven API requests interact with the database.

The login performance with enterprise authentication is dependent on the performance of the external authentication provider and the complexity of the mapping of the external authentication attributes to RBAC attributes in Ansible Automation Platform. After successful login, the browser uses session authentication for subsequent requests, which is generally a faster authentication method as some session data is cached.

The Ansible Automation Platform UI receives live updates through WebSockets and periodically requests updates from all components to properly render options and update on-screen information. Users can configure the frequency of these periodically maintained update requests by adjusting the "Refresh Interval" setting in the UI **User Preferences** tab. This action affects the load that an open browser tab with the Ansible Automation Platform UI generates on backend services.

Through WebSockets in the user interface, the browser receives real-time job updates. The browser can subscribe to any job running on any automation controller node, because events are accessible everywhere. However, live streaming updates to the job detail page might increase the load on the automation controller service. To disable these updates, set `UI_LIVE_UPDATES_ENABLED` to false in the automation controller configuration.

Note
Disabling updates prevents the job detail page from automatically updating when events are received. In this case, you must manually refresh the page to access the most recent details.



