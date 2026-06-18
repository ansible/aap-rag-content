# Workload types and access methods

Learn about enabling performance tuning for your Ansible Automation Platform deployment.

This section covers the following topics:

- The types of workloads and the components these workloads rely on to perform well
- The services each workload uses
- Reference workloads supported by the tested deployment models
- Reasons for scaling each service beyond the base configurations of the tested deployment models

## UI authentication and platform load

Users can access the Ansible Automation Platform UI via enterprise authentication. UI clients apply load to the platform gateway proxy, gRPC authentication service, component web servers, and the database, as most UI-driven API requests interact directly with the database.

Login performance with enterprise authentication depends on two factors: the performance of the external authentication provider, and the complexity of mapping external attributes to RBAC attributes in Ansible Automation Platform. After a successful login, the browser uses session authentication for subsequent requests. This method is generally faster because some session data is cached.

The Ansible Automation Platform UI receives live updates through WebSockets and periodically requests updates from all components. This is necessary to properly render options and update on-screen information.

Users can configure the frequency of these periodic update requests. This is done by adjusting the "Refresh Interval" setting in the UI User Preferences tab. This action affects the load that an open browser tab with the Ansible Automation Platform UI generates on backend services.

Through WebSockets in the user interface, the browser receives real-time job updates. The browser can subscribe to any job running on any automation controller node, because events are accessible everywhere.

However, live streaming updates to the job detail page might increase the load on the automation controller service. To disable these updates, set `UI_LIVE_UPDATES_ENABLED` to false in the automation controller configuration.

Note:

Disabling updates prevents the job detail page from automatically updating when events are received. In this case, you must manually refresh the page to access the most recent details.

## REST API access and client load

Ansible Automation Platform provides a REST API, offering access to all its functionalities. You can access this API by using various clients, including cURL, Python, Ansible Automation Platform configuration collections, or the Ansible URI module.

You can use the API to automate the following tasks:

- Launching jobs
- Updating inventories
- Checking automation status
- Pushing events into an Event Stream for Event-Driven Ansible
- Automating the upload or publication of collections in automation hub
- Managing automation execution environments in the automation hub container registry using a Podman client that connects to automation hub over its registry API


API clients apply load to the platform gateway proxy, the gRPC service for authentication, the web server of the targeted component, and the database, because most API client queries interact with the database.

To access the API, you can use the following common authentication methods: Basic authentication (using a username and password) and Token authentication (your chosen authentication method). Token authentication is recommended for better performance.

Use the platform gateway to create tokens and link them to an OAuth application or your account. The platform gateway’s gRPC service authenticates each request and directs it to the appropriate application server based on the specified route.
